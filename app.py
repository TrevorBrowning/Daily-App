from flask import Flask, render_template
import requests
import random
import time

app = Flask(__name__)

@app.route("/")
def homepage():
    current = time.localtime()
    date = time.strftime("%A, %B %d", current)
    try:
        
        
        quote_response = requests.get("https://zenquotes.io/api/today")
        quote_data = quote_response.json()
        quote = quote_data[0]["q"]
        author = quote_data[0]["a"]

   
        today_response = requests.get("https://today.zenquotes.io/api")
        today_data = today_response.json()

        all_events = today_data["data"]["Events"]
        top_events = all_events[:3]  

        all_births = today_data["data"]["Births"]
        top_births = all_births[:3]

        all_deaths = today_data["data"]["Deaths"]
        top_deaths = all_deaths[:3]

        return render_template("index.html", quote=quote, author=author, events=top_events, date=date, births=top_births, deaths=top_deaths)

    except Exception as e:
        print("Something went wrong:", e)
        return "Error occurred while loading data."

if __name__ == "__main__":
    app.run(debug=True)
