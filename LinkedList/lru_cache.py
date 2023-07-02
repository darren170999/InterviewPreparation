# LRUCache init -> gives Capacity
# if Cap exceeded, we want to remove LRU
# Thus, important to maintain order of items used.
# Doubly Linked List should be used here to maintain the order
# Left is LRU right is Most recently used
# new nodes put are considered to be most recently used
# back to back puts will push the existing order left
# HashMap is needed because we want constant lookup time
# Size of Hashmap == capacity
# HashMap holds key and pointer to node

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int) : 
        self.cap = capacity
        self.cache = {} # map key to node
        # left = lru, right = most recent
        self.left, self.right= Node(0,0), Node(0,0)
    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.next = nxt, prev
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key:int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key:int, value: int) -> None:
        if ket in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]