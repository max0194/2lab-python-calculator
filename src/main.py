def calculator():
    print("Приветствую!")
    print("Я простой калькулятор")
    print("Доступные операции:")
    print("+ - сложение")
    print("- - вычитание") 
    print("* - умножение")
    print("/ - деление")
    print("^ - возведение в степень")
    print("q - выход")
    
    while True:
        try:
            # Ввод данных
            num1 = float(input("\nВведите первое число: "))
            operation = input("Введите операцию (+, -, *, /, ^): ")
            
            if operation == 'q':
                print("Выход из калькулятора")
                break
                
            num2 = float(input("Введите второе число: "))
            
            # Выполнение операции
            if operation == '+':
                result = num1 + num2
                print(f"Результат: {num1} + {num2} = {result}")
                
            elif operation == '-':
                result = num1 - num2
                print(f"Результат: {num1} - {num2} = {result}")
                
            elif operation == '*':
                result = num1 * num2
                print(f"Результат: {num1} * {num2} = {result}")
                
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    result = num1 / num2
                    print(f"Результат: {num1} / {num2} = {result}")
            elif operation == '^':
                result = num1 ** num2
                print(f"Результат: {num1}^{num2} = {result}")        
            else:
                print("Неверная операция!")
                
        except ValueError:
            print("Ошибка: введите корректные числа!")
        except KeyboardInterrupt:
            print("\nВыход из калькулятора")
            break

# Запуск калькулятора
if __name__ == "__main__":
    calculator()