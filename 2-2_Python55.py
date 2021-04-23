# 練習問題55本ノック(2周目)②
## 2021/04/23

## 出題元(https://gotutiyan.hatenablog.com/entry/2020/04/14/174007)
## こちらに記載してあるものは、すべて「解答部分のみ」になります


# 21.
li = [1,2,3,4,5]
for i, name in enumerate(li):   #添え字を取得
    if i % 2 == 0:              #もし、添え字が偶数なら
        print(name)             #要素を出力

# 22.
li = [11,22,33,44,55,66]
print(len(li))      #リストの長さを出力

# 23.
li = [11,22,33,44,55,66]
if 44 in li:        #リストの中に値が存在するか
    print(True)
else:
    print(False)

# 24.
li = [1,2,3,4,5]
t = (li[0], li[-1])     #先頭と末尾をタプルに格納
print(t)

# 25.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(dic)

# 26.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(list(dic.keys()))     #キーを要素としたリストを作成

# 27.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(list(dic.values()))   #値を要素としたリストを作成

# 28.
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
item = list(dic.items())    #要素のリストを作成
print(item)
##　https://qiita.com/6ONsNMCaB3FzaKa/items/ca1107f7e26b61a6ec6e

# 29.
d = {'apple':10, 'grape':20, 'orange':30}
d['apple'] = d.get('apple', -1)         #キーが存在しない場合は追加
d['pineapple'] = d.get('pineapple', -1) #キーが存在しない場合は追加
print(d)
## https://note.nkmk.me/python-dict-get/

# 30.
s = "training"
print(s[1:5])   #1～4番目を取り出して出力