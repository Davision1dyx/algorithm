from com.dyx.Algorithm.hash_map.array_hash_map import Pair


class HashMapOpenAddressing:
    def __init__(self):
        self.__size = 0
        self.__capacity = 4
        self.__load_thres = 2.0/3.0
        self.__extend_ratio = 2
        self.__buckets: list[Pair| None] = [None] * self.capacity
        self.TOMBSTONE = Pair(-1, "-1")
    def __hash_func(self, key: int) -> int:
        return key % self.__capacity
    def __load_factor(self) -> float:
        return self.__size / self.__capacity
    def __find_bucket(self, key:int) -> int:
        index = self.__hash_func(key)
        first_tombstone = -1
        while self.__buckets[index] is not None:
            if key == self.__buckets[index].key:
                if first_tombstone != -1:
                    self.__buckets[first_tombstone] = self.__buckets[index]
                    self.__buckets[index] = self.TOMBSTONE
                    return first_tombstone
                return index
            if first_tombstone == -1 and self.__buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            index = (index +1) % self.__capacity
        return index if first_tombstone == -1 else first_tombstone
    def extend(self):
        self.__capacity *= self.__extend_ratio
        new_buckets = [None] * self.__capacity
        for bucket in self.__buckets:
            if bucket not in [self.TOMBSTONE, None]:
                self.put(bucket.key, bucket.value)
        self.__buckets = new_buckets