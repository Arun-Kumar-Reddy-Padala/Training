
from tkinter import *
from pytube import YouTube
import requests


url = "https://www.google.com"
timeout = 10
try:
	request = requests.get(url, timeout=timeout)

	Window = Tk()
	Window.geometry('500x300')
	Window.title("YOUTUBE DOWNLOADER")
	Label(Window,text = 'Youtube Video Downloader').pack()
	link = StringVar()

	Label(Window, text = 'Paste Link Here:').place(x= 180 , y = 60)
	link_enter = Entry(Window, width = 70,textvariable = link).place(x = 32, y = 90)
	def Downloader():     
	    url =YouTube(str(link.get()))
	    url.streams.get_highest_resolution().download()
	    Label(Window, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

	Button(Window,text = 'DOWNLOAD', command = Downloader).place(x=180 ,y = 150)

	Window.mainloop()

except (requests.ConnectionError, requests.Timeout) as exception:
	print("Please Connect to internet")
