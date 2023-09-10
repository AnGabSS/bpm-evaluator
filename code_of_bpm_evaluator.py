age = int(input('Digite sua idade: '))
bpm = float(input('Digite seu BPM: '))

if age <= 2:
    if 120 <= bpm <= 140:
        print('Batimento está saudável')
    elif bpm < 120:
        print('batimento está baixo')
    else:
        print('batimento está alto')

elif 8 <= age <= 17:
    if 80 <= bpm <= 100:
        print('Batimento está saudável')
    elif bpm < 80:
        print('Batimento está baixo')
    else:
        print('Batimento está alto')

elif 18 <= age < 60:
    if 70 <= bpm <= 80:
        print('Batimento está saudável')
    elif bpm < 70:
        print('Batimento está baixo')
    else:
        print('Batimento está alto')

elif age >= 60:
    if 50 <= bpm <= 60:
        print('Batimento está saudável')
    elif bpm < 50:
        print('Batimento está baixo')
    else:
        print('Batimento está alto')
