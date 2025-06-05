class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # update existing
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash(key)
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        return str(self.table)

if __name__ == "__main__":
    ht = HashTable(size=5)

    ht.insert("apple", 5)
    ht.insert("banana", 10)
    ht.insert("grape", 15)
    ht.insert("apple", 7)  # update value
    ht.delete("banana")

    print("Search 'apple':", ht.search("apple"))
    print("Search 'banana':", ht.search("banana"))
    print("Full Table:")
    print(ht)
