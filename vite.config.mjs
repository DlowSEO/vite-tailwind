import { readdirSync, statSync } from "node:fs";
import { join, relative, resolve } from "node:path";
import { defineConfig } from "vite";

const root = resolve(import.meta.dirname, "src");

// Every index.html under src/ becomes its own page (multi-page build).
function findPages(dir, pages = {}) {
  for (const entry of readdirSync(dir)) {
    if (entry === "public") continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) findPages(full, pages);
    else if (entry === "index.html") {
      const name = relative(root, dir) || "home";
      pages[name] = full;
    }
  }
  return pages;
}

export default defineConfig({
  server: {
    open: "/index.html",
  },
  build: {
    outDir: "../dist",
    emptyOutDir: true,
    rollupOptions: {
      input: findPages(root),
    },
  },
  root: "src",
});
