// Offline cache: network first for the page, cache first for static assets.
const CACHE = 'mvb-tuner-v74m';
const ASSETS = ['/', '/index.html', '/manifest.webmanifest', '/favicon.svg', '/icon-192.png', '/icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS))); self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  if (req.mode === 'navigate') {
    const isApp = ['/', '/index.html'].includes(new URL(req.url).pathname);
    e.respondWith(fetch(req).then(r => { if (isApp && r.ok) { const copy = r.clone(); caches.open(CACHE).then(c => c.put('/', copy)); } return r; })
      .catch(() => caches.match(isApp ? '/' : req).then(h => h || caches.match('/'))));
    return;
  }
  e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => {
    if (r.ok && (req.url.startsWith(self.location.origin) || req.url.includes('fonts.g'))) {
      const copy = r.clone(); caches.open(CACHE).then(c => c.put(req, copy));
    }
    return r;
  })));
});
