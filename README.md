# GeoFrontier Analytics

Website for **GeoFrontier Analytics**, a proposed scientific consultancy and capacity building initiative focused on Earth observation, GPS and GNSS field positioning, environmental monitoring, forecasting support, geospatial data and responsible AI education.

Live URL (after GitHub Pages deployment): https://stephen-nyaranga.github.io/geofrontier-analytics/

## Main website architecture

| Page | Purpose |
| --- | --- |
| `index.html` | Company introduction, mission and vision, core capabilities, focus areas, links to other pages |
| `services.html` | Earth observation, GPS/GNSS field positioning, InSAR, climate analytics, forecasting and monitoring, data/AI; methods, deliverables, limitations and engagements |
| `monitoring.html` | Proposed flood monitoring, ENSO and La Niña climate-driver monitoring, subseasonal forecasts, drought, extreme heat and environmental observation. Explicitly separates analytical support from official warnings. |
| `education.html` | Proposed Earth observation and AI learning pathways for primary and secondary schools, TVET institutions, colleges, universities and educators, with safeguarding and no accreditation claims. |
| `sectors.html` | Government, energy/infrastructure, environment, agriculture/water, research; intended applications and limits |
| `approach.html` | Workflow, scientific quality standards, deliverables, collaboration and data safeguards |
| `insights.html` | Original technical explainers, links to data sources, a glossary and the independent forecasting initiative |
| `forecasting.html` | An explicitly attributed, independent ECMWF AI Weather Quest competition project by the founder, with methods, reported results and limitations. It is not GeoFrontier client work or a commercial forecasting product. |
| `about.html` | Proposed mission, vision, strategic goals, company values, founder, unfilled team and leadership, business readiness |
| `contact.html` | Enquiry guidance, partnership pathways, founder's existing professional contact route and current business-status notice |
| `privacy.html` | Accurate website information and privacy notice |
| `media-credits.html` | Scientific images, source links, usage notes and a transparent documentary media register |
| `sitemap.xml` | Current pages for discovery |

## Active assets

- `assets/geofrontier-orbital-logo.png` — approved GF monogram, circular mark and separate satellite
- `assets/favicon.svg` — compact GF/favicon mark
- `css/site-v2.css` — active responsive styling
- `js/site-v2.js` — mobile navigation, year and viewport-aware documentary video playback
- `assets/media/` — locally optimised USGS and NASA imagery and historical NASA video
- `scripts/cache_media.py` — download and optimise only approved, source-attributed media
- `.github/workflows/media-cache.yml` — optional media caching workflow using a trusted GitHub runner
- `docs/GNSS_AND_MEDIA_IMPLEMENTATION.md` — page-by-page placement, links and code examples

The homepage's Apollo 17 Earth photograph is linked with NASA public-domain credit and a source URL. The founder portrait comes from the founder's own public website.

## Editorial safeguards

- **Do not publish PhD work or portray the founder's personal research as GeoFrontier client contracts.** The single forecasting initiative is displayed by the founder's explicit request and prominently labelled independent competition work.
- The business is described as **in development**, not incorporated or procurement-qualified unless this can be verified.
- Founder: Stephen Nyaranga. Team and Leadership positions must remain unfilled until confirmed.
- Avoid fictional employees, addresses, contact details, contracts, testimonials, registrations, certificates, quantitative project outcomes or client endorsements.
- Documentary NASA/USGS photos and video must remain visibly source-attributed and must not be described as GeoFrontier's own work. GNSS mapping is not a claim to be licensed for regulated land surveying in Kenya.
- Service and sector applications are prospective rather than claims of completed commercial delivery.
- The GeoFrontier Learning Initiative is a proposed programme with no confirmed partner institutions, completed cohorts or accredited qualifications.
- For programmes involving minors, host-institution supervision, parental and institutional permissions where required, data minimisation and age-appropriate technology are essential.
- **Keep the founder’s business model, pricing, funding structure, entity options and internal strategy document private. Do not publish those plans to the website.**
- Forecast interpretation and hazard monitoring services must cite sources, issue times, uncertainty, validation status and lead times. GeoFrontier does not currently provide 24/7 alerts, official hazard warnings or guaranteed live forecasts.
- Public warnings and emergency directives remain with authorised national meteorological, hydrological and disaster-management authorities.
- Any future project needs a verifiable source and permission to publish images, results, datasets and partner names.

## Company mission and goals

The proposed mission and vision and six strategic goals are published in the About page. Their wording should be reviewed by the founder before formal incorporation and used consistently in external materials.

## Deployment and maintenance

Static site, served from `main` at repository root through GitHub Pages. No build system or authentication secrets are required.

To preview locally: `python -m http.server 8000`, then open `http://localhost:8000`.

Before a formal business launch, verify name clearance and registration with Kenya's Business Registration Service, determine applicable tax/permit/data protection obligations, assess procurement eligibility, and establish an official company email and privacy-compliant enquiry system.

## Audit checklist

Verify all local links and anchored sections, image/video source credits, local media assets, approved logo, mobile navigation, age-appropriate education claims, academic-project exclusion, clear separation of forecasting competition work and proposed consulting services, mission/vision/values presence, empty Team/Leadership, and successful GitHub Pages deployment after each substantive change.
