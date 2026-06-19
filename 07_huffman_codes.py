import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(characters, frequencies):
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
    codes = {}
    def generate(node, code):
        if node.char is not None:
            codes[node.char] = code
            return
        generate(node.left, code + "0")
        generate(node.right, code + "1")
    generate(heap[0], "")
    return sorted(codes.items())

print(huffman_codes(['a','b','c','d'], [5,9,12,13]))
print(huffman_codes(['f','e','d','c','b','a'], [5,9,12,13,16,45]))
