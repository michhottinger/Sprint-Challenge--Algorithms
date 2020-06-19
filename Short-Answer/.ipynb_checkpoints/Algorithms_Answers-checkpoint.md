#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) This first code is a while loop, and will loop through n times with one operation occuring each time.


b)O(n^2) This is two loops, so this makes it n*n complexity! This with large data can be an issue since its in the "horrible" category of complexity.


c)O(n) returns two bunny ears each time it loops recursively around.

## Exercise II
pseudocode:

find value of f while minimizing the number of eggs used (both dropped and broken)
def finding_f:
    
 #using binary search here is a complexity of O(log(n))--excellent
 
<!-- class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None -->
<!-- def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            #go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            #got right if the right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target) -->
<!--     
 #if 
floors = [] 
     egg_broken = 1
     egg_clean = -1
     target = 0
    #using BSTNode:
    for floor in floors:
        if BSTNode contains(target)
            floors.append(target)
   
 '''
# Function to get minimum number of trials  
# needed in worst case with n eggs and k floors  
def eggDrop(n, k): 
  
    # If there are no floors, then no trials 
    # needed. OR if there is one floor, one 
    # trial needed. 
    if (k == 1 or k == 0): 
        return k 
  
    # We need k trials for one egg  
    # and k floors 
    if (n == 1): 
        return k 
  
    min = sys.maxsize 
  
    # Consider all droppings from 1st  
    # floor to kth floor and return  
    # the minimum of these values plus 1. 
    for x in range(1, k + 1): 
  
        res = max(eggDrop(n - 1, x - 1),  
                  eggDrop(n, k - x)) 
        if (res < min): 
            min = res 
  
    return min + 1
'''