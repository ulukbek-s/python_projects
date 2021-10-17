import weather_forecast as wf

location=input('Enter Location: ')
weather = wf.forecast(place=location)

print(weather)