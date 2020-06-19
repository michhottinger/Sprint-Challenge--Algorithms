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

    
  
'''
def target_floor(n, breaks):
# If there are no floors, then no trials 
    # needed. OR if there is one floor, one 
    # trial needed. 
    
    if (breaks == 1 or breaks == 0): 
        return breaks 
        
    min = 0
    max = n
#while the min is less then the max, converge on a value here
    while min < max:  
        mid = (max-min) // 2
        if breaks(mid) == True:
            max = mid - 1
        else:
            min = mid + 1
    return min + 1
