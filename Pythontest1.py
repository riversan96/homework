print("="*30
      print("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.나가기")
      print("="*30)
while True:
    menu = int(input("원하는 계산기 기능을 입력하시오."))
    if(menu <= 4);
     numberA = int(input("첫번째 숫자를 입력하시오."))
     numberB = int(input("두번째 숫자를 입력하시오."))
     if(menu == 1):
         print("결과는 %d 입니다."%(numberA+numberB))
     elif(menu == 2):
         print("결과는 %d 입니다."%(numberA-numberB))
     elif(menu == 3):
         print("결과는 %d 입니다."%(numberA*numberB))
     elif(menu == 4):
         print("결과는 %d 입니다."%(numberA/numberB))
elif(menu == 5):
    break
else:
    print("잘못입력하셨습니다. 다시 입력해 주세요.")




