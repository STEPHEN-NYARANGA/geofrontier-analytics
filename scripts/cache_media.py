#!/usr/bin/env python3
"""Cache approved NASA/USGS educational images in GitHub Pages assets.

This script is intended for a trusted GitHub Actions runner. It downloads only
the explicit third-party media URLs recorded here, converts images to modest
WebP assets, and rewrites HTML source attributes ONLY after each file succeeds.
Sources, author/agency credits and terms remain linked in media-credits.html.
"""
from __future__ import annotations

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "assets" / "media"
MEDIA.mkdir(parents=True, exist_ok=True)
PAGES = [
    "index.html", "services.html", "monitoring.html", "education.html",
    "sectors.html", "about.html", "approach.html", "insights.html",
    "forecasting.html", "contact.html", "privacy.html", "media-credits.html",
]
SOURCES = [
    ("gnss-receiver", "https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/images/20221102_113357.jpg"),
    ("gps-field", "https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/200703_CA_GPS.JPG"),
    ("gps-backpack", "https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/images/EN7BackpackGPS.jpg"),
    ("mozambique-flood-2026", "https://assets.science.nasa.gov/dynamicimage/assets/science/esd/eo/images/iotd/2026/floods-inundate-southern-mozambique/mozambiqueflood_amo_20260125_lrg.jpg?crop=faces%2Cfocalpoint&fit=clip&h=1659&w=2155"),
    ("mozambique-pre-flood-2025", "https://assets.science.nasa.gov/dynamicimage/assets/science/esd/eo/images/iotd/2026/floods-inundate-southern-mozambique/mozambiqueflood_tmo_20251217_lrg.jpg?crop=faces%2Cfocalpoint&fit=clip&h=1659&w=2155"),
    ("gibs-sst", "https://raw.githubusercontent.com/nasa-gibs/gibs-web-examples/main/examples/cesium/gibs-layers/images/sea_surface_temperature.png"),
    ("gibs-landtemp", "https://raw.githubusercontent.com/nasa-gibs/gibs-web-examples/main/examples/cesium/gibs-layers/images/land_surface_temperature_day.png"),
    ("suomi-npp", "https://raw.githubusercontent.com/nasa/api-docs/gh-pages/assets/img/general/global_suomi_NPP.png"),
    ("gibs-terra", "https://raw.githubusercontent.com/nasa-gibs/gibs-web-examples/main/examples/cesium/gibs-layers/images/terra_corrected_reflectance.png"),
    ("gibs-night", "https://raw.githubusercontent.com/nasa-gibs/gibs-web-examples/main/examples/cesium/gibs-layers/images/earth_at_night.png"),
    ("mozambique-flood-2000-still", "https://svs.gsfc.nasa.gov/vis/a000000/a001200/a001235/a001235_sidebyside_still.jpg"),
]
VIDEO = (
    "mozambique-flood-comparison-2000",
    "https://svs.gsfc.nasa.gov/vis/a000000/a001200/a001235/a001235_sidebyside.mp4",
)

def get_bytes(url: str, max_size: int = 20_000_000) -> bytes:
    req = Request(url, headers={"User-Agent": "GeoFrontierAnalytics/1.0 (website image cache; source-attributed)", "Accept": "*/*"})
    with urlopen(req, timeout=45) as response:
        size = response.headers.get("Content-Length")
        if size and int(size) > max_size:
            raise ValueError("Asset exceeds maximum permitted size")
        result = response.read(max_size + 1)
    if len(result) > max_size:
        raise ValueError("Download is too large")
    return result

from PIL import Image, ImageOps

replacements = {}
success = []
failed = []
for name, url in SOURCES:
    try:
        im = Image.open(BytesIO(get_bytes(url)))
        im.verify()
        im = Image.open(BytesIO(get_bytes(url)))
        im = ImageOps.exif_transpose(im)
        im.thumbnail((1520, 1100), Image.Resampling.LANCZOS)
        out = MEDIA / (name + ".webp")
        im.convert("RGB").save(out, "WEBP", quality=80, method=6)
        if out.stat().st_size < 5000:
            raise ValueError("Unusually small output")
        replacements['src="' + url + '"'] = 'src="assets/media/' + out.name + '"'
        replacements['poster="' + url + '"'] = 'poster="assets/media/' + out.name + '"'
        success.append((name, out.stat().st_size))
    except Exception as exc:
        failed.append((name, str(exc)))
        print("Unable to cache", name, repr(exc))

try:
    name, url = VIDEO
    original = MEDIA / (name + "-original.mp4")
    original.write_bytes(get_bytes(url, max_size=18_000_000))
    dst = MEDIA / (name + ".mp4")
    # Short mute loop, modest bandwidth. The source is a historical NASA
    # SVS animation of Mozambique flooding in 1999 and 2000.
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(original),
         "-t", "12", "-an", "-vf", "scale=w=640:h=-2:flags=lanczos",
         "-c:v", "libx264", "-preset", "slow", "-crf", "26", "-movflags", "+faststart", str(dst)],
        check=True, timeout=95,
    )
    original.unlink()
    if dst.stat().st_size < 10000:
        raise ValueError("Encoded video too small")
    replacements['src="' + url + '"'] = 'src="assets/media/' + dst.name + '"'
    success.append((name, dst.stat().st_size))
except Exception as exc:
    failed.append(("flood-video", str(exc)))
    print("Unable to cache flood video:", repr(exc))
    try:
        original.unlink(missing_ok=True)
    except NameError:
        pass

for page in PAGES:
    path = ROOT / page
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    changed = text
    for src, local in replacements.items():
        changed = changed.replace(src, local)
    if changed != text:
        path.write_text(changed, encoding="utf-8")
print("Saved:", success)
print("Uncached:", failed)
if not success:
    raise SystemExit("No third-party assets could be cached")
