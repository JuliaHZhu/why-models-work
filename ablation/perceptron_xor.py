"""可复现消融 #1：感知机的 XOR 能力边界

对应 PAPERS.md「框架 1 · Perceptron」的能力边界结论：
    单层感知机是线性分类器，无法表示 XOR（Minsky & Papert 1969，定理级证明）。

消融变量：隐层 + 非线性。
    实验 A（拿掉）：单层线性感知机 → loss 卡在 0.25，学不会 XOR。
    实验 B（加回）：1 个隐层 + tanh 非线性 → loss 收敛到 ~0，秒学 XOR。

成本：numpy 纯 CPU，几十秒内跑完，零深度学习框架依赖。

运行：python3 ablation/perceptron_xor.py
"""

import numpy as np

np.random.seed(0)

# XOR 的四个样本（经典线性不可分数据集）
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)


def train_linear(X, y, lr=0.5, epochs=5000):
    """实验 A：单层感知机（线性，无隐层，无非线性）。"""
    w = np.random.randn(2)
    b = 0.0
    for _ in range(epochs):
        pred = X @ w + b
        err = pred - y
        w -= lr * (X.T @ err) / len(X)
        b -= lr * err.mean()
    return w, b


def train_mlp(X, y, lr=0.1, epochs=20000, hidden=2):
    """实验 B：双层（1 隐层 + tanh 非线性）。"""
    W1 = np.random.randn(2, hidden) * 0.5
    b1 = np.zeros(hidden)
    W2 = np.random.randn(hidden) * 0.5
    b2 = 0.0
    for _ in range(epochs):
        h = np.tanh(X @ W1 + b1)          # 关键：非线性
        out = h @ W2 + b2
        err = out - y                     # (4,)
        dW2 = h.T @ err / len(X)
        db2 = err.mean()
        dh = err[:, None] * W2            # (4, hidden)
        dW1 = X.T @ (dh * (1 - h ** 2)) / len(X)
        db1 = (dh * (1 - h ** 2)).mean(0)
        W2 -= lr * dW2
        b2 -= lr * db2
        W1 -= lr * dW1
        b1 -= lr * db1
    return W1, b1, W2, b2


def main():
    print("=" * 60)
    print("消融：单层 vs 双层，对 XOR 的分类能力")
    print("=" * 60)

    # 实验 A
    w, b = train_linear(X, y)
    pred_a = X @ w + b
    loss_a = float(np.mean((pred_a - y) ** 2))
    print(f"\n[A] 单层感知机（线性）")
    print(f"    loss = {loss_a:.4f}  （理论下限 0.25，永远学不会）")

    # 实验 B
    W1, b1, W2, b2 = train_mlp(X, y)
    h = np.tanh(X @ W1 + b1)
    out = h @ W2 + b2
    loss_b = float(np.mean((out - y) ** 2))
    pred_b = np.round(out).astype(int)
    print(f"\n[B] 双层（1 隐层 + tanh）")
    print(f"    loss = {loss_b:.6f}")
    print(f"    预测 = {pred_b.tolist()}  真值 = {y.astype(int).tolist()}")

    print("\n" + "-" * 60)
    ok = (loss_a > 0.24) and (loss_b < 1e-3) and (pred_b == y.astype(int)).all()
    print(f"结论验证：{'✅ 通过' if ok else '❌ 未通过'}"
          " —— 拿掉隐层学不会，加回隐层秒学")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
