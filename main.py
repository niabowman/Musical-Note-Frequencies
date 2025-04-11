import math

f0 = int(input("Input frequency: \n"))
r = pow(2, 1/12)
n = 0
count = 0

while count < 4:
    a=f0*r**n
    print(f'{a:.2f} Hz')
    n+=1
    count+=1