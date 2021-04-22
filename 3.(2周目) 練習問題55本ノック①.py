# 練習問題55本ノック(2周目)①
## 2021/04/22

## 出題元(https://gotutiyan.hatenablog.com/entry/2020/04/14/174007)
## こちらに記載してあるものは、すべて「解答部分のみ」になります


# 1.
x = 2
print(x * 3)    #値を3倍にして出力

#　2.
a = 100
b = 200
a, b = b, a     #値を入れ替え
print(a, b)

# 3.
a = 10
b = 2
print(a + b, a - b, a * b, a / b)   #和，差，積，商を出力

# 4.
a = 5
b = 3
print(a % b)    #余りを出力

# 5.
a = 5
b = 10
print(a ** b)   #aのb乗を出力

# 6.
a = 5
b = 10
if a < b:       #もしaよりbが大きければ
    print(b)    #bの値を出力
else:           #そうでなければ
    print(a)    #aの値を出力

# 7.
a = 5
if a % 2 == 0:    #aを2で割った余りが0なら偶数
    print(True)   #偶数なら出力
else:             #そうでなければ
    print(False)  #(奇数なら)出力

# 8.
s = "python"
print(s[2])     #2番目の文字を出力(先頭が0番)

# 9.
a = "py"
b = "thon"
print(a + b)    #aとbを結合して出力

# 10.
a = 5
b = 3
print("{}%{}=2".format(a,b))    #{}内に当てはめて出力

# 11.
s = "some1"
print(s.replace('1', 'one'))    #文字を置き換えて出力

# 12.
s = "This Is A Sentence ."
print(s.lower())    #小文字に変換して出力

# 13.
s = "This Is A Sentence ."
print(s.upper())    #大文字に変換して出力

# 14.
s = "How many characters?"
print(len(s))   #文字数を出力

# 15.
a = "34"
b = "43"
print(int(a) + int(b))  #文字列を数値に変換し和を出力

# 16.
li = [1,2,3,4,5]
print(li[3])    #リストの3番目の要素を出力(先頭が0番)

# 17.
li1 = [1,2,3]
li2 = [4,5]
li1.extend(li2)     #li1にli2を結合
print(li1)

# 18.
li = [1,2,3,4,5]
li.append(6)    #末尾に6を追加
li.append(7)    #末尾に7を追加
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
