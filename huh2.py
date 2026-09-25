weight = float(input())
heigh = float(input())

#convert heigh form centimeter to meter

height_in_metres = heigh / 100
BMI = weight / (height_in_metres ** 2)

print(f"{BMI:.2f}")