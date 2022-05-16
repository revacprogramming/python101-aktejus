# Loops and iteration

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num_i=int(num)
    except:
        print("Invalid input")
	continue

    if largest is None:
        largest=num_i
    elif num_i>largest:
        largest=num_i
    if smallest is None:
        smallest=num_i
    elif num_i<smallest:
        smallest=num_i

print("Maximum is", largest)
print("Minimum is", smallest)