#added to check
#Maudood Fareed
import argparse
# ANSI escape code for red text
RED = '\033[91m'
# ANSI escape code for blue text
BLUE = '\033[94m'
# ANSI escape code to reset text color to default
RESET = '\033[0m'

def colored_text(text, color):
    return f"{color}{text}{RESET}"



#Function to check the highest, lowest Temperatures and humidity
def find_temperatures_humidity(filename, max_temp, max_temp_date, min_temp,
                               min_temp_date, max_humidity, max_humidity_date,
                               year):
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()

  except FileNotFoundError:
    print("File not Found")
    return max_temp, max_temp_date, min_temp, min_temp_date, max_humidity, max_humidity_date

  else:

    for line in lines:
      if not line.startswith(str(year)):
        continue

      data = line.strip().split(',')
      date = data[0]

      try:
        max_temp_c = float(data[1])

        if max_temp_c > max_temp:
          max_temp = max_temp_c
          max_temp_date = date

        min_temp_c = float(data[3])
        if min_temp_c < min_temp:
          min_temp = min_temp_c
          min_temp_date = date

        humidity_c = float(data[7])
        if humidity_c > max_humidity:
          max_humidity = humidity_c
          max_humidity_date = date

      except ValueError:
        pass

  return max_temp, max_temp_date, min_temp, min_temp_date, max_humidity, max_humidity_date


# function find_highest_lowest_temperature and Humidty ends here


#Function find month against number
def find_month(date):
  year, month, day = map(int, date.split('-'))
  month_names = [
    None, "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
  ]
  return f"{month_names[month]} {day}"
# find_month(date) ends here


#Function to check the average highest, average lowest Temperatures and average humidity
def find_average_temperatures_humidity(filename, sum_max_temp, sum_min_temp,
                               sum_max_humidity, year):
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()

  except FileNotFoundError:
    print("File not Found")
    return sum_max_temp, sum_min_temp, sum_max_humidity

  else:
    count1 = 0
    count2 = 0
    count3 = 0
    for line in lines:
      if not line.startswith(year):
        continue

      data = line.strip().split(',')

      try:
        max_temp_c = float(data[1])
        sum_max_temp += max_temp_c
        count1 = count1 + 1

        min_temp_c = float(data[3])
        sum_min_temp += min_temp_c
        count2 = count2 + 1

        humidity_c = float(data[7])
        sum_max_humidity += humidity_c
        count3 = count3 + 1

      except ValueError:
        pass

  avg_max_temp = find_Average(sum_max_temp, count1)
  avg_min_temp = find_Average(sum_min_temp, count2)
  avg_max_humidity = find_Average(sum_max_humidity, count3)
  return avg_max_temp, avg_min_temp, avg_max_humidity
# function find_highest_lowest_temperature and Humidty ends here


#find average
def find_Average(sum, count):
  avg = sum // count
  return avg
#function ends here

#Function to make graph for MAX and MIN temperature
def graph(filename, year):
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()

  except FileNotFoundError:
    print("File not Found")
    return 

  else:
    cnt=1
    max_temp = float('0')
    min_temp = float('0')
    for line in lines:
      if not line.startswith(year):
        continue

      data = line.strip().split(',')

      try:
        max_temp = int(data[1])
        print("0"+ str(cnt) + " " + colored_text("+",RED) *max_temp,str(max_temp)+"C")
        
        min_temp = int(data[3])
        print("0"+ str(cnt) + " " + colored_text("+",BLUE) *min_temp,str(min_temp)+"C")
        
        cnt=cnt+1
        max_temp=0
        min_temp=0
      except ValueError:
        pass

  return
# function  ends here


#main 1 starts here
def main1(args,filename_temp):
  max_temp = float('-inf')
  max_temp_date = None
  min_temp = float('inf')
  min_temp_date = None
  max_humidity = float('-inf')
  max_humidity_date = None
  month_names = [
  "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
  "Dec"]
  
  for i in month_names:
    filename = filename_temp + '/lahore_weather_' + str(args.year) + '_' + i + '.txt'  # declare the file name
    max_temp, max_temp_date, min_temp, min_temp_date, max_humidity, max_humidity_date = find_temperatures_humidity(filename, max_temp, max_temp_date, min_temp, min_temp_date, max_humidity, max_humidity_date, args.year)
  print(f"Highest: {max_temp}C on {find_month(max_temp_date)}.")
  print(f"Lowest: {min_temp}C on {find_month(min_temp_date)}.")
  print(f"Humidity: {max_humidity}% on {find_month(max_humidity_date)}.")
#main 1 ends here


#main 2 starts here
def main2(args,filename_temp):
  year, month = args.year_month.split('/')
  avg_max_temp = float('0')
  avg_min_temp = float('0')
  avg_max_humidity = float('0')
  
  month_names = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec"
  }
  
  filename = filename_temp+'/lahore_weather_' + year + '_' + month_names[month] + '.txt'  # declare the file name
  avg_max_temp, avg_min_temp, avg_max_humidity = find_average_temperatures_humidity(
    filename, avg_max_temp, avg_min_temp, avg_max_humidity, year)
  
  print(f"Highest Average: {avg_max_temp}C")
  print(f"Lowest Average: {avg_min_temp}C")
  print(f"Average Humidity: {avg_max_humidity}%")
  print("\n\n---------------Graph---------------\n\n")
  graph(filename,year)
#main 2 ends here


#Code starts from here



parser = argparse.ArgumentParser(description='Find weather data for a given year or year and month.')
parser.add_argument('-e', '--year', type=int, help='Year to find weather data for')
parser.add_argument('-a', '--year_month', type=str, help='Year and month (format: YYYY/MM) to find weather data for')
parser.add_argument('folder_path', type=str, help='Path to the folder containing weather data files')
args = parser.parse_args()
filename_temp = args.folder_path.lstrip(args.folder_path[0])
#In case only year is passed through Command line
if args.year:
  main1(args,filename_temp)

#In case both year and month are passed through Command line
elif args.year_month:
  main2(args,filename_temp)  
  
