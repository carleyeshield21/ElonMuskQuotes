import requests
from bs4 import BeautifulSoup
import textwrap
from tkinter import *
import os
import random

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
# elon_img = PhotoImage(file=f'elon_musk_img/{new_img}')
elon_img = PhotoImage(file='elon_musk_img/Elon-Musk-PNG-Isolated-File.png')
elon_canvas.create_image(500,550,image=elon_img)

new_img1 = PhotoImage(new_img)



# ======================= Functions ===========================
def change_img():
    # pass
    color = ['red','blue','yellow']
    rand_photo = random.choice(os.listdir('elon_musk_img'))
    print(rand_photo)
    elon_window.config(background=random.choice(color))
    new_quote = random.choice(list_quotes)
    # elon_canvas.itemconfig(elon_quote,text=new_quote)
    label.config(text=new_quote)



# button
elon_btn_img = PhotoImage(file='get-quote-button.png')
elon_btn = Button(padx=200,pady=200, image=elon_btn_img,command=change_img)
elon_btn.grid(row=1,column=0,columnspan=2)


# ======================= main ==================================
elon_musk_quotes1 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes').text
elon_musk_quotes2 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_2').text
elon_musk_quotes3 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_3').text
elon_musk_quotes4 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_4').text
# elon_musk_quotes1.raise_for_status()

soup1 = BeautifulSoup(elon_musk_quotes1, 'lxml')
soup2 = BeautifulSoup(elon_musk_quotes2, 'lxml')
soup3 = BeautifulSoup(elon_musk_quotes3, 'lxml')
soup4 = BeautifulSoup(elon_musk_quotes4, 'lxml')
# print(soup1.prettify())

list_quotes = []

quotes1 = soup1.find_all('a',class_='b-qt')
for quote in quotes1:
    q1 = quote.find('div').text.strip()
    # print(q1)
    list_quotes.append(q1)

quotes2 = soup2.find_all('a',class_='b-qt')
for quote in quotes2:
    q2 = quote.find('div').text.strip()
    # print(q2)
    list_quotes.append(q2)

quotes3 = soup3.find_all('a',class_='b-qt')
for quote in quotes3:
    q3 = quote.find('div').text.strip()
    # print(q3)
    list_quotes.append(q3)

quotes4 = soup4.find_all('a',class_='b-qt')
for quote in quotes4:
    q4 = quote.find('div').text.strip()
    # print(q4)
    list_quotes.append(q4)

random_quote = random.choice(list_quotes)
# print(random_quote)
# ======================= main ==================================
# elon_quote = elon_canvas.create_text(200,200,text=random_quote,font=('Times New Roman',20,'italic'),justify='right')

# text = Text(elon_window,wrap=WORD)
# text.insert(INSERT,elon_quote)
# text.grid(row=0,column=0)
#
label = Label(text=random.choice(list_quotes),justify='left',font=('helvetica 14',18,'italic'),wraplength=500,background='white',anchor=N)
label.grid(row=0,column=0,columnspan=2)



elon_window.mainloop()