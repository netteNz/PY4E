count = 0
sum_ = 0
print('Before', count, sum_)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum_ = sum_ + value
    print(count, sum_, value)
print('After', count, sum_, sum_ // count)
