def calculate_total_minutes(hour, minute):
    return (hour * 60) + minute

x = int(input())
y = int(input())

print("Total time in minutes:" , calculate_total_minutes(x, y))
calculate_total_minutes(x, y)

