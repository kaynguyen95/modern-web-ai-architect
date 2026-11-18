#### `references/core-web-vitals.md`
```markdown
# Web Performance & Responsiveness Reference

## 1. Core Web Vitals Thresholds (2025/2026 Standards)
| Metric | Measures | Good | Needs Improvement | Poor |
| :--- | :--- | :--- | :--- | :--- |
| **LCP** (Largest Contentful Paint) | Loading performance | $\le 2.5\text{s}$ | $2.5\text{s} - 4.0\text{s}$ | $> 4.0\text{s}$ |
| **INP** (Interaction to Next Paint) | Runtime responsiveness | $\le 200\text{ms}$ | $200\text{ms} - 500\text{ms}$ | $> 500\text{ms}$ |
| **CLS** (Cumulative Layout Shift) | Visual stability | $\le 0.1$ | $0.1 - 0.25$ | $> 0.25$ |

## 2. Optimizing INP (Main Thread Hygiene)
- **Break Up Long Tasks:** Any JavaScript execution exceeding $50\text{ms}$ blocks the main thread. Yield to the main thread using `scheduler.yield()` or `setTimeout(..., 0)` during heavy state updates.
- **Minimize Hydration Cost:** Avoid full-page hydration for static content. Prefer **Islands Architecture** (Astro, Fresh) or **Resumability** (Qwik) or **React Server Components (RSC)**.
- **Web Workers for Heavy Compute:** Offload client-side JSON parsing, Markdown rendering, and local vector similarity calculations to Web Workers.

## 3. Modern Rendering & Caching Patterns
- **Streaming SSR:** Flush initial HTML shell and critical CSS immediately (`Transfer-Encoding: chunked`), streaming slow database or AI-generated components as they resolve.
- **Stale-While-Revalidate (SWR):** Serve cached edge responses instantly while refreshing data asynchronously in the background via `Cache-Control: public, s-maxage=60, stale-while-revalidate=300`.
- **Network Transport:** Enforce HTTP/3 (QUIC) and Brotli/Zstd compression for static assets.
