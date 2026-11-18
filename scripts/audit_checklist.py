#!/usr/bin/env python3
"""
Modern Web & AI Architecture Readiness Auditor
Evaluates a web project configuration against Performance, AI, and Security pillars.
"""

import json
import sys
from dataclasses import dataclass, asdict


@dataclass
class AuditInput:
    lcp_seconds: float
    inp_milliseconds: float
    cls_score: float
    uses_streaming_ai: bool
    uses_semantic_cache: bool
    has_rate_limiting: bool
    sanitizes_llm_output: bool
    exposes_api_keys_client: bool


def evaluate_architecture(data: AuditInput) -> dict:
    score = 100
    findings = []

    # 1. Performance Pillar
    if data.lcp_seconds > 2.5:
        score -= 15
        findings.append(f"[PERFORMANCE] High LCP ({data.lcp_seconds}s > 2.5s): Optimize hero asset delivery and SSR.")
    if data.inp_milliseconds > 200:
        score -= 15
        findings.append(f"[PERFORMANCE] Sluggish INP ({data.inp_milliseconds}ms > 200ms): Break up long main-thread JS tasks.")
    if data.cls_score > 0.1:
        score -= 10
        findings.append(f"[PERFORMANCE] Layout instability (CLS {data.cls_score} > 0.1): Reserve explicit dimensions for media/AI containers.")

    # 2. AI Pillar
    if not data.uses_streaming_ai:
        score -= 10
        findings.append("[AI UX] Blocking AI responses detected: Implement SSE/WebSocket streaming to lower perceived latency.")
    if not data.uses_semantic_cache:
        score -= 5
        findings.append("[AI SCALE] No semantic caching: Add vector cache to reduce repetitive LLM token costs.")

    # 3. Security Pillar
    if data.exposes_api_keys_client:
        score -= 25
        findings.append("[CRITICAL SECURITY] API keys exposed in client bundle: Move all LLM calls behind a secure backend proxy.")
    if not data.has_rate_limiting:
        score -= 10
        findings.append("[SECURITY] Missing rate limiting: Enforce per-user/IP quotas to prevent Denial of Wallet attacks.")
    if not data.sanitizes_llm_output:
        score -= 10
        findings.append("[SECURITY] Unsanitized LLM output: Use DOMPurify before rendering AI-generated HTML/Markdown.")

    status = "PRODUCTION READY" if score >= 85 else "NEEDS OPTIMIZATION" if score >= 60 else "HIGH RISK"
    return {
        "readiness_score": max(score, 0),
        "status": status,
        "findings": findings,
    }


if __name__ == "__main__":
    # Sample baseline audit when executed directly without arguments
    sample = AuditInput(
        lcp_seconds=2.8,
        inp_milliseconds=240,
        cls_score=0.05,
        uses_streaming_ai=True,
        uses_semantic_cache=False,
        has_rate_limiting=True,
        sanitizes_llm_output=False,
        exposes_api_keys_client=False,
    )
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            raw = json.load(f)
            sample = AuditInput(**raw)

    report = evaluate_architecture(sample)
    print(json.dumps(report, indent=2))
