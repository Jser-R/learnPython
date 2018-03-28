
# ----------------dict 字典------------------
person = {
    'name': 'Jay',
    'age': 18,
    'job': 'manager'
}
print(person['job'])

# 通过 in 判断key值是否存在
print('aaa' in person)  # False

# 通过 get() 方法 如果key值不存在 返回None 或者指定的值
print(person.get('country'))    # None
print(person.get('country', 'China'))   # China
print(person)   # {'name': 'Jay', 'age': 18, 'job': 'manager'}

# 删除字典中的元素
person.pop('job')
print(person)   # {'name': 'Jay', 'age': 18}


# 和list比较
# 特点：
#     1.查找和插入的速度极快，不会随着key的增加而变慢
#     2.需要占用大量的内存


# -------------set ------------------------
# set 和dict类似 也是一组key的集合 但是不存储value
setObj = set(list(range(5)))
print(setObj)   # {0, 1, 2, 3, 4}

# 添加元素到set
setObj.add(6)
print(setObj)   # {0, 1, 2, 3, 4, 6}

# 删除元素
setObj.remove(4)
print(setObj)   # {0, 1, 2, 3, 6}

