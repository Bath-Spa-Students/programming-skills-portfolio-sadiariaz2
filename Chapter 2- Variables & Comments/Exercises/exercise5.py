'''Chapter 2 Exercise:5  USB Shopper '''

# Cost of each USB stick
usb_price = 6

# Total budget in pounds
total_budget = 50

#Maximum number of USB sticks she can buy
num_usb = total_budget // usb_price

#Remaining pounds after buying USB sticks
remaining_pounds = total_budget % usb_price

# Output the results
print("She can buy", num_usb, "USB sticks.")
print("She will have £", remaining_pounds, "left.")
