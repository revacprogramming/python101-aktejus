#Functions

def computepay(h, r):
    p = computepay(h,r)
    return 0

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the rate of hours:")
r = float(rate)

if h<=40:
    p=h*r
    print("Pay",p)
    
elif h>40:
    p=(40*r)+((h-40)*1.5*r)
    print("Pay",p)
