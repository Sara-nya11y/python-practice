
# Program: Armstrong Number Checker
# Concept: While loop, Modulus, Exponents
# Author: Sara-nya11y
# Logic: 153 = 1^3 + 5^3 + 3^3 = 153

n = int(input("Number ivvu: ")) 
temp = n 
sum = 0  
while temp > 0: 
    digit = temp % 10    
    sum += digit ** 3  
    temp //= 10          


print("Armstrong" if sum == n else "Not Armstrong")




