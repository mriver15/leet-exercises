class HashSet:
    def __init__(self) -> None:
        self.set = []
        pass
    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)
        pass
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)
        pass
    def contains(self, key: int) -> bool:
        return key in self.set


obj = HashSet()
obj.add(1)
obj.add(2)
obj.add(2)
obj.add(4)
obj.remove(1)
param_1 = obj.contains(1)

print(obj.set)