# Moodle LMS & AI Integration Architecture Guide

## 1. Performance & Responsiveness in Moodle (PHP + AMD JS)
- **Moodle Universal Cache (MUC):** Offload expensive database queries (`$DB->get_records_sql`) and external API metadata into MUC (`cache::make()`) backed by Redis or Memcached. Never execute uncached queries inside course view loops or custom blocks.
- **AMD / ES6 Module Hygiene (INP Optimization):**
  - Place custom JavaScript inside `amd/src/` and compile via Grunt/Rollup (`amd/build/`).
  - Lazy-load heavy UI components (e.g., AI chat widgets, interactive charts) using `core/fragment` or dynamic imports only when the user clicks to open them, keeping initial course page INP under $200\text{ms}$.
- **Mustache Templates:** Keep logic out of templates. Pre-process view data in PHP `renderable` / `templatable` classes to ensure clean separation and fast server-side rendering.

## 2. AI Integration Patterns (RAG & Streaming in Moodle)
- **Non-Blocking Streaming (SSE over PHP):**
  - Standard Moodle External Functions (`core_external\external_api`) buffer the entire HTTP response before returning JSON, causing 10–15s UI freezes for LLM responses.
  - For real-time AI chat/assistants, implement a dedicated lightweight streaming endpoint (e.g., `local/yourplugin/stream.php`) using `header('Content-Type: text/event-stream')`, disabling output buffering (`@ob_end_flush()`), and calling `core\session\manager::write_close()` early so the user's PHP session lock does not block concurrent Moodle navigation.
- **Course-Scoped RAG Pipeline:**
  - Chunk Moodle course resources (`mod_page`, `mod_book`, `mod_resource` PDFs) asynchronously via **Adhoc Tasks** (`\core\task\adhoc_task`) triggered by Moodle Events (`\core\event\course_module_created` / `updated`), never synchronously during teacher file uploads.
  - Store embeddings alongside `courseid`, `cmid` (course module ID), and `contextid` metadata for strict access filtering.

## 3. Moodle Security & OWASP LLM Compliance
- **Capability & Context Enforcement (Row-Level Security):**
  - Every custom endpoint or External Function must enforce `require_login($course, false, $cm)` and verify permissions via `has_capability('local/yourplugin:use', $context)`.
  - Filter vector database retrieval strictly by the `courseid` and `cmid` values the current `$USER` is enrolled in and permitted to view (respecting hidden activities and group restrictions).
- **CSRF & Input/Output Sanitization:**
  - Validate `sesskey()` on all state-changing or AI-triggering endpoints (`require_sesskey()`).
  - Sanitize all incoming user prompts using `required_param(..., PARAM_TEXT)` or `PARAM_RAW` with strict length caps.
  - Sanitize AI-generated Markdown/HTML before rendering in the browser using Moodle's `format_text($response, FORMAT_MARKDOWN, ['context' => $context])` on the backend and `DOMPurify` in AMD JS on the frontend.
- **Secret Management:** Store LLM provider API keys exclusively in Moodle Admin Settings (`get_config('local_yourplugin', 'apikey')`), never exposed in `M.cfg` or AMD module parameters.
