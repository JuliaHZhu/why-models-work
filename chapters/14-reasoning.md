# 14 · Test-time Compute / Reasoning（2024–2025）—— 先验，回到「思考」本身

> 归因四段法 · 第十四篇（终章）。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

所谓「推理能力」不是「模型突然变聪明了」，而是「把训练期的『学习』搬到了推理期『现场算』」——Snell et al. 2024 证明「推理时多算」可以匹敌「训练时更大」（FLOPs 匹配下，小模型 + 推理时多算能赢 14 倍参数的大模型）。这是 scaling 的「第二轴」：不只是「训练时更大」，还有「推理时多想」。OpenAI o1 用 RL 教模型「思考」，DeepSeek-R1 进一步证明：**纯 RL、无监督数据、只给「结果对错」，推理行为（自反思、验证）就会自发涌现。** 最深一层：test-time compute 标志着「先验」绕了一大圈，最终回到了「搜索 / 思考」这个最古老的 AI 范式——**从「把先验写进权重」，回到「现场计算」。**

## 现象

- 2024，OpenAI 发布 o1——第一个「在回答前先思考」的商用模型。
- 2025，DeepSeek-R1 开源复现，用纯 RL 训练出「会自己反思、验证」的推理模型。
- 「推理时多算」（test-time compute）成为继「训练时更大」之后，第二个被系统性挖掘的 scaling 轴。

## 主流归因

教科书叙事：**o1 / R1 让模型「学会了推理」——通过强化学习，模型获得了「逻辑思考」的新能力。**

## 真实机制

拆开看，「学会推理」是个误读——模型没有「学到一个新器官」，它只是「换了个地方算」：

**① 传统模型 vs 推理模型：差别不在「聪明」，在「什么时候算」。**

一个经典语言模型（GPT 系）的「知识」在训练期就被压进了权重——**推理时只是一次前向传播，把预计算的答案「吐」出来**。而推理模型（o1 / R1）的关键变化是：**在回答之前，允许模型「现场花更多计算」去思考、搜索、验证。** 用一句话概括这个转变[4]：

> shifting computational investment from **training time** to the exact moment the model analyzes a question and deliberates its response.

——把「计算」这笔投资，从「训练期」挪到了「回答的当口」。模型没有「更聪明」，它只是**被允许在回答前多算一会儿**。

**② 这是 scaling 的「第二轴」——「更大」之外，还有「多想」。**

第十章讲的 Kaplan scaling，是**训练期**的轴：参数、数据、算力。Snell et al. 2024 开辟了**推理期**的轴[1]——他们问的问题很具体：

> if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance?

答案惊人：在 **FLOPs 匹配**的比较中，一个「小模型 + 推理时多算」能在多数任务上赢过一个**约 14 倍参数**的大模型[1]。换句话说：**算力花在「让模型现场多想」上，可以比花在「把模型训更大」上更划算。** 这是 scaling 定律（第十章）被扩展成「两条腿」——一条是「训练时更大」，一条是「推理时多想」。

**③ OpenAI o1：RL 教模型「思考」，而不只是「生成」。**

o1 的技术说明写得很清楚[2]：

> Our large-scale reinforcement learning algorithm **teaches the model how to think productively using its chain of thought**.

注意：这不是「提示工程诱导思考」（如 few-shot CoT），而是**用 RL 把「思考」这个行为内化进模型**——这直接承接第十二章 RLHF 的教训：**RL 不只是「教偏好」，还能「教行为」。** 于是「思考」从一种「外挂的提示技巧」，变成了一种「训练出来的内在习惯」。

**④ DeepSeek-R1 的「顿悟时刻」：纯 RL 就能让「反思」涌现。**

DeepSeek-R1 更进一步，做了一个近乎「实验」的设定[3]：**R1-Zero 用纯 RL 训练，无监督数据、无人类标注的推理轨迹，奖励只给「结果对错」**（GRPO）。结果：**自反思（self-reflection）、验证（verification）、动态策略调整**这些推理行为，**自发地涌现**了出来，甚至论文里记录了一个「aha moment」——模型中途停下来说「等等，让我重新检查一下」[3]。

这是全书「涌现」母题的最实在一次登场：第十章说「涌现可能是度量伪影」（Schaeffer 的 mirage 假说），但 DeepSeek-R1 的「aha moment」是**行为层面**的涌现——模型真的改变了行为模式（停下来反思），不是打分表造成的错觉。**它给「涌现」提供了一个比「度量伪影」更硬的例证，也让这两章形成了一个微妙的对照：有些「涌现」是幻觉，有些「涌现」是真的。**

