import tkinter as tk 
import requests 
import time 

def getWeather(): 
    city = textfield.get() 
    api = "https://api.openweathermap.org/data/2.5/weather?q=austin&appid=f2d2d1da76696f63a6fbf47c176880f2"

display = tk.Tk() 
display.geometry("700x700")
display.title("Weather")

f = ("Helvetica", 16, "bold italic") 
t = ("Helvetica", 36, "bold")

textfield = tk.Entry(display, font = t)  
textfield.pack(pady = 20) 
textfield.focus() 

text1 = tk.Label(display, font = t)
text1.pack() 
text2 = tk.Label(display, font = f)  
text1.pack() 

display.mainloop() 



