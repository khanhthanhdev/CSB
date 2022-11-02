name = ['BĐ','BTL','CG','ĐĐ','HBT']
population = [247100,333300,266800,420900,318000]
print("Name of:")
max_population = population[0]
min_population = population[0]
for i in population:
    if i > max_population:
        max_population = population.index(i)-1
for i in population:
    if i == min_population:
        min_population = population.index(i)
    elif i < min_population:
        min_population = population.index(i)-1

print(name[max_population])
print(f"- Most populated dist: {name[max_population]} ")
print(f"- Least populated dist: {name[min_population]}")