**⑤ 最深的一层：先验，绕了一大圈，回到了「搜索 / 思考」。**

把全书「先验迁徙史」的最后一步补上：

> 结构（CNN/LSTM/ResNet）→ 任务（word2vec/预训练）→ 输入信号（位置编码）→ 数据（scaling）→ 人类偏好（RLHF）→ **搜索 / 思考（test-time compute）**。

这是全书最意味深长的一个闭环：**AI 最早的范式（1950–60 年代的符号 AI）就是「搜索」——在解空间里系统地找答案。** 后来神经网络用「学习」取代了「搜索」：把知识压进权重，推理时不再搜，只是「算」。而 test-time compute 标志着「搜索」的回归——只不过这次，**「搜索」不是程序员写死的启发式，而是被 RL 训练出来的「思考」**。

一句话：**先验绕了一大圈，从「写进权重」回到了「现场计算」。**

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 模型级 | Snell 2024：FLOPs 匹配下，小模型+推理多算赢 14x 大模型 | 「推理时多想」是 scaling 的第二轴 |
| 机制级 | o1：RL「teaches the model how to think」 | 「思考」从提示技巧内化为训练出的行为 |
| 行为级 | R1-Zero 纯 RL、只给结果对错，反思/验证自发涌现 | 「aha moment」是行为层面的真实涌现 |
| 概念级 | 「从训练期挪到回答当口」 | 先验从「权重」回到「现场计算」 |
| 历史级 | 符号 AI「搜索」→ 神经网络「学习」→ test-time「思考」 | 一个 70 年的圆 |

## 反常识推论（母题 · 全书收束）

> **从「学」到「想」，从「记住」到「现场算」——AI 走了一个 70 年的圆。**

终章把全书十四篇收成一条线：

> 第一章：Perceptron 证明了「能表达 ≠ 能学习」。
> 第二章：BP 证明了「发明 ≠ 生效」。
> 第三～七章：先验被一次次写进结构（CNN 的平移等变、LSTM 的 CEC、ResNet 的恒等）。
> 第五、九章：先验被搬进任务（word2vec 的预测、预训练的填空/续写）。
> 第八章：Transformer 把结构清空，成了一个「可被数据无限填充的空容器」。
> 第十章：scaling 把先验彻底外包给数据——「放弃理解」的胜利。
> 第十二章：数据喂完了，人类偏好被重新请回来（RLHF）。
> 第十三章：算力墙逼出了 MoE——「聪明地大」。
> 第十四章：最后，先验回到了「思考」本身。

而全书真正的主角，从头到尾只有一个：**梯度。** 从 BP 让「可微」成为入场券，到 attention/残差给梯度开路，到 scaling 让梯度吃到无限数据，到 test-time compute 让「思考」本身也能被梯度优化——**每一次飞跃，本质都是「让更多的东西，进入梯度可以优化的范围」。** 而这，或许就是《why-models-work》最想说的那句话：

> **模型为什么有效？因为「有效」这件事，从来不是被设计出来的，而是被「微分」出来的——能被微分的东西，才有资格被算力放大；能被放大的东西，才会在历史里「生效」。**

一句话收束全书：**Test-time compute 没有让模型「学会推理」，它让「思考」这个最古老的 AI 范式，重新成为可被梯度优化的对象；先验绕了一个 70 年的圆，最终从「写进权重」，回到了「现场计算」——而这一路的每一次飞跃，都是同一个故事的重复：把更多的东西，交给梯度去算。**

---

## References

1. Snell, C., Lee, J., Xu, K., & Kumar, A. (2024). Scaling LLM test-time compute optimally can be more effective than scaling model parameters. [arXiv:2408.03314](https://arxiv.org/abs/2408.03314)
2. OpenAI. (2024). Learning to reason with LLMs. [官方博客](https://openai.com/index/learning-to-reason-with-llms/)
3. Guo, D., Yang, D., Zhang, H., et al. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. [arXiv:2501.12948](https://arxiv.org/abs/2501.12948)
4. Test-time compute & inference scaling. *Reinforcement Learning KB*. [链接](https://www.reinforcement-learning.com/kb/test-time-compute)

---

**关联**：[PAPERS.md §14](PAPERS.md#f14)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[13 · MoE 稀疏专家](13-moe.md) · [THE_THESES.md](THE_THESES.md) · **全书 14 篇，至此完结。**
