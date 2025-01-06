import datetime

#Get today's date and time 
today = datetime.datetime.now()

#Print today's date nd time
print(f"Today's date and time: {today}")

#Access individual components of the datetime object
year = today.year
month = today.month
day = today.day
hour = today.hour
minute = today.minute
second = today.second

#Print individual components
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")

#Create a specific date and time object
specific_datetime = datetime.datetime(2025,01,07,00,25,0)#Year,Month,Day,Hour,Minute,Second

#print the specific date and time object
print(f"\nSpecific date and time: {specific_datetime}")

#Perform time arithmetic - Add or subtract time from date and time object
time_delta = datetime.timedelta(days=2, hours=5) # Create a timedelta object (days, hours, minutes, seconds)
future_datetime = today + time_delta

#Print the future date and time
print(f"nDate and time after adding time delta: {future_datetime}")

#Formatting datetime objects
formatted_date = today.strftime("%Y-%m-%d") #YYYY-MM-DD format
formatted_time = today.strftime("%H:%M:%S") #HH:MM:SS format

#Print formatted date and time
print(f"\nFormatted date: {formatted_date}")
print(f"Formatted time: {formatted_time}")
