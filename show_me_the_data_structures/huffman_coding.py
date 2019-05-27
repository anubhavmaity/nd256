import sys

class Node:
    def __init__(self, char, frequency, bit = 0):
        self.char = char
        self.frequency = frequency
        self.right = None
        self.left = None
        self.bit = bit

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, char, frequency):
        if not self.root:
            self.root = Node(char, frequency)
        else:
            self.current = self.root
            while True:
                if self.current.left:
                    self.current = self.current.left
                else:
                    break

                if self.current.right:
                    self.current = self.current.right
                else:
                    break
            if not self.current.left:
                self.current.left = Node(char, frequency, 0)
            elif not self.current.right:
                self.current.right = Node(char, frequency, 1)






def get_frequencies(data):
    char_frequency = {}
    for ch in data:
        if ch in char_frequency:
            char_frequency[ch] += 1
        else:
            char_frequency[ch] = 1
    return char_frequency

def build_tuple_list(char_frequency):
    char_frequency_list = []
    for ch in char_frequency:
        char_frequency_list.append((char_frequency[ch], ch))
    return sorted(char_frequency_list)

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
