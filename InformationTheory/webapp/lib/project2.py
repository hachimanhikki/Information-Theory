from webapp.lib.MinHeap import Node
from webapp.lib.MinHeap import MinHeap


def post_order(root, encoded_data, val=""):
    if root == None:
        return
    new_val = f"{val}{root.bin}"
    post_order(root.left, encoded_data, new_val)
    post_order(root.right, encoded_data, new_val)
    if root.left == None and root.right == None:
        encoded_data[root.char] = new_val


def huffman_encode(heap):
    while heap.size > 1:
        left = heap.pop()
        right = heap.pop()
        left.bin = 0
        right.bin = 1
        nn = Node(left.data + right.data, left.char + right.char, left, right)
        heap.insert(nn)


def get_heap(dict):
    heap = MinHeap()
    for key, value in dict.items():
        nn = Node(value, key)
        heap.insert(nn)
    return heap


def get_final_seq(encoded_data, text):
    print(encoded_data, text)
    final_seq = ""
    for ch in text:
        final_seq += encoded_data[ch]
    return final_seq


def get_result(dict, text):
    heap = get_heap(dict)
    huffman_encode(heap)
    root = heap.peek()
    encoded_data = {}
    post_order(root, encoded_data)
    final_seq = get_final_seq(encoded_data, text)
    return (encoded_data, final_seq, heap.peek())


def main():
    encoded_data, final_seq, root = get_result(dict)
    for key, value in encoded_data.items():
        print(repr(key), value)
    print(final_seq)


