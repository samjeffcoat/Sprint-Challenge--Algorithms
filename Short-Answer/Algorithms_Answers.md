#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear Time- O(n). As n increases, our run time will increase. As n decreases, our run time decreases. For example if n is 1 then the run time will be much smaller than if n is 10. 


b)O(n^3). There are 3 operations being performed in this equation. We are establishing j in the first loop, multiplying j by 2, then we are also incrementing sum within the last loop. This is a inefficient program. 


c) O(n). This code will run exactly n amount of times. Our return relies on bunnies-1. Runtime will then be dependent on n. 

## Exercise II

Ok we have a building that is n stories tall. We have an unlimited number of eggs, so eggs will never run out.  Egg is broken if it is thrown off story f or higher. If it is less than story f it does not get broken. So we want to find the value of f so that the number of eggs dropped and broken is minimized. 

We will need to find a midpoint so we can compare the number of eggs dropped+broken.
If we have 0 floors to evaluate then our function will need to exit out. 
We will need to evaluate f against a midpoint. If our midpoint is greater than f, then we will need to go down a level of floors. If our midpoint is smaller than f, we go up a level and continue our evaluation.

Run time= O(log n). When evaluating out floors, it is unlikely that we will get to the midpoint of floors first. We will most likely have to do multiple comparisons.

def floor_search(floors, f):

//establishes midpoint or a halfway point
midpoint = floor // 2

//base case
if len(floors) <>=0
    return 0 

if floors[midpoint] ===f:
        f=floors[midpoint]
        return f
    elif floors[midpoint] < f:
    return floor_search(floors[midpoint +1 ]:, f )

    else:
        return floor_search(floors[:midpoint], f )
n = stories
n > f ===0
n < f = 1
def 
