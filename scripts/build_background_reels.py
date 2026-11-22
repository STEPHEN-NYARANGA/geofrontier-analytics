#!/usr/bin/env python3
"""Produce real moving NASA documentary footage for GeoFrontier's hero sections.

All clips are sourced from NASA Scientific Visualization Studio, not from the
reference website. This script deliberately strips audio and overlays no
titles, logos or NASA branding. Source and provenance are credited elsewhere.

Runs in GitHub Actions (network + ffmpeg), outputs locally hosted compact MP4
loops and JPEG still fallbacks for reduced-motion users.
"""
from __future__ import annotations

import json
import subprocess
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "assets" / "media"
MEDIA.mkdir(parents=True, exist_ok=True)
SOURCE_URLS = {
    "orbit": "https://svs.gsfc.nasa.gov/vis/a030000/a030700/a030771/ISS_View_of_Planet_Earth_720p.mp4",
    "crew": "https://svs.gsfc.nasa.gov/vis/a030000/a030700/a030771/ISS_Crew_Earth_Observations_720p.mp4",
    "overview": "https://svs.gsfc.nasa.gov/vis/a010000/a011800/a011834/11858-540-MASTER_high.mp4",
}
# Segments are taken from NASA videos with deliberately different content.
# Approximate durations are kept short for responsible bandwidth consumption.
REELS = {
    # Start AFTER the NASA title cards so actual moving imagery appears at once.
    "geofrontier-home-reel": [("orbit", 20.0, 5.5), ("overview", 40.0, 5.5), ("crew", 20.0, 5.5)],
    "geofrontier-monitoring-reel": [("overview", 40.0, 6.0), ("orbit", 30.0, 6.0)],
    "geofrontier-learning-reel": [("crew", 20.0, 6.0), ("orbit", 28.0, 6.0)],
}

def run(*command: str, timeout: int = 100) -> None:
    subprocess.run(command, check=True, timeout=timeout,
                   stdout=subprocess.DEVNULL)

def download(url: str, target: Path) -> None:
    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 GeoFrontier/1.0 (attributed NASA documentary media)",
                      "Accept": "video/mp4,*/*"},
    )
    with urllib.request.urlopen(req, timeout=75) as response, target.open("wb") as output:
        content_type = response.headers.get("Content-Type", "")
        if "html" in content_type.lower():
            raise RuntimeError(f"Unexpected content type: {content_type}")
        total = 0
        while chunk := response.read(1024 * 1024):
            total += len(chunk)
            if total > 65_000_000:
                raise RuntimeError("NASA source clip exceeds 65 MB budget")
            output.write(chunk)
    if target.stat().st_size < 200_000:
        raise RuntimeError("Downloaded NASA video appears incomplete")
    print("Downloaded", url, "bytes", target.stat().st_size, flush=True)

def duration(path: Path) -> float:
    p = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        text=True, timeout=30
    )
    return float(p.strip())

def encode_segment(source: Path, out: Path, offset: float, seconds: float) -> None:
    clip_duration = duration(source)
    print("Video duration", source.name, clip_duration, "requested offset", offset, flush=True)
    if clip_duration < seconds + 0.3:
        raise RuntimeError(f"Clip too short: {source.name} ({clip_duration}s)")
    offset = min(offset, clip_duration - seconds - 0.2)
    run(
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", str(offset), "-i", str(source), "-t", str(seconds),
        "-an", "-vf", "scale=960:540:force_original_aspect_ratio=increase,crop=960:540,fps=24,format=yuv420p",
        "-c:v", "libx264", "-preset", "medium", "-crf", "27",
        "-maxrate", "1200k", "-bufsize", "2400k",
        "-profile:v", "main", "-level", "3.1",
        "-video_track_timescale", "24000",
        str(out), timeout=120
    )

def main() -> None:
    with tempfile.TemporaryDirectory(prefix="geofrontier-media-") as tmpname:
        temp = Path(tmpname)
        originals = {}
        for key, url in SOURCE_URLS.items():
            src = temp / (key + ".mp4")
            download(url, src)
            originals[key] = src

        for outname, segments in REELS.items():
            files = []
            for idx, (key, offset, seconds) in enumerate(segments):
                path = temp / f"{outname}-{idx}.mp4"
                encode_segment(originals[key], path, offset, seconds)
                files.append(path)
            playlist = temp / (outname + ".txt")
            playlist.write_text("".join("file '" + str(f) + "'\n" for f in files))
            output = MEDIA / (outname + ".mp4")
            run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-f", "concat", "-safe", "0", "-i", str(playlist),
                "-c", "copy", "-movflags", "+faststart", str(output), timeout=65)
            if output.stat().st_size < 100_000:
                raise RuntimeError(f"Invalid output {outname}")
            # Still fallback is from the REAL video, not a simulated animation.
            poster = MEDIA / (outname + "-poster.jpg")
            run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-ss", "2.0", "-i", str(output), "-frames:v", "1",
                "-q:v", "4", str(poster), timeout=25)
            print("Created", output.name, output.stat().st_size,
                  "bytes; still", poster.stat().st_size, flush=True)
    print("NASA documentary background reels ready.", flush=True)

if __name__ == "__main__":
    main()
