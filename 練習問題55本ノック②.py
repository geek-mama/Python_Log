# 6.
a = 5
b = 10
if a < b:
    print(b)
else:
    print(a)

# 7.
a = 5
if a % 2 == 0:
    print(True)
else:
    print(False)

# 8.
a = "python"
print(a[2])

# 9.
a = "py"
b = "thon"
print(a + b)

# 10.
a = 5
b = 3
print("{}%{}=2".format(a,b))

# 11.
a = "some1"
print(a.replace("1", "one"))

# 12.
a = "This Is A Sentence ."
print(a.lower())

# 13.
a = "This Is A Sentence ."
print(a.upper())

# 14.
a = "How many characters?"
print(len(a))

# 15.
a = "34"
b = "43"
print(int(a) + int(b))

# 16.
ary = [1,2,3,4,5]
print(ary[3])

# 17.
li1 = [1,2,3]
li2 = [4,5]
li1.extend(li2)
print(li1)

# 18.
li = [1,2,3,4,5]
li.append(6)
li.append(7)
print(li)

# 19.
li = [1,2,3,4,5]
li.insert(1, 100)
print(li)

# 20.
li = [1,2,3,4,5]
for i in li:
    if i % 2 == 0:
        print(i)

# 21.★
li = [1,2,3,4,5]
for i, name in enumerate(li):
    if i % 2 == 0:
        print(name)

# 22.
li = [11,22,33,44,55,66]
print(len(li))

# 23.
li = [11,22,33,44,55,66]
print(44 in li)

# 24.★
li = [1,2,3,4,5]
tup = (li[0], li[-1])
print(tup)

# 25.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(dic)

# 26.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(list(dic.keys()))

# 27.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(list(dic.values()))

# 28.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
li = list(dic.items())
print(li)

# 29.★
d = {'apple':10, 'grape':20, 'orange':30}
d['apple'] = d.get('apple', -1)
d['pineapple'] = d.get('pineapple', -1)
print(d)

# 30.
s = "training"
print(s[1:5])

# 31.
s = "understand"
print(s[1::2])

# 32.
li = [1,2,3,4,5]
print(li[::-1])

# 33.
li = [1,1,2,3,3,4,5]
print(set(li))

# 34.
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 & set2)

# 35.
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.update(set2)
print(set1)

# 36.
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 - set2)

# 37.
data1 = {'A':1, 'B':2}
data2 = "hoge"
data3 = {1,2,3,4,5}
print(type(data1),type(data2),type(data3))

# 38.
s = "This is sentence .\n"
print(s.rstrip())

# 39.
s = "C C++ // python java"
print(s.split())
print(s.split("/"))

# 40.
s = ['This', 'is', 'a', 'sentence']
print(" ".join(s))

# 41.
li = [11,2,7,13,5]
print(max(li))

# 42.
li = [11,2,7,13,5]
print(min(li))

# 43.
li = [11,2,7,13,5]
print(sum(li))

# 44.
li = [5,3,1,4,2]
li.sort()
print(li)

# 45.★
li = [{'a': 6, 'b': 7, 'c': 6},
      {'a': 4, 'b': 2, 'c': 3},
      {'a': 1, 'b': 5, 'c': 8}]
sorted_li = sorted(li, reverse=True, key=lambda x:x['b'])
print(sorted_li)

# 46.
li = list(range(0,100))
print(li)

# 47.★
li = [5,4,3,2,1]
ans_li = [idx + elem for idx, elem in enumerate(li)]
print(ans_li)

# 48.
a = 0
b = 5
try:
    print(a / b)
except ZeroDivisionError:
    print("zero division")
try:
    print(b / a)
except ZeroDivisionError:
    print("zero division")

# 49.
a = 10
b = 5
print(a|b, a&b, a^b)

# 50.★
import math
theta = math.pi / 2
ans = math.sin(theta)**2 + math.cos(theta)**2
print(ans)

# 演習1 ★
li1 = list(range(1, 32))
li2 = list(range(1, 13))
counter = 0
for elem1 in li1:
    for elem2 in li2:
        if elem1%10 == elem2%10:
            counter += 1
print(counter)

# 演習2 ★
dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}
items_list = list(dic.items())
sorted_items_list = sorted(items_list, key=lambda x:x[1])
ans = [elem[0] for elem in sorted_items_list]
print(ans)

# 演習3 ★
nums = [1,2,4,3,2,1,5,1]
num2freq = {}
for num in nums:
    num2freq[num] = num2freq.get(num, 0) + 1
print(num2freq)

# 演習4 ★
doc = 'i bought an apple .\ni ate it .\nit is delicious .'
word2freq = {}
sents = doc.split('\n')
for sent in sents:
    words = sent.split()
    for word in words:
        word2freq[word] = word2freq.get(word, 0) + 1
print(word2freq)

# 演習5 ★
list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]
A = set(list1)
B = set(list2)
inter_set = A.intersection(B)
union_set = A.union(B)
print(len(inter_set) / len(union_set))