import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(characters, frequencies):
    heap = []
    for char, freq in zip(characters, frequencies):
        heapq.heappush(heap, Node(char, freq))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def decode(root, encoded_string):
    result = []
    current = root
    for bit in encoded_string:
        current = current.left if bit == '0' else current.right
        if current.char is not None:
            result.append(current.char)
            current = root
    return ''.join(result)

root1 = build_huffman_tree(['a','b','c','d'], [5,9,12,13])
print(decode(root1, '1101100111110'))
root2 = build_huffman_tree(['f','e','d','c','b','a'], [5,9,12,13,16,45])
print(decode(root2, '110011011100101111001011'))
