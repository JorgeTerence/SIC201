"""
Ask the user their name and their grades throughout the year (4 * 3 = 12 grades in total). 
Show them their average and their status:
    < 4: reproved
    < 6: recovery
    >= 6: approved
"""

name = input("Name: ")

print("\nEnter your grades:")

averages = []

for i in range(1, 5):
    g1 = float(input(f"Test 1 ({i}): "))
    g2 = float(input(f"Test 2 ({i}): "))
    g3 = float(input(f"Project ({i}): "))
    print()

    averages += (g1 + g2 + g3) / 3

average = sum(averages) / 4 # All grades have the same weight

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