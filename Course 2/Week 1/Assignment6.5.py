text = "X-DSPAM-Confidence:    0.8475";
numbers = text.find('0')
slice = text.find ('', numbers)
number = text[numbers:]
x = float(number)
print(x)
