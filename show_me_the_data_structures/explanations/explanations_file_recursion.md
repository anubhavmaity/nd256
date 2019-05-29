### Time Complexity

The total time taken by the program is traversing  all the files and folders in a path.
If the total count of files and folders in a path is n, then the time taken will be O(n).

### Space Complexity
The space will be occupied by call stack and the returned list.
In recursion, the call stack is occupied by the function calls.
The total call stack space taken will be determined by no of folders within the folder.
So the space complexity will be O(n) where n is the no of files and folders.

### Code Design
Thinking recursive way is easy when you dont know about the depth of an item with an item and you know there is a pattern of substructure to follow.
The iterative solution would have needed more code than recursion.

I have used assert statements in the test cases function as I find that to be better practice.