import requests
from bs4 import BeautifulSoup
from tkinter import *
import os
import random

# ======================= HTML files ===========================
list_quotes = []

# page1
with open('quotes1.html') as html1:
    html_one = html1.read()
html1_soup = BeautifulSoup(html_one)

for h1 in html1_soup.find_all('a',class_='b-qt'):
    list_quotes.append(h1.text.strip())

# page2
with open('quotes2.html') as html2:
    html_two = html2.read()
html2_soup = BeautifulSoup(html_two)

for h2 in html2_soup.find_all('a',class_='b-qt'):
    list_quotes.append(h2.text.strip())

# page3
with open('quotes3.html') as html3:
    html_three = html3.read()
html3_soup = BeautifulSoup(html_three)

for h3 in html3_soup.find_all('a',class_='b-qt'):
    list_quotes.append(h3.text.strip())

# ======================= User interface ===========================
elon_window = Tk()
elon_window.title('Elon Quotes')
elon_window.config(padx=50,pady=50)

# comic strip bubble
elon_canvas = Canvas(width=800,height=600)
elon_comic_strip_bubble = PhotoImage(file='comic_strip_bubble.png')
elon_canvas.create_image(400,350,image=elon_comic_strip_bubble)
elon_canvas.grid(row=0,column=0,columnspan=2)

# image
new_img = random.choice(os.listdir('elon_musk_img'))
elon_img = PhotoImage(file='elon_musk_img/Elon-Musk-PNG-Isolated-File.png')
elon_canvas.create_image(500,550,image=elon_img)
rand_photo = random.choice(os.listdir('elon_musk_img'))

# ======================= Functions ===========================
def change_img():
    color = ['red','blue','yellow','#b6a066','#a47afe','#205a13','#760bbb','#f0881f','cyan','dark cyan']
    elon_window.config(background=random.choice(color))
    new_quote = random.choice(list_quotes)
    elon_canvas.itemconfig(elon_quote,text=new_quote)

# button
elon_btn_img = PhotoImage(file='get-quote-button.png')
elon_btn = Button(padx=200,pady=200, image=elon_btn_img,command=change_img)
elon_btn.grid(row=1,column=0,columnspan=2)

random_quote = random.choice(list_quotes)
# ======================= main ==================================
elon_quote = elon_canvas.create_text(400,300,text=random_quote,font=('helvetica 14',20,'italic'),justify='right',width=500)

elon_window.mainloop()