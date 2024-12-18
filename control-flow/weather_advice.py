#weather input prompt
weather = input("what's the weather like today? (sunny/rainy/cold):")

#clothing recommendations with control-flow
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

#the function call
if __name__=="__main__":
    "get_weather_recommendation()"