name = ['BĐ','BTL','CG','ĐĐ','HBT']
population = [247100,333300,266800,420900,318000]
area = [9.224,43.35,12.04,9.96,10.09]
density = []
new_density = []
average = 0
sum = 0
for i in range(len(name)):
    density.append(f"- {name[i]} : {population[i] / area[i]}")
    new_density.append(population[i] / area[i])
# for i in range(len(density)):
#     # print(density[i])



for i in population:
    i+=1
for i in new_density:
    sum +=i
for i in range(len(new_density)):
    average = sum / len(new_density)
print(f"Average population density: {average}")



