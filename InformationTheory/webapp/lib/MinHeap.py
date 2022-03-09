class Node:
    def __init__(self, data, char, left=None, right=None):
        self.data = data
        self.char = char
        self.bin = ""
        self.left = left
        self.right = right


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def __has_left_child(self, index):
        return self.__get_left_child_index(index) < self.size

    def __has_right_child(self, index):
        return self.__get_right_child_index(index) < self.size

    def __has_parent(self, index):
        return self.__get_parent_index(index) >= 0

    def __heapifyUp(self):
        index = self.size - 1
        while self.__has_parent(index) and self.heap[self.__get_parent_index(index)].data > self.heap[index].data:
            parent_index = self.__get_parent_index(index)
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp
            index = parent_index

    def __heapifyDown(self):
        index = 0
        while self.__has_left_child(index):
            smaller_child_index = self.__get_left_child_index(index)
            right_child_index = self.__get_right_child_index(index)
            left_child_index = self.__get_left_child_index(index)
            if self.__has_right_child(index) and self.heap[right_child_index].data < self.heap[left_child_index].data:
                smaller_child_index = right_child_index

            if self.heap[index].data < self.heap[smaller_child_index].data:
                break
            else:
                temp = self.heap[index]
                self.heap[index] = self.heap[smaller_child_index]
                self.heap[smaller_child_index] = temp
            index = smaller_child_index

    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        self.__heapifyUp()

    def peek(self):
        if self.size > 0:
            return self.heap[0]
        return None

    def pop(self):
        if self.size == 0:
            return None
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.size -= 1
        self.heap.pop()
        self.__heapifyDown()
        return item
