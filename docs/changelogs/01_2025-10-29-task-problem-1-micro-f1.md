# Changelog: 01_2025-10-29 - Micro-F1 Helper (Problem-1)

**Task:** [[Problem-1]] Implement Micro-F1 helper function  
**Status:** Done

### Files Updated:
- **CREATED:** `problem_1_micro_f1/micro_f1.py` – Added micro-F1 implementation with stepwise business-context commentary.
- **UPDATED:** `problem_1_micro_f1/micro_f1.py` – Added manual smoke-test harness with expected outputs inline.
- **CREATED:** `problem_1_micro_f1/README.md` – Documented problem statement and CEO-friendly explanations for core metrics.
- **UPDATED:** `problem_1_micro_f1/README.md` – Added real-world micro-F1 application notes referencing support ticket routing research.
- **CREATED:** `docs/changelogs/01_2025-10-29-task-problem-1-micro-f1.md` – Recorded rationale, decisions, and validation notes for Problem #1.

### Description:
Delivered the initial micro-F1 utility and supporting documentation tailored for non-technical leadership, establishing the reference solution for Problem #1. Source: https://www.tensortonic.com/problems/metrics-f1-micro

Supplemented documentation with external research (Open Ticket AI, Oct 2025) to show micro-F1 in production ticket triage systems.

### Reasoning:
Prioritised a minimal, readable implementation with direct explanations to align with the requirement for clarity and leadership-friendly framing.

### Key Decisions & Trade-offs:
- Chose a single-pass loop to count matches and mismatches, trading minor redundancy for transparency and auditability.
- Returned 0.0 when no positive predictions exist to avoid division errors while keeping behaviour explicit.

### Implementation Details:
- Validates equal-length, non-empty inputs before computation.
- Counts true positives and mismatches, mapping mismatches to both false positives and false negatives in the single-label scenario.
- Applies the micro-F1 formula using Python primitives only, ensuring performance up to 10⁵ items.

### Testing:
- Formal automated tests not run (not requested). Manual reasoning validated sample scenarios from specification.

### Follow-up:
- Extend changelog series as additional problems are completed to maintain historical traceability.
