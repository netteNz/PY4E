def computepay(h, r):
    if h <= 40:
        p = r * h
    else :
        p = r * 40 + (r * 1.5) * (h - 40)
    return p

try:
    hrs = input("Enter Hours: ")
    hours = float(hrs)
    rate_ = input("Enter Rate: ")
    rate = float(rate_)
except:
    print("Please enter a numeric value")
    quit()

pay = computepay(rate, hours)
print(pay)