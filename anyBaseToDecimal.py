# You are given a number A. You are also given a base B. A is a number on base B.
# You are required to convert the number A into its corresponding value in decimal number system.
# Input
# A = 1010
# B = 2
# Output
# 10
def any_base_to_decimal(number,base):
    decimal=0
    i=0
    while number>0:
        l=number%10
        n=l*base**i
        decimal+=n
        number=number//10
        i+=1
    return decimal
number=int(input())
base=int(input())
print(any_base_to_decimal(number,base))
