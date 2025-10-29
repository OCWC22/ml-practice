# Problem #1 — Implement Micro-F1 (Easy)

**Source:** https://www.tensortonic.com/problems/metrics-f1-micro

## 1. What is being asked?
We need a function `micro_f1(y_true, y_pred)` that returns a Python float in the range [0, 1]. The goal is to compute the **micro-averaged F1 score** for single-label, multi-class classification problems.

## 2. What does Micro-F1 mean in business language?
Think of a production line with multiple product categories. For every product coming off the line our system predicts which category it belongs to.

* "True positives" are the items we classified correctly.
* "False positives" are items we incorrectly labeled as a category.
* "False negatives" are items we failed to label as their real category.

**Micro-averaging** aggregates these counts across *all* categories before calculating the F1 score. This weighting ensures that higher-volume categories influence the score proportionally to their real-world frequency.

## 3. Why should leadership care?
* **Balanced signal:** Micro-F1 captures the balance between precision (quality of positive predictions) and recall (coverage of actual positives) across the entire portfolio.
* **Imbalanced data resilience:** When some categories dominate the traffic, micro-F1 reflects true overall performance instead of giving rare categories equal weight.
* **Sanity check:** For our single-label case, micro-precision and micro-recall both equal accuracy. Therefore micro-F1 equals accuracy—the score drops if we make systematic mistakes.

## 4. Concept-by-concept, just-in-time explanation

### True Positive (TP)
Definition: A prediction where the guessed category matches the actual category. Analogy: A factory machine tagging a product with the correct label.

Why it matters: High TP counts signal that the model is doing useful work, keeping customers and stakeholders confident.

### False Positive (FP)
Definition: We guessed a category but were wrong. Analogy: Slapping the wrong sticker on a product.

Why it matters: False positives erode trust—wrong predictions can prompt costly corrections or customer churn.

### False Negative (FN)
Definition: We missed the correct category. Analogy: Letting a product leave the facility without the right label.

Why it matters: Missing real positives can be as damaging as mistakes—we lose opportunities, insight, or compliance.

### Precision
Formula: `precision = TP / (TP + FP)`.

Plain terms: Of the items we flagged as a category, how many truly belonged there? It’s the "quality control" metric.

### Recall
Formula: `recall = TP / (TP + FN)`.

Plain terms: Of all the items that should have been labeled, how many did we actually tag correctly? It’s the "did we see everything?" metric.

### F1 Score
Formula: `F1 = 2 * precision * recall / (precision + recall)`.

Plain terms: F1 combines precision and recall into a single score. Leadership can use this number to balance quality and coverage during reviews.

### Micro vs. Macro F1
* **Micro:** Sum TP/FP/FN across categories first, then compute F1. Reflects overall operations.
* **Macro:** Compute F1 per category, average across categories. Gives each category equal importance.

Use micro-F1 when the volume distribution matters (our default). Use macro-F1 if leadership wants to give small but strategic categories equal voice.

## 5. Implementation strategy (human terms)
1. Validate inputs: sequences must be the same length and not empty.
2. Count how many predictions exactly match the truth (TP).
3. Count how many do not match (each mismatch is both an FP and an FN in a single-label setting).
4. Plug the counts into the micro-F1 formula: `2 * TP / (2 * TP + FP + FN)`.
5. If the denominator is zero (which happens only when everything is negative), return 0.0 to avoid division errors.

## 6. Constraints recap
* Input sequences up to 100,000 items.
* Labels are integers in 0..K-1, inferred from the data.
* No external ML libraries.
* Return a Python `float` (not a NumPy scalar).

## 7. Tests to prove correctness (mental model)
1. Perfect prediction → score 1.0.
2. Example with one mislabel → score falls accordingly (aligns with provided sample: 2/3 ≈ 0.6667).
3. All mismatches → score 0.0.
4. Large list sanity check to ensure performance stays linear.

## 8. Linking back to business outcomes
* **Decision support:** Micro-F1 helps prioritise model improvements that move the needle for the entire population.
* **Risk management:** By monitoring the combined signal, leadership avoids blind spots in dominant categories.
* **Operational transparency:** Plain-language metrics build cross-functional trust in AI-driven processes.

## 9. Real-world ML system integration
Micro-F1 shows up in production ML stacks wherever class frequency is uneven but the business wants one global performance number.

### Example: Customer support ticket triage
Real helpdesk data skews heavily toward a few “general inquiry” style categories, yet teams also track rarer, high-impact tickets such as billing disputes or outages. Micro-F1 is used to monitor end-to-end ticket routing systems because it:

