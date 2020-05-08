import pyowm

# You MUST provide a valid API key
owm = pyowm.OWM('c2a7db9aa27108e3819f53ead03da2b3', language="ru")

place = input("В каком городе/стране")
observation = owm.weather_at_place(place)
w = observation.get_weather()
print(w)
