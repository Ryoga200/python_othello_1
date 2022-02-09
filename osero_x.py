import tkinter
import pyautogui as pag

root=tkinter.Tk()
canvas=tkinter.Canvas(root,width=1210,height=1730)
root.title("オセロ")
for i in range(8):
    for j in range(8):
        canvas.create_rectangle(10+150*i,10+150*j,160+150*i,160+150*j,fill="white",outline="black",width=3)

mouse_x = 0
mouse_y = 0
mouse_c = 0
koma=["","●","○"]
check=([0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,1,2,0,0,0,0],
       [0,0,0,0,2,1,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],)
direction=([0,0,0],#ひっくり返す方向を記録する
           [0,0,0],
           [0,0,0])
mark=check

def mouse_move(e):
    global mouse_x, mouse_y#キャンバスでの座標
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global masu_x,masu_y#指定されたマス目について
    global player
    global opponent
    global skip
    skip=0
    masu_x=int((e.x-10)/150)+1
    masu_y=int((e.y-10)/150)+1
    #print(check[masu_y][masu_x])
    isput=0#駒を置けるか調べる変数
    if(masu_x>=masu_y):#ななめ方向にひっくり返すときに用いる
        leftup=masu_y
        rightdown=8-masu_x
    else:
        leftup=masu_x
        rightdown=8-masu_y
    if(masu_x>=8-masu_y):
        leftdown=8-masu_y
        rightup=8-masu_x
    else:
        leftdown=masu_x
        rightup=masu_y
    
    if(check[masu_y][masu_x]==0):
        isputa=0#駒を置けるか調べる変数
        for i in range(masu_x+1,9,1):
            isputa=isablerev(i,masu_y,isputa)
            if(isputa==2):
                direction[1][2]=1
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        for i in range(masu_x-1,0,-1):
            isputa=isablerev(i,masu_y,isputa)
            if(isputa==2):
                direction[1][0]=1
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        for i in range(masu_y+1,9,1):
            isputa=isablerev(masu_x,i,isputa)
            if(isputa==2):
                direction[2][1]=1
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        for i in range(masu_y-1,0,-1):
            isputa=isablerev(masu_x,i,isputa)
            #print(isputa)
            if(isputa==2):
                direction[0][1]=1
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        if(leftup>0):
            for i in range(1,leftup,1):
                isputa=isablerev(masu_x-i,masu_y-i,isputa)
                if(isputa==2):
                    direction[0][0]=1
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
        if(rightdown<8):
            for i in range(1,rightdown,1):
                isputa=isablerev(masu_x+i,masu_y+i,isputa)
                if(isputa==2):
                    direction[2][2]=1
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
        if(rightup>0):
            #print("aafjd")
            for i in range(1,rightup,1):
                isputa=isablerev(masu_x+i,masu_y-i,isputa)
                if(isputa==2):
                    direction[0][2]=1
                    isput=isput+1
                    #print("isputa"+str(isputa))
                    break
                if(isputa==3):
                    break
        isputa=0
        if(leftdown>0):
            for i in range(1,leftdown,1):
                isputa=isablerev(masu_x-i,masu_y+i,isputa)
                if(isputa==2):
                    direction[2][0]=1
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
            
    if(isput>0):
        revable=0
        if(direction[1][2]==1):
            for i in range(masu_x,8,1):
                revable,check[masu_y][i]=reverse(i,masu_y,revable)
                if(revable==2):
                    break
        revable=0
        if(direction[1][0]==1):
            for i in range(masu_x,0,-1):
                revable,check[masu_y][i]=reverse(i,masu_y,revable)
                if(revable==2):
                    break
        revable=0
        if(direction[2][1]==1):
            for i in range(masu_y,8,1):
                #print(revable)
                revable,check[i][masu_x]=reverse(masu_x,i,revable)
                #print("checkis"+str(check[4][2]))
                #print("abcd")
                #print(i)
                if(revable==2):
                    #print("break")
                    break
        revable=0
        if(direction[0][1]==1):
            for i in range(masu_y,0,-1):
                revable,check[i][masu_x]=reverse(masu_x,i,revable)
                if(revable==2):
                    break
        revable=0
        if(direction[0][0]==1):
            #print("ac")
            for i in range(0,leftup,1):
                revable,check[masu_y-i][masu_x-i]=reverse(masu_x-i,masu_y-i,revable)
                if(revable==2):
                    break
        revable=0
        if(direction[2][2]==1):
            for i in range(0,rightdown,1):
                revable,check[masu_y+i][masu_x+i]=reverse(masu_x+i,masu_y+i,revable)
                if(revable==2):
                    break
        revable=0
        if(direction[0][2]==1):
            for i in range(0,rightup,1):
                revable,check[masu_y-i][masu_x+i]=reverse(masu_x+i,masu_y-i,revable)
                if(revable==2):
                    break
        revable=0
        if(direction[2][0]==1):
            for i in range(0,leftdown,1):
                revable,check[masu_y+i][masu_x-i]=reverse(masu_x-i,masu_y+i,revable)
                if(revable==2):
                    break
        #print("beforeplayer"+str(player)+str(opponent))
        change()
        #print("afterplayer"+str(player)+str(opponent))
        for i in range(0,3,1):
            for j in range (0,3,1):
                direction[i][j]=0
        #for i in range(0,8,1):
            #for j in range (0,8,1):
                #print(check[i][j], end='')
            #print("\n")
