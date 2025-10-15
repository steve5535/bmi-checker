import pygame
import sys

pygame.init() # 초기화
screen = pygame.display.set_mode((600,400)) # 화면 크기 설정
pygame.display.set_caption("Bmi-Checker (Pygame)") # 창 이름 설정

step = "name"
user_input = '' # 유저 입력 받는 변수
name = '' # 이름 변수
height = 0 # 키 변수
weight = 0 # 몸무게 변수
message = "이름을 입력해주세요." # 메시지 변수
font = pygame.font.SysFont("malgungothic", 36) # 글자 크기 설정

while True: # 화면 표시 메인 루프
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 화면 끄는 기능
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # enter 입력 시
                if step == "name":
                    name = user_input
                    user_input = ''
                    message = "키를 입력해주세요 (cm)"
                    step = "height"
                elif step == "height":
                    try:
                        height = float(user_input)
                        if height <= 0:
                            message = "0보다 큰 수를 입력해 주세요."
                        else:
                            user_input = ''
                            message = "몸무게를 입력해주세요 (kg)"
                            step = "weight"
                    except ValueError:
                        message = "숫자를 입력해주세요."
                elif step == "weight":
                    try:
                        weight = float(user_input)
                        if weight <= 0:
                            message = "0보다 큰 수를 입력해주세요"
                        else:
                            bmi=round(weight/((height/100)**2),1)
                            if bmi < 18.5:
                                result = "저체중"
                            elif 18.5 <= bmi < 22.9:
                                result = "정상체중"
                            elif 23 < bmi < 24.9:
                                result = "과체중"
                            else:
                                result = "비만"
                            message = f"{name}님의 BMI지수: {bmi} ({result})"
                            step = "done"
                            user_input = ""
                    except ValueError:
                        message = "숫자를 입력해주세요."

            elif event.key == pygame.K_BACKSPACE: # backspace 키를 눌렀을때
                user_input = user_input[:-1] # 지우는 기능
            else:
                user_input += event.unicode


    text = font.render(user_input, True, (255, 255, 255)) # 현재 입력 중인 텍스트
    screen.blit(text, (200, 150))

    message_text = font.render(message, True, (255, 255, 0)) # 안내 메시지
    screen.blit(message_text, (100, 250))

    pygame.display.update()