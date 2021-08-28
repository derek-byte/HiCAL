from bs4 import BeautifulSoup

fd = open('topics.xml', 'r')
xml_file = fd.read()
soup = BeautifulSoup(xml_file, 'lxml')

topic = input(str("Which topic would you like to view? Type the topic number: "))
x = input(str("If retrieving id, enter 'i' \nIf retrieving link, enter 'l'"))

all_links = []

for tag in soup.findAll("sources" + topic):
    links = tag.text
    all_links.append(links.split(",")) 

if x == "l":
    for link in all_links:
        for id in link:
            print("http://boston.lti.cs.cmu.edu/Services/clueweb12_render/renderpage.cgi?id=" + id)
    print("No more links.")
else:
    id_string = ""
    for link in all_links:
        for id in range(len(link)):
            id_string += link[id] + ", "

    print(id_string[:-2])
    print("No more ids.")

fd.close()
