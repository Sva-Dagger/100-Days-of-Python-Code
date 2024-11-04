 import pandas

"""data = pandas.read_csv("weather-data.csv")
data_dict = data.to_dict()
print(data_dict)
Total_temp = 0

temp_list = data["temp"].to_list()
Nr_temp_data = len(temp_list)
#for temp in temp_list:
#    Total_temp += temp
#Total_temp = sum(temp_list)
#Avg_temp = Total_temp/Nr_temp_data
Avg_temp = data["temp"].mean()
print(round(Avg_temp,2))
Max_data = data["temp"].max()
print(Max_data)
conditions_data = data.condition.to_list()
print(conditions_data)"""
"""
data = pandas.read_csv("weather-data.csv")
row = data[data.day == "Monday"]
temp_1 = row.temp[0]
Farenheit = (temp_1 * 9/5) + 32
#Get data in row
print(Farenheit)"""
"""max_data = data.temp.max()
print(data[data.temp == max_data]) """

"""data_dict = {"Students": ["Amy", "James", "Angela"],
             "scores" : [76, 56, 65]}
data = pandas.DataFrame(data_dict)
data.to_csv("New_data.csv")"""
Color_count = []
data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
Gray_Squirrel_Count = len(data[data["Primary Fur Color"] == "Gray"])
print(Gray_Squirrel_Count)
Cinnamon_Squirrel_Count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(Cinnamon_Squirrel_Count)
Black_Squirrel_Count = len(data[data["Primary Fur Color"] == "Black"])
print(Black_Squirrel_Count)
Data_dict = {
    "Fur Color" :["Gray", "Cinnamon", "Black"],
    "Count" :[Gray_Squirrel_Count, Cinnamon_Squirrel_Count, Black_Squirrel_Count]
}
New_csv = pandas.DataFrame(Data_dict)
New_csv.to_csv("New_CSV.csv")




