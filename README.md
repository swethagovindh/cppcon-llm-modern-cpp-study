# How Modern Is LLM-Generated C++?
## Reproducibility package for the CppCon poster study

This repository contains the frozen prompts, **120 frozen V3 LLM responses**, source-backed evaluation data, manually verified findings, static-analysis records, analysis scripts, and figure-generation code for:

**How Modern Is LLM-Generated C++? An Empirical Evaluation of Modern C++ Coding Practices**

Author: **Swetha Govindaiah, Ph.D.**

## Experimental design

- **10 scenarios × 3 models × 4 prompt conditions = 120 frozen outputs**
- OpenAI — **GPT-5.6 Sol** (`gpt-5.6-sol`)
- Anthropic — **Claude Opus 5** (`claude-opus-5`)
- Google — **Gemini 3.1 Pro Preview** (`gemini-3.1-pro-preview`)
- Prompt conditions: **Baseline**, **Modern C++**, **Safety/Robustness**, **Performance**

The same scenario statement is used across the four conditions; only the additional evaluation criterion changes. Baseline has no additional criterion.

## Final evaluation framework

The 202-row source-backed inventory is split before analysis:

1. **121 Feature / Syntax rows → 84 canonical concrete features**
   - `1 = present`, `0 = absent`
   - source-level feature presence is descriptive, not a quality score
2. **75 broader Modern C++ practices**
   - `1 = present`, `0 = absent`, `U = undetermined`
   - `U` is retained when generated source does not provide enough evidence for a reliable determination
3. **6 quality/tool-derived rows**
   - compiler/static-analysis evidence is evaluated separately from feature presence

The final method does **not** use an expert-reference implementation or the earlier architecture-aware U/M/R/N evaluator as a scoring baseline.

## Locked findings

- 10,080 concrete-feature cells
- 9,000 broader-practice cells
- **3,253 / 9,000 = 36.1%** broader-practice evaluations are `U`
- **11** manually verified overlooked-practice opportunities
- **10** high-confidence generated-code defect instances
- **2** additional portability issues

The clearest recurring manually verified opportunity is **Bounds & Data Safety**: raw pointer + separate size/count interfaces where a bounds-carrying view such as `std::span` is applicable. These are improvement opportunities, not correctness defects.

## Run the reproducibility pipeline

Python 3.10+:

```bash
python -m pip install -r requirements.txt
python run_all.py
```

This validates the frozen inputs, regenerates numerical summaries, audits traceability of the manually verified cases to the frozen raw responses, and regenerates the figures.

Optional C++ block extraction:

```bash
python scripts/04_extract_cpp.py
```

## Repository layout

```text
.github/workflows/           GitHub Actions reproduction check
data/
  raw/
    prompts/                 40 frozen prompts
    responses/               120 frozen V3 responses
  reference/                 202/84/75/6 source-backed reference data + manifests
  evaluation/                frozen feature/practice labels and verified findings
  derived/                   regenerated summaries
scripts/                     validation, aggregation, audit, figures, extraction
figures/                     regenerated poster figures
static_analysis/             locked tool configuration, runner, raw logs
experimental/                earlier screening work; NOT final scoring
docs/                        methodology, data dictionary, result lock, source policy
run_all.py                   one-command numerical reproduction
```

## Static-analysis configuration

- Clang / clang-tidy **22.1.8**
- C++23
- `-Wall -Wextra -Wpedantic`
- clang-tidy groups: `clang-analyzer`, `bugprone`, `performance`, `modernize`, `readability`
- Cppcheck **2.21.0**: warning/style/performance/portability, exhaustive, inconclusive

Raw warning count is not treated as a quality score. The poster uses only manually adjudicated high-confidence findings.

## Source policy

The source roles are explicit in `data/reference/source_catalog.csv`.

- C++ Core Guidelines — primary best-practice guidance
- ISO/IEC 14882:2024 — normative C++ basis through C++23
- WG21 current working draft — C++26/current-draft technical basis
- cppreference — technical feature/library/version verification, not normative best-practice guidance
- SEI CERT C++ — supplemental security/correctness guidance
- MISRA C++:2023 — supplemental safety-critical guidance where relevant
- Clang / clang-tidy / Cppcheck documentation — quality/correctness tool basis

## Reproducibility boundary

Concrete feature presence is stored as frozen source-level evidence. Broader-practice labels and the final semantic verdicts for overlooked opportunities/diagnostics contain human judgment and are therefore published as **frozen adjudication data**, rather than pretending they can be regenerated faithfully by regex.

See `docs/PIPELINE.md`, `docs/DATA_DICTIONARY.md`, and `docs/RESULTS_LOCK.md`.

## AI assistance disclosure

See `docs/AI_DISCLOSURE.md`.
