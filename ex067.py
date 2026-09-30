while True:
    num = int(input('Que tabuada você quer ver? '))
    if num < 0:
        break
    print('-=' *20)
    for num2 in range(1, 11):
        print(f'{num} x {num2} = {num * num2}')
    print('-=' *20)
print('Tabuada encerrada!')