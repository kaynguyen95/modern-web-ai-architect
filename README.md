# Modern Web & AI Solution Architect Skill

An open-source AI Agent Skill designed to transform coding assistants (Claude Code, Cursor, Windsurf, Gemini CLI, etc.) into a Senior Web & AI Solution Architect.

## Core Capabilities
- **Web Performance & Responsiveness:** Diagnoses Core Web Vitals bottlenecks (LCP, INP, CLS) and recommends modern rendering patterns (Streaming SSR, Islands Architecture).
- **AI-Native Web Engineering:** Guides implementation of Hybrid AI (WebGPU/Wasm + Cloud LLMs), Streaming/Generative UI, RAG pipelines, and Semantic Caching.
- **Security & Governance:** Enforces OWASP Top 10 for LLMs alongside traditional web security headers (CSP, CORS, WebAuthn).

## Repository Structure
```text
modern-web-ai-architect/
├── SKILL.md                                # Core instructions & trigger metadata
├── README.md                               # Documentation & installation guide
├── references/                             # Progressive-disclosure domain knowledge
│   ├── core-web-vitals.md                  # Performance metrics & rendering patterns
│   ├── ai-web-patterns.md                  # Hybrid AI, Streaming UI & RAG architectures
│   └── owasp-llm-security.md               # AI & Web security hardening checklists
├── scripts/
│   └── audit_checklist.py                  # CLI readiness & architecture scoring script
└── assets/
    └── architecture-review-template.md     # Standardized output template for reviews
