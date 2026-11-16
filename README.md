# GeoFrontier Analytics — website prototype

A responsive, original static website for **GeoFrontier Analytics**, a provisional geospatial AI and Earth intelligence company. This is a development prototype; it is not an assertion of incorporation, commercial history, or operational certifications.

## Files

- `index.html` — homepage
- `services.html` — service areas
- `projects.html` — proposed portfolio and case-study themes
- `about.html` — approach and business status
- `contact.html` — prototype enquiry form
- `css/styles.css` — shared visual design and responsive layouts
- `js/main.js` — mobile menu, date, and email-draft form behavior
- `assets/earth-africa.png` — original Earth-centred rendering produced from the bundled NASA Blue Marble Next Generation image in Basemap; base image credit: NASA Earth Observatory
- `assets/favicon.svg` — original provisional brand icon

## Run locally

Open `index.html` in a browser. For reliable local testing, from this folder run:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploy on GitHub Pages

1. Create a new repository and add the contents of this folder at its root.
2. Commit and push to the default branch.
3. In **Settings → Pages**, deploy from the selected branch and repository root.
4. Update the published website URL and optionally connect a domain after verification.

No frameworks, databases, secrets, paid APIs, or build steps are required.

## Before publishing for business use

- Verify name and trademark availability; confirm incorporation and relevant regulatory statements.
- Replace provisional copy with approved business details and founder profile.
- Configure a real business email in `contact.html` (`data-email="..."`) or install a privacy-compliant contact backend. Until configured, the form displays a setup message and does not transmit data.
- Review privacy and cookie obligations before adding analytics or data-collection services.
- Publish actual, approved case studies with documented sources, licensing, validation and permissions.
- Check public image attribution/licensing for any new visual assets.

## Attribution

The globe is generated from the NASA Blue Marble Next Generation image included with `mpl_toolkits.basemap_data`. Design, layout and logo are original and are *not* copies of UP42 branding. The screenshot shared for inspiration is intentionally not incorporated into the live site.