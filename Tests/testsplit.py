# working on replacing the singular didget with a 0 in front for correct directory ordering

x = "Example12\B06_00_5_37_142467.jpg"
print(x)
y = x.replace("_5", "_05")
# y = x.split('_')[2]

# print(y)

if len(y) <= 1:
#     # print('adding 0 before singular digit')
    y = x.replace('_5', '_05')

# print(x)
print(y)
# print(f"{int(y):02}")
# print(a)
# print(f"{a:02}")
