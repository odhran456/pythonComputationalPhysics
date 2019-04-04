from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get('https://myanimelist.net/users.php')
soup = BeautifulSoup(response.text,'html.parser')
test = soup.find('td') #Ok so this looks random but the standard cell with all the users was the first cell
names = test.find_all('a',href=True) #Every person is contained within <a> tag with a href of their name
users = []
for name in names:
    users.append(name.get_text())
users = users[::2] #Every second entry into users was blank for some reason, so easy fix haha
print(users) #showing it works, nothing more
webstring = 'https://myanimelist.net/profile/'
urls = [webstring + user for user in users] #now this is a link to each persons page


def main(url): # Function that has all the instructions to be done
    response = requests.get(url) # Do the request with the url provided to the Function
    soup = BeautifulSoup(response.text,'html.parser')
    items = soup.find_all(class_='stats anime')
    p = []
    days = []
    score = []
    watching = []
    for person in users:
        p.append(person) #i remade the 'users' list because im a bad programmer
    for element in items:
        days = element.find(class_="di-tc al pl8 fs12 fw-b").contents[1]
        score = element.find(class_="di-tc ar pr8 fs12 fw-b").contents[1]
        watching = element.find(class_="di-ib fl-r lh10").get_text()
    print(person, days, score, watching) # Print the stuff after all is find/extracted
    csv_writer.writerow([days, score, watching]) # Write all of the stuff found to the csv

if __name__ == "__main__": # Used to call the function and do the setup
    with open('MALTake4.csv','w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['User','Days Watched','Average Score','Currently Watching']
        csv_writer.writerow(headers)
        for url in urls:
            main(url) # Sends a url and the csv instruction to write to the function
