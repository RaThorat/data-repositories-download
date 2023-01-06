# data-repositories-download
Importing repositories from Re3data

This code is used to import repository information from the website Re3data. It begins by sending a request to the Re3data API and saving the response as an xml file. The code then imports the ElementTree module and uses it to parse the xml file, getting the root tag and printing it out along with its memory location. The code also prints out the attributes of the first tag from the parent and the text contained within the first subtag of the 5th tag.

The code then creates an empty list and iterates over each 'name' tag in the xml file, appending the text contained within each tag to the list. Finally, the code iterates over each 'name' tag again and prints out the text contained within each tag. The names of the repositories can then be copied and pasted into an Excel file, which should be named 'Repositories.xlsx'.
