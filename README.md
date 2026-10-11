# why-models-work

> **Not how strong AI models are — *why* they're strong.**
> Exploring the evidence of model leaps — evidence-chained attribution of every major capability leap in model frameworks.

The mainstream asks *how strong* (benchmarks, leaderboards). This repo asks *why strong* — and answers with an attribution chain for every major capability leap in AI history:

**现象 → 主流归因 → 真实机制 → 证据/证明**
**phenomenon → mainstream attribution → real mechanism → evidence/proof**

## The Method — 归因四段法 (Attribution Chain)

Every framework gets the same four-step dissection:

| Step | Question | What it is |
|------|----------|-----------|
| 1. 现象 Phenomenon | What measurable capability leap happened? | The observed effect, with concrete numbers |
| 2. 主流归因 Mainstream attribution | How does the field explain it? | Usually the oversimplified (or wrong) story — the target |
| 3. 真实机制 Real mechanism | What actually made it work? | The structural cause — the one step that mattered |
| 4. 证据/证明 Evidence | How do we know? | Hard evidence, labeled by strength |

**Proof strength labels** (honest, per chapter):

| Label | Meaning |
|-------|---------|
| `定理级` theorem-level | Mathematical proof |
| `经验规律` empirical-law | Scaling laws & measurable regularities |
| `消融证据` ablation-evidence | Causal experiments |

## The Map — 14 Capability Leaps

▶ **[交互式全景图 · Interactive Timeline](timeline.html)** — 深色时间轴，14 次跃迁一图看全，悬停展开「主流归因 vs 真实机制」+ 证明强度标签。（浏览器直接打开，或部署 GitHub Pages 后访问）

| # | Framework | Year | One-line attribution (the contrarian thesis) | 📄 |
|---|-----------|------|---------------------------------------------|-----|
| 1 | Perceptron | 1958 | The first ceiling was set by a mathematical proof, not engineering | [→](PAPERS.md#f1) |
| 2 | Backpropagation | 1986 | Made learning *differentiable*, not just trainable | [→](PAPERS.md#f2) |
| 3 | CNN / Convolution | 1989–2012 | Wins by *learning less* — hardcoded translation invariance | [→](PAPERS.md#f3) |
| 4 | LSTM gating | 1997 | Its power is learning to *forget*, not to remember | [→](PAPERS.md#f4) |
| 5 | Distributed representations | 2013 | Proved meaning is *computable geometry* | [→](PAPERS.md#f5) |
| 6 | Seq2Seq + Attention | 2014 | Attention was for *alignment*; parallelism came later by accident | [→](PAPERS.md#f6) |
| 7 | Residual connections | 2015 | Made networks safely *shallower*, not deeper | [→](PAPERS.md#f7) |
| 8 | Transformer self-attention | 2017 | Turned the sequence from a *chain* into a *complete graph* | [→](PAPERS.md#f8) |
| 9 | Pretraining (BERT/GPT) | 2018 | The *learning objective* changed, not the model | [→](PAPERS.md#f9) |
| 10 | Scaling Laws | 2020 | Made capability growth *predictable* — engineering, not alchemy | [→](PAPERS.md#f10) |
| 11 | Diffusion | 2020–22 | Splits one hard problem into a thousand easy ones | [→](PAPERS.md#f11) |
| 12 | RLHF | 2022 | Makes models *obedient*, not smarter | [→](PAPERS.md#f12) |
| 13 | MoE sparse experts | 2023–24 | Power is in *sparsity*, not the experts | [→](PAPERS.md#f13) |
| 14 | Test-time compute | 2024 | The *location* of compute moved, not the model | [→](PAPERS.md#f14) |

See [`THE_THESES.md`](THE_THESES.md) for the full contrarian theses — each with the mainstream attribution vs. the real mechanism.

See [`PAPERS.md`](PAPERS.md) for the curated reading list — 14 frameworks × 3–5 papers, annotated by three questions (what it is / its properties / its capability boundaries). See [`ABLATIONS.md`](ABLATIONS.md) for the reproducible ablations — one runnable XOR experiment plus curated entry points, ranked by reproduction cost.

## Status

- [x] 14 contrarian theses (`THE_THESES.md`)
- [x] The big picture — AI capability-leap timeline map (`timeline.html`)
- [x] Papers — 14 frameworks × 3–5 papers, three-question annotation (`PAPERS.md`)
- [x] Per-framework chapters — first two exemplars: [`01-perceptron.md`](chapters/01-perceptron.md), [`02-backpropagation.md`](chapters/02-backpropagation.md) (2/14)
- [x] Reproducible ablations — 1 runnable (XOR) + curated entry points (`ABLATIONS.md`)
