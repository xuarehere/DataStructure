"""
LeetCode 102. 二叉树的层序遍历 (Binary Tree Level Order Traversal)
知识点: 广度优先搜索 (BFS)、队列先进先出 (FIFO)
直接复用 06 底座: 072_TreeTraversal.py 第 53-63 行原生队列实现
求职对应场景:
- 树状决策分层推演
- 3D 空间八叉树 (Octree) 逐层尺度特征提取与建图
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        基于 072_TreeTraversal.py 原生 BFS 的分层收集升级:
        1. 判空: 若 root 为 None，直接返回空列表 []
        2. 初始化队列 queue = deque([root])
        3. while queue 循环中，首先获取当前层节点数 level_size = len(queue)
        4. 遍历 level_size 次，依次 popleft() 出当前层节点，并将其子节点压入队尾
        5. 每一层作为一个独立列表收集到最终结果中
        
        时间复杂度: O(N) 每个节点入队和出队各一次
        空间复杂度: O(N) 最下层叶子节点最大约为 N/2
        """
        if not root:
            return []
            
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # 对应 072_TreeTraversal.py 中的左右子节点加入逻辑
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(current_level)
            
        return res


# 辅助测试构造二叉树
def build_tree(nodes: list) -> TreeNode:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        curr = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()
    
    # 用例 1: [3, 9, 20, None, None, 15, 7]
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    res1 = sol.levelOrder(root1)
    print("用例 1 层序遍历结果:", res1)
    assert res1 == [[3], [9, 20], [15, 7]]
    
    # 用例 2: 仅单节点 [1]
    root2 = build_tree([1])
    res2 = sol.levelOrder(root2)
    assert res2 == [[1]]
    
    # 用例 3: 空树 []
    assert sol.levelOrder(None) == []
    
    print("\n✅ LeetCode 102 / 基于 072 树层序遍历算法测试全部通过！")
