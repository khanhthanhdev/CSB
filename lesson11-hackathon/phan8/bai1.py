skill = [{'Name': 'Tackle ','Minimum level': 1,'Damage':5,'Hit rate':0.3},
         {'Name': 'Quick Attack ','Minimum level': 2,'Damage':3,'Hit rate':0.5},
         {'Name': 'Strong kick ','Minimum level': 4,'Damage':9,'hit rate':0.2}
]

count = 1
for i in skill:
    print(f"Skill {count} : {i['Name']}")
    count = count + 1

level = 2


n = int(input("Chose skill by number: "))

if n < len(skill) or n > 1:
    if skill[n-1]['Minimum level'] < level:
        print(f"You choose {skill[n-1]['Name']}")
        print(f"Damage {skill[n-1]['Damage']}")
    else:
        print("Cannot deploy. Required level 4.")


