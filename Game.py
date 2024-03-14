import random as rd
import base64 as b64
# import tkinter as tkinterr
de = b64.b64decode
RR = ['ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',
      'ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',
      'ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',
      'ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',
      'ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',
      'ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',
      'ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง','ว่าง',]
secret_data = 'eydwYW5nJywnYWVrJywncGhvbmUnfQ=='
Ll = False
LL = True
while LL == True:
    if Ll == True:
        print('เริ่ม')
        
        score = 0
        lives = 3
        # words_data = {'pang','aek','phone'}
        words = list(words_data)

        def update_clue(guess, secret_word, clue):
            global win
            
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    clue[i] = guess
                win = ''.join(clue) == secret_word

        
        while (len(words) > 0) and (lives > 0):
            
            rd.shuffle(words)
            secret_word = words.pop()
            clue = list('?' * len(secret_word))

           
            while True:
                print('--------------')
                print(clue)
                print('ชีวิตทีเหลือ: ' + str(lives))
                print('คะแนนปัจจุบัน: ' + str(score))        
                guess = input('ทายตัวอักษรมาซิ: ')
                if len(guess) > 1:
                    print("---------------")
                    print("** ทายทีละตัวครับหนุ่ม **")
                    continue
                guess = guess.lower()

                
                if guess in secret_word:
                    update_clue(guess, secret_word, clue)  
                    if win:
                        print('-----------------')
                        print('เย่! คำนั้นก็คือ: ' + secret_word)
                        score = score + 1
                        print('คะแนน: +1' )
                        break
                else: 
                    print("---------------")
                    print('ผิด! เลือดสาด')
                    lives = lives - 1
                    print('ชีวิต: -1' )
                    if lives == 0:
                        print('เจ้านั้นได้ตายไปแล้ว!! คำนั้นก็คือ: ' + secret_word)
                        break
        print("")
        print('จบเกมแล้ว!')
        print("คะแนนสูงสุด: " + str(score))
        print("__________________")
        
        KK = input('รีวิวเกมนี้: ')
    
        if 'TT' not in KK:
                if 'end' not in KK:
                    1+1
                if 'RR' not in KK:
                    for i in range(len(RR)):
                        if RR[i] == 'ว่าง':
                            RR[i] = KK
                            break
   
        

        if 'end' in KK:
            LL = False 
        if 'RR' in KK:
            for i in RR:
                if i != 'ว่าง':
                    print(i)











    else:
        words_data = eval(de(secret_data).decode("utf-8"))
        Ll = True