"""
Ask the user their name and their grades (3 in total). 
Show them their average and their status:
    < 4: reproved
    < 6: recovery
    >= 6: approved
"""

name = input("Name: ")

print("\nEnter your grades:")

g1 = float(input("Test 1: "))
g2 = float(input("Test 2: "))
g3 = float(input("Project: "))

average = (g1 + g2 + g3) / 3 # All grades have the same weight

if average < 4:
    status = "reproved"
elif average < 6:
    status = "recovery"
else:
    status = "approved"

print("Bimonthly report", "-" * 10)
print(f" {name} ".center(27, "#"))
print("-" * 3, f"Test 1: {g1}")
print("-" * 3, f"Test 2: {g2}")
print("-" * 3, f"Group project: {g3}")
print(f"\nAverage: {average:.2f}")
print(f"Status: {status}")