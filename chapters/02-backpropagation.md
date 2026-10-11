# 02 · Backpropagation（1986）—— 发明 ≠ 生效

> 归因四段法 · 第二篇。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

BP 不是 1986 年被「发明」的——它的数学早在 1970 就发表了，神经网络应用也早在 1974/1982 就有了。1986 年 Rumelhart/Hinton/Williams 真正的贡献不是「发明算法」，而是「用实验证明它 work，并让整个社区信服」；而它真正统治世界，还要再等 26 年，到 2012 年的 ImageNet。

## 现象

- 1986，Rumelhart, Hinton & Williams 发表《Learning representations by back-propagating errors》（Nature 323:533）[4]，及 PDP 书卷一的同题章节。
- 多层神经网络的训练问题被「解决」，联结主义复兴，深度学习由此奠基。
- 今天训练每一个深度模型的梯度引擎（TensorFlow、PyTorch 等），数学上都是这个东西。

## 主流归因

教科书叙事：**1986 年，Rumelhart、Hinton、Williams 三人「发明」了反向传播算法，让多层网络终于可以被训练。**

## 真实机制

把「发明」和「生效」拆开，时间线立刻错位：

**① BP 的数学（反向模式自动微分）早在 1970 就发表了——而且作者根本没提神经网络。**

芬兰硕士生 Seppo Linnainmaa 1970 年在赫尔辛基大学的硕士论文里，首次发表 reverse mode of automatic differentiation（反向模式自动微分），含 FORTRAN 代码[1]。Schmidhuber 的定论[5]：

> BP's modern version (also called the reverse mode of automatic differentiation) was first published in 1970 by Finnish master student Seppo Linnainmaa.

更早的前驱在控制理论：Kelley (1960)、Bryson (1961)、Dreyfus (1962) 已经在用链式法则 + 变分法做参数梯度优化[5]。链式法则本身是 Leibniz 1676。所以「BP 的数学」比「BP 的名字」早 16 年，且属于一个和神经网络**几乎没有交集的学科**（最优控制/自动微分）。

**② 神经网络的首次应用也早在 1974/1982 就有（Werbos）。**

Paul Werbos 1974 年哈佛博士论文 *Beyond Regression*[2] 的 §5.5.1 里已有初步的 NN 讨论；首个 NN 特定的高效 BP 应用发表于 1982 年（IFIP，Springer）[3]——注意 Schmidhuber 的精确修正：常说的「Werbos 1974 发明了 NN 的 BP」实际是「1974 有初步想法，1982 才有首个 NN 应用」。无论如何，都比 1986 早。

**③ 1986 三人组的贡献不是「发明」，是「实验证明 + 说服」。**

Schmidhuber 对 1986 那篇的定性[5]是「experimental analysis」——它**证明**了 BP 能在隐藏层里学出有用的分布式内部表征（distributed representations），这是让社区**信服**的关键一步。同时他明确指出：这篇**没有引用** Linnainmaa 1970、Werbos 1974、Amari 1967、Ivakhnenko 1965 的先行工作[5]。于是「发明者」和「让世界相信它的人」在归因里被混成了同一个人。

**④ 更早还有用 SGD 训练「深层」网络的人。**

Amari 1967–68 用随机梯度下降训练过一个五层 MLP，学出了内部表征[7]；Ivakhnenko & Lapa 1965 的 GMDH 网络是第一个真正「深度」的学习系统（逐层增长训练）[5]。换言之，在 BP 被「发明」之前，训练多层网络的想法和初步实践都已有记录。

**⑤ 为什么偏偏是 1986 才「起效」？算力。**

Schmidhuber 给出了物质答案[5]：到 1985 年，算力比 1970 年便宜约 **1000 倍**，桌面电脑开始进入富裕的学术实验室。BP 作为「思想」1970 年就摆在那了，但它作为「可训练性」需要算力、数据、工程细节（sigmoid、初始化、调参）三样东西同时到位，才能从「数学对象」变成「可跑的东西」。

**⑥ 即使 1986 之后，「深度」仍被长期过度悲观——然后又被证伪。**

Hinton 在 2007 年 Google Tech Talk 里亲口说过[6]：

> "Nobody in their right mind would ever suggest" 用 plain backpropagation 训练深度网络。

