# File

fname = input("Enter file name: ")
fh = open(fname)
count =0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        num += float(line[line.find(' '):]) 
        count += 1
print('Average spam confidence:', num/count)