#user number prompt
number = float(input("Enter a number to see its multiplication table:"))

#generate and print multiplication table
print(f"multiplication table for {number}:")
for float in range (1,10):
    product = number * float

#print result
    print(f"{number} * {float} = {product}")