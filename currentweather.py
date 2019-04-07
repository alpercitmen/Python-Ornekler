#A Python GUI To Get The Current Weather Update Of Any City
#Get Your Free API Key From https://openweathermap.org/
#Create an account https://openweathermap.org/

import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def CreateWidgets():
    cityLabel = Label(root, text="Enter City Name: ", bg="skyblue")
    cityLabel.grid(row = 0, column = 0, padx = 10, pady = 5)
    cityEntry = Entry(root, width=36, textvariable = cityName)
    cityEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

    findButton = Button(root, text = "Find Weather", command = findWeather)
    findButton.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)

    cityCoord = Label(root, text = "City Coordinates: ", bg="skyblue")
    cityCoord.grid(row = 2, column = 0, padx = 10, pady = 5)
    root.cityCoord = Entry(root, width=36)
    root.cityCoord.grid(row = 2, column = 1, padx = 10, pady = 5)

    tempCoord = Label(root, text = "Temprature: ", bg="skyblue")
    tempCoord.grid(row = 3, column = 0, padx = 10, pady = 5)
    root.tempEntry = Entry(root, width=36)
    root.tempEntry.grid(row = 3, column = 1, padx = 10, pady = 5)

    humidityLabel = Label(root, text = "Humidity: ", bg="skyblue")
    humidityLabel.grid(row = 4, column = 0, padx = 10, pady = 5)
    root.humidityEntry = Entry(root, width=36)
    root.humidityEntry.grid(row = 4, column = 1, padx = 10, pady = 5)

    windLabel = Label(root, text = "Wind: ", bg="skyblue")
    windLabel.grid(row = 5, column = 0, padx = 10, pady = 5)
    root.windEntry = Entry(root, width=36)
    root.windEntry.grid(row = 5, column = 1, padx = 10, pady = 5)

    pressureLabel = Label(root, text = "Pressure: ", bg="skyblue")
    pressureLabel.grid(row = 6, column = 0, padx = 10, pady = 5)
    root.pressureEntry = Entry(root, width=36)
    root.pressureEntry.grid(row = 6, column = 1, padx = 10, pady = 5)

    descLabel = Label(root, text = "Weather Description: ", bg="skyblue")
    descLabel.grid(row = 7, column = 0, padx = 10, pady = 5)
    root.descEntry = Entry(root, width=36)
    root.descEntry.grid(row = 7, column = 1, padx = 10, pady = 5)

def findWeather():
    APIKey = "8d8435fdebe5fb58e4cb6efaad5c5189"

    weatherUrl = "http://api.openweathermap.org/data/2.5/weather?"

    cityname = cityName.get()

    requestUrl = weatherUrl + "appid=" + APIKey + "&q=" + cityname + "&units=metric"

    response = requests.get(requestUrl)

    weatherResponse = response.json()

    if weatherResponse["cod"] != "404":
        weatherPARA = weatherResponse["main"]

        coordinates = weatherResponse["coord"]
        latitude = coordinates["lat"]
        longitude = coordinates["lon"]

        wind = weatherResponse["wind"]
        windSpeed = wind["speed"]
        windDirect = wind["deg"]

        temprature = weatherPARA["temp"]

        pressure = weatherPARA["pressure"]

        humidity = weatherPARA["humidity"]

        weatherDesc = weatherResponse["weather"]

        weatherDescription = weatherDesc[0]["description"]

        #printing the results

        root.cityCoord.insert('0', "Latitude: " +str(latitude) + "Longitude: " + str(longitude))
        root.tempEntry.insert('0', str(temprature) + "°C")
        root.humidityEntry.insert('0', str(humidity) + "%")
        root.windEntry.insert('0', "Speed: " + str(windSpeed) + " meter/sec " + "Direction: " + str(windDirect) + "°")
        root.pressureEntry.insert('0', str(pressure) + "hPa")
        root.descEntry.insert('0', str(weatherDescription))

        # if code is 404 then city is not found
    else:
        messagebox.showerror("ERROR", "City is not found!")


#creating object of tkinter class
root = tk.Tk()

#setting the title and bg color
#disabling the resize property
root.title("CurWeatherPy")
root.resizable(False, False)
root.config(background = "skyblue")

cityName = StringVar()

CreateWidgets()
root.mainloop()
