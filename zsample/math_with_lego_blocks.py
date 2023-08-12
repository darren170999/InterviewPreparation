a=sum(A)+A.count(0)
b=sum(b)+B.count(0)

return -1 if a!=b and [A,B][a>b].count(0)==0 else max(a,b)

a = sum(A) + A.count(0)

# Calculate the sum of elements in list B and count the occurrences of 0
b = sum(B) + B.count(0)

# Check if the sums are different and 0 is not present in the appropriate list
if a != b and 0 not in (A if a > b else B):
    return -1  # If the condition is true, return -1

# If the condition is false, return the maximum of a and b
return max(a, b)