<p align="center">
  <img src="assets/header.svg" alt="Nitesh Kumar Shah — Research and engineering. Learning from choices. Building systems to explore ideas." width="100%" />
</p>

<p align="center">
  <a href="https://www.niteshkumarshah.com.np">Website</a> &nbsp;·&nbsp;
  <a href="https://scholar.google.com/citations?user=hgJWNAUAAAAJ&amp;hl=en">Google Scholar</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/niteshkumarshah">LinkedIn</a> &nbsp;·&nbsp;
  <a href="#publications">Publications</a> &nbsp;·&nbsp;
  <a href="#cybersecurity">Cybersecurity</a> &nbsp;·&nbsp;
  <a href="#recent-pull-requests">Recent PRs</a> &nbsp;·&nbsp;
  <a href="https://rbhdsks.github.io/Lowrankcdmexplorer/#matrix">Interactive lab ↗</a>
</p>

## About me

I'm **Nitesh**, an M.Tech student in **Data Science & Artificial Intelligence at IIT Madras**, with a B.Tech in Information Technology (Business Informatics) from **IIIT Allahabad**.

I study how we can learn preferences from observed choices, and how context changes those choices. I also build interactive ML tools and work on Bluetooth and IoT security.

**Currently:** working on preference learning with **Prof. Suryanarayana Sankagiri**—from Bradley–Terry models to full and low-rank context-dependent models.

---

## M.Tech thesis

### Learning from Comparison Data

**What can observed choices tell us about the preferences behind them?**

My M.Tech thesis explores parameter recovery, maximum-likelihood estimation, context effects, and cyclic preferences. I connect mathematical examples with reusable implementations, synthetic experiments, and documented fit diagnostics.

| Research question | What I explore |
| :--- | :--- |
| Can we recover the preferences that generated the data? | Synthetic recovery experiments and sample-size scaling |
| When does a finite estimate exist? | MLE existence, separation, and optimization diagnostics |
| What changes when the available alternatives change? | Bradley–Terry/Luce and context-dependent choice models |
| What do low-rank models trade off? | Predictive fit, parameterization, and computational cost |

[**Explore the thesis repository →**](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) &nbsp; [Read the notes ↗](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/blob/main/docs/thesis/Notes.pdf)

<details>
<summary><strong>Look inside the research workflow</strong></summary>

- **Start small:** derive the model and verify its behavior on worked examples.
- **Simulate:** generate choices with known parameters and inspect recovery.
- **Compare:** fit models to shared data splits and examine held-out likelihood.
- **Diagnose:** retain stopping criteria, separation checks, and runtime measurements.
- **Communicate:** connect notebooks, reusable source code, figures, and thesis notes.

This is ongoing research. The repository distinguishes completed experiments, pilot results, and planned extensions; numerical stopping alone does not establish the existence of a finite unregularized MLE.

</details>

### Context Lab · an interactive companion

**Change the context. Watch the choice probabilities change.**

A browser-based lab for exploring directed interactions, low-rank factors, and choice models. Built as an independent educational companion to the CDM of Seshadri, Peysakhovich, and Ugander (ICML 2019), under Prof. Sankagiri's supervision.

