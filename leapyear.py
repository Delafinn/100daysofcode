
year = int(input("Which year do you want to check? "))

if int(year) % 4:
  print("not a leap year")
elif int(year) % 100:
  print("leap year")
elif int(year) % 400:
  print("not a leap year.")
else:
  print("leap year.")
