import sys
import heapq


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.right = None
        self.left = None

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.frequency < other.frequency
        return NotImplemented


def build_frequency_tuple(data):
    char_frequency = {}
    for ch in data:
        if ch in char_frequency:
            char_frequency[ch] += 1
        else:
            char_frequency[ch] = 1

    pq = []
    for key in char_frequency:
        node = Node(key, char_frequency[key])
        heapq.heappush(pq, node)

    return pq


def encode(root, str, char_codes):
    if root is None:
        return

    if root.char is not None:
        char_codes[root.char] = str
        return

    encode(root.left, str + "0", char_codes)
    encode(root.right, str + "1", char_codes)


def decode(encoded_data, root, index):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return index, root.char

    index += 1

    if encoded_data[index] is '0':
        index, char = decode(encoded_data, root.left, index)
    else:
        index, char = decode(encoded_data, root.right, index)
    return index, char


def build_tree(data):
    pq = build_frequency_tuple(data)

    while len(pq) > 1:
        node1 = heapq.heappop(pq)
        node2 = heapq.heappop(pq)
        new_node = Node(None, node1.frequency + node2.frequency)
        new_node.left, new_node.right = node1, node2
        heapq.heappush(pq, new_node)

    char_codes = {}
    root = heapq.heappop(pq)
    encode(root, '', char_codes)
    byte_string = ''
    for char in data:
        byte_string += char_codes[char]
    return byte_string, root


def huffman_encoding(data):
    if len(data) == 1:
        return '0', Node('a', 1)
    elif len(data) > 1:
        return build_tree(data)
    return None, None


def huffman_decoding(data, tree):
    str = ''
    index = -1

    if data and len(data) == 1:
        return tree.char

    while(data and index < len(data) - 2):
        index, char = decode(data, tree, index)
        str += char
    return str


if __name__ == "__main__":
    codes = {}

    ## Test Case 1
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


    ## Test Case 2
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    if decoded_data:
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


    ## Test Case 3

    a_great_sentence = "a"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))


    ## Test Case 4

    a_great_sentence = "Huffman coding using priority queue to compress the data"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

