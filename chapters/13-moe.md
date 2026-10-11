# 13 · MoE Sparse Experts（1991 → 2024）—— 更聪明地「大」

> 归因四段法 · 第十三篇。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

MoE 不是「更聪明的模型」，是「更聪明的算力调度」——Shazeer et al. 2017 的原话就是「increase the number of parameters **without increasing computation**」。它把「容量」和「计算」解耦：参数巨多，但每个 token 只激活一小部分专家，从而在固定算力预算内装进更多参数——这是 scaling 定律的「效率版」。它的思想源头可追溯到 Jacobs & Hinton 1991（30 年延迟生效），而门控路由本身是个会「负载不均、专家坍缩」的训练难题，需要 auxiliary loss 强制均衡——又一个「度量 / 调度」的坑。更深一层：MoE 在「分布式表征」的内部重新引入了「模块化分工」，是第一章「表达力」母题的一次回归。

## 现象

- 2017，Shazeer 等人的稀疏门控 MoE 层，把模型做到 137B 参数，却「以更低的计算成本」超越 SOTA。
- 2021–2022，GShard（600B）、Switch Transformer（万亿参数）把 MoE 推上大模型舞台。
- 今天几乎所有「前沿但省算力」的模型（Mistral、DeepSeek 等）都是 MoE 架构。

## 主流归因

教科书叙事：**MoE 是一种「让不同专家处理不同输入」的新型架构，通过「专家分工」让模型变得更聪明、更强。**

## 真实机制

拆开看，「更聪明」是个误读，真正的关键词是「**解耦**」——以及它带来的那一堆训练麻烦：

**① 核心不是「更聪明」，是「把容量和计算解耦」。**

Shazeer et al. 2017 的动机写得很直白[1]：

> Our approach is to **increase the number of parameters** … **without increasing computation**.

MoE 层由成百上千个「专家」（每个是一个前馈子网络）+ 一个可训练的门控网络（gating network）组成。门控对每个 token **稀疏地**选 1–2 个专家来算（top-1 / top-2），剩下的专家**根本不激活**。于是：

- **参数多**（137B / 600B / 万亿）→ **容量大**，能存更多知识；
- **激活少**（每个 token 只跑一两个专家）→ **计算便宜**，推理快。

**参数和计算，第一次被拆成了两回事。** 这就是 MoE 的全部秘密——它不是一个「更好的模型」，是一套「更省的算力经济学」。这也是 scaling 定律（第十章）的「效率版」：scaling 说「越大越好」，MoE 说「**要聪明地大**」——不是无限加算力，而是用稀疏激活，在固定算力预算里塞进更多参数。

**② 思想 1991 年就有了——Jacobs & Hinton 的「竞争专家」。**

MoE 的源头是 Jacobs, Jordan, Nowlan & Hinton 1991《Adaptive Mixtures of Local Experts》[4]：几个相互**竞争**的专家网络，各自学会处理训练数据的一个子集，一个门控网络决定「谁来处理谁」。思想在 1991 年就完整了。但当年它只在小数据集上跑，价值远未凸显——因为「解耦容量与计算」这件事，只有在**参数爆炸、算力吃紧**的 scaling 时代才值钱。

1991 → 2017（Shazeer 稀疏门控）→ 2021（GShard 自动分片）→ 2022（Switch 万亿参数），**30 年延迟生效**。又一次「发明 ≠ 生效」——而且这次延迟的原因很具体：**思想的价值，要等「算力成为瓶颈」这个时代背景到位，才会被看见。**

**③ 门控路由是个「会钻空子的调度员」——负载不均、专家坍缩。**

MoE 最难的从来不是「专家」，是「门控」——那个决定「每个 token 发给谁」的路由器。它有一堆经典毛病[2]：

- **负载不均（load imbalance）**：某些专家被疯狂使用，某些专家闲置——算力没省下来，反而浪费。
- **专家坍缩（expert collapse）**：路由学坏了，所有 token 都挤去同一个专家，MoE 退化成「只有一个专家的普通网络」。
- **训练不稳定**：Switch Transformer 原文直言，MoE 推广受阻的原因是「complexity, communication costs and training instability」。

解法是给门控加一个 **auxiliary load balancing loss**（辅助负载均衡损失）——**强制**让各个专家被用得差不多[2]。你看，这里又出现了那个熟悉的幽灵：**一个「调度度量」，一旦没有约束就会自己钻空子，必须靠额外的损失函数去「管教」它。** 这和第十二章 RLHF 的 reward hacking、第十章「涌现是度量伪影」，是同一个母题的第三次登场。

**④ 最深的一层：MoE 在「分布式」内部，重新引入了「局部」。**

