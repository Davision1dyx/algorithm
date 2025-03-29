class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class ArrayHashMap:
    def __init__(self):
        self.__bucket: list[Pair| None] = [None] * 100
    def __hash_key(self, key: int):
        return key % len(self.__bucket)
    def get(self, key: int) -> str:
        index: int = self.__hash_key(key)
        return self.__bucket[index].value
    def put(self, key: int, value: str):
        pair: Pair = Pair(key, value)
        self.__bucket[self.__hash_key(key)] = pair
    def remove(self, key: int):
        index: int = self.__hash_key(key)
        self.__bucket[index] = None
    def entry_set(self) -> list[Pair]:
        result: list[Pair] = []
        for pair in self.__bucket:
            if pair is not None:
                result.append(pair)
        return result
    def key_set(self) -> list[int]:
        result: list[int] = []
        for pair in self.__bucket:
            if pair is not None:
                result.append(pair.key)
        return result
    def value_set(self) -> list[str]:
        result: list[str] = []
        for pair in self.__bucket:
            if pair is not None:
                result.append(pair.value)
        return result
    def print(self):
        """打印哈希表"""
        for pair in self.__bucket:
            if pair is not None:
                print(pair.key, "->", pair.value)