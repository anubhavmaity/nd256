### Time Complexity

The program is implemented to simulate a LRU Cache. The get and set operation takes O(1) time.

### Space Complexity

The program occupies O(n) space. Both the doubly linked list and hashmap takes O(n) space each.

### Code Design
I have used two datastructures - maps and doubly linked list.
There are two markers - head and tail - on the doubly linked list.
At the head I keep the most recent element accessed or inserted. And at the tail I keep the oldest element.
The linked list helps in maintaining the elements in time order.
I have used Doubly Linked List, because removing a node takes O(1) time. A node in this type of linked list has two pointers i.e. next and previous.
We can traverse forward and backward from any node in the linked list and can change the references in O(1) time.
If we would have used Singly Linked List, removing a node would have taken O(n) time as we have to traverse to that node.

The hash maps keeps the key and node pair. The hashmaps enable to retreive, replace and insert a node in O(1) time.

Using these two datastructures helps us in getting a LRU cache with O(1) time operations.

I have used assert statements in the test cases function as I find that to be better practice.