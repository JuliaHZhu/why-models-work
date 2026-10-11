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

| # | Framework | Year | One-line attribution (the contrarian thesis) |
|---|-----------|------|---------------------------------------------|
| 1 | Perceptron | 1958 | The first ceiling was set by a mathematical proof, not engineering |
| 2 | Backpropagation | 1986 | Made learning *differentiable*, not just trainable |
| 3 | CNN / Convolution | 1989–2012 | Wins by *learning less* — hardcoded translation invariance |
| 4 | LSTM gating | 1997 | Its power is learning to *forget*, not to remember |
| 5 | Distributed representations | 2013 | Proved meaning is *computable geometry* |
| 6 | Seq2Seq + Attention | 2014 | Attention was for *alignment*; parallelism came later by accident |
| 7 | Residual connections | 2015 | Made networks safely *shallower*, not deeper |
| 8 | Transformer self-attention | 2017 | Turned the sequence from a *chain* into a *complete graph* |
| 9 | Pretraining (BERT/GPT) | 2018 | The *learning objective* changed, not the model |
| 10 | Scaling Laws | 2020 | Made capability growth *predictable* — engineering, not alchemy |
| 11 | Diffusion | 2020–22 | Splits one hard problem into a thousand easy ones |
| 12 | RLHF | 2022 | Makes models *obedient*, not smarter |
| 13 | MoE sparse experts | 2023–24 | Power is in *sparsity*, not the experts |
| 14 | Test-time compute | 2024 | The *location* of compute moved, not the model |

See [`THE_THESES.md`](THE_THESES.md) for the full contrarian theses — each with the mainstream attribution vs. the real mechanism.

## Status

- [x] 14 contrarian theses (`THE_THESES.md`)
- [x] The big picture — AI capability-leap timeline map (`timeline.html`)
- [ ] Per-framework chapters (full attribution chains)
- [ ] Reproducible ablations
