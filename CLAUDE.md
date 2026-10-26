# Working on MVB Tuner

- Everything lives in `index.html` (CSS + one inline script). No build step; Netlify serves the repo root from `main`.
- Two builds: `main` = with MIDI, branch `no-midi` = without MIDI. Apply shared changes to both.
- Every release: bump the version in the footer line ("Version NN · © 2026 Michael Van Bebber…") and the cache name in `sw.js` (`mvb-tuner-vNNm` on main, `mvb-tuner-vNN` on no-midi).
- Test through a local server (`python3 -m http.server`), not file:// — impulse responses in `ir/` fail to load from disk.
- The owner wants short, plain replies and American spelling.
