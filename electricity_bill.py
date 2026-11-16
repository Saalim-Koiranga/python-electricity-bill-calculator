print("=== ELECTRICITY BILL CALCULATOR ===")

# Part 1: collect customer information
full_name = input("Enter customer's name: ")
meter_number = input("Enter meter number: ")
tariff_category = input("Enter tariff category (Residential, Commercial, Industrial): ").strip().title()
consumption = float(input("Enter electricity consumed (in kWh): "))

# ADDITIONAL CHALLENGE 1: Negative consumption check
if consumption < 0:
    print("Error: Electricity consumption cannot be negative.")
    exit()

# Part 2: Calculate the electricity rate
if tariff_category == "Residential":
    rate_per_kwh = 50
elif tariff_category == "Commercial":
    rate_per_kwh = 75
elif tariff_category == "Industrial":
    rate_per_kwh = 100
else:
    print("Invalid tariff category")
    exit()
#Part 3 & Part 4: Service charge and consumption level
if consumption < 100:
    service_charge = 500
    consumption_level = "Low Consumption"
elif consumption < 300:
    service_charge =1000
    consumption_level = "Moderate Consumption"
else :
    service_charge =2000
    consumption_level = "High Consumption"

#Part 5: Calculations
electricity_charge = consumption * rate_per_kwh
total_bill = electricity_charge + service_charge

#Addtional challenge 3 & 4: Payment status and outstanding balance
paid = input("Has the customer paid their bill? (Yes or No): ").strip().title()

if paid == "Yes":
    payment_status = "Payment Successful"
    outstanding_balance = 0
else:
    payment_status = "Payment Pending"
    outstanding_balance = total_bill

# Display the well-formatted bill
print("\n" + "=" * 45)
print("           ELECTRICITY BILL RECEIPT")
print("=" * 45)
print(f"Customer Name      :  {full_name}")
print(f"Meter Number       :  {meter_number}")
print(f"Tariff Category    :  {tariff_category}")
print(f"Consumption        :  {consumption:,.2f} kwh")
print(f"Consumption Level  :  {consumption_level}")
print("-" * 45)
print(f"Unit Rate          :  ₦{rate_per_kwh:,.2f} / kwh")
print(f"Electricity Charge :  ₦{electricity_charge:,.2f}")
print(f"Service Charge     :  ₦{service_charge:,.2f}")
print("-" * 45)
print(f"TOTAL PAYABLE      :  ₦{total_bill:,.2f}")
print(f"Payment Status     :  {payment_status}")

if payment_status == "Payment Pending":
    print(f"Outstanding Balance: ₦{outstanding_balance:,.2f}")

print("=" * 45)