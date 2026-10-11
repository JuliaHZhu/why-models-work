# 04 · LSTM / Gated Recurrent Networks（1997）—— 把「记忆」写进梯度流

> 归因四段法 · 第四篇。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

LSTM 的胜利不是「发明了记忆」，而是「硬编码了一条梯度不衰减的高速公路——CEC（恒定误差旋转木马，一个权重固定为 1.0 的线性自连接）」，把「长期记忆保持」这条**时间先验**编译进梯度传播的结构里。网络真正学到的，只是这条公路的「收费站」（门）何时开合。

## 现象

- 1997，Hochreiter & Schmidhuber 发表 LSTM。
- 2010s 深度学习爆发后，LSTM 一度统治序列建模：机器翻译、语音识别、语言模型，几乎全是它的地盘。
- 传统 RNN 学不了「长序列依赖」，LSTM 能。

## 主流归因

教科书叙事：**Hochreiter & Schmidhuber 1997 年「发明」了 LSTM，用「门控」解决了 RNN 的梯度消失问题，让神经网络学会了「记忆」。**

## 真实机制

拆开看，「记忆」这个词恰恰是主流叙事里最误导人的部分：

**① 问题早在 1991 就被诊断了——但用德文写的，几乎没人读。**

Sepp Hochreiter 1991 年的德国硕士论文（导师 Schmidhuber）数学上识别了梯度消失/爆炸问题：误差信号沿时间回传，每步乘一个 Jacobian，结果**按步数指数衰减或指数爆炸**[1]。这篇论文「in German and largely unread at the time」。直到 Bengio, Simard & Frasconi 1994 用英文系统论证，这个诊断才进入主流视野[2]：

> Long-term dependencies get a weight that is **exponentially smaller (in T)** compared to short-term dependencies.

——「学长期依赖，等于让误差信号穿过 T 步乘法，每一步都把它缩小一点，最后小到学不动。」这就是传统 RNN 的死因。

**② LSTM 的解法不是「更聪明的学习规则」，是「结构手术」。**

Hochreiter & Schmidhuber 1997 的核心不是任何新的训练技巧，而是一个被写死在结构里的东西——**CEC（Constant Error Carousel，恒定误差旋转木马）**：记忆单元内部有一个**线性自连接，权重固定为 1.0**，让误差信号可以原样穿过时间，既不消失也不爆炸[3]：

> The self-recurrent connection (with weight 1.0) … builds the basis of the “constant error carrousel” CEC.

用一句流传的话说：**「The Constant Error Carousel is the 1.0 tunnel through which gradients flow forever.」** 梯度流经一个权重恒为 1.0 的隧道，所以「记忆」能被传回去更新很久之前的参数——**「记忆」不是学出来的，是这条隧道「结构保证」的。**

**③ 门控只是「收费站」，高速公路本身是硬编码的。**

输入门、输出门是 1997 就有的；**遗忘门是 2000 年才加的**（Gers, Schmidhuber & Cummins, "Learning to Forget"）[4]——因为 CEC 的「永不衰减」有个副作用：老信息永远堆着，占满资源。遗忘门的用处是让 cell 「在恰当的时候自我 reset，释放内部资源」。所以准确的分工是：

- **硬编码**：CEC 这条「不衰减的记忆公路」（权重 1.0，不学）。
- **可学习**：三个门（sigmoid 输出的 0–1 开关）——即「收费站」何时开、何时关、何时清空。

**④ 和 CNN 是严格同构的——同一个思想，从空间换到时间。**

- CNN 把「平移等变」这条**空间先验**写死成权重共享。
- LSTM 把「恒定梯度传导」这条**时间先验**写死成 CEC 的 1.0 权重。

两者都是同一招：**把「关于世界/关于梯度流的先验」编译进网络结构，换取可训练性。** 第三章说「结构先验是用已知换可学的货币」，第四章就是同一货币在时间轴上的再次发行。

**⑤ 这是 ResNet 残差连接的先声（伏笔，框架 7）。**

CEC 的本质是「给梯度一条不衰减的高速公路」。这个思想在 2015 年的 ResNet（skip connection）里换了件衣服重新登场——只不过 ResNet 把它从「时间上的循环」搬到了「深度上的堆叠」。框架 4 到框架 7，是同一个「梯度高速公路」思想在两个尺度上的两次应用。

