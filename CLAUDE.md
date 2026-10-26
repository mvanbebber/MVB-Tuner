# Working on MVB Tuner

- Everything lives in `index.html` (CSS + one inline script). No build step; Netlify serves the repo root from `main`.
- One build only, always with MIDI keyboard support.
- Every release: bump the version in the footer line ("Version NN · © 2026 Michael Van Bebber…") and the cache name in `sw.js` (`mvb-tuner-vNNm`).
- Test through a local server (`python3 -m http.server`), not file:// — impulse responses in `ir/` fail to load from disk.
- The owner wants short, plain replies and American spelling.
