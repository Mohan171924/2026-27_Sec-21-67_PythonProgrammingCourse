#example for compound interest
principle = float(input("enter the principle amount"))
rate = float(input("enter the rate of interest"))
time = float(input("enter the time in years "))
total = principle * (1 + rate / 100) ** time
compound = total - principle 
print("the total amount after compound is:",compound)



