temperature = [28, 30, 31, 29, 35, 34, 32, 30, 29, 50]
average = sum(temperature) / len(temperature)
maximum = max(temperature)
minimum = min(temperature)
above_32 = sum(t > 32 for t in temperature)
print( average)
print(maximum)
print( minimum)
print( above_32)