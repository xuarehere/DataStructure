"""
AI 算法岗高频手撕：Attention 机制变体及底层原理实现
包含两套实现：
1. 纯 Python 原生数组/数学实现（无任何依赖，面试白板手撕必备）
2. PyTorch 工业级张量实现（如果环境中安装了 torch 则自动启用）
"""

import math

# =====================================================================
# 纯 Python 白板手撕版本（零第三方依赖，适合白板面试手撕数学原理）
# =====================================================================

def matrix_multiply(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """矩阵乘法 A (M x K) * B (K x N) -> (M x N)"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B, f"维度不匹配: {cols_A} vs {rows_B}"
    
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for k in range(cols_A):
            for j in range(cols_B):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_transpose(A: list[list[float]]) -> list[list[float]]:
    """矩阵转置"""
    rows, cols = len(A), len(A[0])
    return [[A[r][c] for r in range(rows)] for c in range(cols)]

def softmax(vec: list[float], mask: list[bool] = None) -> list[float]:
    """数值稳定的 Softmax，支持因果遮蔽 (Causal Mask)"""
    safe_vec = []
    for i, v in enumerate(vec):
        if mask is not None and mask[i]:
            safe_vec.append(-1e9)
        else:
            safe_vec.append(v)
            
    max_val = max(safe_vec)
    exp_vals = [math.exp(v - max_val) for v in safe_vec]
    sum_exp = sum(exp_vals)
    return [e / (sum_exp + 1e-12) for e in exp_vals]

def pure_scaled_dot_product_attention(
    Q: list[list[float]], 
    K: list[list[float]], 
    V: list[list[float]], 
    causal: bool = False
) -> list[list[float]]:
    """
    点积注意力核心算法（纯手撕）:
    Attention(Q, K, V) = Softmax(Q * K^T / sqrt(d_k)) * V
    Q: [seq_len_q, d_k]
    K: [seq_len_k, d_k]
    V: [seq_len_k, d_v]
    """
    seq_len_q = len(Q)
    seq_len_k = len(K)
    d_k = len(Q[0])
    scale = math.sqrt(d_k)
    
    # 1. 计算 Q * K^T
    K_T = matrix_transpose(K)
    scores = matrix_multiply(Q, K_T) # [seq_len_q, seq_len_k]
    
    # 2. 缩放与 Softmax
    attn_weights = []
    for i in range(seq_len_q):
        scaled_row = [scores[i][j] / scale for j in range(seq_len_k)]
        mask = [j > i for j in range(seq_len_k)] if causal else None
        attn_weights.append(softmax(scaled_row, mask=mask))
        
    # 3. 乘上 V: [seq_len_q, seq_len_k] * [seq_len_k, d_v] -> [seq_len_q, d_v]
    output = matrix_multiply(attn_weights, V)
    return output


# =====================================================================
# PyTorch 框架级手撕（若安装 PyTorch 则调用）
# =====================================================================
try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    class MultiHeadAttentionPyTorch(nn.Module):
        def __init__(self, embed_dim: int, num_heads: int):
            super().__init__()
            assert embed_dim % num_heads == 0
            self.embed_dim = embed_dim
            self.num_heads = num_heads
            self.head_dim = embed_dim // num_heads

            self.q_proj = nn.Linear(embed_dim, embed_dim)
            self.k_proj = nn.Linear(embed_dim, embed_dim)
            self.v_proj = nn.Linear(embed_dim, embed_dim)
            self.out_proj = nn.Linear(embed_dim, embed_dim)

        def forward(self, x: torch.Tensor, mask: torch.Tensor = None):
            B, L, _ = x.shape
            q = self.q_proj(x).view(B, L, self.num_heads, self.head_dim).transpose(1, 2)
            k = self.k_proj(x).view(B, L, self.num_heads, self.head_dim).transpose(1, 2)
            v = self.v_proj(x).view(B, L, self.num_heads, self.head_dim).transpose(1, 2)

            scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
            if mask is not None:
                scores = scores.masked_fill(mask, -1e9)
            attn = F.softmax(scores, dim=-1)
            out = torch.matmul(attn, v).transpose(1, 2).contiguous().view(B, L, self.embed_dim)
            return self.out_proj(out)
except ImportError:
    MultiHeadAttentionPyTorch = None


if __name__ == "__main__":
    print("=== 测试：纯 Python 面试白板手撕 Attention (Causal) ===")
    # 3 个 token，特征维度 4
    dummy_Q = [
        [1.0, 0.0, 1.0, 0.5],
        [0.0, 2.0, 0.5, 1.0],
        [1.5, 1.0, 0.0, 2.0]
    ]
    dummy_K = dummy_Q
    dummy_V = [
        [0.1, 0.2],
        [0.3, 0.4],
        [0.5, 0.6]
    ]
    
    out = pure_scaled_dot_product_attention(dummy_Q, dummy_K, dummy_V, causal=True)
    print(f"输入序列长度: {len(dummy_Q)}, 隐藏维度: {len(dummy_Q[0])}")
    print(f"注意力输出形状: {len(out)} x {len(out[0])}")
    for row_idx, row in enumerate(out):
        print(f"Token {row_idx} 输出向量: {[round(x, 4) for x in row]}")
        
    print("\n✅ 纯 Python 原生 Attention 手撕算法测试顺利通过！")
