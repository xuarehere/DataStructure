"""
AI 算法岗必考底层手撕 03: Diffusion Policy / 世界模型加噪与调度器 (Noise Schedule)
核心数学公式:
1. 线性调度器: beta_t 从 beta_start 线性递增到 beta_end
2. alpha_t = 1 - beta_t, alpha_bar_t = cumprod(alpha_1, ..., alpha_t)
3. 前向加噪步 (Forward Diffusion Step):
   q(x_t | x_0) = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * epsilon,  epsilon ~ N(0, I)
对应具身控制与世界模型场景:
- Diffusion Policy 动作生成轨迹扩散加噪
- 视频生成世界模型前向扩散训练
"""

import math
import random

class LinearDiffusionScheduler:
    def __init__(self, timesteps: int = 1000, beta_start: float = 1e-4, beta_end: float = 0.02):
        self.timesteps = timesteps
        self.betas = [
            beta_start + (beta_end - beta_start) * (t / (timesteps - 1))
            for t in range(timesteps)
        ]
        self.alphas = [1.0 - b for b in self.betas]
        
        # 计算累计连乘积 alpha_bars
        self.alpha_bars = []
        prod = 1.0
        for a in self.alphas:
            prod *= a
            self.alpha_bars.append(prod)
            
        self.sqrt_alpha_bars = [math.sqrt(ab) for ab in self.alpha_bars]
        self.sqrt_one_minus_alpha_bars = [math.sqrt(1.0 - ab) for ab in self.alpha_bars]

    def add_noise(self, x_0: list[float], t: int, noise: list[float] = None) -> tuple[list[float], list[float]]:
        """
        前向加噪步: x_t = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * noise
        """
        assert 0 <= t < self.timesteps, f"时间步 t 越界: {t}"
        dim = len(x_0)
        
        # 若未提供高斯噪声，则从标准正态分布采样
        if noise is None:
            noise = [random.gauss(0.0, 1.0) for _ in range(dim)]
            
        sqrt_ab = self.sqrt_alpha_bars[t]
        sqrt_omab = self.sqrt_one_minus_alpha_bars[t]
        
        x_t = [
            sqrt_ab * x + sqrt_omab * eps
            for x, eps in zip(x_0, noise)
        ]
        return x_t, noise


if __name__ == "__main__":
    scheduler = LinearDiffusionScheduler(timesteps=1000)
    
    # 模拟一个机器人 6-DoF 关节动作向量 (Action Trajectory Token)
    action_x0 = [0.5, -0.2, 1.2, 0.0, -0.8, 0.4]
    
    # 在 t=0 (微量加噪) 与 t=999 (全高斯纯噪) 分别测试
    x_t0, noise0 = scheduler.add_noise(action_x0, t=0)
    x_t999, noise999 = scheduler.add_noise(action_x0, t=999)
    
    print(f"原始动作向量 x_0: {action_x0}")
    print(f"t=0 (起步加噪): {[round(v, 4) for v in x_t0]}")
    print(f"t=999 (纯高斯白噪): {[round(v, 4) for v in x_t999]}")
    
    # 理论验证: t=0 时 sqrt(alpha_bar_0) 极接近 1.0，偏离很小
    assert abs(x_t0[0] - action_x0[0]) < 0.1
    print("\n✅ Diffusion Policy 前向加噪步与调度器公式测试全部通过！")
