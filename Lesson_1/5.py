'''
Урок 1
Задание 5
Пользователь вводит две буквы. Определить, на каких местах алфавита они
стоят и сколько между ними находится букв.
'''

C1 = input("Введите первую букву: ").lower()
C2 = input("Введите вторую букву: ").lower()

I1 = ord(C1) - 96
I2 = ord(C2) - 96
DIFF = abs(I2 - I1) - 1

print(f"Места букв в алфавите: {I1} и {I2}")
print(f"Между ними находится {DIFF} букв")