| Start here | Try this |
| :--- | :--- |
| [**Matrix Studio ↗**](https://rbhdsks.github.io/Lowrankcdmexplorer/#matrix) | Edit an interaction, change the rank, and inspect reconstructed entries. |
| [**Experiment Lab ↗**](https://rbhdsks.github.io/Lowrankcdmexplorer/#experiment) | Generate or upload choices; compare models using validation and test splits. |
| [**Paper Guide ↗**](https://rbhdsks.github.io/Lowrankcdmexplorer/#paper) | Follow a worked example from factor vectors to choice probabilities. |

[Source code →](https://github.com/rbhdsks/Lowrankcdmexplorer) · [Original paper ↗](https://proceedings.mlr.press/v97/seshadri19a.html)

<details>
<summary><strong>A two-minute experiment you can try</strong></summary>

1. Open **Matrix Studio** and edit the effect of item B on item A.
2. Compare a rank-1 reconstruction with a rank-3 reconstruction.
3. Add another item to the choice set and inspect how the A/B odds change.
4. Open **Paper Guide** to trace the calculation behind the probabilities.

The browser lab uses small educational experiments; its outputs are not the original paper's reported results.

</details>

---

## Publications

[**Google Scholar profile ↗**](https://scholar.google.com/citations?user=hgJWNAUAAAAJ&hl=en)

| Publication | Venue | Links |
| :--- | :--- | :--- |
| **RainGAN-Kathmandu:** A Generative Adversarial Framework for Synthetic Rainfall Augmentation in Urban Road Scene Datasets | IEEE TENCON, 2025 · First author | [Paper](https://doi.org/10.1109/TENCON66050.2025.11374935) · [Code](https://github.com/rbhdsks/RainGAN) |
| **A Comprehensive Bluetooth Security Audit Framework for IoT Devices** | Computers & Security, 2026 · Co-author | [Paper](https://doi.org/10.1016/j.cose.2026.104840) |
| **Novel Adaptation of the UNIT Framework for Cross-Domain Climate Data Translation with Enhanced Feature Preservation** | International Conference on Signal Processing and Integrated Networks, 2025 · First author | [Scholar record](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hgJWNAUAAAAJ&citation_for_view=hgJWNAUAAAAJ:8k81kl-MbHgC) |
| **An Efficient ADAS Framework for Cross-Domain Image Translation and Feature Preservation Utilizing CycleGAN** | 2025 · Co-author | [Scholar record](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hgJWNAUAAAAJ&citation_for_view=hgJWNAUAAAAJ:MXK_kJrjxJIC) |
| **Integrating FinBERT Sentiment with Financial Stress for Optimized Portfolio Performance** | Academy of Marketing Studies Journal, 2025 · Co-author | [Scholar record](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=hgJWNAUAAAAJ&citation_for_view=hgJWNAUAAAAJ:kNdYIx-mwKoC) |

---

## Recent pull requests

<!-- recent-pull-requests:start -->
- [updated the ppt part](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/104) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 11 Nov 2026
- [Complete Phase I viva slides](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/103) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Open · 11 Nov 2026
- [updated the phase1\.tex part till cdm recovery](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/102) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 10 Nov 2026
- [Docs/add overleaf thesis](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/101) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 10 Nov 2026
- [docs: save local thesis changes](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/100) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 09 Nov 2026
- [Docs/add overleaf thesis](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/99) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 08 Nov 2026
- [kept some outputs to archive](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/98) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 07 Nov 2026
- [Feature/context dependent models](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-/pull/97) on [`rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-`](https://github.com/rbhdsks/Learning-from-Comparison-Data-Master-Thesis-Project-) · Merged · 07 Nov 2026
<!-- recent-pull-requests:end -->

[All my public pull requests ↗](https://github.com/pulls?q=is%3Apr+is%3Apublic+author%3Arbhdsks+sort%3Acreated-desc)

---

## Selected engineering

### 01 / Road damage detection

An end-to-end **MLOps course project** connecting a YOLOv8 detector with model serving, experiment tracking, data versioning, orchestration, and monitoring.

`Python` · `FastAPI` · `Docker` · `MLflow` · `DVC` · `Airflow` · `Prometheus / Grafana`

[Explore the system →](https://github.com/rbhdsks/MLOPS-FINAL-PROJECT)

### 02 / Local research assistant

A **laptop-hosted AI prototype** with a browser chat interface accessible from an iPad on the same trusted network. The laptop runs inference through Ollama; the tablet provides the interface.

`Python` · `Ollama` · `Local inference` · `Browser UI`

[Explore the prototype →](https://github.com/rbhdsks/LOCAL-LLM)

<details>
<summary><strong>Current scope and next steps</strong></summary>

The prototype supports local chat. Document retrieval, persistent conversations, fine-tuning, and distributed execution are future work. My next interest is connecting research material to local retrieval and evaluating the resulting answers.

</details>

---

## Cybersecurity

### Bluetooth and IoT security

During my **C3iHub fellowship at IIT Kanpur**, I used Python and Pyshark to inspect Bluetooth HCI traffic and identify encryption-related packets. I co-authored a paper in *Computers & Security* on auditing Bluetooth-enabled IoT devices, contributing software, validation, visualization, and methodology.

[Bluetooth packet analysis code ↗](https://github.com/rbhdsks/Encryption-checker-Bluetooth) · [Read the paper ↗](https://doi.org/10.1016/j.cose.2026.104840)

---

## Tools I work with

| Area | Tools and methods |
| :--- | :--- |
| Research & modeling | Python, PyTorch, NumPy, Jupyter, likelihood-based estimation |
| Interactive explanations | JavaScript, HTML, CSS, browser-based experiments |
| ML systems | FastAPI, Docker, MLflow, DVC, Airflow |
| Everyday workflow | Git, Linux, macOS, LaTeX |

## Connect

I'm best reached via [email](mailto:sirali.nitesh@gmail.com), [GitHub](https://github.com/rbhdsks), or [LinkedIn](https://www.linkedin.com/in/niteshkumarshah).

---

<p align="center"><sub>Everyone we meet is fighting a battle we know nothing about. Be kind, always.</sub></p>
