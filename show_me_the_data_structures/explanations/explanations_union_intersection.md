### Time Complexity

The time taken for both union and traversing will be traversing both the linked list which will be O(n).
The time taken for adding an element and checking element in a set will be O(1) time.

### Space Complexity

The space will be occupied by the hashset and the new linked list.
The worst case for both union and intersection will be O(n)

### Code Design

For union of two linked list, the hashset is kept to avoid duplicate elements inserting in the new linked list.
For intersection of two linked list, the hashset is used to keep track of the common elements between the two linked lists.