# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"
# user_input = float(input("Enter temperature:   "))
# print(weather_condition(user_input))

name = input("Enter your name:  ")
surname = input("Enter your surname:  ")
when = "Today"


message = "Hello %s %s" % (name, surname)  #Para versiones anteriores de Python
message = f"Hello, {name} {surname}. What's up {when}"  #Para versiones posteriores de Python
print(message)

#Otra forma de hacerlo es:
name = "Juan"
surname = "Reina"

message_2 = "Your name is {}. Your surname is {}.".format (name, surname)
print(message_2)