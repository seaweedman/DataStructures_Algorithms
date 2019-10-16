class Array:
    # 构造函数，传入数组的容量capacity构造Array
    def __init__(self, capacity=10):
        self.__data = []
        self.__capacity = capacity
        self.__size = 0

    # 获取数组的容量
    def getCapacity(self):
        return len(self.__data)

    # 获得数组中的元素个数
    def getSize(self):
        return self.__size

    # 返回数组是否为空
    def isEmpty(self):
        return self.__size == 0

    # 获取指定位置的元素
    def get(self, index):
        if index < 0 or index > self.__size:
            return False
        return self.__data[index]

    # 更新指定位置的元素
    def set(self, index, e):
        if index < 0 or index > self.__size:
            return False
        self.__data[index] = e

    # 删除指定位置元素
    def remove(self, index):
        if index < 0 or index > self.__size:
            return False

        ret = self.__data[index]
        i = index + 1
        while i < self.__size:
            self.__data[i-1] = self.__data[i]
            i += 1

        self.__size -= 1

        return ret

    # 删除数组中第一个元素
    def removeFirst(self):
        return self.remove(0)

    # 删除数组中最后一个元素
    def removeLast(self):
        return self.remove(self.__size - 1)

    # 删除数组中指定元素
    def removeElement(self, e):
        index = self.find(e)
        return self.remove(index)

    # 查找数组中是否有指定元素
    def contains(self, e):
        for i in self.__data:
            if i == e:
                return True
        return False

    # 查找数组指定元素所在位置
    def find(self, e):
        for k, v in enumerate(self.__data):
            if v == e:
                return k
        return -1

    # 向所有元素前添加一个新元素
    def addFirst(self, e):
        self.add(0, e)

    # 向所有元素后添加一个新元素
    def addLast(self, e):
        self.add(self.__size, e)

    # 向任意位置插入一个新元素
    def add(self, index, e):
        if self.__size >= self.__capacity:
            return False

        if index < 0 or index > self.__size:
            return False

        i = self.__size - 1
        while i >= index:
            self.__data.insert(i + 1, self.__data[i])
            i -= i
        self.__data.insert(index, e)

        self.__size += 1

    # 输出数组信息
    def __str__(self):
        arrs = '['
        # for i, k in enumerate(self.__data):
        #     arrs += str(k)
        #     if i != self.__size - 1:
        #         arrs += ','
        for i in range(self.__size):
            arrs += str(self.__data[i])
            if i != self.__size - 1:
                arrs += ','
        arrs += ']'

        return arrs

test = Array(5)
test.addLast(10)
test.addLast(11)
test.addLast(12)
test.addLast(13)
test.set(0, 20)
test.remove(2)
print(test.find(11))
print(test)