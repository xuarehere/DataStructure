"""
LeetCode 207. 课程表 (Course Schedule)
知识点: 有向无环图 (DAG)、拓扑排序 (Topological Sort)、入度表 BFS (Kahn 算法)
求职对应场景:
- 深度学习计算图算子依赖分析 (Operator dependency analysis in ONNX / TensorRT)
- 自动驾驶时空感知与规划模块任务调度
"""

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Kahn 算法 (基于入度的 BFS 拓扑排序):
        1. 统计每个节点的入度 (in_degree)，并构建邻接表 (adjacency list)
        2. 将所有入度为 0 的节点放入队列
        3. 不断从队列取出节点，并将该节点所有下游邻居的入度减 1
        4. 若邻居入度变为 0，则加入队列
        5. 最终若弹出的节点总数等于 numCourses，说明图无环，拓扑排序成功
        
        时间复杂度: O(V + E)
        空间复杂度: O(V + E)
        """
        in_degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # 1. 建图: edge: [cur, pre] 表示 pre -> cur
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].append(cur)
            
        # 2. 初始所有入度为 0 的节点入队 (对应 06 中的 050_Queue 思想)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        visited_count = 0
        
        # 3. BFS 拓扑遍历
        while queue:
            node = queue.popleft()
            visited_count += 1
            for nxt in adj[node]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
                    
        return visited_count == numCourses


if __name__ == "__main__":
    sol = Solution()
    
    # 用例 1: 2门课，选 1 需先修 0 -> 可以完成
    assert sol.canFinish(2, [[1, 0]]) == True
    print("用例 1 通过: [1, 0] -> True")
    
    # 用例 2: 2门课，相互依赖 [1, 0] 和 [0, 1] -> 形成死锁环，无法完成
    assert sol.canFinish(2, [[1, 0], [0, 1]]) == False
    print("用例 2 通过: 互相依赖死锁环 -> False")
    
    # 用例 3: 4门课程的算子拓扑图
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True
    print("用例 3 通过: DAG 算子计算图 -> True")
    
    print("\n✅ LeetCode 207 / 拓扑排序算法全部通过！")
