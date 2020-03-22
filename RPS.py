import random
import time
def getnum(inta,inte):
    error_msg="Choose enter the right action!"
    while True:
        try:
            i=int(input("What to do?"))
            if i<=inte and i>=inta:
                return i
            else:
                print(error_msg)
        except:
            print(error_msg)
rps=["Rock","Paper","Scisor"]
rpsp=["Rock","Paper","Scissor"]
health=100
healtho=100
while health>=0 or healtho>=0:
    print("you have", health,"health points")
    a1=random.randint(0,2)
    a=rps[a1]
    print("IT IS A DUEL. CHOOSE YOUR ACTION!")
    print("1.Attack,2.Attack\n3.Attack,4,Attack")
    getnum(1,4)
    print("CHOOSE YOUR ATTACK Strategy!")
    print('1.Rock\n2.Paper\n3.Scissor')
    b1=getnum(1,3)-1
    b=rps[b1]
    print("Waiting for Opponent...")
    for i in range(3):
        time.sleep(1)
        print(i+1,"...")
    print("The Opponent Used ",rpsp[a1]," and you used",rpsp[b1])
    dmg=random.randint(1,30)
    if(a==b):
        print("Tied!")
    elif (len(a)-len(b)==1):
        print("enemy Won! You Lose",dmg,"health points!")
        health-=dmg
    elif len(b)-len(a)==2:
        print("enemy Won! You Lose",dmg,"health points!")
        health-=dmg
    else:
        print('You won! Enemy lose',dmg,"Health points!")
        healtho-=dmg
    print("Enemy Health:",healtho)
    time.sleep(1)
if(health<=0):
    print("You Failed")
if(healtho<=0):
    print("Enemy Fainted! You Won!")