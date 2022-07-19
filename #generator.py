from bs4 import BeautifulSoup
import requests
import os

def clear_console():
	os.system('clear')

print("#ashTag Generator for IG      by @itz_pa1\n")
print("Please enter your username and then topic of your post only in one word\n")
user = input("Enter Username : ")
print("Enter topic related to post e.g. technology :")
topic = input("")
url = "https://h.bdir.in/hashtags/search/" + str(topic)
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
hashtags = doc.find("div", {"class": "alert-info"})
tag = hashtags.b.string
post = f"*Caption*\n\nFollow @{user}\nFollow @{user}\nFollow @{user}\n.\n.\n.\nHashtags\n{tag}" 
clear_console()
print(post)