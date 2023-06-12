from time import localtime
from nltk.chat.util import Chat, reflections
from tkinter import *
import requests, json

# for weather
api_key = "cf8a9cb4078604d0f839b9e401562390"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "Amaravati"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

	y = x["main"]

	current_temperature = y["temp"]

	current_pressure = y["pressure"]

	current_humidity = y["humidity"]

	z = x["weather"]

	weather_description = z[0]["description"]
# -----

def respond(message):
    try:
        result = eval(message)
        return str(result)
    except:
        if message.endswith("?"):
            return "I'm sorry, I'm not able to answer questions at this time."
        else:
            return "I'm sorry, I'm not able to understand your input. Can you please rephrase that?"

pairs = [
    ["my name is (.*)", ["Hello %1, how can I help you today?"]],
    ["hi|hello|hey", ["Hello there! How can I help you?"]],
    ["what is the temperature?", [f"The temperature is {current_temperature} in Kelvin."]],
    ["(.*) weather (.*)", [f"The current weather is {weather_description} with current temperature being {int(current_temperature)} Kelvin"]],
    ["(.*) sports (.*)", ["I'm sorry, I'm not able to provide sports information at this time."]],
    ["(.*) time (.*)", [f"It is currently {localtime().tm_hour}:{localtime().tm_min}."]],
    ["(.*) date today?", [f"Today is {localtime().tm_mday} of month {localtime().tm_mon} in {localtime().tm_year}"]],
    ["where am i?", ["I'm sorry, I'm not able to provide your current location at this time."]],
    ["(.*)?", ["Sorry, I do not understand."]]
]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

chatbot = Chat(pairs, reflections)

window = Tk()
window.title("Chatbot")

history_frame = Frame(window)
history_frame.pack()

scrollbar = Scrollbar(history_frame)
scrollbar.pack(side = RIGHT, fill = Y)

history = Text(history_frame, yscrollcommand = scrollbar.set)
history.pack(side = LEFT, fill = BOTH)

scrollbar.config(command = history.yview)

input_frame = Frame(window)
input_frame.pack()

input_field = Entry(input_frame, width = 60)
input_field.pack(side = LEFT, fill=BOTH)

submit_button = Button(input_frame, text="Submit", command=lambda: submit_input(), background= '#FFFFFF')
submit_button.pack(side = RIGHT)

def submit_input():
    user_input = input_field.get()
    history.config(state=NORMAL)
    history.insert(END, "You: " + user_input + "\n")
    response = chatbot.respond(user_input)
    history.insert(END, "Bot: " + response + "\n")
    history.config(state=DISABLED)
    input_field.delete(0, END)

window.mainloop()