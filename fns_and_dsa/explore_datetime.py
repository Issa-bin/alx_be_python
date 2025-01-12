from datetime import datetime, timedelta
    
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ",current_date)


display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current: "))

def calculate_future_date():
    future_date = datetime.now() + timedelta(days=number_of_days)
    calculated_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Future date: ",calculated_future_date)

calculate_future_date()