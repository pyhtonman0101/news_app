from bs4 import BeautifulSoup as bs
import requests
import urllib.request
from tkinter import *
import webbrowser
from PIL import Image, ImageTk


global num
num=1
global heading,headlines,links,articles
def news(num):
    global artical_link,recievers,img,summary,headtext
    articles = body.find_all(class_='xrnccd F6Welf R7GTQ keNKEd j7vNaf')
    head=articles[num].find(class_='ipQwMb ekueJc gEATFF RD0gLb')
    headtext=head.text
    img_link = articles[num].find('img').get('src')
    print(img_link)
    urllib.request.urlretrieve(img_link,'thumbnail.jpg')
    span=articles[num].find('span')
    spantext=span.text
    link=articles[num].find('a')
    get=link.get('href')
    artical_link=('https://news.google.com' + str(get[1:len(get)]))
    print(artical_link)
    print('--------------------------x-------------------------x-------------------')

    recievers = Label(frame1, text=headtext, font=('arial', 14, 'bold'), fg='white', bg='gray18',padx=8,pady=8, wraplength=700)
    recievers.grid(row=1,sticky=W)
    load = Image.open("thumbnail.jpg")
    load=load.resize((250,250),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(frame2, image=render,relief=RAISED)
    img.grid(row=1,sticky=W)
    img.image = render
    summary = Label(frame2, text=spantext, font=('arial', 12), fg='white', bg='gray18', wraplength=500)
    summary.grid(row=1,column=2,columnspan=2,sticky=E)

def next():
    global num
    num=num+1
    recievers['text']=""
    summary['text'] = ""
    img.destroy()
    news(num)

def back():
    global num
    num=num-1
    recievers['text'] = ""
    summary['text'] = ""
    img.destroy()
    news(num)

def know_more():
    webbrowser.open(artical_link)

page=requests.get('https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en')
soup=bs(page.text,'html.parser')
body=soup.find(id='yDmH0d')


#GUI Programming
win = Tk()
win.config(bg='gray18')
win.title("News App")
label = Label(win,bg='gray18')
label.pack()

frame1 = Frame(label, relief=SUNKEN, bg="gray18", bd=1)
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(label, relief=SUNKEN, bg="gray18", bd=1)
frame2.pack()

nextbtn= Button(frame2,text='next',bd=5,fg='white',bg='gray14',font=('arial',15,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:next()).grid(row=2,column=3,sticky=E)
Know_more=Button(frame2,text='Know More',bd=5,fg='white',bg='green2',font=('arial',15,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:know_more()).grid(row=2,column=2,sticky=E)
back_btn=Button(frame2,text='Previous',bd=5,fg='white',bg='gray14',font=('arial',15,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:back()).grid(row=2,sticky=W)

news(1)
win.mainloop()
