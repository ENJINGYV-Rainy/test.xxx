import random
player_score=0
computer_score=0
print('''************
welcome game
************''')
player_name=input('import name:')
print('1.mouse 2.cat 3,dog')
choice=eval(input('jiaose'))
if choice==1:
    computer_name='mouse'
elif choice==2:
    computer_name = 'cat'
elif choice==3:
    computer_name = 'dog'
else:
    computer_name = 'niming'
print(player_name,'VS',computer_name)
while True:
    player_fist=eval(input('qingchuquan\n'))
    if player_fist==1:
        player_fister_name = '石头'
    elif player_fist==2:
        player_fister_name = '剪刀'
    elif player_fist==3:
        player_fister_name = '布'
    else:
        player_fister_name = '石头'
        player_fist=1#默认
    computer_fist=random.randint(1,3)
    if  computer_fist==1:
        computer_fister_name = '石头'
    elif computer_fist==2:
        computer_fister_name = '剪刀'
    else:
        computer_fister_name = '布'
    print(player_name,'chuquan',player_fister_name)
    print(computer_name, 'chuquan', computer_fister_name)
    if player_fist==computer_fist:
        print('ping')
    elif (player_fist==1 and computer_fist==2) or (player_fist==2 and computer_fist==3) or (player_fist==3 and computer_fist==1):
        print('wanjia win')
        player_score+=1
    else:
        print('diannao win')
        computer_score+=1
    answer = input('y/n')
    if answer!='y':
        break
print('------------------------')
print(player_name,player_score)
print(computer_name,computer_score)
