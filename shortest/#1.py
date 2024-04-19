# [TYPE-SHORTEST]

# Goal
# Depending on type, Sum up all of the odd or even numbers from 1 to value

# Input
# Line 1 : A String type, either odd or even, for the type of number to sum
# Line 2 : A number value , for the maximum value to sum up

# Output
# Line 1: The sum of all the type integers less than or equal to value

# Constraints
# type = odd or even
# 1 ≤ value < 1000
# Example

# Input
# even
# 11

# Output
# 30


# solution [python]

t=input()
print(sum(i for i in range(1,int(input())+1)if(t=='odd'and i%2)or(t=='even'and i%2<1)))
