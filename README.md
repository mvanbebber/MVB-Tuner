# MVB Tuner — pureintonation.com

Free pure (just) intonation tuner and chord drone by Michael Van Bebber.
Single-file web app (`index.html`) plus a service worker, icons and room impulse responses (`ir/`).

- `main` — the live site (with MIDI keyboard support). Netlify deploys every push to `main`.
- `no-midi` — the same app without MIDI support.

No build step: Netlify publishes this folder as-is (`netlify.toml`).
