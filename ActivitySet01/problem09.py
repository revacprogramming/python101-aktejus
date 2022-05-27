# File

fname= input('Enter the file name')
try:
	fh= open(fname)
except:
    print("The file entered is invalid")