# OWASP LLM Top 10 — Security Research

This directory documents hands-on security research performed against the AI application.

Each research case follows an iterative security engineering methodology:

> **Attack → Observe → Root Cause → Mitigate → Re-Attack → Bypass Test → Regression Test**

The objective is not only to identify vulnerabilities, but also to evaluate the effectiveness of defensive controls, document observed behaviors, implement mitigations where appropriate, and verify that fixes remain effective through regression testing.

| Attack / Vulnerability                                                 | Root Cause & Security Impact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Mitigation & Current Result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Detailed Research                                                                                                 |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Ignore Previous Instructions / Direct Instruction Override**         | User-controlled instructions may attempt to override higher-priority application policies. If successful, this can alter intended model behavior and potentially expose sensitive data or privileged capabilities when chained with tools, RAG, memory, or agents.                                                                                                                                                                                                                                               | Implemented structured system-prompt policy enforcement with instruction hierarchy and protected-information rules. **Result:** **2/2** tested direct override payloads blocked; **0/2** OS disclosures; **0/2** observed `get_os` executions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [View Research](./llm01-prompt-injection/01-direct-prompt-injection/ignore-previous-instructions.md)              |
| **Persona Adoption / Roleplay / DAN Jailbreak**                        | Semantic reframing can manipulate model behavior without explicitly overriding system instructions. Testing produced fabricated protected system information and possible multi-turn persona persistence, although no real OS disclosure or unauthorized `get_os` execution occurred.                                                                                                                                                                                                                            | **Mitigation not yet implemented.** Existing prompt-level controls were evaluated. **Result:** **0/6** real OS disclosures and **0/6** observed `get_os` executions, but behavioral bypasses occurred in **3/6** scenarios through hallucinated protected information or persona compliance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [View Research](./llm01-prompt-injection/02-semantic-jailbreaks/persona-roleplay-jailbreak.md)                    |
| **Instruction Hierarchy Manipulation & Conflict Exploitation**         | Attackers may attempt to impersonate trusted instruction sources (System, Developer, Administrator, Security Policy) or manipulate instruction priority to influence model behavior. Even when protected capabilities remain inaccessible, reasoning inconsistencies may cause contradictory responses, fake tool invocations, or fabricated protected information that could mislead users or downstream systems.                                                                                               | Implemented prompt-level instruction hierarchy hardening, trusted-context rules, authorization policy, and enhanced safety guardrails. **Result:** **7** attack scenarios evaluated. **0/7** observed `get_os` executions and **0/7** real OS disclosures. Fake system messages, fake developer messages, authority impersonation, and policy replacement attacks were prevented from executing the protected tool. Behavioral inconsistencies such as hallucinated tool calls and fabricated protected information were still observed. **Application-level authorization intentionally deferred to a later hardening phase.**                                                                                                                                                                                                      | [View Research](./llm01-prompt-injection/03-instruction-hierarchy-conflict/instruction-hierarchy-manipulation.md) |
| **Obfuscated Prompt Injection (Encoding & Character Transformations)** | Obfuscated payloads attempt to evade application-level keyword filters by transforming malicious instructions using encodings or Unicode manipulations before reaching the LLM. Security impact depends on whether the application canonicalizes input before validation and whether the model reconstructs the hidden instruction. Testing demonstrated that naive keyword matching is vulnerable to several obfuscation techniques, while model behavior varied significantly depending on the transformation. | **Seven obfuscation techniques evaluated.** **Base64, Hex, URL Encoding, Unicode Escape, and ROT13** did **not** result in successful prompt injection. **Zero-Width Character** and **Unicode Homoglyph** attacks successfully bypassed the application's keyword-based validator and reached the LLM, demonstrating a weakness in application-layer validation. However, the XML system prompt, protected tool authorization, and instruction hierarchy prevented system prompt disclosure and unauthorized `get_os` execution in every case. **Recommended mitigation:** Unicode normalization, removal of invisible characters, canonicalization before validation where applicable, semantic prompt injection detection, strict prompt isolation, and tool-level authorization rather than relying solely on keyword filtering. | [View Research](./llm01-prompt-injection/04-obfuscated-prompt-injection/)                                         |

---

# Obfuscated Prompt Injection Research Summary

The following techniques were evaluated during the obfuscated prompt injection research.

| Technique                 | Application Filter    | Prompt Reached LLM | Prompt Injection | Notes                                                                                                                                                 |
| ------------------------- | --------------------- | ------------------ | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Base64**                | ✅ Bypassed           | ⚠️ Partially       | ❌ Failed        | Model inconsistently decoded Base64 and did not execute hidden instructions.                                                                          |
| **Hex Encoding**          | ✅ Bypassed           | ⚠️ Yes             | ❌ Failed        | Model failed to reliably decode hexadecimal payloads and occasionally hallucinated decoded content.                                                   |
| **URL Encoding**          | ✅ Bypassed           | ⚠️ Yes             | ❌ Failed        | Model generally requested clarification instead of decoding URL-encoded instructions.                                                                 |
| **Unicode Escape**        | ❌ Blocked            | ❌ No              | ❌ Failed        | JSON parsing canonicalized `\uXXXX` sequences before validation, allowing the validator to detect the original blocked keywords.                      |
| **Zero-Width Characters** | ❌ Validator Bypassed | ✅ Yes             | ❌ Failed        | Invisible Unicode characters bypassed substring matching. LLM understood the recovered instruction but system prompt protections prevented execution. |
| **Unicode Homoglyphs**    | ❌ Validator Bypassed | ✅ Yes             | ❌ Failed        | Confusable Unicode characters bypassed validation. LLM correctly interpreted the text, but protected resources remained inaccessible.                 |
| **ROT13**                 | ❌ Validator Bypassed | ✅ Yes             | ❌ Failed        | LLM recognized ROT13 but failed to accurately decode it, hallucinating unrelated plaintext instead of reconstructing the original instruction.        |

---

# Overall Findings

The obfuscated prompt injection experiments demonstrate several important security observations:

- Simple keyword-based validation is vulnerable to Unicode-based obfuscation.
- Canonicalization order significantly affects detection capability.
- Different obfuscation techniques trigger fundamentally different LLM behaviors.
- Recognizing an encoding does **not** guarantee deterministic decoding.
- Prompt-level defenses alone should not be considered sufficient security controls.
- Protected tool authorization remained effective across all evaluated attacks.
- XML system prompt isolation successfully prevented system prompt disclosure throughout all experiments.

---

# Research Status

| Category                                 | Status       |
| ---------------------------------------- | ------------ |
| Direct Prompt Injection                  | ✅ Completed |
| Semantic Jailbreaks / Persona Attacks    | ✅ Completed |
| Instruction Hierarchy Manipulation       | ✅ Completed |
| Obfuscated Prompt Injection              | ✅ Completed |
| • Base64                                 | ✅ Completed |
| • Hex Encoding                           | ✅ Completed |
| • URL Encoding                           | ✅ Completed |
| • Unicode Escape                         | ✅ Completed |
| • Zero-Width Character Injection         | ✅ Completed |
| • Unicode Homoglyph Attacks              | ✅ Completed |
| • ROT13                                  | ✅ Completed |
| Indirect Prompt Injection                | ⏳ Planned   |
| Multi-turn Prompt Injection              | ⏳ Planned   |
| Agent / Tool Prompt Injection            | ⏳ Planned   |
| Application-Level Authorization Controls | ⏳ Planned   |
| Regression Testing                       | ⏳ Planned   |
