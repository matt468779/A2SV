class LRUCache:
    class ListNode:
        def __init__(self, val=0, key=None, next=None, prev=None) -> None:
            self.val = val
            self.key = key
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = None
        self.start = None

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        node = self.cache[key]
        if node.next == None:
            return node.val
        elif node.prev == None:
            self.start = self.start.next
            self.start.prev = None
            self.queue.next = node
            node.prev = self.queue
            self.queue = self.queue.next
            return node.val

        prev = node.prev
        next = node.next
        self.queue.next = node
        prev.next = next
        next.prev = prev
        node.prev = self.queue
        self.queue = self.queue.next
        self.queue.next = None
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value
            self.get(key)
            return
        
        if len(self.cache.keys()) >= self.capacity:
            self.cache.pop(self.start.key)
            if not self.start.next:
                self.start = self.ListNode(val=value, key=key)
                self.cache[key] = self.start
                return
            self.start = self.start.next
            self.start.prev = None
    
        if self.queue == None:
            self.queue = self.ListNode(val=value, key=key)
            self.start = self.queue
            self.cache[key] = self.queue
            return
        self.queue.next = self.ListNode(val=value, key=key, prev=self.queue)
        self.queue = self.queue.next
        self.cache[key] = self.queue
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)