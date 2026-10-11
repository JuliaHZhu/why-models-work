# Papers — 14 次能力跃迁的代表研究（精版）

> 每个框架 3–5 篇奠基/代表论文，按三问标注：
> **是什么**（奠基/定义）· **特性**（理论性质）· **能力边界**（局限与上限）
>
> 格式：**标题** — 第一作者 et al. (年份) · 链接 · `标签` · 一句话核心贡献

---

## 1. Perceptron (1958)

- **The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain** — Rosenblatt (1958) · *Psychological Review* · `是什么` · 首个可学习的人工神经元模型，提出感知机学习规则。
- **Perceptrons: An Introduction to Computational Geometry** — Minsky & Papert (1969) · MIT Press · `能力边界` · 定理级证明：单层感知机是线性分类器，无法表示 XOR，定死第一代神经网络的能力上限。

## 2. Backpropagation (1986)

- **Learning representations by back-propagating errors** — Rumelhart, Hinton & Williams (1986) · *Nature* · `是什么` · 提出反向传播，让多层网络可训练，深度学习自此可微分。
- **Learning long-term dependencies with gradient descent is difficult** — Bengio, Simard & Frasconi (1994) · *IEEE TNN* · `能力边界` · 揭示梯度消失/爆炸，为 RNN 的长程依赖缺陷给出经验与理论证据。

## 3. CNN / Convolution (1989–2012)

- **Gradient-Based Learning Applied to Document Recognition** — LeCun et al. (1998) · *Proc. IEEE* · `是什么` · LeNet：卷积 + 池化 + BP 的完整视觉架构，确立卷积网络范式。
- **Group Equivariant Convolutional Networks** — Cohen & Welling (2016) · ICML · `特性` · 把卷积的平移等变性推广为群等变性，解释卷积为何高效且泛化。
- **Dynamic Routing Between Capsules** — Sabour, Frosst & Hinton (2017) · NeurIPS · `能力边界` · 指出 CNN 对物体姿态/部件关系的盲区，提出胶囊网络补位。

## 4. LSTM Gating (1997)

- **Long Short-Term Memory** — Hochreiter & Schmidhuber (1997) · *Neural Computation* · `是什么` · 用门控单元（遗忘门/输入门）解决 RNN 梯度消失，实现长程记忆。
- **Learning long-term dependencies with gradient descent is difficult** — Bengio et al. (1994) · *IEEE TNN* · `能力边界` · LSTM 所针对的问题本身：梯度下降难以学习长程依赖。

## 5. Distributed Representations / Embedding (2013)

- **Efficient Estimation of Word Representations in Vector Space** — Mikolov et al. (2013) · ICLR WS · `是什么` · Word2Vec：用 CBOW/Skip-gram 高效学出词向量。
- **Distributed Representations of Words and Phrases and their Compositionality** — Mikolov et al. (2013) · NeurIPS · `特性` · 发现向量空间的类比性质（国王−男人+女人≈王后），语义可做几何运算。
- **Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings** — Bolukbasi et al. (2016) · NeurIPS · `能力边界` · 词向量会继承语料的性别/社会偏见，揭示分布式表示的隐性缺陷。

## 6. Seq2Seq + Attention (2014)

- **Sequence to Sequence Learning with Neural Networks** — Sutskever, Vinyals & Le (2014) · NeurIPS · `是什么` · 编码器-解码器框架，端到端序列到序列学习。
- **Neural Machine Translation by Jointly Learning to Align and Translate** — Bahdanau, Cho & Bengio (2014) · ICLR 2015 · `特性` · 引入注意力，用软对齐替代固定长度瓶颈向量。

## 7. Residual Connections (2015)

- **Deep Residual Learning for Image Recognition** — He, Zhang, Ren & Sun (2016) · CVPR · `是什么` · ResNet：残差连接让百层以上网络可训练。
- **Identity Mappings in Deep Residual Networks** — He et al. (2016) · ECCV · `特性` · 论证恒等捷径让梯度无损直达，是深层可训练的关键。
- **Residual Networks Behave Like Ensembles of Relatively Shallow Networks** — Veit, Wilber & Belongie (2016) · NeurIPS · `能力边界` · 残差网络可视为浅层网络的集成，揭示其「有效深度」其实有限。

