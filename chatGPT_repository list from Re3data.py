import requests
import xml.etree.ElementTree as ET
import pandas as pd

response = requests.get("https://www.re3data.org/api/v1/repositories")
print(response.status_code)
# 200 Returned when the list could be successfully generated.

# saving the xml file 
with open('re3data.xml', 'wb') as f: 
    f.write(response.content) 

# importing element tree 
# under the alias of ET 
tree = ET.parse('re3data.xml') 
  
# getting the parent tag of 
# the xml document 
root = tree.getroot() 
  
# Create an empty list 
Repo_list =[] 
  
# Iterate over each row 
for name in root.iter('name'):
    my_list=name.text      
    # append the list to the final list 
    Repo_list.append(my_list) 
  
#Print the list 
print(Repo_list) 

# Create a dataframe from the list
df = pd.DataFrame(Repo_list)

# Write the dataframe to excel
df.to_excel('Repositories.xlsx', index=False, header=False)