**⑥ 「发明 ≠ 生效」第四次出现。**

LSTM 1997 就有了，但 1997–2010s 这十几年，序列建模的主流是 HMM、n-gram、CRF 这些统计方法，LSTM 被当成「太复杂」的异类。直到算力、数据、以及整个深度学习的声誉被 AlexNet 带起来，LSTM 才从「冷门」变成「标配」。而梯度爆炸的工程解法（gradient clipping）还要再等 Pascanu et al. 2013 才系统化[5]。

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 史料级 | Hochreiter 1991 德文硕士论文（largely unread）+ Bengio et al. 1994 英文论证 | 诊断早于解法 3–6 年，且被语言埋没 |
| 结构级 | CEC：权重固定 1.0 的线性自连接，梯度不衰减 | 「记忆」是结构保证，不是学出来的 |
| 史料级 | 遗忘门 2000 年才加（Gers et al.） | 门是「收费站」，CEC 是硬编码的「公路」 |
| 同构级 | CNN 权重共享（空间先验）↔ LSTM CEC（时间先验） | 同一思想在两个轴上的发行 |
| 伏笔级 | CEC「梯度高速公路」↔ ResNet skip connection（2015） | 框架 4 → 框架 7 的同源 |

## 反常识推论（母题）

> **「记忆」不是学出来的——是结构写死的。**

LSTM 教会我们的事，比「怎么处理序列」更深：

> 网络能「记住」多久，从来不取决于「学习算法有多聪明」，而取决于「梯度能不能原样穿过时间」。**凡是说「模型有记忆」的地方，下面都藏着一条被写进结构的、梯度不衰减的路径**——LSTM 是 CEC，ResNet 是 skip connection，Transformer 是 attention 的残差流。名字不同，通道是同一个。

再看「诊断 → 解法 → 统治」这条时间线：**1991 诊断、1997 解法、2010s 才统治**。这和前面每一章都共振：

- 第一章：能表达 ≠ 能学习（多层 1969 就能表达，1986 才会学）。
- 第二章：发明 ≠ 生效（BP 1970 就有，1986 证明，2012 统治）。
- 第三章：先验换可训练性（CNN 1980 有结构，1989 缝合 BP，2012 统治）。
- 第四章：**时间先验换可训练性（LSTM 1997 有解法，2010s 才统治）——而且它的「诊断」（1991）比「解法」（1997）还早，却被语言埋没了 3 年。**

一句话收束第四章：**LSTM 没有「发明记忆」，它发明的是「把记忆保持写死成一条权重恒为 1.0 的梯度隧道」。所谓门控，只是在这条已经铺好的高速公路上，装了几个可学习的收费站。**

---

## References

1. Hochreiter, S. (1991). *Untersuchungen zu dynamischen neuronalen Netzen.* Diploma thesis, TU München. [概述（Schmidhuber 官方页面）](https://people.idsia.ch/~juergen/fundamentaldeeplearningproblem.html)
2. Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. *IEEE Trans. Neural Networks*, 5(2), 157–166. [IEEE](https://ieeexplore.ieee.org/abstract/document/279181) · [Bengio 回顾演讲 PDF](https://www.iro.umontreal.ca/~bengioy/talks/back-to-the-future-ICML2016-23June.pdf)
3. Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 9(8), 1735–1780. [PDF](https://www.bioinf.jku.at/publications/older/2604.pdf) · [Wikipedia](https://en.wikipedia.org/wiki/Long_short-term_memory)
4. Gers, F. A., Schmidhuber, J., & Cummins, F. (2000). Learning to forget: Continual prediction with LSTM. *Neural Computation*, 12(10), 2451–2471. [MIT Press](https://direct.mit.edu/neco/article/12/10/2451/6415/Learning-to-Forget-Continual-Prediction-with-LSTM)
5. Pascanu, R., Mikolov, T., & Bengio, Y. (2013). On the difficulty of training recurrent neural networks. *ICML 2013*. [arXiv:1211.5063](https://arxiv.org/abs/1211.5063)

---

**关联**：[PAPERS.md §4](PAPERS.md#f4)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[03 · CNN](03-cnn.md) · [THE_THESES.md](THE_THESES.md)
