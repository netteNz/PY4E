hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please enter a numeric input")
    quit()
# Conditioning
pay = h * r
if h <= 40:
    print(pay)
else:
    pay = r * 40 + (r * 1.5) * (h - 40)
    print(pay)
