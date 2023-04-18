# Калькулятор веса

print("Введите свой рост в сантиметрах:")
height = int(input())

print("Введите свой пол (м - мужской, ж - женский):")
gender = input()

if gender == "м":
    ideal_weight = (height - 100) * 1.15
else:
    ideal_weight = (height - 110) * 1.15

print("Ваш идеальный вес составляет:", round(ideal_weight, 2), "кг.")
