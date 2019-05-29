### Time Complexity

Adding a block will take O(1) time as we are prepending an element to the head of the linked list.
Removing a block will take O(n) time in worst case as we have to traverse the linkedlist to remove that block.

### Space Complexity

I am using hashmap and linked list. Using hashmap to store the pair sshkey and the node.
The node's ssh address are stored as key in the hashmap.

### Code Design

Pair of address and node are stored in hashmap. The key value pair simulates the connectivity of the node.