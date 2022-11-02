list = ['blue','red','teal','green']
color_list = ', '.join(list)
print(f"Color list: {color_list}")

item_delete = int(input("Item to delete: "))
del list[item_delete-1]
new_list = ', '.join(list)
print(f"New color: {new_list}")