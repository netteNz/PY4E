largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        n = int(num)
        if largest < n:
            largest = n
        if smallest is None or smallest > n:
            smallest = n
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
