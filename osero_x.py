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
koma=["","●","○","★","☆","×"]
check=([5,5,5,5,5,5,5,5,5,5],
       [5,0,0,0,0,0,0,0,0,5],
       [5,0,0,0,0,0,0,0,0,5],
       [5,0,0,0,0,0,0,0,0,5],
       [5,0,0,0,1,2,0,0,0,5],
       [5,0,0,0,2,1,0,0,0,5],
       [5,0,0,0,0,0,0,0,0,5],
       [5,0,0,0,0,0,0,0,0,5],
       [5,0,0,0,0,0,0,0,0,5],
       [5,5,5,5,5,5,5,5,5,5],)
"""mark
2 3 5
    7 C 11
    13 17 19
    """   
mark=([5,5,5,5,5,5,5,5,5,5],
      [5,1,1,1,1,1,0,0,0,5],
      [5,0,1,2,1,2,0,0,0,5],
      [5,0,0,0,0,0,0,0,0,5],
      [5,0,0,0,0,0,0,0,0,5],
      [5,0,0,0,0,0,0,0,0,5],
      [5,0,0,0,0,0,0,0,0,5],
      [5,0,0,0,0,0,0,0,0,5],
      [5,0,0,0,0,0,0,0,0,5],
      [5,5,5,5,5,5,5,5,5,5],)
def mouse_move(e):
    global mouse_x, mouse_y#キャンバスでの座標
    mouse_x = e.x
    mouse_y = e.y
def mouse_press(e):
    global frag
    global masu_x,masu_y#指定されたマス目について
    global player
    global opponent
    global skip
    skip=0
    masu_x=int((e.x-10)/150)+1
    masu_y=int((e.y-10)/150)+1
    if(check[masu_y][masu_x]==player+2):
        canvas.delete("error")
        check[masu_y][masu_x]=player
        reverse()
        change()
    else:
        fnt = ("Times New Roman", 20)
        if(frag==0):
            canvas.create_text(850, 1300, text="そこには置けません", fill="black", font=fnt, tag="error")
    
def reverse():
    global masu_x,masu_y#指定されたマス目について
    global player
    global opponent
    global skip
    skip=0
    i=1
    if(mark[masu_y][masu_x]%2==0):
        while(check[masu_y-i][masu_x-i]==opponent):
            check[masu_y-i][masu_x-i]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%3==0):
        while(check[masu_y-i][masu_x]==opponent):
            check[masu_y-i][masu_x]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%5==0):
        while(check[masu_y-i][masu_x+i]==opponent):
            check[masu_y-i][masu_x+i]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%7==0):
        while(check[masu_y][masu_x-i]==opponent):
            check[masu_y][masu_x-i]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%11==0):
        while(check[masu_y][masu_x+i]==opponent):
            check[masu_y][masu_x+i]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%13==0):
        while(check[masu_y+i][masu_x-i]==opponent):
            check[masu_y+i][masu_x-i]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%17==0):
        while(check[masu_y+i][masu_x]==opponent):
            check[masu_y+i][masu_x]=player
            i=i+1
    i=1
    if(mark[masu_y][masu_x]%19==0):
        while(check[masu_y+i][masu_x+i]==opponent):
            check[masu_y+i][masu_x+i]=player
            i=i+1
    
def isablerev(x,y,isputa):
    global player
    global opponent
    if(check[y][x]==opponent):
        isputa=1
    if(check[y][x]==player and isputa==1):
        isputa=2
    if(check[y][x]==player and isputa==0):
        isputa=3
    if(check[y][x]==0 or check[y][x]==3 or check[y][x]==4):
        isputa=3
    return isputa   
def isableput():
    for a in range(1,9,1):
        for b in range(1,9,1):
            mark[b][a]=1
            if(check[b][a]==3 or check[b][a]==4):
                check[b][a]=0
    for a in range(1,9,1):
        for b in range(1,9,1):              
            one_put(a,b)
            if(check[b][a]!=1 and check[b][a]!=2 and mark[b][a]>1):
                check[b][a]=player+2
    for i in range(1,9,1):
        for j in range(1,9,1):
            """if(mark[i][j]==1 or mark[i][j]==2 or mark[i][j]==3 or mark[i][j]==5 or mark[i][j]==7):
                print(mark[i][j],end='')
            elif(mark[i][j]==11):
                print("A",end='')
            elif(mark[i][j]==13):
                print("B",end='')
            elif(mark[i][j]==17):
                print("C",end='')
            elif(mark[i][j]==19):
                print("D",end='')
        print("\n")
    print("-----------")"""