def isableput():
    isputb=0
    for a in range(1,9,1):
        for b in range(1,9,1):
            #print(check[a][b])
            isput=0#駒を置けるか調べる変数
            if(b>=a):#ななめ方向にひっくり返すときに用いる
                leftup=a
                rightdown=8-b
            else:
                leftup=b
                rightdown=8-a
            if(b>=8-a):
                leftdown=8-a
                rightup=8-b
            else:
                leftdown=b
                rightup=a
    
            if(check[a][b]==0):
                isputa=0#駒を置けるか調べる変数
                for i in range(b+1,9,1):
                    isputa=isablerev(i,a,isputa)
                    if(isputa==2):
                        direction[1][2]=1
                        isput=isput+1
                        break
                    if(isputa==3):
                        break
                isputa=0
                for i in range(b-1,0,-1):
                    isputa=isablerev(i,a,isputa)
                    if(isputa==2):
                        direction[1][0]=1
                        isput=isput+1
                        break
                    if(isputa==3):
                        break
                isputa=0
                for i in range(a+1,9,1):
                    isputa=isablerev(b,i,isputa)
                    if(isputa==2):
                        direction[2][1]=1
                        isput=isput+1
                        break
                    if(isputa==3):
                        break
                isputa=0
                for i in range(a,0,-1):
                    isputa=isablerev(b,i,isputa)
                    #print(isputa)
                    if(isputa==2):
                        direction[0][1]=1
                        isput=isput+1
                        break
                    if(isputa==3):
                        break
                isputa=0
                if(leftup>0):
                    for i in range(1,leftup,1):
                        isputa=isablerev(b-i,a-i,isputa)
                        if(isputa==2):
                            direction[0][0]=1
                            isput=isput+1
                            break
                        if(isputa==3):
                            break
                isputa=0
                if(rightdown<8):
                    for i in range(1,rightdown,1):
                        isputa=isablerev(b+i,b+i,isputa)
                        if(isputa==2):
                            direction[2][2]=1
                            isput=isput+1
                            break
                        if(isputa==3):
                            break
                isputa=0
                if(rightup>0):
                    #print("aafjd")
                    for i in range(1,rightup,1):
                        isputa=isablerev(b+i,a-i,isputa)
                        if(isputa==2):
                            direction[0][2]=1
                            isput=isput+1
                            #print("isputa"+str(isputa))
                            break
                        if(isputa==3):
                            break
                isputa=0
                if(leftdown>0):
                    for i in range(1,leftdown,1):
                        isputa=isablerev(b-i,a+i,isputa)
                        if(isputa==2):
                            direction[2][0]=1
                            isput=isput+1
                            break
                        if(isputa==3):
                            break
                isputa=0
                if(isput>0):
                    isputb=isputb+1
    return isputb
    
def game_main():
    fnt = ("Times New Roman", 30)
    if(player==1):
        txt = "黒の番です"
    if(player==2):
        txt="白の番です"
    
    canvas.delete("TEXT")
    canvas.create_text(300, 1300, text=txt, fill="black", font=fnt, tag="TEXT")
    canvas.delete("koma")
    oku()
    root.after(1000, game_main)
def change():
    global skip,player,opponent
    tmp=player
    player=opponent
    opponent=tmp
    skip=skip+1
    if(skip>=2):
        print("intheend")
        finaldeal()
    else:
        if(isableput()==0):
            change()
def finaldeal():
    sum_white=0
    sum_black=0
    fnt = ("Times New Roman", 30)
    for a in range(1,9,1):
        for b in range(1,9,1):
            if(check[b][a]==1):
                sum_black=sum_black+1
            elif(check[b][a]==2):
                sum_white=sum_white+1
    canvas.delete("TEXT")
    canvas.create_text(300, 1400, text=str(sum_black)+"ー"+str(sum_white), fill="black", font=fnt, tag="Win")
    if(sum_black>sum_white):
        canvas.create_text(300, 1500, text="黒の勝ちです", fill="black", font=fnt, tag="Winner")
    if(sum_black<sum_white):
        canvas.create_text(300, 1500, text="白の勝ちです", fill="black", font=fnt, tag="Winner")
    if(sum_black==sum_white):
        canvas.create_text(300, 1500, text="ひきわけです", fill="black", font=fnt, tag="Winner")
    print("oi")
def oku():
    for a in range(1,9,1):
        for b in range(1,9,1):
            canvas.create_text(-70+150*b,-70+150*a,text=koma[check[a][b]],font=("Hleventica",50),tag="koma")
def isablerev(x,y,isputa):
    #print("xis"+str(x)+"yis"+str(y))
    if(check[y][x]==opponent):
        #print("num")
        isputa=1
    if(check[y][x]==player and isputa==1):
        #print("player is "+str(player))
        isputa=2
    if(check[y][x]==player and isputa==0):
        isputa=3
    if(check[y][x]==0):
        isputa=3
    return isputa
def reverse(x,y,revable):
    tmp=check[y][x]
    if(check[y][x]==opponent or check[y][x]==0):
        tmp=player
        revable=1
    if(check[y][x]==player and revable==1):
        revable=2
    #print("yis"+str(y)+"xis"+str(x)+"checkisa"+str(check[4][2]))
    return revable,tmp
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
global player#プレイヤーがどちらか示す。
player=1
global opponent#相手
opponent=2
global error#エラーであるか示す
global revable#ひっくり返せるか調べる変数
global skip#パスした回数
skip=0
game_main()
canvas.pack()
root.mainloop()
