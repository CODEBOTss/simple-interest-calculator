# Simple Interest Calculator

# Formula: SI = (P * R * T) / 100

principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
print("Total Amount =", principal + simple_interest)