def one_put(a,b):
    isput=0
    if(check[b][a]==0):
        isputa=0#駒を置けるか調べる変数
        for i in range(b+1,9,1):#下
            if(check[i][a]==5):
                break
            isputa=isablerev(a,i,isputa)
            if(isputa==2):
                mark[b][a]=mark[b][a]*17
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        for i in range(b-1,0,-1):#上
            if(check[i][a]==5):
                break
            isputa=isablerev(a,i,isputa)
            if(isputa==2):
                mark[b][a]=mark[b][a]*3
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        for i in range(a+1,9,1):#右
            if(check[b][i]==5):
                break
            isputa=isablerev(i,b,isputa)
            if(isputa==2):
                mark[b][a]=mark[b][a]*11
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        for i in range(a-1,0,-1):#左
            if(check[b][i]==5):
                break
            isputa=isablerev(i,b,isputa)
            #print(isputa)
            if(isputa==2):
                mark[b][a]=mark[b][a]*7
                isput=isput+1
                break
            if(isputa==3):
                break
        isputa=0
        if(check[b-1][a-1]!=5):
            for i in range(1,9,1):#左上
                if(check[b-i][a-i]==5):
                    break
                isputa=isablerev(a-i,b-i,isputa)
                if(isputa==2):
                    mark[b][a]=mark[b][a]*2
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
        if(check[b+1][b+1]!=5):
            for i in range(1,9,1):#右下
                if(check[b+i][a+i]==5):
                    break
                isputa=isablerev(a+i,b+i,isputa)
                if(isputa==2):
                    mark[b][a]=mark[b][a]*19
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
        if(check[b+1][a-1]!=5):
            for i in range(1,9,1):#左下
                if(check[b+i][a-i]==5):
                    break
                isputa=isablerev(a-i,b+i,isputa)
                if(isputa==2):
                    mark[b][a]=mark[b][a]*13
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
        if(check[b-1][a+1]!=5):
            for i in range(1,9,1):#右上
                if(check[b-i][a+i]==5):
                    break
                isputa=isablerev(a+i,b-i,isputa)
                if(isputa==2):
                    mark[b][a]=mark[b][a]*5
                    isput=isput+1
                    break
                if(isputa==3):
                    break
        isputa=0
def change():
    global skip,player,opponent
    tmp=player
    player=opponent
    opponent=tmp
    skip=skip+1
    isableput()
    if(skip>=2):
        finaldeal()
    else:
        if(end_check()==64):
            change()
def end_check():
    sum=0
    for i in range(1,9,1):
        for j in range(1,9,1):
            sum=mark[i][j]+sum
    return sum
            
def oku():
    for a in range(1,9,1):
        for b in range(1,9,1):
            canvas.create_text(-70+150*b,-70+150*a,text=koma[check[a][b]],font=("Hleventica",50),tag="koma")
def finaldeal():
    global frag
    sum_white=0
    sum_black=0
    canvas.delete("TEXT")
    fnt = ("Times New Roman", 30)
    for a in range(1,9,1):
        for b in range(1,9,1):
            if(check[b][a]==1):
                sum_black=sum_black+1
            elif(check[b][a]==2):
                sum_white=sum_white+1
    canvas.delete("Winner")
    canvas.create_text(300, 1400, text=str(sum_black)+"ー"+str(sum_white), fill="black", font=fnt, tag="Win")
    if(sum_black>sum_white):
        canvas.create_text(300, 1500, text="黒の勝ちです", fill="black", font=fnt, tag="Winner")
    if(sum_black<sum_white):
        canvas.create_text(300, 1500, text="白の勝ちです", fill="black", font=fnt, tag="Winner")
    if(sum_black==sum_white):
        canvas.create_text(300, 1500, text="ひきわけです", fill="black", font=fnt, tag="Winner")
    print("end")
    frag=1
def game_main():
    global frag
    fnt = ("Times New Roman", 30)
    if(player==1):
        txt = "黒の番です"
    if(player==2):
        txt="白の番です"
    
    canvas.delete("TEXT")
    if(frag==0):
        canvas.create_text(300, 1300, text=txt, fill="black", font=fnt, tag="TEXT")
    canvas.delete("koma")
    oku()
    if(frag==0):
        root.after(1000, game_main)
root.resizable(False,False)
global frag
frag=0
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
isableput()
game_main()
canvas.pack()
root.mainloop()

