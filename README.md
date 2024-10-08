# weather-activity-suggester
A Python app that suggests fun activities based on local weather, using OpenWeatherMap and OpenAI APIs

## Overview
This application suggests fun activities to do based on the current weather in your city. It uses the OpenWeatherMap API to fetch the weather data and the OpenAI GPT model to provide activity suggestions tailored to the weather conditions.

## Features
- Fetches real-time weather information for any city.
- Provides activity suggestions based on the current weather conditions and temperature.

## Technologies Used
- **Python**: The core language used for the application.
- **OpenWeatherMap API**: To get the weather data for the specified city.
- **OpenAI API**: To generate activity suggestions based on the weather data.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-activity-suggestion-app.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd weather-activity-suggestion-app
   ```
3. **Install required packages**:
   The application requires `requests` and `openai` Python packages. Install them using:
   ```bash
   pip install requests openai
   ```

## Setup
1. **API Keys**:
   - Get your API key from [OpenWeatherMap](https://openweathermap.org/).
   - Get your API key from [OpenAI](https://platform.openai.com/).
2. **Configure API keys**:
   Replace `'YOUR_OPENAI_API_KEY'` and `'YOUR_OPENWEATHERMAP_API_KEY'` in the script with your actual API keys.

## Usage
1. **Run the script**:
   ```bash
   python weather_activity_app.py
   ```
2. **Enter your city name** when prompted to get real-time weather data and activity suggestions.

## Example Output
```
Enter your city: New York
Current weather in New York: clear sky, 25°C
Suggested activities: Go for a walk in the park or have a picnic outside.
```

## Deployment on Replit
You can easily deploy this app on [Replit](https://replit.com/) to make it accessible online.

1. **Create a Replit Account**:
   - Go to [Replit](https://replit.com/) and create an account if you don't already have one.
2. **Create a New Repl**:
   - Click on the **+ Create** button and select **Python** as the template.
3. **Upload the Code**:
   - Copy and paste the code from `weather_activity_app.py` into the main file in your Replit project.
4. **Add Environment Variables**:
   - Click on the **Secrets (Environment Variables)** option on the left panel.
   - Add your `OPENAI_API_KEY` and `OPENWEATHERMAP_API_KEY` as environment variables.
5. **Run the App**:
   - Click the **Run** button to start the application.
   - The console will prompt you to enter a city name, and you'll receive the weather data along with activity suggestions.

## Notes
- Make sure you have an active internet connection to fetch weather data and interact with the OpenAI API.
- Replace API keys with your valid keys before running the application.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit pull requests for improvements or additional features. Suggestions are always welcome!

## Author
Developed by Pratheesh Chambeth using ChatGPT.