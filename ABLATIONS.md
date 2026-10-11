# 可复现消融（Ablations）

> 归因四段法（现象 → 主流归因 → 真实机制 → 证据）里，「真实机制」最硬的证据不是
> 「加了 X 有效」，而是**「拿掉 X 就塌」**。消融 = 控制变量地拿掉某个机制，看能力是否
> 对应地消失，从而把「归因」从叙事变成可检验的因果断言。
>
> 本目录按**复现成本从低到高**分三档，只收录「真的能复现」的入口，不堆链接。

---

## ✅ 已落地：可自行运行的消融

### #1 感知机 XOR —— 单层学不会，双层秒学（框架 1）

**消融变量**：隐层 + 非线性。

**结论**（对应 PAPERS.md 框架 1 的能力边界，Minsky & Papert 1969 的定理级证明）：

| 实验 | 配置 | 结果 |
|------|------|------|
| A | 单层感知机（线性，无隐层） | loss 卡死在 **0.25**，学不会 XOR |
| B | 双层（1 隐层 + tanh） | loss 收敛到 **0**，预测全对 |

**运行**（零深度学习框架依赖，纯 numpy，CPU 秒级）：

```bash
python3 ablation/perceptron_xor.py
```

**实测输出**：

```
[A] 单层感知机（线性）
    loss = 0.2500  （理论下限 0.25，永远学不会）
[B] 双层（1 隐层 + tanh）
    loss = 0.000000
    预测 = [0, 1, 1, 0]  真值 = [0, 1, 1, 0]
结论验证：✅ 通过 —— 拿掉隐层学不会，加回隐层秒学
```

**为什么它够「最低成本」**：XOR 是「能力边界」里最干净、最便宜的那个实验——
单层感知机的线性不可分性，不需要 GPU、不需要数据集、不需要训练大模型，就能复现一条
**定理级**结论。

---

## 🔗 现成可复现入口（搜索验证，可直接 fork / 运行）

### 残差连接（框架 7）—— 拿掉 skip，深层退化

- **消融问题**：拿掉 skip connection，深层网络还训得动吗？
- **预期结果**：退化（degradation）——越深 loss 越高、训不动（ResNet 原论文的动机）。
- **可复现入口**：
  - `asoueidan3/resnet-ablation` — 复现并扩展原论文（plain net vs ResNet-20，CIFAR-10，还加了数据效率实验）
    <https://github.com/asoueidan3/resnet-ablation>
  - `samirsen/resnet-ablation` — ResNet-34 vs 无残差的 VGG，抗噪鲁棒性对比
    <https://github.com/samirsen/resnet-ablation>
- **成本**：单卡 GPU + CIFAR-10，小时级。

### 缩放定律（框架 10）—— 参数/数据/算力的最优配比

- **消融问题**：给定算力预算，参数和数据该怎么配才是 compute-optimal？
- **预期结果**：Chinchilla 定律——参数与数据应**同比**缩放，而非只堆参数（修正 Kaplan）。
- **可复现入口**：
  - `karpathy/nanoGPT` 的 `scaling_laws.ipynb` — Karpathy 官方复现 Chinchilla scaling laws（含 FLOPs/参数量计算工具）
    <https://github.com/karpathy/nanoGPT/blob/master/scaling_laws.ipynb>
- **成本**：公式拟合部分笔记本 CPU 可跑；全量训练网格需 GPU（nanoGPT 有 speedrun 教程）。

### 感知机 XOR（框架 1，外部权威版）

- **可复现入口**：Princeton NEU-PSY-502「Perceptron and XOR」notebook（学术课程级，含线性不可分性的严格论证）
  <https://princetonuniversity.github.io/NEU-PSY-502/content/502B/Computation/Primer/notebooks/3+Perceptron+and+XOR.html>
- **成本**：笔记本，即开即用。与本地脚本 #1 互为印证。

---

## ⚠️ 需自建 / 高成本（诚实标注，暂无「一键可跑」入口）

> 这些框架的消融要么需要 GPU + 数据集训练，要么网上只有教学博客、没有强可复现
> notebook。给出消融设计和建议入口，供后续按需补建。

| 框架 | 消融问题 | 预期结果 | 现状与建议 |
|------|---------|---------|-----------|
| Backprop (2) | 拿掉 BP，换随机搜索/逐层贪心 | 多层端到端训不动 | 需自建小 MLP；对比 BP vs 非 BP 的收敛速度 |
| CNN (3) | 拿掉卷积，换等参数 MLP | 图像性能大幅塌 | 需自建小 CNN vs MLP；教学级代码很多 |
| LSTM (4) | 拿掉门控，退回 vanilla RNN | 长程依赖（copying task）塌 | 需自建 copying task；经典 notebook 可搜 |
| Embedding (5) | 拿掉分布式表示，用 one-hot | 语义类比（国王−男人+女人≈王后）消失 | 需自建 Word2Vec 小语料对比 |
| Seq2Seq+Attention (6) | 拿掉注意力 | 长句翻译质量塌 | Bahdanau 原论文有消融表，可小规模复现 |
| Transformer (8) | 拿掉位置编码 | 序列顺序信息丢失 | 搜到的多为教学博客；可用 alexliap/attention-is-all-you-need-build-the-transformer-from-scratch 自建 copy task |
| Pretraining (9) | 拿掉预训练，从零训下游任务 | 下游性能大幅塌 | 高成本（需预训练 + 下游微调网格） |
| Diffusion (11) | 减少去噪步数 / 移出潜空间 | 采样质量-速度权衡 | 可用 diffusers 库小规模对比 |
| RLHF (12) | 拿掉 RLHF 只 SFT | 对齐退化；reward overoptimization | Gao 的 reward hacking 有公开，但需 GPU |
| MoE (13) | 拿掉稀疏路由，变 dense | 容量-计算权衡失衡 | 高成本（需大模型 + 多卡） |
| Test-time compute (14) | 限制推理时思考预算 | 推理能力下降 | 高成本；DeepSeek-R1 开源权重可参考 |

---

## 复现方法论（怎么读这些消融）

1. **控制变量**：每次只动一个机制（隐层、skip、门控、注意力…），其余不动。
2. **看方向不看绝对值**：消融要回答的是「拿掉 X，能力是否**对应地**塌」，不是刷 SOTA。
3. **记录失效边界**：有些机制只在特定规模/深度才体现作用（如残差要「足够深」才拉开差距），
   消融时要注明在什么尺度下结论成立——这正是 PAPERS.md 里「能力边界」那一问的意义。
