str = "My name is kim kyeongtak"

# 1.
print(len(str))

# 2.
for i in range(0, 10):
    print(f"{i + 1} => {str}")

# 3.
print(str[0])

# 4.
print(str[:4])

# 5.
print(str[len(str)-4:])

# 6.
print(str[::-1])

# 7.
print(str[1:len(str)-1])

# 8.
print(str.upper())

# 9.
print(str.lower())

# 10.
temp = str.replace('a', 'e')
print(temp)