shop = {"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
price = {'HP':600, 'DELL':650, 'MACBOOK':1200, 'ASUS':400}


print('Total value of available brands:')
for brand in shop:
    print('- {}: {}'.format(brand, shop.get(brand)*price.get(brand)))

'''
Total value of
available brands:
- HP: 12000
- DELL: 32500
- MACBOOK: 14400
- ASUS: 12000
'''