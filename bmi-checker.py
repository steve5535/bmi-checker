def get_valid_float(message):
    while True:
        try:
            value = float(input(message))
            
            if value<=0:
                print('0보다 큰수를 입력해 주세요.')
                continue
            return value
        
        except ValueError:
            print('숫자를 입력해주세요.')

name = input('이름을 입력해주세요 : ')
print(f'안녕하세요 {name}님')

height = get_valid_float('키를 입력해주세요(cm) : ')
weight = get_valid_float('몸무게를 입력해주세요(kg) : ')

bmi=round(weight/((height/100)**2),1)
if bmi < 18.5:
    print(f'{name}님의 BMI(체질량)지수는 {bmi}이고 저체중 입니다.')
elif 18.5 <= bmi < 22.9:
    print(f'{name}님의 BMI(체질량)지수는 {bmi}이고 정상체중 입니다.')
elif 23 < bmi < 24.9:
    print(f'{name}님의 BMI(체질량)지수는 {bmi}이고 과체중 입니다.')
else:
    print(f'{name}님의 BMI(체질량)지수는 {bmi}이고 비만 입니다.')