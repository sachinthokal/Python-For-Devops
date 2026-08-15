# Variables, data types and operators.

environment = "staging"
cpu_cores = 4
load_average = 1.75
is_production = False

print("environment  :", environment, "->", type(environment))
print("cpu_cores    :", cpu_cores, "->", type(cpu_cores))
print("load_average :", load_average, "->", type(load_average))
print("is_production:", is_production, "->", type(is_production))

a = 100
b = 30
print("\nAddition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor division :", a // b)
print("Remainder      :", a % b)

# input() always gives you a str, so cast when you need a number.
disk_used_str = "82"
disk_used = int(disk_used_str)
print("\nDisk used (int):", disk_used, "->", type(disk_used))
