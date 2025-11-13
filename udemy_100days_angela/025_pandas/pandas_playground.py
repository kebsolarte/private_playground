
# using the basic method of opening a file
# with open('weather_data.csv', mode='r') as file:
#     data = [row.strip() for row in file.readlines()]
# print(data)

# Using csv module to open csv files
# import csv

# with open('weather_data.csv', mode='r') as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
# print(temperatures)

# Using pandas to work on csv files
import pandas as pd

data = pd.read_csv("weather_data.csv")

temp_list = data['temp'].to_list()

average_temp = sum(temp_list)/len(temp_list)
print(average_temp)

# Some pandas methods
print(data['temp'].mean())
print(data['temp'].max())

# Accessing columns. Pandas treat columns as attributes
print(data['condition'])
print(data.condition)

# Accessing specific rows
print(data[data.day == 'Monday'])
print(data[data['day'] == 'Monday']['temp'])
print(data[data.day == 'Monday'].temp)
print(data[data.temp == data.temp.max()])

# Creating DataFrames from dicts
cute_dogs = {
    'Name': ['Tiny', 'Babe', 'Chewy'],
    'Breed': ['Pug', 'Terrier', 'Poddle']
}

cute_dogs = pd.DataFrame(cute_dogs)

print(cute_dogs)