# -------------------list 列表----------
arr = [1, 2, 3]
print(len(arr))   # 3
print(arr[0], arr[1], arr[2])   # 1 2 3
print(arr[-1])  # 3
# 插入元素到指定位置
arr.insert(0, 4)
print(arr)  # [4, 1, 2, 3]
# 追加元素到末尾
arr.append(5)
print(arr)  # [4, 1, 2, 3, 5]
# 删除末尾元素
arr.pop()
print(arr)  # [4, 1, 2, 3]
# 删除指定位置元素
arr.pop(0)
print(arr)  # [1, 2, 3]

# --------------tuple 元组------------
# tuple 初始化后不能修改
tupleArr = (0, 1, 2, ['a', 'b'])
print(tupleArr)  # (0, 1, 2, ['a', 'b'])
tupleArr[3][0] = 'c'
# 即指向不变 但是指向的这个list本身是可变的
print(tupleArr)     # (0, 1, 2, ['c', 'b'])




# 和dict比较
# 特点：
#     1.查找和插入的时间随着元素的增加而增加
#     2.占用空间小，浪费内存少


