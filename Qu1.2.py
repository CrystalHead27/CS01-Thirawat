total = 0
count = 0

while count < 10:
    number = float(input("Input Number: "))
    
    if number < 0:
        print("Don't Count")
        continue
    
    total += number
    count += 1

print("Sum of Non-Negative Numbers:", total)