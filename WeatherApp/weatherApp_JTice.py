import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load initial DataFrame from CSV
weatherDataFrame = pd.read_csv('WeatherStationData.csv', keep_default_na=False, na_values=[], dtype=str)
optionsList = ["print", "add", "edit", "remove", "stats", "exit"]

print("Welcome to my Weather App")

loopProgram = True

class Weather:

    def __init__(self, station, location, date, time_start, time_end, temp_high, temp_low, humid, wind, weather):
        self.station = station
        self.location = location
        self.date = date
        self.time_start = time_start
        self.time_end = time_end
        self.temp_high = temp_high
        self.temp_low = temp_low
        self.humid = humid
        self.wind = wind
        self.weather = weather
        self.csvLine = f"{self.station},{self.location},{self.date},{self.time_start},{self.time_end},{self.temp_high},{self.temp_low},{self.humid},{self.wind},{self.weather}"

    def printSelf(self):
        print(f"Station: {self.station} | Location: {self.location} | Date: {self.date} | Start: {self.time_start} | End: {self.time_end} | High: {self.temp_high}°F | Low: {self.temp_low}°F | Humidity: {self.humid}% | Wind: {self.wind} mph | Weather: {self.weather}")
       
        

def printStations(df):
    print("<=====================================================================================================================================>")
    for x, (index, row) in enumerate(df.iterrows(), 1):
        print(f"Station {x}")
        print(f"Station: {row['Station']} | Location: {row['Location']} | Date: {row['Date']} | Start: {row['Time Start']} | End: {row['Time End']} |\n| High: {row['Temperature Highest']}°F | Low: {row['Temperature Lowest']}°F | Humidity: {row['Humidity (%)']}% | Wind: {row['Wind in mph']} mph | Weather: {row['Weather']}")
        print("<=====================================================================================================================================>")

def addStation():
    global weatherDataFrame
    print("Input station: ")
    station = input(">>")
    print("Input location: ")
    location = input(">>")
    print("Input date: ")
    date = input(">>")
    print("Input time start: ")
    time_start = input(">>")
    print("Input time end: ")
    time_end = input(">>")
    print("Input high temperature: ")
    temp_high = input(">>")
    print("Input low temperature: ")
    temp_low = input(">>")
    print("Input humidity: ")
    humid = input(">>")
    print("Input wind: ")
    wind = input(">>")
    print("Input weather: ")
    weather = input(">>")
    new_row = pd.DataFrame([{
        'Station': station,
        'Location': location,
        'Date': date,
        'Time Start': time_start,
        'Time End': time_end,
        'Temperature Highest': temp_high,
        'Temperature Lowest': temp_low,
        'Humidity (%)': humid,
        'Wind in mph': wind,
        'Weather': weather
    }])
    weatherDataFrame = pd.concat([weatherDataFrame, new_row], ignore_index=True)
    print("Station Created")

def removeStation():
    global weatherDataFrame
    printStations(weatherDataFrame)
    print("What number station would you like removed")
    stationToRemove = int(input(">>"))
    if stationToRemove <= len(weatherDataFrame) and stationToRemove > 0:
        weatherDataFrame = weatherDataFrame.drop(stationToRemove-1).reset_index(drop=True)
    else:
        print("Station not found")

def editStation():
    printStations()
    print(f"Input the station you would like to edit.")
    stationToEdit = input(">>")

def stats():

    df = weatherDataFrame.copy()

    print("File Information: All")
    print(df.info())

    print("First Five Rows")
    print(df.head(5))

    # Data Cleaning

    df['Date'] = pd.to_datetime(df['Date'])

    temp_high = df['Temperature Highest'].to_numpy()
    temp_low = df['Temperature Lowest'].to_numpy()
    humidity = df['Humidity (%)'].to_numpy()
    wind = df['Wind in mph'].to_numpy()

    print(f"Highest Temp: {temp_high}")
    print(f"Lowest Temp: {temp_low}")
    print(f"Humidity: {humidity}")
    print(f"Wind: {wind}")

    plt.plot(df['Date'], temp_high, label = 'High Temp', marker = "o")
    plt.plot(df['Date'], temp_low, label = 'Low Temp', marker = "x")

    plt.title("Daily Tempature Overview")
    plt.xlabel("Date")
    plt.ylabel("Tempature (F)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Bar Chart Wind Speeds

    plt.bar(df['Location'], wind, color = 'skyblue')
    plt.title("WInd Speeds by Location")
    plt.xlabel("Location")
    plt.ylabel("Wind (MPH)")
    plt.show()

    plt.scatter(temp_high, humidity, color = "Green")

    plt.title("Humidity vs High Tempature")
    plt.xlabel("Temperature (F)")
    plt.ylabel("Humidity (%)")
    plt.show()
    

while (loopProgram):
    print("What would you like to do?")
    print(", ".join(optionsList))
    userInput = input(">>")
    match userInput:
        case "print":
            printStations(weatherDataFrame)
        case "add":
            addStation()
        case "remove":
            removeStation()
        case "stats":
            stats()
        case "exit":
            loopProgram = False
        case _:
            print("Invalid Command")

    # Save once at exit and preserve explicit N/A text
    weatherDataFrame = weatherDataFrame.fillna('N/A')
    weatherDataFrame.to_csv("WeatherStationData.csv", index=False)
