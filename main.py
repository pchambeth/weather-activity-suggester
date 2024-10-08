import requests
import openai

# Set your API keys
openai.api_key = 'YOUR_OPENAI_API_KEY'
weather_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

# Function to get weather information
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get activity suggestions based on weather conditions
def get_activity_suggestion(weather_description, temperature):
    prompt = f"The weather is described as {weather_description} with a temperature of {temperature} degrees Celsius. Suggest some fun activities to do in this weather."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Main function
def main():
    city = input("Enter your city: ")
    weather_data = get_weather(city)

    if weather_data:
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        print(f"Current weather in {city}: {weather_description}, {temperature}°C")

        # Get activity suggestions
        suggestion = get_activity_suggestion(weather_description, temperature)
        print(f"Suggested activities: {suggestion}")
    else:
        print("Unable to fetch weather data. Please check the city name or try again later.")

if __name__ == "__main__":
    main()