# Program to display calendar of the given month and year
# importing calendar module
import calendar
yy =int(input("Enter the year in yyyy format: "))  # year
mm =int(input("Enter the month in mm format: "))    # month
# display the calendar
print(calendar.month(yy, mm))
