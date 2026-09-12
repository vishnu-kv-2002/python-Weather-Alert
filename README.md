# 🌧️ Weather Alert

A Python weather alert application that checks the weather forecast for a specified location. If rain is expected, the program sends an **SMS notification** reminding the user to carry an umbrella.

## 🚀 Features

* 🌦️ Gets weather forecast data using the OpenWeatherMap API
* ☔ Checks whether rain is expected
* 📱 Sends an SMS alert using Twilio
* 🔐 Keeps API keys and credentials in environment variables
* 🐍 Built with Python

## 🛠️ Technologies Used

* Python
* Requests
* OpenWeatherMap API
* Twilio
* python-dotenv

## 📁 Project Structure

```text
Weather-Alert/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 📦 Installation

Install the required libraries:

```bash
pip install requests twilio python-dotenv
```

Or use `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project directory:

```env
MY_LAT=your_latitude
MY_LON=your_longitude
API_KEY=your_openweathermap_api_key

ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
```

The program uses `python-dotenv` to load these values without putting them directly into the Python code.

### ⚠️ Security

Never upload your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
```

Also, never publish your OpenWeatherMap API key or Twilio credentials.

## ⚙️ How It Works

1. Loads the API keys and Twilio credentials from `.env`.
2. Sends the latitude, longitude, API key, and forecast count to the OpenWeatherMap API.
3. Receives the weather forecast as JSON data.
4. Checks the weather condition code for the forecast periods.
5. If a condition code is below `700`, rain or other precipitation is considered possible.
6. If rain is detected, the program prints:

```text
Bring an Umbrella
```

7. The program then sends an SMS using Twilio.

## ☔ Rain Detection

The program checks the weather condition ID:

```python
condition_code = hour_data['weather'][0]['id']

if condition_code < 700:
    will_rain = True
```

OpenWeatherMap uses weather condition codes to represent different weather conditions. Codes below `700` include precipitation-related conditions such as rain and snow.

## 📱 SMS Notification

When rain is expected, Twilio sends a message similar to:

```text
Its going to rain today, Remember to bring an UMBRELLA.
```

The SMS is sent only when the program detects a suitable weather condition.

## 🧠 Concepts Learned

* Working with REST APIs
* Sending HTTP GET requests
* Using API parameters
* Processing JSON responses
* Using environment variables
* Using `python-dotenv`
* Working with Twilio
* Sending SMS notifications
* Conditional statements
* Loops
* Exception handling with `raise_for_status()`

## 🔮 Future Improvements

* Check forecasts at regular intervals
* Send alerts only once per day
* Include the expected rain time in the SMS
* Include temperature and weather conditions
* Add multiple locations
* Create a graphical user interface
* Add support for email notifications
* Schedule the program to run automatically

## 👨‍💻 Author

**Vishnu K V**

A Python project created to practice API integration, weather data processing, environment variables, and SMS automation.
