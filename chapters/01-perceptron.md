# 01 · Perceptron（1958）—— 能表达 ≠ 能学习

> 归因四段法 · 第一篇打样。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

杀死感知机的不是「它表达不了 XOR」这个数学事实，而是 Minsky & Papert 对「多层扩展是徒劳的（sterile）」这个**未经证明的直觉判断**——它把「表达力」与「可训练性」之间的断裂，误判成了「表达力」本身的死刑。

## 现象

- 1958，Frank Rosenblatt 在《Psychological Review》发表感知机（perceptron）[1]，单层、线性阈值、有可证明的收敛定理。它能学会字母分类，媒体热炒——《纽约时报》宣称它将来能「走路、说话、看、写、自我复制」。
- 1969，Marvin Minsky 与 Seymour Papert 出版《Perceptrons: An Introduction to Computational Geometry》[3]。
- 1970s，联结主义（connectionism）研究衰退，第一次 AI 寒冬（约 1974–1980）到来。

## 主流归因

教科书叙事（几乎每本 AI 史都这么讲）：**Minsky & Papert「证明了」单层感知机连 XOR 都学不会，用数学杀死了神经网络。**

## 真实机制

主流叙事把三件事压成了一件事。拆开后，真相是：

**① 那个数学证明只针对「单层」，而且这些局限在当时早已是已知的。**

Melanie Mitchell（2019，《Artificial Intelligence: A Guide for Thinking Humans》Ch.1）[7]：

> The limitations Minsky and Papert proved for simple perceptrons were already known to people working in this area. **Frank Rosenblatt himself had done extensive work on multilayer perceptrons and recognized the difficulty of training them.**

Rosenblatt 在 1962 年的《Principles of Neurodynamics》[2] Part III（第 15–20 章）里，已经专门讨论「multi-layer and cross-coupled perceptrons」。XOR 类反例针对的「单层感知机」，从来就不是 Rosenblatt 研究的完整图景。

**② 真正致命的是对「多层」的推测，不是定理。**

Minsky & Papert 1969 原文 [3]（Ch.13, p.231–232）——注意这是一句**自我标注为直觉判断**的话：

> There is no reason to suppose that any of these virtues carry over to the many-layered version. Nevertheless, we consider it to be an important research problem **to elucidate (or reject) our intuitive judgment that the extension is sterile**.

他们说的是「我们的**直觉判断**：多层扩展是 sterile（徒劳）的」，并且明明白白地把它当作一个「待阐明或推翻」的研究问题。这是**推测**，不是证明。但流传出去的，却是「证明」的硬度。

**③ 根因是训练算法的缺失，不是表达力的缺失。**

Rosenblatt 自己都「recognized the difficulty of training them」——多层能表达 XOR（一个隐层 + 非线性就够），但 1969 年没有人知道怎么训练多层网络。

Minsky & Papert 在 1988 增订版《Prologue: A View from 1988》[6] 里也亲口承认：

> One popular version is that the publication of our book so discouraged research on learning in network machines that a promising line of research was interrupted. **Our version is that progress had already come to a virtual halt because of the lack of adequate basic theories.**

——停滞的原因是他们自己说的「缺乏足够的基础理论」（即训练算法），而不是他们的书。

**④ 反向传播（1986）正是「回答这个挑战」。**

Rumelhart, Hinton & Williams（PDP Vol.1, Ch.8, p.361）[5] 在提出 BP 时，明确把它定位成对 1969 年那本书的回应：

> we believe that **we have answered Minsky and Papert's challenge** and have found a learning result sufficiently powerful to demonstrate that **their pessimism about learning in multilayer machines was misplaced**.

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 定理级 | 单层感知机线性不可分（Minsky & Papert 1969） | 只约束**单层**，且早已已知 |
| 史料级 | 「the extension is sterile」原文自称「intuitive judgment」（Ch.13, p.231–232） | 是推测，不是证明 |
| 消融级 | `ablation/perceptron_xor.py`：单层 loss 卡 0.25，加一层隐层+tanh loss→0 | 直接演示「表达」与「训练」的分离 |
| 文献级 | Mitchell 2019（「it was their speculation, not the mathematics」）；Minsky & Papert 1988 自辩；PDP 1986 回应 | 学界对主流叙事的修正，三源互证 |

