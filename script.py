# Ground shipping prices
def ground_shipping(weight):
  if weight <= 2:
    return weight * 1.50 + flat_charge
  elif weight <= 6:
    return weight * 3.00 + flat_charge
  elif weight <= 10:
    return weight * 4.00 + flat_charge
  else:
    return weight * 4.75 + flat_charge
# Ground shipping flat charge
flat_charge = 20.00

# Drone shipping prices
def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight <= 6:
    return weight * 9.00 
  elif weight <= 10:
    return weight * 12.00
  else:
    return weight * 14.25

# Premium ground shipping flat charge
premium_shipping = 125.00


# Cheapest shipping calculator
def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_shipping:
    return print("The cheapest method to ship your package would be by Ground Shipping.", "This would come to a total of $", ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_shipping:
    return print("The cheapest method to ship your package would be by Drone Shipping.", "This would come to a total of $", drone_shipping(weight))
  else:
    return print("The cheapest method to ship your package would be by Premium Ground Shipping.", "This would come to a total of $", premium_shipping)


print(cheapest_shipping(41.5))