# 05 · Distributed Representations / Embeddings（2013）—— 语义从「分布」里涌现

> 归因四段法 · 第五篇。模板：一句话论点 → 现象 → 主流归因 → 真实机制 → 证据 → 反常识推论。

## 一句话论点（Thesis）

word2vec 没有「发明分布式表征」——那东西 1986 年就有了，2003 年神经语言模型也早就做出了词向量。它真正做的是：**把「分布假说」这条 56 年的语言学先验，写进「预测上下文」这个可大规模计算的训练任务里**，让「语义」从「词在上下文中的分布」中涌现，变成可加减的向量几何。

## 现象

- 2013 年 Google 发布 word2vec 工具，一夜爆红。
- 最炸裂的演示：`king − man + woman ≈ queen`——语义关系居然能做向量算术。
- Embedding 从此成为所有深度学习的「输入层标准件」：文本、图像、图谱、推荐，万物皆可 embedding。

## 主流归因

教科书叙事：**2013 年 Mikolov 等人发明了 word2vec，用神经网络把词编码成「稠密向量」，从此机器「懂了」语义。**

## 真实机制

拆开看，这个叙事在三个地方都是反的：

**① 「语义从上下文来」不是神经网络发现的——是 1957 年的语言学家。**

分布假说（Distributional Hypothesis）由结构语言学家提出：Harris 1954、Firth 1957。Firth 那句话如今成了 word2vec 的墓志铭[1]：

> You shall know a word by the company it keeps.（「看一个词跟谁做伴，就知道它什么意思。」）

词义不是一个词「自带」的抽象属性，而是**从它的使用分布中涌现的**。这条假设比 word2vec 早 56 年，比神经网络本身还早。word2vec 的全部功劳，是把这条旧假设「算」了出来，而不是「想」了出来。

**② 「分布式表征」这个术语，是 1986 年 Hinton 们提的。**

在 PDP（Parallel Distributed Processing）两卷本里，Hinton, McClelland & Rumelhart 1986 明确区分了「局部表征」（localist，一个神经元 = 一个概念，符号主义的做法）和「分布式表征」（distributed，一个概念由**许多神经元的激活模式共同**表示）[2]。分布式表征自带一个副产品——**自动泛化**：网络对某个模式做出反应，就会自动对「相似的模式」做出相似反应。这是后来一切 embedding 的根基，1986 年就已经写清楚了。

**③ Bengio 2003 就做出了「神经网络语言模型 + 词向量」，但被算力困了十年。**

Bengio, Ducharme, Vincent & Jauvin 2003 的《A Neural Probabilistic Language Model》是第一个神经网络语言模型，词向量（word embedding）在那里是**预测下一个词的副产物**[3]。评论界一致承认它「ahead of its time」：

> It took 10 years and dramatically faster hardware before the approach became practical at scale.

所以 2013 年 word2vec 爆红，爆的**不是「新理论」，是「工程化」**。

**④ word2vec 真正的贡献：把「先验」从结构搬进了「训练任务」。**

Mikolov 等 2013 的贡献是两件事[4][5]：

- **两个可扩展的训练目标**：CBOW（用上下文预测中心词）、Skip-gram（用中心词预测上下文）。
- **负采样（negative sampling）**：不精确计算 softmax 的分母（那要遍历整个词表），而是采样少量「负例」近似——让十亿级词库可训练。

但请注意这里更深的一层：**「预测上下文」这个任务本身就是「分布假说」的先验**。你没让网络「学语义」，你让它「猜上下文」——而「上下文相似的词」自动会得到相似的向量。**先验不必写进网络结构，可以写进「你要网络去做的任务」。**

这跟前两章是一个母题的升级：

| 章 | 先验 | 载体 |
|----|------|------|
| 03 CNN | 平移等变（空间） | 写进**结构**（权重共享） |
| 04 LSTM | 恒定梯度传导（时间） | 写进**结构**（CEC 1.0） |
| 05 Embedding | 分布假说（语义） | 写进**任务**（预测上下文） |

**⑤ `king − man + woman ≈ queen` 不是设计出来的——是涌现的。**

