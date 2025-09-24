class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # 返回迭代器对象自身
    def __iter__(self):
        return self

    # 返回下一个元素
    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            # 没有更多元素时抛出StopIteration
            raise StopIteration

# 使用迭代器
counter = Counter(1, 5)

# 方式1：使用for循环
print("使用for循环迭代：")
for num in counter:
    print(num)

# 方式2：使用next()函数
print("\n使用next()函数迭代：")
counter2 = Counter(10, 13)
iterator = iter(counter2)  # 获取迭代器，等价于调用__iter__()
try:
    while True:
        print(next(iterator))  # 等价于调用__next__()
except StopIteration:
    pass

