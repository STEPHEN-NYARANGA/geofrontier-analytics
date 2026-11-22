# GeoFrontier Analytics: GPS/GNSS and Scientific Media Update

**Date:** 22 November 2026
**Scope:** Existing GitHub Pages website, `main` branch.
**Status:** Implemented. Local assets are the authoritative copy when cached; source-page links provide provenance.

## Editorial and accuracy principles

- GPS is the United States' Global Positioning System and one constituent of the broader GNSS family. Position accuracy depends on receiver, configuration, corrections, geometry and site conditions.
- Do not promise centimetre accuracy simply because GNSS equipment is mentioned.
- Cadastral surveying and other regulated survey work in Kenya must only be performed by appropriately licensed professionals.
- Depicted scientific agency field teams and satellite scenes are **documentary examples**, never GeoFrontier staff, contracts or project evidence.
- Do not publish the founder's PhD research, private company business model or unconfirmed partner/team details.
- The source register is public at `media-credits.html`; the approved GF-satellite logo is unchanged.

## Page by page implementation

| Page | Content inserted | Near-bottom media and purpose |
| --- | --- | --- |
| `index.html` | GPS/GNSS bridge between field evidence and satellite analysis; link to GNSS service | GNSS receiver, NASA 2026 Mozambique flood, NASA Suomi NPP global view |
| `services.html` | `#gnss` full service: methods, possible deliverables and accuracy/legal boundary | GPS fieldworker, GNSS receiver, NASA GIBS corrected-reflectance imagery |
| `monitoring.html` | GNSS for field checks, reference observations and monitoring-site mapping | MODIS pre-flood and flood scenes, historical Landsat Mozambique comparison video |
| `education.html` | `#field-positioning` for school GPS exercises, college GIS data capture and university GNSS uncertainty | GPS fieldworker, NASA land-surface temperature example, Suomi NPP |
| `sectors.html` | GNSS references in public, infrastructure and education sector applications | GPS coastal survey, NASA Mozambique flood, NASA nighttime lights |
| `about.html` | Include field positioning in the scientific scope, without implying survey licensing | GNSS receiver, NASA GIBS reflectance imagery |
| `media-credits.html` | Public sources, original publishers, usage cautions and licence references | Provenance register |
| `privacy.html` | Discloses locally hosted images and remaining external media or links | No gallery |

The main navigation remains unchanged rather than introducing an additional top-level GPS tab. GNSS is linked from the homepage and from the Services anchor.

## Source and cache register

