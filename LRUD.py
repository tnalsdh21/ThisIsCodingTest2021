def solution(n, lrud):
    x=1
    y=1
    for cmd in lrud:
        if cmd == 'l':
            if not y==1:
                y -= 1
        elif cmd =="r":
            if not y==n:
                y+=1
        elif cmd =="u":
            if not x==1:
                x-=1
        elif cmd =="d":
            if not x == n:
                x+=1
    print("(",x,",",y,")")

solution(5, ["r","r","r","u","d","d"])