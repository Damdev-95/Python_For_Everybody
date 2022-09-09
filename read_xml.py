#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#Don't name the python file xml.py 


from urllib import request
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_24966.xml'
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count_no=len(results)
total=0

for result in results:
    total += float(result.find('count').text)
print(count_no)
print(total)
