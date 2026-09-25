
first_line = input().split()
rows = int(first_line[0])
cols = int(first_line[1])
target = int(first_line[2])

vulnerable_count = 0
max_total = 0

for i in range(rows):
    row_values = input().split()
    
    
    row_sum = 0
    for item in row_values:
        strength = int(item)
        row_sum = row_sum + strength
    
    if row_sum >= target:
        vulnerable_count = vulnerable_count + 1
        
        if row_sum > max_total:
            max_total = row_sum

print(vulnerable_count)
print(max_total)