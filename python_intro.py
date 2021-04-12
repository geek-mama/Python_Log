# コメントを変更しました
if 3 > 2:
    print("Hello!")


# 数値を変更しました
if 7 > 5:
    print('7 is indeed greater than 5')
else:
    print('7 is not greater than 5')


# 名前を変更しました
name = 'Ichikawa'
if name == 'Rie':
    print('Hey Rie!')
elif name == 'Ichikawa':
    print('Hey Ichikawa!')
else:
    print('Hey anonymous!')


# 数値を変更しました
volume = 34
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")


# 数値を変更しました
# ボリュームが大きすぎたり小さすぎたりしたら変更する
if volume < 20 or volume > 80:
    volume = 34
    print("That's better!")


#
def hi():
    print('Hi there!')
    print('How are you?')
hi()


# 名前を変更しました
def hi(name):
    if name == 'Rie':
        print('Hi Rie!')
    elif name == 'Ichikawa':
        print('Hi Ichikawa!')
    else:
        print('Hi anonymous!')
hi("Rie")


# 名前を変更しました
def hi(name):
    print('Hi ' + name + '!')
hi("Ichikawa")


#
def hi(name):
    print('Hi ' + name + '!')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')


#　数値を変更しました
for i in range(1, 8):
    print(i)