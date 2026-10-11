# 08 · Transformer / Self-Attention（2017）—— 「扔掉」，然后把顺序手动塞回去

> 归因四段法 · 第八篇。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

Transformer 真正的贡献不是「发明 attention」（2015 年就有了），而是「**扔掉**」——它把循环和卷积全部扔掉，只用 self-attention，把「长距离依赖的路径」从 O(n) 压到 O(1)。但「扔」是有代价的：裸 self-attention 是**排列等变**的、对顺序是瞎的，所以必须手动把「顺序」这个先验作为「位置编码」重新注入。这标志着先验的载体从「结构」降级成了「输入上的一个附加信号」，也标志着深度学习从「用结构先验换可训练性」转向「放弃结构先验，用数据 + 任务 + 规模换一切」。

## 现象

- 2017，Vaswani 等人发表《Attention Is All You Need》，提出 Transformer。
- 它彻底统治了 NLP，随后扩散到 CV（ViT）、语音、多模态，成为「一个架构通吃」的通用骨架。
- 今天所有大语言模型（GPT、BERT 及一切）都是 Transformer 的后代。

## 主流归因

教科书叙事：**Transformer 发明了「自注意力」机制，让模型能并行地关注序列里所有位置，从此取代了 RNN。**

## 真实机制

拆开看，「发明自注意力」是错的，真正的关键词是「扔掉」——以及「扔完之后的补救」：

**① Attention 不是新的——2015 年 Bahdanau 就发明了。**

第六章已经讲过：attention 机制 2015 年就在 seq2seq 里当「RNN 的辅助」用了[2]。Vaswani et al. 2017 做的不是「发明 attention」，是论文摘要里那句精准的表述[1]：

> a new simple network architecture, the Transformer, based **solely** on attention mechanisms, **dispensing with recurrence and convolutions entirely**.

——把 attention 从「辅助」扶正为「唯一主角」，同时**把 RNN 和 CNN 从架构里删掉**。这才是那篇论文真正做的事。

**② 为什么「扔掉」是革命？三个动机，核心是「路径长度」。**

论文自己列了三个动机[1]：

1. **计算复杂度**（每层的总计算量）；
2. **可并行化的程度**（RNN 是顺序的：第 t 步必须等第 t−1 步，没法并行）；
3. **长距离依赖的路径长度**（信息从一个位置传到另一个位置，要穿过多少步）。

前两条是工程（并行 = 规模），第三条才是深层机制：**RNN 里信息从位置 i 到位置 j 要走 |i−j| 步，每步还可能衰减（梯度消失）；self-attention 里任意两个位置直接相连，路径长度 O(1)，梯度也是 O(1)**。这是「给梯度开直连路」这个思想的终点——前面几章是「**加一条**直连路」（CEC 单行道、attention 加权直连、残差加法直连），Transformer 是「**把路连成一张全连接网**」：所有位置两两直连。

**③ 但「扔掉循环」是有代价的：self-attention 对顺序是瞎的。**

这是全书最反直觉、也最该讲清楚的一点：**裸 self-attention 是排列等变（permutation equivariant）的**——它根本不知道词序。你打乱输入，输出也跟着同样地打乱；「cat sat on mat」和「mat sat on cat」对它来说是同一个东西[3]。为什么？因为 attention 权重只取决于 query-key 的「内容兼容性」，不取决于「位置索引」。

所以「扔掉循环」不是免费的：**循环里本来就藏着「顺序」这个先验**（一步一步走，顺序天然在场）。把循环删掉，顺序就丢了。

**④ 于是必须「手动把顺序塞回去」——位置编码（positional encoding）。**

Transformer 的补救是：把「位置」编码成正弦信号（sinusoidal positional encoding），**直接加在输入向量上**，让「顺序」变成一个输入特征[1][3]。这句话是本篇的灵魂：

> **Transformer 把「序列顺序」这个先验，从「结构」降级成了「输入上的一个附加信号」。**

这是先验主题的一次深刻转折。回顾全书：CNN 把「平移等变」写进结构（权重共享），LSTM 把「恒定梯度传导」写进结构（CEC），word2vec 把「分布假说」写进任务。**Transformer 反过来了——它拒绝把顺序写进结构，而是把它「外化」成一个可加、可换、可学的输入信号**（所以后来位置编码才演化出 learned embeddings、RoPE 等无数变体——因为它已经不再是「结构」，只是一个「输入插槽」）。

