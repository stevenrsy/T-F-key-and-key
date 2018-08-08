import time
import sys
import random
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title('《 T F》 ！！！')
theLabel = tk.Label(root, text = 'well come!')
theLabel.pack()
mainloop()
class App:
    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame, text = '开启--OPEN', bg = 'yellow', fg = 'black', command = self.say_hi)
        self.hi_there.pack(side = tk.LEFT)
    def say_hi(self):
        print('加载中……')
        for x in range(100):
            print(str(x+1) + '%')
            time.sleep(int(0.9))
        root = tk.Tk()
        root.title('《 T F》 ！！！')
        theLabel = tk.Label(root, text = '加载完毕，请将除shell和代码以外的所有Python窗口关闭！')
        theLabel.pack()
        root.mainloop()
root = tk.Tk()
app = App(root)
root.mainloop()
time.sleep(1)
root = tk.Tk()
root.title('《 T F》 ！！！')
theLabel = tk.Label(root, text = '请向商家索要生成码！')
theLabel.pack()
root.mainloop()
time.sleep(1)
print('')
print('')
print('')
print('')
print('')
print('你好')
time.sleep(1)
print('欢迎打开《 T F》幸运密码生成器，生成你意想不到的代码！')
time.sleep(1)
print('结尾有彩蛋哦哦！')
time.sleep(1)
print('请输入生成码')
print('…………')
time.sleep(1)
key = input()
print('…………')
print('加载中……')
time.sleep(3)
if (len(str(key)) == 10) and (key == '05360fgtyK'):
    print('OK')
    time.sleep(1)
else:
    print('错误，请再输一遍')
    key = input()
    if (len(str(key)) == 10) and (key == '05360fgtyK'):
        print('OK')
    else:
        print('错误，请再输一遍！如需前五位的提示请回答“YTS”。')
        key = input()
        if (len(str(key)) == 10) and (key == '05360fgtyK'):
            print('OK')
        else:
            if (key == 'YTS'):
                print('前五位都是数字！值不超过70000，不小于00002。')
                for g in range(1,6):
                    print('猜一猜')
                    guss = int(input())
                    if guss < int('05360'):
                        print('太低了')
                    elif guss > int('05360'):
                        print('太高了')
                    else:
                        break
                if guss == int('05360'):
                    print('对了前五位就是05360！')
                else:
                    print('次数用完了，再好好想想生成码！')
                key = input()
                if (len(str(key)) == 10) and (key == '05360fgtyK'):
                    print('OK')
            else:
                print('错误!')
                root = tk.Tk()
                root.title('mirror！！！')
                theLabel = tk.Label(root, text = 'mirror！ mirror！！ mirror！！！忽略点Ⅹ')
                theLabel.pack()
                root.mainloop()
                for i in range(10):
                    print('系统即将关闭' + str(i+1))
                    time.sleep(1)
                root = tk.Tk()
                root.title('mirror！！！')
                theLabel = tk.Label(root, text = 'mirror！ mirror！！ mirror！！！忽略点Ⅹ')
                theLabel.pack()
                root.mainloop()
                while True:
                    print('mirrror!!!')
for s in range(16):
    print(random.randint(1,9),end='')
    time.sleep(1)
print(' ')
print('密码已生成。')
print('是否生成16位英文密码？(回答“T”，或“F”）')
TF = input()
if (str(TF) == 'T'):
    print('生成中……')
    time.sleep(3)
    ad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','_']
    for d in range(16):
        print(ad[random.randint(0,25)],end='')
        time.sleep(1)
    print(' ')
    time.sleep(3)
    print('密码已生成！')
    time.sleep(5)
    print('是否生成16位含自己信息密码？(回答“T”，或“F”）')
    TF2 = input()
    if (str(TF2) == 'T'):
        print('以下问题的答案必须由一个字母或数字组成，否则密码将长于16位，关键字于密码中的第4,8,12，16位。')
        print('请输入关键数字！  第一位： ')
        important1 = input()
        print('请输入关键数字！  第二位： ')
        important2 = input()
        print('请输入关键数字！  第三位： ')
        important3 = input()
        print('请输入关键数字！  第四位： ')
        important4 = input()
        print('生成中……')
        time.sleep(3)
        for f in range(4):
            for d in range(3):
                print(ad[random.randint(0,35)],end='')
                time.sleep(1)
            print(str(important1),end='')
            time.sleep(1)
            important1 = important2
            important2 = important3
            important3 = important4
        print('   ')
        time.sleep(3)
        for f in range(3):
            print('谢谢使用，系统即将关闭' + str(f+1))
            time.sleep(1)
        print('再见！！！')
        time.sleep(1)
        root = tk.Tk()
        root.title('附加100位随机密码，彩蛋')
        ad1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','_']
        theLabel = tk.Label(root, text = ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)] + ad1[random.randint(0,35)])
        theLabel.pack()
        root.mainloop()
        sys.exit()
    else:
        for f in range(3):
            print('谢谢使用，系统即将关闭' + str(f+1))
            time.sleep(1)
        print('再见！！！')
        time.sleep(1)
        root = tk.Tk()
        root.title('附加100位suiji密码 哈哈')
        ad2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','_']
        theLabel = tk.Label(root, text = ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)] + ad2[random.randint(0,35)])
        theLabel.pack()
        root.mainloop()
        sys.exit()
else:
    for f in range(3):
        print('谢谢使用，系统即将关闭' + str(f+1))
        time.sleep(1)
    print('再见！！！')
    time.sleep(1)
    root = tk.Tk()
    root.title('附加100位随机密码（开个玩笑的）')
    ad3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','_']
    theLabel = tk.Label(root, text = ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)] + ad3[random.randint(0,35)])
    theLabel.pack()
    root.mainloop()


