#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file:")

fh = open(fname)

lst = list()

for line in fh:
    line = line.rstrip()
    if line == "": continue
        
    words = line.split()
    if words[0] !="From": continue
    lst.append(words[1])
    

counts= dict()

for new in lst:
    counts[new] = counts.get(new,0) + 1

bigcount = None
bigword = None
for new,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = new

print (bigword,bigcount)
