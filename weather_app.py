from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

# api key
url_api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

#calling the text file
api_file = 'weather.key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key']

# finding the weather of the city
def weather_find(city):
    final = requests.get(url_api.format(city, api_key))
    if final:
        # using the json file
        json_file = final.json()
        city = json_file['name']
        country_name = json_file['sys']['country']
        # taking the temperature
        k_temperature = json_file['main']['temp']
        # celcius temperatute
        c_temperature = k_temperature - 273.15
        # farenhite temprature
        f_temperature = (((k_temperature - 273.15) *9 )/ 5)+32

        weather_display = json_file['weather'][0]['main']
        result = (city, country_name, c_temperature, f_temperature, weather_display)

        return result
    else:
        return None


# printing all the details of weather
def print_weather():
    city = search_city.get()
    weather = weather_find(city)
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0],weather[1])
        temperature_entry['text'] = '{:.2f} C, {:.2f} F'.format(weather[2],weather[3])
        weather_entry['text'] = weather[4]

    else:
        messagebox.showerror("Error", "Please Enter a Valid Country Name")



root = Tk()
# Title Name
root.title("Weather App")
# giving background a colour
root.config(background="black")
# giving dimension
root.geometry("700x400")

# entry box to search our city
search_city = StringVar()
enter_city = Entry(root, textvariable= search_city, bg = "yellow", fg="blue", font=("Arial", 40, "bold"))
enter_city.pack()

# search button
search_button = Button(root, text="SEARCH WEATHER", width=20, bg="white", fg="blue", font=("Arial", 30, "bold"), command=print_weather)
search_button.pack()

#geting location
location_entry = Label(root, text='', font=("Arial", 35, "bold"), bg="lightblue")
location_entry.pack()

#temperature
temperature_entry = Label(root, text='', font=("Arial", 35, "bold"), bg="lightpink")
temperature_entry.pack()

#weather information
weather_entry = Label(root, text='', font=("Arial", 35, "bold"), bg= "lightgreen")
weather_entry.pack()


root.mainloop()