def explore_datetime():
    #import the datetime module
    import datetime

    #get the current date and time using datetime.now()
    now = datetime.now()
    print('Current date and time:',now)

    #add 3 days to the current date using timedelta
    number_of_days = 3
    future_date = now + datetime.timedelta(days = number_of_days)
    print('Date and time after adding 3 days:',future_date)

#access individual components
if__name__=='__main__':
explore_datetime() 