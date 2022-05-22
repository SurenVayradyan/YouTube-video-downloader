from tkinter import *
from pytube import YouTube

# Создаем окно
root = Tk()
root.geometry('500x300') # Размер окна
root.resizable(0,0) # Фиксируем окно
root.title('YouTube video downloader') # Название окна
Label(root, text = 'YouTube Video Downloader', font='arial 20 bold').pack()

# Поле для ссылки
link = StringVar()
Label(root, text= 'Вставьте ссылку на видео:', font='arial 15 bold').place(x=120, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

# Функция для скачивания
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x=500, y=210)
Button(root, text = 'Скачать', font='arial 15 bold', bg='pale violet red', padx=2, command= Downloader).place(x=180, y=150)
root.mainloop()