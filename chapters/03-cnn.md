# 03 · Convolutional Networks（1989 → 2012）—— 用「先验」换「可训练性」

> 归因四段法 · 第三篇。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

CNN 的跃迁不是「发明了更强的学习算法」，而是「把『平移等变』这条关于世界的先验知识，硬编码成网络结构（局部连接 + 权重共享），换来参数量的指数级下降与可训练性」。它的胜利是**结构更省**，不是**算法更强**。

## 现象

- 2012，Krizhevsky, Sutskever & Hinton 的 AlexNet 在 ImageNet 上把错误率打下来一大截，深度学习革命自此引爆，计算机视觉被 CNN 统治至今。
- 卷积 + 池化 + 多层，成了视觉模型的标准骨架。

## 主流归因

教科书叙事：**LeCun 在 1989/1998 年「发明」了卷积神经网络，2012 年 AlexNet 把它引爆。**

## 真实机制

拆开看，「卷积」的结构和「CNN 的胜利」之间，隔着一整条被主流叙事略过的时间线：

**① 卷积/感受野的思想来自神经科学，不是机器学习。**

Hubel & Wiesel（1959/1962）记录猫视觉皮层的细胞，发现了**感受野（receptive field）**：简单细胞对特定位置的特定朝向条状刺激响应，复杂细胞对更大范围、对位置不敏感。这是 CNN 里「局部连接 → 逐层抽象」的生物蓝本[6]。

**② 1980 年的 Neocognitron，已经把卷积的整个结构做出来了。**

Fukushima 1980 的 Neocognitron，直接受 Hubel & Wiesel 启发，实现了**局部感受野 + 分层特征检测 + 权重共享 + 空间池化**[1]：S-cell 就是今天的卷积层，C-cell 就是今天的池化层。而且 Fukushima 在 1980 年原文里，已经把「平移等变」这件事写得明明白白：

> all the cells in a single cell-plane have receptive fields of the same function, but at different positions.

——「同一功能的感受野，平移到不同位置」，这就是卷积的权重共享。**结构上，CNN 在 1980 年已经完整了。**

**③ 但 Neocognitron 用的不是 BP，而是无监督的 Hebbian 式规则。**

Fukushima 的 Neocognitron 用「无监督、局部 winner-take-all」的类 Hebbian 学习规则[1]——**结构对了，学习算法不对**。于是它再次卡在了第一章的那个断点上：能表达，但难以高效训练。这是「能表达 ≠ 能学习」的第二个实例。

**④ LeCun 1989 的贡献，是把第二章的 BP「缝合」到第三章的卷积结构上。**

LeCun et al. 1989 首次用 BP 训练卷积网络识别 USPS 手写邮编[2]。注意他原话——「先验硬编码」这件事，他自己 1989 年就说得清清楚楚：

> the architecture of the network was **highly constrained and specifically designed for the task**.

「高度约束、专门为任务设计」——这八个字，就是「把先验写进结构」的一手自述。LeNet-5（1998）随后把 MNIST 做到 99%+，并在银行的支票识别系统里跑了多年[3]。

**⑤ 平移等变是「免费的数据」，不是学出来的。**

卷积的数学本质是**严格等变（equivariant）**：输入平移，特征图跟着平移。这不是网络「学」到的性质，是权重共享这个结构约束**强制**出来的性质[5]。等价地说：**inductive bias 就是免费的数据**——把「图像里的东西平移后还是同一个东西」这条世界知识硬编码进结构，等于凭空送给网络海量「几何先验」，让它在数据稀少时依然样本高效。

**⑥ 为什么偏偏 2012 才爆发？—— 结构 1980 就有，爆发靠的是别的东西。**

LeNet-5 1998 年就工业部署了，但 1998–2012 这十几年，视觉主流是 SVM + 手工特征（HOG/SIFT），CNN 被边缘化。AlexNet 2012 的突破**不是卷积结构**（那东西 32 年前就有了），而是三样「条件」同时到位：**ImageNet 的 120 万张标注图 + GPU 并行 + ReLU/dropout 这些训练细节**[4]。这又是第二章「发明 ≠ 生效」的翻版：**结构早已就绪，等的是数据、算力、和工程细节。**

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 史料级 | Fukushima 1980 原文描述「同一感受野功能，平移复制」（cell-plane 机制） | 卷积结构 + 平移等变，1980 已完成 |
| 史料级 | Neocognitron 用无监督 Hebbian 规则而非 BP | 结构对、算法不对 → 又卡在「能表达 ≠ 能学习」 |
| 原文级 | LeCun 1989 摘要「highly constrained and specifically designed」 | 「先验硬编码」的一手自述 |
| 史料级 | LeNet-5 1998 工业部署（ATM 支票），却到 2012 才引爆 | 「发明 ≠ 生效」再验证 |
| 数学级 | 卷积严格等变，权重共享是平移等变的离散实现 | 平移等变是结构约束，非数据学来 |

## 反常识推论（母题）

> **结构先验，是用「人类已知」换「机器可学」的货币。**

CNN 的深层教训不是「卷积真聪明」，而是：

> 把「关于世界的先验知识」编译进「网络结构」，是降低学习负担最有效的手段——**inductive bias 就是免费的数据**。CNN 赢，不是因为它「算法更强」，而是因为它「结构更省」：把平移等变这条先验写死，换来了参数量的指数级下降和样本效率。

但这是一把**双刃剑**，而且刀刃的方向，正好指向下一章的 Transformer：

- CNN 的胜利，靠的是「写死先验」（局部性 + 平移等变）。
- 这个先验在图像上极强，但也正是它，让 CNN 在处理**长程 / 全局关系**时天然吃亏——因为它假设「远处的信息不重要」。
- **Transformer 反其道而行**：它把这个先验「删掉」，靠 attention 学任意两两位置的关系，代价是**需要海量数据**。

于是三章的母题在这里收成一句话：

> **从 CNN 到 Transformer，不是「算法变强了」，而是「先验与数据的天平」从「写死先验省数据」这一端，摆到了「删掉先验吃数据」那一端。** 谁赢，取决于那一刻数据是稀缺还是过剩。

一句话收束第三章：**CNN 没有发明任何新的学习原理——它发明的是「把先验知识变成网络结构」这件事本身。它的统治，是「结构更省」对「算法更巧」的胜利。**

---

## References

1. Fukushima, K. (1980). Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position. *Biological Cybernetics*, 36, 193–202. [PDF](https://www.rctn.org/bruno/public/papers/Fukushima1980.pdf)
2. LeCun, Y., Boser, B., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W., & Jackel, L. D. (1989). Handwritten digit recognition with a back-propagation network. *NIPS 2*. [PDF](https://proceedings.neurips.cc/paper/1989/file/53c3bce66e43be4f209556518c2fcb54-Paper.pdf)
3. LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to document recognition. *Proc. IEEE*, 86(11), 2278–2324. [PDF](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf)
4. Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *NIPS 25*. [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)
5. Weiler, M. *Equivariant neural networks — what, why and how?* [Blog](https://maurice-weiler.gitlab.io/blog_post/cnn-book_1_equivariant_networks/)
6. Hubel, D. H., & Wiesel, T. N. (1959–1962). Receptive fields of single neurones in the cat's striate cortex / Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *J. Physiology*, 148 & 160. [背景：Receptive field](https://en.wikipedia.org/wiki/Receptive_field)

---

**关联**：[PAPERS.md §3](PAPERS.md#f3)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[02 · Backpropagation](02-backpropagation.md) · [THE_THESES.md](THE_THESES.md)
