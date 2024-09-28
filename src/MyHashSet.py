class MyHashSet:
    def __init__(self, capacity=100):
        self.buckets = [[] for _ in range(capacity)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            bucket_index = self.get_bucket_index(key)
            self.buckets[bucket_index].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            bucket_index = self.get_bucket_index(key)
            self.buckets[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = self.get_bucket_index(key)
        return key in self.buckets[bucket_index]

    def get_bucket_index(self, key: int) -> int:
        return key %  len(self.buckets)

mySet =  MyHashSet()
mySet.add(1)
mySet.add(2)
mySet.add(1)
mySet.add(1)
mySet.add(1)
mySet.add(1)

print(mySet.buckets)
