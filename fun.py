a = "Hii Guys %%% 5666"
z = []

for i in a:
    if i.isalnum():
        z.append(i)
    elif i == " ":
        z.append('_')
    elif i == "|":
        z.append('-')
    else:
        z.append('_')

print(''.join(z))