## 反常识推论（母题）

归因层真正的教训不是「单层感知机太弱」，而是：

> **能表达 ≠ 能学习。**

表达力与可训练性之间的断裂，是整条 14 框架链反复出现的母题：

- **CNN**：靠硬编码平移等变来「降低学习负担」——把「表达」的一部分写成先验，才能让剩余部分「可训练」。
- **残差连接**：不是为了「网络更强」，是为了「让深层可训练」。
- **Transformer**：表达力在 2017 就摆在那了，但要 scaling 到一定规模才真正「可学习/可涌现」。
- **RLHF / 推理时计算**：把「新的行为方式」兑现成「可训练/可利用」的机制。

一句话收束：**每一次 AI 能力跃迁，本质都是把一种「表达力」兑现成一种「可训练性」。** Perceptron 是第一次、也是最干净的一次演示——它死在「表达」与「训练」的断点上，而 BP（框架 2）恰好缝合了这个断点。这就是为什么这一章必须排在第一章。

## 附：归因边界——别把两场「寒冬」混为一谈

主流叙事里最隐蔽的错误，是把两件不同尺度的事合并了：

1. **「感知机之死」** = 联结主义**支线**的衰退。Minsky & Papert 的书是重要因素，但其作用机制是对**多层可训练性**的悲观推测，不是对单层的数学证明。
2. **「第一次 AI 寒冬」** = 整个 AI 领域（**含符号主义**）的资金收缩。主因是 Lighthill 报告 [4]（1973，英国）与 DARPA 资金转向（1974 Mansfield Amendment 后，美国）。

把 1 和 2 混为一谈，会得到一个方便但错误的故事：「一本数学书冻结了一个领域」。真相是：一本数学书（严格但只对单层）+ 一句悲观的直觉判断（对多层）+ 两场独立的资金政治事件，共同构成了那个十年。

---

## References

1. Rosenblatt, F. (1958). *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain.* Psychological Review, 65(6), 386–408. [doi:10.1037/h0042519](https://doi.org/10.1037/h0042519)
2. Rosenblatt, F. (1962). *Principles of Neurodynamics: Perceptrons and the Theory of Brain Mechanisms.* Spartan Books. [PDF (gwern.net)](https://gwern.net/doc/ai/nn/1962-rosenblatt-principlesofneurodynamics.pdf)
3. Minsky, M., & Papert, S. (1969). *Perceptrons: An Introduction to Computational Geometry.* MIT Press. [MIT Press](https://mitpress.mit.edu/9780262630221/perceptrons/) · [PDF](https://papers.baulab.info/papers/Minsky-1969.pdf)
4. Lighthill, J. (1973). *Artificial Intelligence: A General Survey* (the Lighthill report). [Wikipedia](https://en.wikipedia.org/wiki/Lighthill_report)
5. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323(6088), 533–536. [doi:10.1038/323533a0](https://www.nature.com/articles/323533a0)
6. Minsky, M., & Papert, S. (1988). *Perceptrons: An Introduction to Computational Geometry* (Expanded ed.). MIT Press. Prologue: “A View from 1988”. [MIT Press](https://mitpress.mit.edu/9780262631112/perceptrons/) · [Prologue](https://direct.mit.edu/books/monograph/3132/chapter/85833/Prologue-A-View-from-1988)
7. Mitchell, M. (2019). *Artificial Intelligence: A Guide for Thinking Humans.* Farrar, Straus and Giroux. [Google Books](https://books.google.com/books/about/Artificial_Intelligence.html?id=65iEDwAAQBAJ)
8. Quote Investigator. (2026). *(Multilayer Perceptrons) Our Intuitive Judgment That the Extension Is Sterile.* [quoteinvestigator.com](https://quoteinvestigator.com/2026/07/24/perceptron-sterile/)

---

**关联**：[PAPERS.md §1](PAPERS.md#f1)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· [THE_THESES.md](THE_THESES.md)
