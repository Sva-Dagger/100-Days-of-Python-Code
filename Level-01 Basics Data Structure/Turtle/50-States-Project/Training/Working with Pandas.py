import pandas

data = pandas.read_csv("weather-data.csv")
print(type(data))
print(type(data["temp"]))