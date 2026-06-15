print("--- Age in Days Calculator ---")

try:
    age = int(input("Nee age years lo cheppu: "))
    days = age * 365
    print(f"Nuvvu putti roughly {days} days aindhi 😄")
    print(f"Exact ga cheppalante leap years kuda lekapovali")
except ValueError:
    print("Number ivvu chitti")

# this is important 
