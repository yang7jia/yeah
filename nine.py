#31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
#extend可以将另一个集合中的元素逐一添加到列表中，区别于append整体添加
list1=[1,5,7,9]
list2=[2,2,6,8]

list1.extend(list2)
print(list1)

list1.sort(reverse=False)
print(list1)