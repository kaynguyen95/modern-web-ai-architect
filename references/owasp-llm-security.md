# Web & LLM Security Hardening Guide

## 1. OWASP Top 10 for LLM Applications (Web Context)
1. **LLM01: Prompt Injection**
   - *Risk:* Malicious user input or retrieved RAG documents hijack system instructions.
   - *Mitigation:* Separate system instructions from untrusted user/document data using strict XML/delimiter tags; apply least-privilege permissions to all AI tool calls.
2. **LLM02: Sensitive Information Disclosure**
   - *Risk:* Model leaks API keys, system prompts, or cross-tenant RAG data.
   - *Mitigation:* Enforce Row-Level Security (RLS) on vector database queries *before* retrieval; sanitize outputs with regex/DLP filters.
3. **LLM05: Improper Output Handling**
   - *Risk:* LLM generates malicious `<script>` tags or SQL payloads executed by the browser/backend.
   - *Mitigation:* Treat all LLM outputs as untrusted user input. Sanitize rendered Markdown/HTML with `DOMPurify` and use parameterized queries.
4. **LLM10: Unbounded Consumption (Denial of Wallet)**
   - *Risk:* Attackers spam expensive AI endpoints, exhausting token budgets.
   - *Mitigation:* Implement per-user/IP rate limiting at the API Gateway, set strict `max_tokens` limits, and enforce monthly spend caps.

## 2. Essential Web Security Headers
- **Content-Security-Policy (CSP):** Restrict script execution (`script-src 'self'`) and restrict `connect-src` strictly to authorized API and LLM inference domains.
- **Authentication:** Use `HttpOnly`, `Secure`, `SameSite=Strict` cookies or Passkeys (WebAuthn); never store LLM provider API keys in client-side JavaScript bundles.
