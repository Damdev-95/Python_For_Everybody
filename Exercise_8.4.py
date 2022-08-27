#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    line = line.split()
    
    for new in line:
        if new not in lst:
            lst.append(new)
        
        
lst.sort()

print(lst)
