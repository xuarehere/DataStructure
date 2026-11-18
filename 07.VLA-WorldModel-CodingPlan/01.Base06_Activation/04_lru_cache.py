"""
LeetCode 146. LRU 缓存机制 (LRU Cache)
知识点: 双向链表 (Doubly Linked List) + 哈希表 (Hash Map)
直接复用 06 底座: 033_DoublyNode.py (双向指针 prev/next 的维护)
求职对应场景:
- 大模型推理显存 Cache 块淘汰策略 (PagedAttention 内存管理)
- 自动驾驶高精地图瓦片与特征缓存驱逐
"""

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU (Least Recently Used) 缓存淘汰机制:
    - 获取 get(key) 和 写入 put(key, value) 均要求 O(1) 时间复杂度。
    - 使用伪头部 (dummy head) 和伪尾部 (dummy tail) 简化边界双向指针操作。
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLinkedNode
        self.size = 0
        # 伪头部和伪尾部节点 (对应 033_DoublyNode 思想)
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_to_head(self, node: DLinkedNode):
        """将节点插入到双向链表头部 (表示最新访问)"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode):
        """从双向链表中移除已有节点"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: DLinkedNode):
        """将已有节点移动到链表头部"""
        self._remove_node(node)
        self._add_node_to_head(node)

    def _pop_tail(self) -> DLinkedNode:
        """弹出尾部最久未使用的节点"""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                removed = self._pop_tail()
                del self.cache[removed.key]
                self.size -= 1


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1       # 返回 1，并且节点 1 变为最新
    lru.put(3, 3)                # 驱逐 key 2
    assert lru.get(2) == -1      # 2 已被淘汰
    lru.put(4, 4)                # 驱逐 key 1
    assert lru.get(1) == -1      # 1 已被淘汰
    assert lru.get(3) == 3       # 返回 3
    assert lru.get(4) == 4       # 返回 4
    print("✅ LeetCode 146 / LRU 缓存双向链表+哈希测试全部通过！")
