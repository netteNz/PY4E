smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


# %#

largest = 0
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = max(num)
    except:
        print('Invalid input')
    print()
    largest = largest + 1

print("Maximum is ", largest)
print("Minimum is ", smallest)

# %#

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)

print("Maximum", largest)
