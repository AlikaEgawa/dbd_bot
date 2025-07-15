import pyautogui as gui
import sys
import time
import random

def awsd():
    return random.choice(["a", "w", "s", "d"])

def jl():
    return random.choice(["j", "l"])

def move(dir):
    print("move")
    time.sleep(0.5)
    gui.keyDown(dir)
    time.sleep(1.5)
    gui.keyUp(dir)

def turn(dir):
    print("turn")
    time.sleep(0.5)
    gui.keyDown(dir)
    time.sleep(0.5)
    gui.keyUp(dir)
    time.sleep(0.5)

def swing(n):
    print("attach")
    cnt = 0
    while cnt < n:
        time.sleep(0.5)
        gui.click()
        time.sleep(3)
        cnt += 1

def abil(n):
    print("ability")
    cnt = 0
    while cnt < n:
        time.sleep(0.5)
        gui.mouseDown(button='right')
        time.sleep(0.5)
        gui.mouseUp(button='right')
        time.sleep(1)
        gui.mouseDown(button='left')
        time.sleep(1)
        gui.mouseUp(button='left')
        time.sleep(0.5)
        cnt += 1

def jump():
    print("jump")
    gui.keyDown("m")
    time.sleep(3)
    gui.keyUp("m")


#起動準備
print('dbdをアクティブ状態にしてください')
time.sleep(5)

#下記処理を1万回繰り返す
cnt1 = 0
while True:
    print("waiting match start......")
    if cnt1 == 0:
        time.sleep(1)
    else:
        time.sleep(5)
    o = 0
    while o<5:
        gui.moveTo(1735, 955)
        gui.click(1735, 955, button="left")
        time.sleep(3)

    # リザルト抜け
        gui.moveTo(1767, 1020)
        gui.click(1767, 1020, button="left")
        time.sleep(3)
        o += 1


    print("match making delaying")
    time.sleep(10)

# main loop
    i = 0
    while i <5:
        print(i)

        turn(jl())

        jump()
        move(awsd())
        jump()
        jump()
        swing(3)
        jump()
        abil(2)

        jump()
        move(awsd())
        jump()
        jump()
        swing(3)
        jump()
        abil(2)

        i += 1

#繰り返しここまで




# リザルト抜け
# 座標(x=1767, y=863)に移動
    gui.moveTo(1767, 1020)
#続けるボタンクリックで(x=1767, y=1014)左クリックを1回） 
    gui.click(1767, 1020, button="left")



#エラー画面対応ーーーーーーーーーーーー
# 座標Point(x=1481, y=579)に移動
    gui.moveTo(1481, 579)
# #エラーokボタンクリック（座標(x=1481, y=579)で左クリックを1回）
    gui.click(1481, 579, button="left")
    time.sleep(2)
#ーーーーーーーーーーーーーーーーーーーーーー


    cnt1 += 1
#ここの10000を大きくする程処理を繰り返します
    if cnt1 >= 10000:
        break
