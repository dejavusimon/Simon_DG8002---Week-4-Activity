# DG8002 - F26 - Activity 4
# Author Name: Simon Su
# Date: Oct.04.2026

#                 M   T   W  Th  F   Sa  Su
temperatures  = [18, 22, 25, 19, 27, 24, 16]

totalTemperature = 0
daysAbove23 = 0
hottestDay = -1

index = 0
for temperature in temperatures:
    print(f"Day {index}: {temperature} degrees")

    totalTemperature += temperature

    if temperature > 23:
        daysAbove23 += 1

    if hottestDay == -1 or temperature > temperatures[hottestDay]:
        hottestDay = index

    index += 1

averageTemperature = totalTemperature / len(temperatures)
print(f"Average temperature for the week: {averageTemperature:.1f} degrees")

print(f"Days above 23 degrees: {daysAbove23}")

print(f"Index of the highest temperature: {hottestDay}")