这条线性语义关系，Mikolov 等人是自己「发现」的，不是「设计」的[5]：训练完一查，发现 `vec(king) − vec(man) + vec(woman)` 的最近邻居然就是 `queen`。这意味着：分布式表征的价值不在于「每个向量编码了某个语义」，而在于**「语义关系」本身变成了可计算的向量运算**——语义从「符号」变成了「几何」。

**⑥ 「发明 ≠ 生效」第五次，且最戏剧性。**

时间线：1986 有思想 → 2003 有模型 → 2013 才爆红。催化剂不是新理论，是**「Google 开源 + 训练极快 + king−queen 这个直觉炸裂的例子」**。一个 56 年前的旧假设、一个 10 年前的旧模型，被「工程化」重新点燃。

## 证据 / 证明

| 强度 | 证据 | 指向 |
|------|------|------|
| 史料级 | Firth 1957「You shall know a word by the company it keeps」 | 分布假说早于 word2vec 56 年 |
| 概念级 | Hinton et al. 1986 PDP 卷「分布式表征」 | 术语与「自动泛化」1986 年已有 |
| 模型级 | Bengio et al. 2003 神经语言模型（embedding 是副产物） | 模型早于 word2vec 10 年 |
| 工程级 | 负采样 + CBOW/Skip-gram（Mikolov 2013） | word2vec 的贡献是「可扩展」，不是「新表征」 |
| 涌现级 | `king − man + woman ≈ queen` 是事后发现 | 语义关系是涌现的几何，非设计 |

## 反常识推论（母题）

> **「语义」不是被编码进去的——是从「上下文分布」里涌现的。**

这一章把前面所有母题收成一条更深的线：

> 前面几章，我们看到的「先验」都被写进了**网络结构**（CNN 的权重共享、LSTM 的 CEC）。这一章开始，先验换了地方——**写进「训练任务」里**。「预测上下文」这个任务本身就是「上下文相似 ⇒ 语义相似」的假设。网络结构可以什么都不懂，只要任务设计对了，语义会自己从分布里长出来。

**这是整本书最重要的一次转向，也是通往框架 9（预训练范式）的桥：** 如果「先验 = 任务」，那么「造一个足够大的通用任务」（BERT 的 masked LM、GPT 的 next-token prediction）就是在「大规模地注入先验」。所谓「预训练」，本质就是**把人类几十年的语言学/世界知识先验，蒸馏进一个「填空 / 续写」任务里**——这是第五章埋下的、后面要用两次的伏笔。

一句话收束第五章：**word2vec 没有教机器「语义」，它只是把 Firth 1957 年的那句老话「看一个词跟谁做伴」做成了一个可以跑十亿个词的填空题——而语义，是填空填出来的几何。**

---

## References

1. Firth, J. R. (1957). A synopsis of linguistic theory, 1930–1955. *Studies in Linguistic Analysis*. [Quote Investigator 考证](https://quoteinvestigator.com/2022/09/18/word-company/) · [Wikipedia: Distributional semantics](https://en.wikipedia.org/wiki/Distributional_semantics)
2. Hinton, G. E., McClelland, J. L., & Rumelhart, D. E. (1986). Distributed representations. In *Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. 1*. MIT Press. [Rogers & McClelland 书章 PDF（一手综述）](https://web.stanford.edu/~jlmcc/papers/RogersMcCBook_7_03.pdf)
3. Bengio, Y., Ducharme, R., Vincent, P., & Jauvin, C. (2003). A neural probabilistic language model. *JMLR*, 3(Feb), 1137–1155. [JMLR](https://jmlr.org/papers/v3/bengio03a.html)
4. Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. [arXiv:1301.3781](https://arxiv.org/abs/1301.3781)
5. Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. [arXiv:1310.4546](https://arxiv.org/abs/1310.4546)

---

**关联**：[PAPERS.md §5](PAPERS.md#f5)（3 篇文献）· [ABLATIONS.md](ABLATIONS.md)（可复现消融）· 上一篇：[04 · LSTM](04-lstm.md) · [THE_THESES.md](THE_THESES.md)