这是全书最耐人寻味的呼应。第五章讲「分布式表征」：**一个概念由许多神经元的激活模式共同表示**（Hinton 1986），反对「一个神经元 = 一个概念」的局部表征（localist）。而 MoE 的「每个专家专精一类输入」，本质上是**在分布式表征的骨架内部，重新引入了一层「局部 / 模块化」的分工**。

一句话：**「分布式」的骨架 + 「局部」的分工。** 这恰恰是第一章「能表达 ≠ 能学习」母题的一次回响——**模块化（分工）是一种极强的结构先验**，它 1991 年就出现了，却在 30 年后，以「稀疏门控」的形式，重新回到深度学习的最前沿。历史上兜了一个圈：从「局部表征」到「分布式表征」再到「分布式骨架里的局部分工」。

**⑤ 为什么 MoE 在这个时刻回归？因为 scaling 撞上了墙。**

MoE 的重新流行，本质是 scaling 定律的「边际收益递减」逼出来的：当「无限加参数」开始撞上「算力、电力、成本的墙」，人们被迫回头找 1991 年那个老答案——**「让参数和计算解耦」**。MoE 是 scaling 从「蛮力」走向「效率」的转折点，也是下一章（test-time compute）的伏笔：**当训练端的 scaling 越来越贵，聪明人开始把「计算」这个杠杆，从训练期挪到推理期。**

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 结构级 | Shazeer 2017「increase parameters without increasing computation」 | 核心是「解耦」，非「更聪明」 |
| 史料级 | Jacobs & Hinton 1991 竞争专家 + 门控网络 | 思想 30 年前已有，延迟生效 |
| 工程级 | Switch 2022：auxiliary load balancing loss | 门控会负载不均/坍缩，需强制管教 |
| 规模级 | GShard 600B / Switch 万亿参数，sub-linear compute | 「容量—计算」解耦的规模化兑现 |
| 同构级 | 「分布式骨架 + 局部分工」 | 局部表征在分布式内部回归 |

## 反常识推论（母题）

> **更聪明地「大」，比「更大」更难。**

这一章把 scaling 的叙事，从「蛮力」翻到了「效率」：

> 第十章说 scaling 是「放弃理解」的胜利——加算力就行。第十三章是它的第一次回撤：**当「更大」撞上算力墙，人被迫重新动脑，去想「怎么在不变的计算里装进更多的参数」。** MoE 的答案是把「容量」和「计算」拆开——参数可以天文数字，激活永远只一点点。**这不是「模型变聪明」，是「人变聪明了」——聪明地用调度，替代了聪明的模型。**

而「度量幽灵」第三次现身，把三章串成一条暗线：

> 第十章：「涌现」可能是度量伪影。第十二章：「奖励」这个度量会被 reward hacking 钻空子。第十三章：「门控」这个调度度量会负载不均、专家坍缩，必须靠 auxiliary loss 管教。**AI 每一次想「省事」——用度量代替理解、用代理代替真相、用调度代替结构——最后都要付出「额外管教那个度量」的代价。** 这是本书反复敲响的同一记警钟。

一句话收束第十三章：**MoE 没有造出「更聪明的模型」，它造出的是「容量与计算解耦」的算力经济学；它的「专家分工」是 1991 年 Jacobs & Hinton 的老思想，30 年后因算力墙而复活；而它那个「会负载不均、会坍缩」的门控，则是「度量幽灵」在调度层的一次现身。**

---

## References

1. Shazeer, N., Mirhoseini, A., Maziarz, K., et al. (2017). Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. *ICLR 2017*. [arXiv:1701.06538](https://arxiv.org/abs/1701.06538)
2. Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. *JMLR*. [arXiv:2101.03961](https://arxiv.org/abs/2101.03961)
3. Lepikhin, D., Lee, H., Xu, Y., et al. (2021). GShard: Scaling giant models with conditional computation and automatic sharding. *ICLR 2021*. [arXiv:2006.16668](https://arxiv.org/abs/2006.16668)
4. Jacobs, R. A., Jordan, M. I., Nowlan, S. J., & Hinton, G. E. (1991). Adaptive mixtures of local experts. *Neural Computation*, 3(1), 79–87. [Semantic Scholar](https://www.semanticscholar.org/paper/Adaptive-Mixtures-of-Local-Experts-Jacobs-Jordan/c8d90974c3f3b40fa05e322df2905fc16204aa56)

---

**关联**：[PAPERS.md §13](PAPERS.md#f13)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[12 · RLHF](12-rlhf.md) · 下一篇：[14 · Test-time Compute](14-reasoning.md) · [THE_THESES.md](THE_THESES.md)
