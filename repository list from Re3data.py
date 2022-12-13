# This is an example of importing repository information from repository website Re3data

response = requests.get("https://www.re3data.org/api/v1/repositories")
print(response.status_code)# 200 Returned when the list could be successfully generated.


# saving the xml file 
with open('re3data.xml', 'wb') as f: 
    f.write(response.content) 
# url of rss feed 
url = 'https://www.re3data.org/api/v1/repositories'

# creating HTTP response object from given url 
resp = requests.get(url) 

# saving the xml file 
with open('re3data.xml', 'wb') as f: 
    f.write(resp.content) 


# importing element tree 
# under the alias of ET 
import xml.etree.ElementTree as ET 
  
# Passing the path of the 
# xml document to enable the 
# parsing process 
tree = ET.parse('re3data.xml') 
  
# getting the parent tag of 
# the xml document 
root = tree.getroot() 
  
# printing the root (parent) tag 
# of the xml document, along with 
# its memory location 
print(root) 
  
# printing the attributes of the 
# first tag from the parent  
print(root[1].attrib) 
  
# printing the text contained within 
# first subtag of the 5th tag from 
# the parent 
print(root[5][0].text) 


# Create an empty list 
Repo_list =[] 
  
# Iterate over each row 
for name in root.iter('name'):
    my_list=name.text      
    # append the list to the final list 
    Repo_list.append(my_list) 
  
#Print the list 
#print(Repo_list) 



for name in root.iter('name'):
    print(name.text)
#the names of the repository appear. Copy paste the repository to excel. Give name 'Repositories.xlsx'.
