from com.dyx.Algorithm.hash_map.array_hash_map import Pair
class HashMapChaining:
    def __init__(self):
        self.__capacity: int = 4 #哈希表容量
        self.__size: int = 0 #键值对数量
        self.__load_thres = 2.0/3.0
        self.__extend_ratio = 2
        self.__buckets: list[list[Pair]] = [[] for _ in range(self.__capacity)]
    def __hash_func(self, key: int) -> int:
        return key % self.__capacity
    def __load_factor(self) -> float:
        return self.__size / self.__capacity
    def get(self, key: int) -> str| None:
        index: int = self.__hash_func(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            for pair in bucket:
                if pair.key == key:
                    return pair.value
        return None
    def put(self, key: int, value: str):
        # 当负载因子超过阈值时，执行扩容操作
        if self.__load_factor() > self.__load_thres:
            self.__extend()
        index: int = self.__hash_func(key)
        bucket = self.__buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.value = value
                return
        bucket.append(Pair(key, value))
        self.__size += 1
    def remove(self, key: int):
        index: int = self.__hash_func(key)
        bucket = self.__buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.__size -= 1
                return
    def __extend(self):
        self.__capacity *= self.__extend_ratio
        new_buckets = [[] for _ in range(self.__capacity)]
        self.__size = 0
        for bucket in self.__buckets:
            for pair in bucket:
                self.put(pair.key, pair.value)
    def print(self):
        res = []
        for bucket in self.__buckets:
            for pair in bucket:
                res.append(str(pair.key) + "->" + pair.value)
        print(res)