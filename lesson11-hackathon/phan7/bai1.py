skill = [{'Name': 'Tackle ','Minimum level': 1,'Damage':5,'Hit rate':0.3},
         {'Name': 'Quick Attack ','Minimum level': 2,'Damage':3,'Hit rate':0.5},
         {'Name': 'Strong kick ','Minimum level': 4,'Damage':9,'hit rate':0.2}
]

count = 1
for i in skill:
    print(f"Skill {count} : {i['Name']}")
    count = count + 1