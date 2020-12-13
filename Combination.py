#python 3
#While running the code please remember to take the inputs in 2 seperate lines (n in one line and r in another)
def Combination(n, r):
    """
    function to calculate ncr recursively 
    """
    if r > n: #if no of elements to be selected is greater than the number available ncr = 0
        return 0
    elif r == 0 or n == r: #if no of elements to be selected is equal to 0 or is equal to the number available ncr = 1
        return 1
    else:
        return Combination(n-1, r-1) + Combination(n-1, r) #recursive call based on the formula ncr = (n-1)c(r-1) + (n-1)c(r)

n = int(input()) #taking a number n as input in a single line
r = int(input()) #taking a number r as input in a single line
print(Combination(n, r))
