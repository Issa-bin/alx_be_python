#prompting the user for task description input
print ("welcome to your daily reminder")

task = input("Enter your task:")
time_bound = input("Is it time-bound? (yes/no:)")
priority = input("priority: (high/medium/low)")

#match case
match (priority, time_bound):
    case ("high", "yes"):
        print ("Reminder: {task} is a high-priority ask that requires immediate attention today!")
    case ("medium", "yes"):
        print ( "Reminder: {task} is a medium-priority task. Address it soon.")
    case ("low", "yes"):
        print ("note: {task} is a low-priority task. consider completing it when you have free time.")
    case _:
        print ("task: {task} doesn't match predefined conditions. please review your input.")

#IF customization
if time_bound == "yes" and priority == "high":
    print ("action required: {task} must be completed immediately due to its high priority")

#call the function
daily_reminder: any 