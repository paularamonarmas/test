from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/<userInputName>")
def hello_someone(userInputName):
	return render_template("hello.html", myname=userInputName.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    send_message(form_data["email"])
    return "All OK"

@app.route("/weather", methods=["POST"])
def weatherIn():
    form_data = request.form
    return weatherInCity(form_data["city"])

def send_message(email):
	print(email)
	return requests.post("https://api.mailgun.net/v3/sandboxbec895c8e12a4174a2462f053a6bad7c.mailgun.org/messages",
        auth=("api", "41f4e00ee0156073d275f5162b7ea638-e566273b-8f7e8104"),
        data={"from": "Excited User <mailgun@sandboxbec895c8e12a4174a2462f053a6bad7c.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

def weatherInCity(city):
	endpoint = "http://api.openweathermap.org/data/2.5/weather"
	payload = {"q": city, "units":"metric", "appid":"f3f22ff0914d7726acb8527b6786f5c4"}

	response = requests.get(endpoint, params=payload)

	print(response.url)
	print(response.status_code)
	print(response.headers["content-type"])
	return response.json



app.run(debug=True)