## 8. Transformer Self-Attention (2017)

- **Attention Is All You Need** — Vaswani et al. (2017) · NeurIPS · `是什么` · 抛弃递归，全注意力架构，序列建模从「链」变「完全图」。
- **Are Transformers Universal Approximators of Sequence-to-Sequence Functions?** — Yun et al. (2020) · ICLR · `特性` · 证明 Transformer（含位置编码）可逼近连续置换等变的序列到序列函数，给出表达能力下界。
- **Theoretical Limitations of Self-Attention in Neural Sequence Models** — Hahn (2020) · *TACL* · `能力边界` · 定理级证明：固定精度下自注意力无法学习某些语言（如计数/层级），硬注意力更弱。

## 9. Pretraining (BERT/GPT) (2018)

- **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** — Devlin et al. (2019) · NAACL · `是什么` · 双向掩码语言模型 + 微调范式，确立「先学语言再学任务」。
- **Improving Language Understanding by Generative Pre-Training** — Radford et al. (2018) · OpenAI · `是什么` · GPT-1：单向生成式预训练 + 微调。
- **Language Models are Few-Shot Learners** — Brown et al. (2020) · NeurIPS · `特性` · GPT-3：规模大到一定程度后涌现 few-shot 能力，无需微调。

## 10. Scaling Laws (2020)

- **Scaling Laws for Neural Language Models** — Kaplan et al. (2020) · arXiv · `是什么` · 发现 loss 随算力/数据/参数呈幂律下降，可外推预测。
- **Training Compute-Optimal Large Language Models** — Hoffmann et al. (2022) · arXiv · `特性` · Chinchilla：参数与数据应同比缩放，修正「只堆参数」的 scaling 定律。
- **Emergent Abilities of Large Language Models** — Wei et al. (2022) · TMLR · `能力边界` · 某些能力随规模「突变」涌现，说明小模型的评估不能外推到大模型。

## 11. Diffusion (2020–22)

- **Denoising Diffusion Probabilistic Models** — Ho, Jain & Abbeel (2020) · NeurIPS · `是什么` · DDPM：加噪-去噪马尔可夫链生成范式。
- **Score-Based Generative Modeling through Stochastic Differential Equations** — Song et al. (2021) · ICLR · `特性` · 用随机微分方程统一扩散模型，给出完整数学框架。
- **High-Resolution Image Synthesis with Latent Diffusion Models** — Rombach et al. (2022) · CVPR · `能力边界` · 指出像素空间采样慢的局限，移到潜空间（LDM）大幅提速。

## 12. RLHF (2022)

- **Deep Reinforcement Learning from Human Preferences** — Christiano et al. (2017) · NeurIPS · `是什么` · RLHF 源头：从人类偏好学奖励函数。
- **Training language models to follow instructions with human feedback** — Ouyang et al. (2022) · NeurIPS · `是什么` · InstructGPT：把 RLHF 用于语言模型对齐。
- **Scaling Laws for Reward Model Overoptimization** — Gao, Schulman & Hilton (2023) · ICML · `能力边界` · 奖励模型被过度优化会「刷分不干正事」（reward hacking），量化对齐的失效边界。

## 13. MoE Sparse Experts (2023–24)

- **Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer** — Shazeer et al. (2017) · ICLR · `是什么` · 稀疏门控 MoE 层，容量与计算解耦。
- **Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** — Fedus, Zoph & Shazeer (2022) · JMLR · `特性` · 用 top-1 路由 + 稀疏激活，把 MoE 做到万亿参数规模。

## 14. Test-time Compute (2024)

- **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters** — Snell et al. (2024) · arXiv · `特性` · 发现「推理时多算」可匹敌「训练时更大」，打开新的 scaling 维度。
- **Learning to Reason with LLMs** — OpenAI (2024) · 技术博客 · `是什么` · o1：用强化学习训练模型在回答前「思考」，test-time compute 首次大规模商用。
- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** — DeepSeek-AI (2025) · arXiv · `能力边界` · 开源复现推理模型，揭示纯 RL 可激发推理且存在可复现的「顿悟时刻」。
