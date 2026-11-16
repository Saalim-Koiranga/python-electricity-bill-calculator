Smart Electricity Bill Calculator
A command-line Python application built to calculate monthly customer electricity bills based on energy consumption and tariff categories.
Features
Customer Information Capture: Collects customer full name, meter number, tariff category, and monthly consumption in kilowatt-hours (kWh).
Tiered Tariff Pricing: Automatically applies the appropriate rate per kWh:
Residential: ₦50 / kWh
Commercial: ₦75 / kWh
Industrial: ₦100 / kWh
Dynamic Service Charges & Classification: Assigns fixed service charges and categorizes usage levels based on consumption:
Below 100 kWh: ₦500 service charge (Low Consumption)
100 – 299 kWh: ₦1,000 service charge (Moderate Consumption)
300 kWh and above: ₦2,000 service charge (High Consumption)
Input Validation: Rejects invalid tariff categories and prevents negative electricity consumption values.
Payment Tracking: Records payment status (Payment Successful or Payment Pending) and displays any outstanding balance owed.
Prerequisites
Python 3.x installed on your system.
How to Run
Clone this repository or download electricity_bill.py to your local machine:
git clone https://github.com<your-username>/python-electricity-bill-calculator.git
Navigate into the project directory:
cd python-electricity-bill-calculator
Run the Python script:
python electricity_bill.py
Follow the on-screen prompts to enter customer details and generate the bill.
Example Output
=== ELECTRICITY BILL CALCULATOR ===
Enter customer's full name: Saalim Koiranga Hamman
Enter meter number: 1234567890
Enter tariff category (Residential, Commercial, Industrial): residential
Enter electricity consumed (in kWh): 150
Has the customer paid their bill? (Yes or No): No

=============================================
           ELECTRICITY BILL RECEIPT
=============================================
Customer Name      : Saalim Koiranga Hamman
Meter Number       : 1234567890
Tariff Category    : Residential
Consumption        : 150.00 kWh
Consumption Level  : Moderate Consumption
---------------------------------------------
Unit Rate          : ₦50.00 / kWh
Electricity Charge : ₦7,500.00
Service Charge     : ₦1,000.00
---------------------------------------------
TOTAL PAYABLE      : ₦8,500.00
Payment Status     : Payment Pending
Outstanding Balance: ₦8,500.00
=============================================