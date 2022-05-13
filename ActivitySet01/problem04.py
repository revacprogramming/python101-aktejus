hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the rate of hours:")
r = float(rate)

if h<=40:
    pay=h*r
    print(pay)
    
elif h>40:
    pay=(40*r)+((h-40)*1.5*r)
    print(pay)