1. **Weights by actual ticket mix:** Summing true/false positives and negatives before scoring mirrors the true distribution that front-line teams experience every day.[^open-ticket-ai]
2. **Balances SLAs:** Precision highlights how often the automation misroutes tickets (causing rework), while recall shows how many urgent tickets the system catches without human triage.
3. **Translates to staffing decisions:** Operations leads can compare micro-F1 before and after model updates to see if automation is reducing backlog without sacrificing quality.

This same pattern appears in other high-class-count domains such as catalog tagging, safety moderation queues, and insurance claim categorization—anywhere the business cares about aggregate throughput without over-indexing on rare labels.

[^open-ticket-ai]: “Evaluating AI Classifiers on Real Ticket Data: Metrics That Matter,” Open Ticket AI (Oct 2025). Highlights support ticket imbalance, the pitfalls of raw accuracy, and the role of precision/recall/F1 in production evaluations. https://open-ticket-ai.com/en/blog/ai_classifiers_metrics

## 10. How large tech companies (FAANG+) apply Micro-F1

### Facebook/Meta – Ads quality and integrity
Meta engineers report that triage pipelines for ads policy enforcement rely on micro-F1 because:
1. **Volume weighting matters:** Billions of ad impressions skew toward common creatives, so micro-F1 tracks how well classifiers behave on the overall traffic mix.
2. **Operational triggers:** High micro-F1 ensures automated takedowns hit service-level agreements without overwhelming human reviewers.
3. **Regression gating:** Launch processes often require micro-F1 to stay above a preset baseline before shipping a new model, preventing broad accuracy regressions.

### Google – Large-scale media classification (e.g., YouTube-8M)
Google’s multi-label video classification benchmarks evaluate models with micro-averaged metrics because:
1. **Dense label space:** Videos can have thousands of possible topics; micro-F1 captures whether the model catches the most common entities reliably.
2. **Cross-dataset generalization:** Research on combining caption and classification datasets notes that micro metrics mirror headline accuracy when models serve billions of users in production.
3. **Comparison to macro/weighted:** Macro-F1 highlights rare classes, while weighted F1 straps per-class results to frequency. Micro-F1 remains the “global reality check” that product owners track.

### Netflix – Personalization and intent modeling
Streaming recommendation teams use micro-F1 when modeling session intents because:
1. **Session-level routing:** Predicting intent drives which UI surfaces appear; micro-F1 measures the correctness bias of the overall experience.
2. **AB testing:** Micro-F1 correlates with key business metrics (engagement/hours watched) when scaled across the entire member base.
3. **Model monitoring:** Detects drifts where the model increasingly misses high-frequency behaviors even if rare intents remain accurate.

## 11. Strengths, weaknesses, and alternatives

### Strengths
1. **Reflects real traffic mix:** Weighted by frequency, so leadership sees the score customers feel day-to-day.
2. **Stable KPI:** Resistant to dramatic swings when a single rare class shifts performance.
3. **Alignment with accuracy:** For single-label tasks, micro-precision = micro-recall = accuracy, making it easy to explain.

### Weaknesses
1. **Rare class blindness:** Under-represents critical but infrequent categories (e.g., fraud, safety incidents).
2. **Masked bias:** High micro-F1 can hide systemic under-performance on minority segments.
3. **Single number compression:** Collapses nuance; teams still need per-class drill-downs.

### Alternatives and when to use them
1. **Macro-F1:** Treats every class equally. Choose this when rare categories have outsized business risk (e.g., child safety filters at Google/YouTube).
2. **Weighted-F1:** Uses class frequency weights but keeps per-class contributions explicit; helpful when leadership wants a compromise between micro and macro.
3. **ROC AUC / PR AUC:** Used at Facebook/Meta and Google Ads for ranking-oriented systems; report alongside micro-F1 when threshold-free evaluation matters.
4. **Log-loss / Cross-entropy:** Emphasized by Meta Ads teams for calibration-sensitive tasks; complements micro-F1 by capturing probabilistic accuracy.
5. **Recall@K / Hit Rate:** Netflix pairs micro-F1 with recommendation metrics that focus on top-K personalization outcomes.

## 12. Classification type for this problem
* **Learning task:** Single-label, multi-class classification.
* **Input/Output:** Each record receives exactly one label out of K possibilities; `micro_f1` expects integer labels 0..K-1.
* **Why it matters:** In this regime, every mismatch counts as both a false positive and false negative, which is why the implementation reuses a single mismatch counter.
