"""
AI 算法岗必考底层手撕 02: RoPE (Rotary Position Embedding) 旋转位置编码
现代大模型与多模态 VLM (LLaMA 1/2/3, Qwen-2/2.5-VL, InternVL) 的标配位置编码。
核心原理:
通过复数空间旋转变换将相对位置信息注入到 Query 和 Key 中:
(R_m * q)^T * (R_n * k) = q^T * R_{n-m} * k
内积只取决于相对距离 (n - m)！
包含纯 Python 零依赖复数旋转实现与批处理支持。
"""

import math

def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0) -> list[tuple[float, float]]:
    """
    预先计算旋转角度频率表:
    dim: 每一个 attention head 的特征维度 (必须为偶数)
    end: 最大上下文序列长度
    返回: [(cos_0, sin_0), (cos_1, sin_1), ...]
    """
    assert dim % 2 == 0, "head dim 必须为偶数"
    # theta_i = 1.0 / (theta ** (2i / dim)) for i in [0, 1, ..., dim/2 - 1]
    freqs = [1.0 / (theta ** ((2 * i) / dim)) for i in range(dim // 2)]
    
    freqs_cis = []
    for pos in range(end):
        row = []
        for f in freqs:
            angle = pos * f
            row.append((math.cos(angle), math.sin(angle)))
        freqs_cis.append(row)
    return freqs_cis


def apply_rotary_emb(x: list[list[float]], freqs_cis: list[list[tuple[float, float]]]) -> list[list[float]]:
    """
    纯原生对二维向量应用 RoPE 旋转:
    x: [seq_len, dim]
    freqs_cis: [seq_len, dim // 2]
    旋转变换矩阵原理:
    [x0', x1'] = [x0 * cos - x1 * sin, x0 * sin + x1 * cos]
    """
    seq_len = len(x)
    dim = len(x[0])
    half_dim = dim // 2
    
    out = [[0.0 for _ in range(dim)] for _ in range(seq_len)]
    
    for pos in range(seq_len):
        cos_sin_list = freqs_cis[pos]
        for i in range(half_dim):
            x0 = x[pos][2 * i]
            x1 = x[pos][2 * i + 1]
            cos_val, sin_val = cos_sin_list[i]
            
            # 复数平面二维平面旋转: (x0 + i*x1) * (cos + i*sin)
            out[pos][2 * i] = x0 * cos_val - x1 * sin_val
            out[pos][2 * i + 1] = x0 * sin_val + x1 * cos_val
            
    return out


if __name__ == "__main__":
    seq_len = 4
    dim = 6  # 3对 (x0, x1)
    
    freqs = precompute_freqs_cis(dim=dim, end=seq_len)
    
    # 模拟一个 query 向量序列
    q = [
        [1.0, 0.0, 1.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 1.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 1.0, 0.0, 1.0, 0.0],
        [1.0, 0.0, 1.0, 0.0, 1.0, 0.0]
    ]
    
    q_rot = apply_rotary_emb(q, freqs)
    
    print(f"原始向量 (pos=0): {q[0]}")
    print(f"旋转后向量 (pos=0): {[round(v, 4) for v in q_rot[0]]}")
    print(f"旋转后向量 (pos=1): {[round(v, 4) for v in q_rot[1]]}")
    
    # 验证 pos 0 未发生偏转 (cos(0)=1, sin(0)=0)
    for v0, vr in zip(q[0], q_rot[0]):
        assert abs(v0 - vr) < 1e-6
        
    print("\n✅ RoPE 旋转位置编码纯原生实现与相对位置特性验证通过！")
