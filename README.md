# data-repositories-download
Importing repositories from Re3data

This code is used to import repository information from the website Re3data. It first sends a request to the Re3data API and saves the response as an xml file. It then parses the xml file using the ElementTree module and prints out the root tag, attributes of the first tag, and text contained within the first subtag of the 5th tag. The code also creates an empty list and iterates over each 'name' tag in the xml file, appending the text contained within the tag to the list. Finally, the code iterates over each 'name' tag again and prints out the text contained within each tag.
