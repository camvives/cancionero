const CACHE_NAME = "cancionero-v1";
const CORE_ASSETS = [
  "./",
  "./assets/estilos.css",
  "./assets/buscador.js",
  "./assets/chordsheetjs.js",
  "./assets/transponer.js",
  "./assets/logo-cip.png",
  "./assets/icon-192.png",
  "./assets/icon-512.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(CORE_ASSETS);
    await self.skipWaiting();
  })());
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const cacheNames = await caches.keys();
    await Promise.all(
      cacheNames
        .filter((name) => name.startsWith("cancionero-") && name !== CACHE_NAME)
        .map((name) => caches.delete(name))
    );
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const request = event.request;
  const requestUrl = new URL(request.url);

  if (request.method !== "GET" || requestUrl.origin !== self.location.origin) {
    return;
  }

  event.respondWith((async () => {
    try {
      const response = await fetch(request);
      if (response.ok && response.type === "basic") {
        event.waitUntil(
          caches.open(CACHE_NAME).then((cache) => cache.put(request, response.clone()))
        );
      }
      return response;
    } catch (error) {
      const cachedResponse = await caches.match(request);
      if (cachedResponse) {
        return cachedResponse;
      }

      if (request.mode === "navigate") {
        const offlinePage = await caches.match("./");
        if (offlinePage) {
          return offlinePage;
        }
      }

      throw error;
    }
  })());
});
