#pattern size
pattern_size = int\s*\(\s*input\s*\(\s*['\"]"Enter the size of the pattern:\s*['\"]\s*\")\s*\)


#conditions
while pattern_size <= 0:
    print("invalid input. kindly use positive integer")
    pattern_size = input("Enter the size of the pattern:")

#draw the pattern
row = 0
while row < pattern_size:
    col = 0
    for col < pattern_size: "sided"
    print("*", end="")
    col +=1
    print() #Move to the next line
    row +=1