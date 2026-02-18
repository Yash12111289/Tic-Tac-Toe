import random
def board():#creates the board
    return [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def display(b):
    for i in range(3):
        print(f"{ b[i][0]} | {b[i][1]} | {b[i][2]} ")
        if i<2:
            print('--+---+--')
def win_check(b):
    for i in b:
        if i[0] !=' ' and i[0]==i[1]==i[2]:
            return i[0]
    for j in range(3):
        if b[0][j]!=' ' and b[0][j]==b[1][j]==b[2][j]:
            return b[0][j]
    if b[0][0]!=' ' and b[0][0]==b[1][1]==b[2][2]:
        return b[0][0]
    if b[0][2]!=' ' and b[0][2] == b[1][1] == b[2][0]:
        return b[0][2]
    return None
def itp_check(b, mark):
    while True:
        p=input("enter no. within 1-9: ")
        if not p.isdigit():
            print("try again")
            continue
        p=int(p)
        if p<1 or p>9:
            print("try again")
            continue
        r=(p-1)//3
        c=(p-1)%3
        if b[r][c]==' ':
            b[r][c]=mark
            break
        else:
            print("try again")
def game():
    b=board()
    cur='X'
    while True:
        display(b)
        print(f"player {cur} turn")
        itp_check(b,cur)
        if win_check(b):
            display(b)
            print(f"player {cur} win")
            break
        if all(cell!=' ' for row in b for cell in row):
            display(b)
            print("Draw match")
            break
        cur='O' if cur=='X' else 'X'
def comp_game():
    b=board()
    cur=random.choice(['X','O'])
    while True:
        display(b)
        # print(f"player {cur} turn")
        # itp_check(b,cur)
        if cur=='X':#let keep everytime X as human for not getting confused
            print(f"player {cur} turn")
            itp_check(b,cur)
        else:
            print(f"player {cur} turn")
            empty=[(r,c) for r in range(3) for c in range(3) if b[r][c]==' ']
            if empty:
                r,c=random.choice(empty)
                b[r][c]=cur
        if win_check(b):
            display(b)
            print(f"player {cur} win")
            break
        if all(cell!=' ' for row in b for cell in row):
            display(b)
            print("Draw match")
            break
        cur='O' if cur=='X' else 'X'
i = int(input("select mode: "))
if i==1:
    game()
elif i==2:
    comp_game()
else:
    print("wrong input")
