class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def hash(self, key):
        return hash(key) % len(self.table)

    def insert(self, key, value):
        index = self.hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None


ht = HashTable()
ht.insert("key1", "value1")
ht.insert("key2", "value2")
print(ht.get("key1"))