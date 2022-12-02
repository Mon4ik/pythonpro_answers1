typical_set = {"foo", "bar", ":O"}
frozen_set = frozenset(["foo", "hello world", "bob", "bar"])

print(typical_set.union(frozen_set))
print(typical_set.intersection(frozen_set))