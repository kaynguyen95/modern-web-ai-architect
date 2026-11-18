# AI-Powered Web Architecture Patterns

## 1. Hybrid AI Topology (Client + Cloud)
Balance cost, latency, and privacy by splitting workloads:
- **Client-Side (Edge/Browser):** Use **WebGPU**, **WebAssembly (ONNX Runtime Web / Transformers.js)**, or **Chrome Built-in AI (Prompt API)** for:
  - Real-time input autocomplete & grammar checks.
  - Client-side PII redaction before sending prompts to the cloud.
  - Lightweight semantic search over local IndexedDB datasets.
- **Cloud-Side (Server/Edge Functions):** Reserve frontier LLMs for multi-step reasoning, complex RAG synthesis, and tool execution.

## 2. Streaming & Generative UI
- **Token Streaming (SSE / WebSockets):** Never block HTTP responses waiting for full LLM completion. Target **Time to First Token (TTFT) < 500ms**.
- **Generative UI:** Instead of streaming raw markdown walls of text, stream structured JSON/tool calls that dynamically render interactive React/Vue components (charts, comparison tables, action buttons) mid-stream.

## 3. Production Scaling & Latency Reduction
- **Semantic Caching:** Store prompt embeddings and responses in an in-memory vector store (e.g., Redis / Upstash Vector). Return cached responses when cosine similarity $> 0.92$, cutting LLM API costs by 30–60%.
- **Model Routing:** Route simple queries to fast, low-cost models (e.g., Gemini Flash / Haiku) and escalate complex queries to reasoning models.
- **Observability & Evals:** Log TTFT, tokens-per-second (TPS), tool-call failure rates, and user feedback signals for continuous regression testing.
