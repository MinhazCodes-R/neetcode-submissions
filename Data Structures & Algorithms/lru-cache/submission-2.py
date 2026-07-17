
class Node:
    def __init__(self, key_v, val, next_p: "Node" = None, prev_p: "Node" = None):
        self.prev_p = prev_p
        self.next_p = next_p
        self.key_v = key_v
        self.val = val
 
 
class LRUCache:
 
    def __init__(self, capacity: int):
        self.seen_values = {}
        self.head = None            # LRU end
        self.tail = None            # MRU end
        self.capacity = capacity
        self.current_capacity = 0
 
    # unlink a node from wherever it sits (head, middle, or tail)
    def _remove(self, node):
        if node.prev_p:
            node.prev_p.next_p = node.next_p
        else:                        # node was the head
            self.head = node.next_p
 
        if node.next_p:
            node.next_p.prev_p = node.prev_p
        else:                        # node was the tail
            self.tail = node.prev_p
 
        node.prev_p = None
        node.next_p = None
 
    # append a node at the tail (MRU end)
    def _add_tail(self, node):
        if self.tail is None:        # empty list
            self.head = node
            self.tail = node
        else:
            node.prev_p = self.tail
            self.tail.next_p = node
            self.tail = node
 
    def _remove_head(self):
        old_head = self.head
        self._remove(old_head)
        del self.seen_values[old_head.key_v]
        self.current_capacity -= 1
 
    def get(self, key: int) -> int:
        if key not in self.seen_values:
            return -1
        node = self.seen_values[key]
        self._remove(node)           # a read counts as recently used
        self._add_tail(node)
        return node.val
 
    def put(self, key: int, value: int) -> None:
        # key already present: update value, bump to MRU
        if key in self.seen_values:
            node = self.seen_values[key]
            node.val = value
            self._remove(node)
            self._add_tail(node)
            return
 
        # new key
        node = Node(key, value)
        self.seen_values[key] = node
        self._add_tail(node)
        self.current_capacity += 1
 
        if self.current_capacity > self.capacity:
            self._remove_head()
 