当时主流认为训深度网络必须靠 unsupervised pre-training（Hinton 2006 的 DBN 那套）。结果 2010 年 Schmidhuber 团队（Ciresan, Meier, Gambardella, Schmidhuber）用 **plain BP** 直接训深度标准网络，打破了基准纪录，证明 pre-training 根本不是必要条件[8]。

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 史料级 | Linnainmaa 1970 硕士论文（含 FORTRAN 代码，未提 NN） | BP 数学比名字早 16 年 |
| 史料级 | Werbos 1974 论文 §5.5.1 + 1982 IFIP 应用 | NN 应用比 1986 早 4–12 年 |
| 文献级 | Schmidhuber 对 1986 论文的定性：experimental analysis，未引用先行工作 | 1986 的贡献是「证明 + 说服」，不是「发明」 |
| 史料级 | Hinton 2007 原话 + Ciresan et al. 2010 证伪 | 「可训练性」边界在 2010 前被系统性低估 |
| 消融级 | `ablation/perceptron_xor.py` 的同一机制 | 同样的多层网络，有 BP（1986）与无 BP（1969）是两个物种 |

## 反常识推论（母题）

> **「发明」和「生效」是两个时刻，中间隔着算力、数据、工程细节、和社区信心。**

把第二章和第一章放在一起看，会发现一个惊人的对称：

- **1969**，Minsky & Papert 把「多层**当时**不可训练」误判成「多层本质上 sterile」。
- **2007**，Hinton 把「深度网络**当时**难以用 plain BP 训练」误判成「必须靠 pre-training」。

**同一个认知错误——把「当前条件下不可训练」误判成「本质上不可训练」——在 41 年里犯了两次，而且两次都被证伪**（1986 证明多层可训练；2010 证明 plain BP 就够深）。

这暴露出整条 14 框架链最深的一条规律：

> **「可训练性」的边界从来不是数学划死的，而是被「算法 × 算力 × 数据 × 工程细节 × 社区信心」共同决定的——而这五者都是时间的函数。** 每当有人说「X 不可训练」，他说的其实是「X 在现有条件下不可训练」；而历史反复证明，「现有条件」这条边界的寿命，远比说这句话的人以为的短。

一句话收束：**BP 是 1970 年就存在的数学、1986 年才被证明 work、2012 年才统治世界。一个思想的「能力跃迁」，不是它被写下的那一刻，而是它被算力和数据「兑现」的那一刻。**

---

## References

1. Linnainmaa, S. (1970). *The representation of the cumulative rounding error of an algorithm as a Taylor expansion of the local rounding errors.* Master's Thesis (in Finnish), Univ. Helsinki. [PDF (idsia.ch)](http://www.idsia.ch/~juergen/linnainmaa1970thesis.pdf) · [Journal version, BIT 1976](http://link.springer.com/article/10.1007%2FBF01931367)
2. Werbos, P. J. (1974). *Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences.* PhD thesis, Harvard University. [PDF (gwern.net)](https://gwern.net/doc/ai/nn/1974-werbos.pdf)
3. Werbos, P. J. (1982). Applications of advances in nonlinear sensitivity analysis. In R. Drenick & F. Kozin (eds.), *System Modeling and Optimization*, Springer. [PDF (werbos.com)](http://werbos.com/Neural/SensitivityIFIPSeptember1981.pdf)
4. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323(6088), 533–536. [doi:10.1038/323533a0](https://www.nature.com/articles/323533a0)
5. Schmidhuber, J. (2014, updated 2025). *Who Invented Backpropagation?* [people.idsia.ch](https://people.idsia.ch/~juergen/who-invented-backpropagation.html)
6. Hinton, G. (2007). *The Next Generation of Neural Networks.* Google Tech Talk. [YouTube (28:16)](https://youtu.be/AyzOUbkUf3M?t=1696)
7. Amari, S. (1967). A theory of adaptive pattern classifier. *IEEE Trans. Electronic Computers*, EC-16, 279–307. [PDF (idsia.ch)](https://people.idsia.ch/~juergen/amari1967.pdf)
8. Ciresan, D. C., Meier, U., Gambardella, L. M., & Schmidhuber, J. (2010). Deep Big Simple Neural Nets For Handwritten Digit Recognition. *Neural Computation*, 22(12), 3207–3220. [arXiv:1003.0358](https://arxiv.org/abs/1003.0358)

---

**关联**：[PAPERS.md §2](PAPERS.md#f2)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[01 · Perceptron](01-perceptron.md) · [THE_THESES.md](THE_THESES.md)
