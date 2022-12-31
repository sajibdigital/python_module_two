#--------- Module One Recap--------

# 01- Use of print commend

print('Jalanta Khalil')



# 02- variable and use of seperator

name = 'Jalanta Khalil'
age = 45
is_nayok = True
print(name, age, is_nayok, sep="---")


# 03--- Checking data type

print(type(name))
print(type(age))
print(type(is_nayok))


egg_price = 13.50
print(egg_price)

print(type(egg_price))


# 04----Changing Datatype

text = 'His name is' +name + 'his age is ' + str(age)

print(text)


# 05--- Use of User input---and change input datatype

price = int(input('Enter egg Price: '))
quantity = 20
total = price * quantity

print(total)