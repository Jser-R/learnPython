
# --------------布尔值---------------------

# and 运算符
print(True and False)  # False
print(True and True)   # True
print(False and False)  # False

# or 运算符
print(True or False)    # True
print(True or True)     # True
print(False or False)   # False

# not 运算符
print(not True)     # False
print(not False)    # True


# 空值 用None表示
print(None)

# ----------变量---------------------
# 动态语言 变量本身类型不固定
a = 123
print(a)    # a为int类型
a = '123'
print(a)    # a为字符串类型
a = True
print(a)    # a为布尔值

b = a
a = '456'
print(b)    # True