| Local media | Original source and source record | Usage description |
| --- | --- | --- |
| `assets/media/gnss-receiver.webp` | USGS, [GNSS Receiver for Monitoring Land Motion](https://www.usgs.gov/media/images/gnss-receiver-monitoring-land-motion) | Public-domain GNSS instrument photo |
| `assets/media/gps-field.webp` | USGS, [Using GPS in the Field](https://www.usgs.gov/media/images/using-gps-field) | Public-domain field data collection photo |
| `assets/media/gps-backpack.webp` | USGS, [Backpack Precision GPS](https://www.usgs.gov/media/images/beach-survey-backpack-mounted-precision-gps-receiver) | Public-domain coastal field survey photo |
| `assets/media/mozambique-flood-2026.webp` | [NASA Earth Observatory](https://science.nasa.gov/earth/earth-observatory/floods-inundate-southern-mozambique/) | MODIS false colour, 25 January 2026 |
| `assets/media/mozambique-pre-flood-2025.webp` | [NASA Earth Observatory](https://science.nasa.gov/earth/earth-observatory/floods-inundate-southern-mozambique/) | MODIS pre-flood, 17 December 2025 |
| `assets/media/mozambique-flood-comparison-2000.mp4` | [NASA SVS 1235](https://svs.gsfc.nasa.gov/1235/) | Side-by-side historical Landsat 1999/2000 footage; 4.6 MB |
| `assets/media/mozambique-flood-2000-still.webp` | [NASA SVS 1235](https://svs.gsfc.nasa.gov/1235/) | Video poster |
| `assets/media/gibs-terra.webp` | [NASA GIBS GitHub](https://github.com/nasa-gibs/gibs-web-examples) | Corrected reflectance sample map |
| `assets/media/gibs-landtemp.webp` | [NASA GIBS GitHub](https://github.com/nasa-gibs/gibs-web-examples) | Daytime land surface temperature sample |
| `assets/media/gibs-sst.webp` | [NASA GIBS GitHub](https://github.com/nasa-gibs/gibs-web-examples) | Sea surface temperature sample, reserved for future usage |
| `assets/media/nasa-night-lights.webp` | [NASA API Docs GitHub](https://github.com/nasa/api-docs) | Nighttime lights over the USA |
| `assets/media/suomi-npp.webp` | [NASA API Docs GitHub](https://github.com/nasa/api-docs) | Global Earth observation example |

NASA media-use guidelines: https://www.nasa.gov/nasa-brand-center/images-and-media/

These media are not presented as GeoFrontier's own outputs. Original agencies, original sources, source dates and scientific limitations remain visible. NASA/USGS branding is not used in GeoFrontier's identity.

## HTML pattern and CSS references

The galleries already use this source-and-caption pattern:

```html
<section class="visual-evidence" id="field-and-orbit">
  <div class="shell">
    <div class="source-visual-grid">
      <figure class="source-visual-card">
        <div class="source-media">
          <img src="assets/media/gnss-receiver.webp"
               alt="GNSS receiver mounted on a survey tripod"
               loading="lazy" decoding="async">
        </div>
        <figcaption>
          <strong>Positioning on the ground</strong>
          <span>GNSS provides a geodetic reference for mapping.</span>
          <small>USGS, public domain.
            <a href="https://www.usgs.gov/media/images/gnss-receiver-monitoring-land-motion">Original source</a>
          </small>
        </figcaption>
      </figure>
    </div>
  </div>
</section>
```

Media presentation rules in `css/site-v2.css`: `.visual-evidence`, `.source-visual-grid`, `.source-visual-card`, `.source-media`, `.gnss-home`, and `.learning-gnss`.

The historical video uses `<video class="source-video" muted loop playsinline controls preload="none">`. In `js/site-v2.js`, an IntersectionObserver starts playback only while the clip is visible, and playback is disabled for those requesting reduced motion. Visible controls remain for manual playback.

## Updating or adding media

1. Choose an actual scientific image or documented fieldwork photo, not generated stock imagery.
2. Confirm agency, date, description, visual interpretation and exact usage rights.
3. Add the original file URL and a destination filename to `scripts/cache_media.py`.
4. Run the `Cache credited science media` GitHub Actions workflow if needed. The script downloads, checks and optimises images into `assets/media/`, then rewrites matching HTML sources to local files.
5. Review captions, visual crop, alt text, page load speed, source credits and licence restrictions.
6. Confirm that any background/warning visualisation does not imply active forecast or warning services.
7. Verify GitHub Pages has deployed the latest `main` commit.

No private strategy files, founder research figures or child photographs should be included without explicit approval and sufficient permission.


## Selected background photographs and videos (22 November 2026)

The website mixes two types of genuine documentary material behind existing
static text, buttons and navigation. No AI-generated image, faux motion
overlay or additional top-level page structure is required.

| Page | Hero background | Footer background |
| --- | --- | --- |
| Home | A muted, looping NASA Earth-observation video | The same NASA video |
| Expertise | A still USGS GNSS receiver photograph | The same USGS photograph |
| Forecasts & Monitoring | A muted NASA Earth-observation video | A still NASA Mozambique flood satellite image |
| Education | A still NASA Suomi NPP Earth-observation image | The same NASA image |
| All other pages | Existing static design | Existing static design |

The dark overlay is retained for legibility without moving the headings or
buttons. The source images and video are stored in `assets/media/`. Images use
the `.geofrontier-photo-media` class; videos use
`.geofrontier-bg-video`. Existing source documentation remains public at
`media-credits.html`, including original USGS/NASA media pages.

**Video sources:** NASA Johnson, [ISS footage](https://svs.gsfc.nasa.gov/30771/),
and NASA Goddard, [Earth From Space](https://svs.gsfc.nasa.gov/11834/).
**Photographs:** USGS,
[GNSS instrument](https://www.usgs.gov/media/images/gnss-receiver-monitoring-land-motion);
NASA API documentation
[Suomi NPP example](https://github.com/nasa/api-docs);
NASA Earth Observatory,
[2026 Mozambique flooding](https://science.nasa.gov/earth/earth-observatory/floods-inundate-southern-mozambique/).

Videos play without audio only while in view. The browser's reduced-motion
or data-saver settings prevent autoplay and use a static poster instead.
Photographs remain static without any CSS zoom, drift or parallax.

The source document and approved GF-and-satellite company logo are unchanged,
as are the other site sections, company claims, and private-project exclusions.
