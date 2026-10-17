# why-models-work — 前沿观察（Frontier Observations）

> 这里是**还没被时间验证**的技术。跟上面 14 个已成定论的跃迁不是一回事：
> 那些证据链已经闭合、进了教科书；这些是刚发布、证据未固化、随时可能被推翻的。
> 所以单独放一个区、单独标注，**不混进成熟主线**——避免未证实的说法被当成"站得住的历史"。

## 成熟度标签（Maturity Labels）

跟「证明强度」（定理级/经验规律/消融证据）并列的**第二条轴**，回答"这个结论站得多稳"：

| Label | Meaning | 范围 |
|-------|---------|------|
| `成熟` settled | 证据链闭合、进教科书、多团队独立复现 | 上面的 14 个跃迁 |
| `前沿` frontier | 刚发布、单团队/单一证据、未经历时间检验 | 本区的条目 |

**升级规则**：某条前沿技术被第三方独立复现、多任务泛化得到验证后，才从「前沿」升级成完整章节（走归因四段法）。不成熟的技术，不用成熟章节的规格去写。

## 收录视角：小模型 / 低成本 / 高稳定

本区收录前沿技术的**筛选标准**，是三个词：

| 维度 | 含义 |
|------|------|
| 小模型 | 参数少，不靠堆规模取胜 |
| 低成本 | 训练/推理便宜，单位能力的花费低 |
| 高稳定 | 行为可预测、不易崩（固定答案集 + 概率，而非自由生成） |

主线（14 跃迁）讲"能力从哪来"；本区跟踪的是另一条追问：**能力能不能不靠规模、靠目标函数和架构换来**——这正是 Scaling Laws（#10）叙事上的一道口子。

---

## FR-01 · CLM-8B（Contrastive Language Model）— `前沿`

| 项 | 内容 |
|---|---|
| 发布 | 2026-09-23 · Stanford（Scaling Intelligence Lab + Hazy Research）+ NVIDIA · **Apache 2.0** |
| 一句话 | 不生成文本，用**对比学习**把 state 和候选 action 各自编码成向量，选最匹配的 —— 一个「快系统一」决策模型 |
| 底层 | frozen Qwen3-8B 做 encoder + **两个 20M 投影头**（state head / action head）——可训参数只在这两个头，不碰 backbone |
| 训练目标 | **双向 InfoNCE**（CLIP 式）——batch 内 B×B 相似度矩阵，正对 (sᵢ, aᵢ) 双向优化 |
| 训练配方 | 60M Nemotron Q&A 对（预训练）→ 30M 合成 hard negatives（中训练）→ 1M agentic trajectories（后训练） |
| 关键设计 | **state / action 解耦**——两者 embedding 独立缓存、复用，所以训练和 serving 都便宜 + 极快 |

**反直觉点（待验证）**：对「决策 / 路由 / 验证」这类 System One 任务，瓶颈**不是生成能力，而是 state-action 匹配度**。换一个目标函数（contrastive 而非 autoregressive），8B 小模型就打得平大模型，还快一个数量级。

**机制细节**（细读官方 README / 训练代码挖出，比新闻稿深一层）：

- **hard negatives 是「精修」不是「替代」**：纯 Q&A 预训练 top-1 就 52.1%，加 hard negatives 中训练拉到 69.2%；但**一开始就用 hard negatives**只到 62.4% 就过拟合——两阶段比 from-start **好 7 个点**
- **40% replay 防灾难性遗忘**：后训练 = 40% Nemotron 回放 + 60% agentic；纯 agentic 会把 Nemotron top-1 从 69% 崩到 56.2%，回放保住 68.5%
- **scaling law 重做了一遍**：InfoNCE loss 随 compute/data/head/encoder 幂律下降，**扩 encoder 收益最大**；最优 head 大小 N* ∝ D^1.02（约 **310 tokens/参数**）
- **vector cache**：server 预留 device memory slab 缓存 state/action embedding，命中跳过 encoder+拷贝+forward，重复 state 实测约 **2.8× 加速**（1.7→0.6ms），LRU 永不增长

**证据现状**（截至 2026-10，官方口径）：

- computer-use / 游戏 / tool-calling 上**打平 Jev**，延迟**快 9×**
- 轻量微调后做 **verifier** 拿到新 SOTA：Terminal-Bench 2.1 **87.6%**、DeepSWE **81.6%**
- 注意：对标对象 **Jev 是 TypeSafe 的闭源黑盒**——无论文、无公开权重，只有 API（第三方 2025-03 开源过同款 recipe 作为 prior art）

**为什么还是「前沿」**：

- 刚发布一周，主创单一（Jacky Kwok），训练配方未经历独立复现
- "打平 Jev"是官方口径，第三方 benchmark 还很少——而 Jev 本身是黑盒，连"打平"的基准都难独立复验
- "快 9×"在 candidate action 多 / action 跨状态复用时才最大——泛化边界没画清楚

**对应维度**：小模型 ✓（8B backbone + 40M 可训 head）｜低成本 ✓（state/action 解耦缓存）｜高稳定 ✓（固定答案集 + 概率，单次 pass）

**关联主线**：Scaling Laws（#10）——把 scaling law 在「对比学习/决策」这个新目标函数上**重做了一遍**（encoder 收益最大、N*∝D^1.02）；MoE（#13）"稀疏即省"的思路延伸。

**下一级台阶**：官方 roadmap 预告 **multimodal CLM-35B**（更多数据/算力/参数，面向 robotics + computer-use），原定 early October 发布，截至 10-17 HF 上尚未落地。

**升级条件**：第三方独立复现 + 多任务泛化被验证后，升级为完整章节。
