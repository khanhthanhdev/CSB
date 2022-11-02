seconds = int(input("Nhập số giây: "))
days = seconds // 86400
seconds = seconds - (days * 86400)
hours = seconds // 3600
seconds = seconds - (hours * 3600)
minutes = seconds // 60
seconds = seconds - (minutes * 60)

#  C2
# days = seconds // 86400
# seconds = seconds%86400
# hours = seconds // 3600
# seconds = seconds % 3600
# minutes = seconds//60
# seconds = seconds%60

print(f"{days} ngay, {hours} gio, {minutes} phut, {seconds} giay")
