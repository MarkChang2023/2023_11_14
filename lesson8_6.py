import pyinputplus as pyip
import math

def getBMI(height:int, weight:int) -> tuple[float,str]:
    BMI = weight / math.pow(height/100,2)
    message = ""
    if BMI < 18.5:
        message = "「您的體重過輕」"
    elif 18.5 <= BMI < 24:
        message = "「您的體重正常」"
    elif 24 <= BMI < 27:
        message = "「您的體重過重」"
    elif 27 <= BMI < 30:
        message = "「您的體重輕度肥胖」"
    elif 30 <= BMI < 35:
        message = "「您的體重中度肥胖」"
    else:
        message = "「您的體重重度肥胖」"
    
    return(BMI,message)

h = pyip.inputFloat("請輸入身高，單位為(公分):")
print(h)
w = pyip.inputFloat("請輸入體重，單位為(公斤):")
print(w)
bmi, message = getBMI(height=h, weight=w)

print(f"您的BMI是{bmi:.2f},{message}")