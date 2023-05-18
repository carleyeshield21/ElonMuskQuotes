import requests
from bs4 import BeautifulSoup
import random
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
elon_canvas.create_image(400,250,image=elon_comic_strip_bubble)
# elon_canvas.grid(row=0,column=0,columnspan=2,rowspan=2)
elon_canvas.grid(row=0,column=0,columnspan=2)


def change_img():
    # pass
    rand_photo = random.choice(os.listdir('elon_musk_img'))
    print(rand_photo)

# image
new_img = random.choice(os.listdir('elon_musk_img'))
elon_img = PhotoImage(file=f'elon_musk_img/{new_img}')
elon_canvas.create_image(500,500,image=elon_img)

# button
elon_btn_img = PhotoImage(file='get-quote-button.png')
elon_btn = Button(padx=200,pady=200, image=elon_btn_img)
elon_btn.grid(row=1,column=0,columnspan=2)


# # ======================= main ==================================
# elon_musk_quotes1 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes').text
# elon_musk_quotes2 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_2').text
# elon_musk_quotes3 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_3').text
# elon_musk_quotes4 = requests.get('https://www.brainyquote.com/authors/elon-musk-quotes_4').text
# # elon_musk_quotes1.raise_for_status()
#
# soup1 = BeautifulSoup(elon_musk_quotes1, 'lxml')
# soup2 = BeautifulSoup(elon_musk_quotes2, 'lxml')
# soup3 = BeautifulSoup(elon_musk_quotes3, 'lxml')
# soup4 = BeautifulSoup(elon_musk_quotes4, 'lxml')
# # print(soup1.prettify())
#
# list_quotes = []
#
# quotes1 = soup1.find_all('a',class_='b-qt')
# for quote in quotes1:
#     q1 = quote.find('div').text.strip()
#     # print(q1)
#     list_quotes.append(q1)
#
# quotes2 = soup2.find_all('a',class_='b-qt')
# for quote in quotes2:
#     q2 = quote.find('div').text.strip()
#     # print(q2)
#     list_quotes.append(q2)
#
# quotes3 = soup3.find_all('a',class_='b-qt')
# for quote in quotes3:
#     q3 = quote.find('div').text.strip()
#     # print(q3)
#     list_quotes.append(q3)
#
# quotes4 = soup4.find_all('a',class_='b-qt')
# for quote in quotes4:
#     q4 = quote.find('div').text.strip()
#     # print(q4)
#     list_quotes.append(q4)
#
# random_quote = random.choice(list_quotes)
# print(random_quote)
# # ======================= main ==================================

elon_window.mainloop()