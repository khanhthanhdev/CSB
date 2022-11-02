name = ['BĐ','BTL','CG','ĐĐ','HBT']
population = [247100,333300,266800,420900,318000]
area = [9.224,43.35,12.04,9.96,10.09]
print("Population density of: ")
density = []

for i in range(len(name)):
    density.append(f"- {name[i]} : {population[i] / area[i]}")

for i in range(len(density)):
    print(density[i])

