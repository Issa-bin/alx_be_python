#prompting the user for task description input
print ("welcome to your daily reminder")

task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes/no):").lower()
priority = input("Priority(high/medium/low):").lower()

#match case
match priority:
    case "high":
        if time_bound == "yes":
            print ("Reminder: {task} is a {priority} task that requires immediate attention today!")
        else:
            print ("Note: {task} is a {priority} task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print ( "Reminder: {task} is a {priority} task that requires immediate attention today!.")
        else:
            print ("Note: {task} is a {priority} task. Consider completing it when you have free time.")

    case "low":
        if time_bound =="yes":
            print ("Note: {task} is a {priority} task. Consider completing it today.")
        else:
            print ("Note: {task} is a {priority} task. Consider completing it when you have free time.")

#IF customization
checker = input("Do you want to add a new task (yes or no):") 
if checker == "yes":
    continue
else:
    break

#call the function
daily_reminder: any 