name = input('이름을 입력해주세요 : ')
print(f'안녕하세요 {name}님')
weight=int(input('몸무게를 입력해주세요(kg) : '))
height=int(input('키를 입력해주세요(cm) : '))
bmi=round(weight/((height/100)**2),1)
print(weight,height)
if bmi < 18.5:
    print(f'당신의 BMI(체질량)지수는 {bmi}이고 저체중 입니다.')
elif 18.5 <= bmi < 22.9:
    print(f'당신의 BMI(체질량)지수는 {bmi}이고 정상체중 입니다.')
elif 23 < bmi < 24.9:
    print(f'당신의 BMI(체질량)지수는 {bmi}이고 과체중 입니다.')
else:
    print(f'당신의 BMI(체질량)지수는 {bmi}이고 비만 입니다.')