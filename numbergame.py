import random
 
print('안녕친구? 이름이 뭐니?')
myName = input()
print('그래, ' + myName +',친구 지금부터 1부터 20 까지 숫자중 정답을 맞춰봐')
 
number = random.randint(1,20)
answer = 0;
cycle = 0
 
while number != int(answer):
    
    print('정답은 뭘까요?')
    answer = input()
 
    if int(answer)>number:
        print('아냐 친구, 그건 너무 커')
    elif int(answer)<number:
        print('아냐 친구, 그건 너무 작아')   
    elif int(answer)==number:
        print('잘했어! ,'+myName+'정답을 맞췄구나!'+ str(cycle) +' guesses!')
        break
 
    cycle+=1
 
    if cycle == 6:
        print('풉 ㅋ 정답은 '+str(number))
        break