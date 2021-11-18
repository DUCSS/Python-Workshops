-1 = a * K + r, r>=0 r<K

-1 = -1*K + K - 1, where K-1 is the remainder, which has to be positive by definition

(i - rotation) = a * N + r 

If we think of array indices in the rotate array problem then we can see that if we 
assign b[(i-rotation)%N] = a[i], where b is the result array, a is the initial one and N is the length of it, 
we get precisely the rotation of the array "rotation" times to the left. 

a = [1, 2, 3, 4, 5] and d (rotation) = 3

////////////////////////
0 - 3 = -3,
-3 = -1*5 + 2
                         
///////////////////////
1 - 3 = -2,
-2 = -1*5 + 3
                         
///////////////////////
2 - 3 = -1,
-1 = -1*5 + 4
                         
//////////////////////
3 - 3 = 0,
0 = 0*5 + 0
                         
/////////////////////
4 - 3 = 1,
1 = 0*5 + 1

So 0 - > 2, 1 - > 3, 2->4, 3->0 and 4->1, which yields [4, 5, 1, 2 ,3]

Let's have a look at the rotations step by step

d = 0 [1, 2, 3, 4, 5]
  
d = 1 [2, 3, 4, 5, 1]
  
d = 2 [3, 4, 5, 1, 2]
  
d = 3 [4, 5, 1, 2, 3]

This way we can perform rotation in one step rather than doing it step by step.
