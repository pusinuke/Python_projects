#Coursera capstone project
#week3
#2020 02 17
from bs4 import BeautifulSoup
import requests

source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text

soup = BeautifulSoup(source, 'lxml')

for table in soup.find_all('table'):
#    line = table.tr.th.text
    
    try:
        line = table.tr.text
    except Exception as e:
        line = None

    print(line)

    print()


# table = soup.find('table')

# line = table.tr.text
# print(line)

#print(table.prettify())

#print(soup.prettify())




# with open('List of postal codes of Canada_ M - Wikipedia.htm') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())


# # match = soup.title.text #randa tik pirma title
# # match = soup.div #tik pirma div su visais priklausiniais
# # match = soup.find('div') #randa ta pati ka anksciau
# # match = soup.find('div', class_='footer')
# #print(match)

# for  article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

#     print()