**⑤ 「Attention Is All You Need」这个标题，其实是个「美丽的谎言」。**

标题字面意思是「注意力就是你所需要的一切」。但论文自己立刻证明了它不全对：attention 不知道顺序，你必须**额外**加位置编码；还要加前馈层、残差连接、层归一化、缩放点积、多头……更准确的说法是「**注意力 + 位置编码 + 前馈 + 残差 + 归一化 = 你所需的一切**」。但恰恰是这个「过分的标题」，成了它传播最有力的引擎——**一个被论文内容自己证伪的标题，反而成了深度学习的口号。** 这本身就是一个「发明 ≠ 生效」的注脚：生效的常常不是最精确的，而是最可传播的。

**⑥ 转折点：从「结构先验」到「无结构先验」，赌注押给「数据 + 规模」。**

Transformer 是全书「结构先验最少」的架构：没有 CNN 的平移等变、没有 LSTM 的时间递归、没有 ResNet 的「深层≈恒等」，几乎只有一个极弱的先验——「任意位置直接相连」。**结构先验越少，就需要越多的数据来弥补。** 这直接解释了后面框架 10（scaling laws）为什么在 Transformer 时代才成立：**Transformer 把「结构里的智慧」清空，换来了「可以被数据无限填充的容器」。** 下一章（框架 9，预训练范式）就是往这个容器里灌数据的开始。

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 史料级 | Bahdanau 2015 已有 attention（seq2seq 辅助） | Transformer 非 attention 发明者 |
| 结构级 | 论文原文「dispensing with recurrence and convolutions entirely」 | 核心贡献是「扔掉」，非「发明」 |
| 数学级 | self-attention 排列等变（打乱输入→打乱输出） | 循环一删，顺序即失 |
| 结构级 | sinusoidal positional encoding 加在输入上 | 「顺序」先验从结构降级为输入信号 |
| 路径级 | 任意位置 O(1) 直连（vs RNN O(n)） | 「梯度直连」思想的终点：连成网 |

## 反常识推论（母题）

> **先验的载体，从「结构」降级成了「输入信号」。**

这一章是前七章的「收束 + 转向」，两条线在这里汇合：

**线一（梯度直连）**：CEC 单行道 → attention 加权直连 → 残差加法直连 → Transformer 全连接网。**「给梯度开一条不衰减的直连路」这个思想，一路被减到最简、又被扩到最大，最终在 Transformer 里变成了默认设置。**

**线二（先验的载体）**：结构（CNN/LSTM/ResNet）→ 任务（word2vec）→ **输入信号（位置编码）**。Transformer 拒绝把「顺序」写进结构，而是把它外化成一个可替换的输入插槽。

两条线合起来，指向同一个历史判断：

> **Transformer 的胜利，是「结构先验最少」的胜利。** 它没有「更聪明」，它「更空」——把结构里的智慧清空，换成一个「任意位置直连 + 无顺序偏置」的极简容器，然后把一切赌注押在「数据 + 任务 + 规模」上。这不是「注意力的胜利」，是「**可被规模无限填充的空容器**」的胜利。

一句话收束第八章：**Transformer 没有发明注意力，它发明的是「扔掉」——扔掉循环和卷积，再把被扔掉时一起丢掉的「顺序」，降级成一个手动塞回去的位置编码。它的真正遗产不是 attention，是那个「结构先验最少、因而能被数据无限填充」的空容器。**

---

## References

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *NeurIPS 2017*. [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
2. Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. *ICLR 2015*. [arXiv:1409.0473](https://arxiv.org/abs/1409.0473)
3. Brenndörfer, M. The position problem: self-attention and word order. [博客](https://mbrenndoerfer.com/writing/position-problem-self-attention-word-order) · [Positional Encoding 详解](https://www.articsledge.com/post/positional-encoding)

---

**关联**：[PAPERS.md §8](PAPERS.md#f8)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[07 · 残差连接](07-residual.md) · 下一篇：[09 · 预训练范式](09-pretraining.md) · [THE_THESES.md](THE_THESES.md)
