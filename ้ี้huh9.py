
first_line = input().split()
rows = int(first_line[0])
cols = int(first_line[1])

count = 0
total_sum = 0


for i in range(rows):
      
    numbers = input().split()
    
    for item in numbers:
        val = int(item)
        
        
        if val >= 10 and val <= 50 and val % 2 == 0:
            count = count + 1
            total_sum = total_sum + val

print(count)
print(total_sum)