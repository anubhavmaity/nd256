### Time Complexity

The time taken for huffman coding is O(nlogn). Priority Queue is used where insertion for each element takes O(logn).
So for every elements take O(nlogn).
Iterating over the char codes --- O(n)
So the total time complexity is O(nlogn) for encoding and decoding

### Space Complexity

The space complexity will be O(n).
Storing the char codes -- O(n)
Elements in the min heap -- O(n)

### Code Design

I have used priority queue where the priority is given to the frequency of character. If the frequency of character is
higher then huffman code length of it will be less. Thus leading to better compression. The priority queue helps in
maintaining the priority order when inserting and removing the element.
