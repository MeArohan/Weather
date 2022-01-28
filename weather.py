import tkinter as tk 
import requests 
import time 

def getWeather(display): 
    city = textfield.get() 
    
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=f2d2d1da76696f63a6fbf47c176880f2" 
    json_data = requests.get(api).json() 
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15) 
    min_temp = int(json_data['main']['temp_min'] - 273.15)  
    max_temp = int(json_data['main']['temp_max'] - 273.15) 
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity'] 
    wind = json_data['wind']['speed']   

    final_info = condition + "\n" +str(temp) + "C" 
    final_data = "\n" + "Max Temperature: " + str(max_temp) + "\n" + "Minimum Temperature: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) 
    text1.config(text = final_info) 
    text2.config(text = final_data) 



display = tk.Tk() 
display.geometry("700x700")
display.title("Weather")

f = ("Helvetica", 16, "bold italic") 
t = ("Helvetica", 36, "bold")

textfield = tk.Entry(display, font = t)  
textfield.pack(pady = 20) 
textfield.focus()  
textfield.bind('<Return>', getWeather) 

text1 = tk.Label(display, font = t)
text1.pack() 
text2 = tk.Label(display, font = f)  
text1.pack() 

display.mainloop()  



