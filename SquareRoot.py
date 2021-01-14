#Ezekial page
#numerical differentiation program
import math

#Square root
trueValue = math.sqrt(2)
print("Calculated the square root of 2 using two different \nfunctions and compute the error")
print("Python square root function = " + str(trueValue))

def SquareRoot(n):
    changeVal = 0.001
    ans = n
    beg = 1
    end = n
    while (beg <= end) :

        mid = beg + (end-beg)/2
        if ( mid*mid == n ) : 
            return mid 
        elif ( mid * mid > n) :
            end = mid - changeVal 
        else :
            ans = mid 
            beg = mid + changeVal 
    
    return ans


num = 2
answer = SquareRoot(2)
print("Binary search function = " + str(answer))

error = trueValue - answer
print("Approximate Error: " + str(error))
