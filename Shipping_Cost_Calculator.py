# Here is a new update by Beast
# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
r = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * r

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

