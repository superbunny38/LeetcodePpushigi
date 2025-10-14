class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity):
        self.size = capacity
        self.cache = {}
        self.left, self.right = Node(),Node()
        self.left.next,self.right.prev = self.right,self.left
    
    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev_mru = self.right.prev
        prev_mru.next = node
        self.right.prev = node
        node.prev, node.next = prev_mru, self.right
    
    def get(self, key):
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key=key,val=value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.size:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]
            

obj = LRUCache(2)
print(obj.put(2,1))
print(obj.cache.keys())
print("lru:",obj.left.next.key)
print()
print(obj.put(1,1))
print(obj.cache.keys())
print("lru:",obj.left.next.key)
print()
print(obj.put(2,3))
print(obj.cache.keys())
print("lru:",obj.left.next.key)
print()
print(obj.put(4, 1))
print(obj.cache.keys())
print("lru:",obj.left.next.key)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

# obj = LRUCache(1)
# print(obj.put(2,1))
# print(obj.cache.keys())
# print(obj.get(2))