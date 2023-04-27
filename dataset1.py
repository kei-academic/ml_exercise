import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    y = np.sin(np.pi * x * 0.8) * 10
    return np.array(y)

print(true_function(0))

# 定義域 -1 <= x <= 1 の範囲で、0.01刻みのx値を生成
x = np.arange(-1, 1, 0.01)

# xに対応するy値を計算
y = true_function(x)

# グラフを描画
plt.plot(x, y, label="y = sin(pi * x * 0.8) * 10")

# 凡例を表示
plt.legend()

# グラフを表示
plt.show()
