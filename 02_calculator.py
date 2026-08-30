#2
num1 = float(input("Modati number ivvu: "))

# Rendo number teeskuntunnam  
num2 = float(input("Rendo number ivvu: "))

# Operation select cheskovadam
print("Operation select chey: +, -, *, /")
operator = input("Operator ivvu: ")

# If-else tho calculation chestunnam
if operator == '+':
    result = num1 + num2
    print("Result:", result)
elif operator == '-':
    result = num1 - num2
    print("Result:", result)
elif operator == '*':
    result = num1 * num2
    print("Result:", result)
elif operator == '/':
    # Zero tho divide cheyakunda check
    if num2 == 0:
        print("Error: Zero tho divide cheyodhu!")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operator! +, -, *, / lo okati ivvu")






