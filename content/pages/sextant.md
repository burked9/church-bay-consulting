Title: SEXTANT — the fitted-parts prediction engine
Slug: sextant
Date: 2026-08-21
Category: Projects
Tags: Aviation, Monte Carlo, Machine Learning, Fitment Prediction, Sextant, AI
Summary: A Monte Carlo prediction engine for aviation part-number fitment across airframe positions with confidence scoring.
Status: published

# SEXTANT — the fitted-parts prediction engine

## SEXTANT

**Enter the MSN. I'll give you the parts list. With confidence.**

A parts trader gets a call at 4pm on a Tuesday. A wide-body is being scrapped in six weeks — a decade-old A330 with a Portuguese operator he's never dealt with. He has the MSN, the registration, and the build year. He has thirty minutes to decide whether to bid.

Everything else is a guess.

Is the ADIRU at position 1FP2 the earlier Honeywell part or the post-mod Thales? Is the ADM at 19FP1 the -BC02 revision or the -AC05? Are the brakes still the pre-2010 assembly or have they been swapped to the newer disc? Each of those decisions is five figures. There are 1,200 positions on the airframe. And he has thirty minutes.

Someone bolder wins the deal. Every time. Not because they're smarter but because they're guessing anyway, and they've priced in a bigger uncertainty margin.

**There has to be a better way.**

There is.

*[SCREENSHOT: SEXTANT prediction output for a single MSN - positions × predicted PN × confidence band, chapter-grouped]*

## What it does, in one breath

SEXTANT is a Monte Carlo prediction engine for aviation part-number fitment. Give it an aircraft — any airframe, any age, in the fleet or already scrapped — and it returns the most likely part number at every confirmed canonical position, with a confidence score and the alternatives ranked behind it. Behind every prediction is real OCCM ground truth from sibling airframes: same aircraft family, same sub-variant, same era, same engine option. The output is a chapter-by-chapter parts list you can walk into a valuation with.

The predictions ship. The methodology does not.

## Why it's different

### Sub-variant awareness, by construction, not extrapolation

Vendors and appraisers routinely blur A330 into a single category. SEXTANT doesn't. A332 (A330-200) is a different sub-variant from A333 (A330-300) which is different again from A338 and A339 — and each has an identifiable fitment fingerprint that emerges from the data. A346 (A340-600) is a different animal from A343 (A340-300) — pairwise position overlap between two A346 airframes runs at 95%; between two A343 airframes it's 49%. That's not a bug, that's a real fleet-diversity signal that can be captured.

*[SCREENSHOT: A340 sub-variant cluster heatmap — 175/179 (A343), 736/753/764 (A346), 626 (loner) with Jaccard percentages]*

### Confidence you can price against

Every prediction ships with a **SEXTANT Score** — a Wilson lower-bound confidence adjusted for sample size and fallback depth. High-confidence predictions (real-backed, sub-variant consensus) score above 80. Sparse-data predictions score below 50. When you're staring at a 1,200-position parts list, you don't want to eyeball a probability plot — you want to know which rows to trust cold and which to eyeball. That's what the score is for.

### Chapter-by-chapter navigation, Closed-box by design

Every prediction is grouped by ATA chapter with a first order approximation assigned OCCM category (Major Avionics, Hard-Time, High Sell Through Rate, Category4) tagged per position. Working through the airframe by ATA chapter is how appraisers already think. SEXTANT respects that.

*[SCREENSHOT: ground-truth reference sheet — chapter sidebar with per-chapter counts, sticky left columns, one row per position × one column per airframe]*

## How it works, briefly

SEXTANT began with very sparsely available OCCM data, then the Monte Carlo engine samples per-bucket, per-position, with deterministic seeds derived from a SHA-256 hash of `(master_seed, family, sub_variant, cohort, position)`. Same seed, same MC, same predictions — every time. Reproducibility is a feature, not a hope.

*[SCREENSHOT: decision log — audit trail of every ground-truth construction step, mechanism additions, sub-variant confirmations]*

## Try it today

SEXTANT launches publicly at [your URL here]. Private walkthrough for teardown houses, lessors, and appraisers — drop me a line.

— **Daniel Burke**, Church Bay Consulting
