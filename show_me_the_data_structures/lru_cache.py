class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.size += 1

    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = self.tail.next
        self.size += 1

    def insert(self, position, node):
        if position == 0:
            self.insert_at_head(node)
        elif position < self.size:
            current = self.head
            counter = 0
            while counter != position:
                current = current.next
                counter += 1
            previous_node = current.previous
            previous_node.next = node
            node.previous = previous_node
            node.next = current
            current.previous = node
            self.size += 1
        else:
            self.append(node)

    def remove_at_end(self):
        remove_node = self.tail
        self.tail = self.tail.previous
        remove_node.previous = None
        self.tail.next = None
        self.size -= 1
        return remove_node

    def remove_at_head(self):
        remove_node = self.tail
        self.head = self.head.next
        remove_node.next = None
        self.head.previous = None
        self.size -= 1
        return remove_node

    def remove(self, node):
        previous_node = node.previous
        next_node = node.next
        if previous_node and next_node:
            previous_node.next = next_node
            next_node.previous = previous_node
            self.size -= 1
        elif previous_node:
            self.remove_at_end()
        else:
            self.remove_at_head()


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.doubly_linked_list = DoublyLinkedList()
        self.map = {}
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.map[key] if key in self.map else None
        if node:
            self.doubly_linked_list.remove(node)
            self.doubly_linked_list.insert(0, node)
            return node.value
        return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.map:
            new_node = Node(key, value)
            replace_node = self.map[key]
            self.doubly_linked_list.remove(replace_node)
            self.map[key] = new_node
            self.doubly_linked_list.insert(0, new_node)
        else:
            new_node = Node(key, value)
            if self.doubly_linked_list.size >= self.capacity:
                removed_node = self.doubly_linked_list.remove_at_end()
                del self.map[removed_node.key]
            self.map[key] = new_node
            self.doubly_linked_list.insert(0, new_node)


def test_cases():
    lru_cache = LRU_Cache(5)
    lru_cache.set(3, 5)
    lru_cache.set(4, 5)
    lru_cache.set(5, 5)
    assert lru_cache.get(3) == 5
    lru_cache.set(6, 5)
    lru_cache.set(7, 5)
    lru_cache.set(8, 5)
    assert lru_cache.get(4) == -1
    lru_cache.set(4, 4)
    assert lru_cache.get(5) == -1
    assert lru_cache.get(4) == 4
    assert lru_cache.get(2) == -1
    assert lru_cache.get(None) == -1
    assert lru_cache.get(6) == 5
    print("All the test cases has passed")

if __name__ == '__main__':
    test_cases()