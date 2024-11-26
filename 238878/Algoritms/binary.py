use = True
while use:
    binary = ""
    num = input('Enter: ')
    if num == 's':
        use =False 
        break
    end =True
    num = int(num)
    while end:
        b = num % 2 != 0
        
        print(int(b))
        num //=2 
        print(num)
        if b:
            binary += "1"
        else:
            binary += "0"
        if num == 0:
            num = f'{num}'
            print(binary[::-1])
            end = False
            break

