deposit = float(input("Deposit: "'\033[1m'))
after1year = deposit/100*105
after2year = deposit/100**2*105**2
after10year = deposit/100**10*105**10
print('\033[0m'+f"{after1year}")
print(after2year)
print(after10year)