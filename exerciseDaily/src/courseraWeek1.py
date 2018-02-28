"""
feet in a mile
"""
def miles2feet(miles):
    return int(miles) * 5820
"""
main body
"""
miles = input("Enter the miles")
print(miles2feet(miles))
    
"""
hours and minutes 2 seconds
"""
def hoursAndMinutes2second(hours,minutes):
    return (hours * 3600) + (minutes * 60)
"""
main body
"""
hours = int(input("Enter the hours"))
minutes = int(input("Enter the minutes"))
print(hoursAndMinutes2second(hours,minutes))

"""
length in inches of the perimeter of a rectangle
"""
def permiterOfRectange(wide,height):
    return (2 * wide) + (2 * height)
"""
main body
"""
wide = int(input("Enter the wide for the perimeter"))
height = int(input("Enter the height for the perimeter"))
print(permiterOfRectange(wide,height))
           
"""
future value
"""
def futureValue(principle,rate,years):
    return principle * ((1 + (0.01 * rate)) ** years)  
"""
main body
"""                      

principle = int(input("Principle "))
rate = int(input("Rate "))
years = int(input("Years "))
print(futureValue(principle,rate,years))

"""
nameAndAge
"""
def nameAndAge(name,age):
    return "My name is " + name + " and I am " + str(age) + " years old!"

"""
main body
"""
name = input("Enter user name")
age = int(input("Enter the user age"))

print(nameAndAge(name,age))

