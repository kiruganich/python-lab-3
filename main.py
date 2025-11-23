import sys
import os
import argparse
sys.path.insert(0, os.path.abspath('src'))
sys.path.insert(0, os.path.abspath('utilities'))

from src.math import factorial, factorial_rec, fib, fib_rec
from src.sorting import bubble_sort, counting_sort, bucket_sort
from src.data_structures import Stack, MinStack
from utilities.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
from utilities.benchmark import benchmark_sorts
from src.costants import *

def save_benchmark_report():
    print("\n--- Сохранение отчёта с бенчмарками ---")
    filename = "report.txt"
    
    try:
        arrays = {
            "Случайный (int)": rand_int_array(1000, 0, 1000, seed=42),
            "Почти отсортированный": nearly_sorted(1000, 50, seed=42),
            "Много дубликатов": many_duplicates(1000, k_unique=10, seed=42),
            "Убывающий": reverse_sorted(1000),
            "Случайный (float)": rand_float_array(1000, 0.0, 1.0, seed=42)
        }

        int_arrays = {k: v for k, v in arrays.items() if isinstance(v[0], int)}
        float_arrays = {k: v for k, v in arrays.items() if isinstance(v[0], float)}

        int_results = benchmark_sorts(int_arrays, {"Bubble Sort": bubble_sort, "Counting Sort": counting_sort})
        float_results = benchmark_sorts(float_arrays, {"Bucket Sort": lambda arr: bucket_sort(arr)})

        import datetime
        report_content = f"=== Отчёт о бенчмарке сортировок ===\n"
        report_content += f"Дата и время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        report_content += "--- Результаты для целочисленных массивов ---\n"
        report_content += format_results_for_file(int_results)

        report_content += "\n--- Результаты для вещественных массивов ---\n"
        report_content += format_results_for_file(float_results)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"Отчёт сохранён в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении отчёта: {e}")

def format_results_for_file(results: dict) -> str:

    output_lines = []
    for algo_name, timings in results.items():
        output_lines.append(f"\n{algo_name}:")
        for array_name, time_taken in timings.items():
            if time_taken == float('inf'):
                output_lines.append(f"  {array_name}: ОШИБКА ВЫПОЛНЕНИЯ")
            else:
                output_lines.append(f"  {array_name}: {time_taken:.6f} сек")
    return "\n".join(output_lines)



def main():

    parser = argparse.ArgumentParser(
        description="Алгоритмический мини-пакет. Используйте без аргументов для запуска интерактивного режима.",
        add_help=False
    )
    parser.add_argument('-h', '--help', action='store_true', help='Показать это сообщение и выйти.')
    
    args, _ = parser.parse_known_args()

    if args.help:
        with open('info.txt', 'r', encoding='utf-8') as f:
            help_text = f.read()
        print(help_text)
        sys.exit(0)

    print("=== Алгоритмический мини-пакет ===")


    while True:
        try:
            print()
            print("Доступные действия:")
            print("1. Вычислить факториал N или N-е число Фибоначчи")
            print("2. Отсортировать список")
            print("3. Работа со стеком")
            print("4. Демонстрация сортировок на случайных данных")
            print("5. Запустить бенчмарк")
            print("6. Сохранить отчёт с бенчмарками в файл")
            print("7. Выйти")
            choice = input("\nВыберите действие (1-7): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nВыход по прерыванию.")
            exit(0)

        if choice == '1':
            calculate_math()
        elif choice == '2':
            sort_user_list()
        elif choice == '3':
            stack_interactive()
        elif choice == '4':
            test_sorts_interactive()
        elif choice == '5':
            run_benchmark()
        elif choice == '6':
            save_benchmark_report()
        elif choice == '7':
            print("До свидания!")
            break
        else:
            print("Ошибка.")

def calculate_math():
    print("\n--- Вычисление факториала N или N-е числа Фибоначчи ---")
    print("1. Факториал (итеративный)")
    print("2. Факториал (рекурсивный)")
    print("3. Число Фибоначчи (итеративное)")
    print("4. Число Фибоначчи (рекурсивное)")

    try:
        calc_choice = input("Выберите (1-4): ").strip()
        n_str = input("Введите целое число n: ")
        n = int(n_str)
    except ValueError:
        print("Ошибка.")
        return
    except (EOFError, KeyboardInterrupt):
        return

    try:
        if calc_choice == '1':

            if n > MAX_FACTORIAL_N:
                print(f"Максимальное значение: {MAX_FACTORIAL_N}).")
                return
            result = factorial(n)
            print(f"Факториал({n}) = {result}")

        elif calc_choice == '2':
            if n > MAX_FACTORIAL_N:
                print(f"Максимальное значение: {MAX_FACTORIAL_N}).")
                return
            result = factorial_rec(n)
            print(f"Факториал рекурсивно({n}) = {result}")

        elif calc_choice == '3':
            if n > MAX_FIB_N:
                print(f"Максимальное значение: {MAX_FIB_N}).")
                return
            result = fib(n)
            print(f"F({n}) = {result}")

        elif calc_choice == '4':
            if n > MAX_FIB_REC_N:
                print(f"Максимальное значение: {MAX_FIB_REC_N}).")
                return
            result = fib_rec(n)
            print(f"F рекурсивно({n}) = {result}")
        else:
            print("Неверный выбор.")
    except ValueError as e:
        print(f"Ошибка: {e}")


def sort_user_list():
    print("\n--- Сортировка списка ---")
    print("Введите int или float (для Bxucket Sort) через пробел.")
    user_input = input("Список: ")
    try:
        elements = user_input.split()
        if not elements:
            print("[]")
            return

        parsed_floats = []
        parsed_ints = []
        is_float_list = True
        is_int_list = True

        for elem in elements:
            try:
                if elem == '0':
                    f_val = int(elem)
                else:
                    f_val = float(elem)
                parsed_floats.append(f_val)
            except ValueError:
                is_float_list = False
                break
        if is_float_list:
            for f_val in parsed_floats:
                if not f_val.is_integer():
                    break
            else:
                is_int_list = True
                parsed_ints = [int(f_val) for f_val in parsed_floats]
            if all(f.is_integer() for f in parsed_floats):
                 parsed_ints = [int(f) for f in parsed_floats]
            else:
                 parsed_ints = []
                 is_int_list = False

        if not is_float_list:
            for elem in elements:
                try:
                    i_val = int(elem)
                    parsed_ints.append(i_val)
                except ValueError:
                    is_int_list = False
                    break

        if not is_int_list and not is_float_list:
            print("Ошибка: Список содержит элементы, которые не int или float.")
            return

        if is_int_list:
            print("Доступные сортировки: 1. Bubble Sort 2. Count Sort")
            sort_choice = input("Выберите сортировку (1-2): ").strip()
            if sort_choice == '1':
                sorted_list = bubble_sort(parsed_ints)
                print(f"Отсортировано (Bubble Sort): {sorted_list}")
            elif sort_choice == '2':
                sorted_list = counting_sort(parsed_ints)
                print(f"Отсортировано (Count Sort): {sorted_list}")
            else:
                print("Неверный выбор сортировки.")
        elif is_float_list and not is_int_list:
            print("Доступные сортировки: 1. Bucket Sort")
            sort_choice = input("Выберите сортировку (1): ").strip()
            if sort_choice == '1':
                 if all(0.0 <= x < 1.0 for x in parsed_floats):
                     sorted_list = bucket_sort(parsed_floats)
                     print(f"Отсортировано (Bucket Sort): {sorted_list}")
                 else:
                     print(f"Внимание: Есть числа не в диапазоне [0, 1).")
                     print(f"Возможны ошибки.")
                     sorted_list = bucket_sort(parsed_floats)
                     print(f"Отсортировано (Bucket Sort): {sorted_list}")
                     
            else:
                print("Неверный выбор сортировки.")

    except ValueError:
        print("Ошибка при парсинге. Убедитесь, что ввели числа через пробел.")
    except Exception as e:
        print(f"Произошла ошибка при сортировке: {e}")


def stack_interactive():
    print("\n--- Работа со стеком ---")
    print("Создаётся обычный стек. Для MinStack введите 'min' при создании.")
    stack_type = input("Создать обычный стек или MinStack? (обычный/min): ").strip().lower()
    if stack_type == 'min':
        stack = MinStack()
        print("Создан MinStack (поддерживает min()).")
    else:
        stack = Stack()
        print("Создан обычный Stack.")
    print("Доступные команды: push <число>, pop, peek, min, is_empty, len, quit")

    while True:
        try:
            command = input(f"Стек: {stack._stack}, Команда: ").strip().split()
            if not command:
                continue

            cmd = command[0].lower()

            if cmd == 'quit':
                break
            elif cmd == 'push':
                if len(command) != 2:
                    print("Использование: push <число>")
                    continue
                try:
                    val = int(command[1])
                    stack.push(val)
                    print(f"Добавлено {val}")
                except ValueError:
                    print("Введите integer для push.")
            elif cmd == 'pop':
                try:
                    val = stack.pop()
                    print(f"Удалено и возвращено: {val}")
                except IndexError as e:
                    print(f"Ошибка: {e}")
            elif cmd == 'peek':
                try:
                    val = stack.peek()
                    print(f"Верхний элемент: {val}")
                except IndexError as e:
                    print(f"Ошибка: {e}")
            elif cmd == 'min':
                if isinstance(stack, MinStack):
                    try:
                        val = stack.min()
                        print(f"Минимальный элемент: {val}")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                else:
                    print("Команда 'min' доступна только для MinStack.")
            elif cmd == 'is_empty':
                print(f"Стек пуст: {stack.is_empty()}")
            elif cmd == 'len':
                print(f"Размер стека: {len(stack)}")
            else:
                print("Неизвестная команда.")
        except (EOFError, KeyboardInterrupt):
            print("\nВыход из режима стека.")
            break


def test_sorts_interactive():
    print("\n--- Демонстрация сортировок ---")
    try:
        n = int(input("Введите размер массива (например, 10): "))
        if n <= 0:
            print("Размер должен быть натуральным числом.")
            return
    except ValueError:
        print("Введите корректное число.")
        return

    print("\nВыберите тип данных:")
    print("1. Случайные целые числа")
    print("2. Случайные вещественные числа [0, 1)")
    try:
        data_choice = input("Выберите (1-2): ").strip()
    except (EOFError, KeyboardInterrupt):
        return

    if data_choice == '1':
        arr = rand_int_array(n, -100, 100, seed=42)
        print(f"Исходный массив: {arr}")
        print(f"Сортировка Bubble Sort: {bubble_sort(arr)}")
        print(f"Сортировка Count Sort: {counting_sort(arr)}")
    elif data_choice == '2':
        arr = rand_float_array(n, 0.0, 1.0, seed=42)
        print(f"Исходный массив: {arr}")
        print(f"Bucket Sort: {bucket_sort(arr)}")
    else:
        print("Неверный выбор.")
        return


def run_benchmark():
    print("\n--- Запуск бенчмарка ---")
    print("Генерация тестовых массивов...")

    arrays = {
        "Случайный (int)": rand_int_array(1000, 0, 1000, seed=42),
        "Почти отсортированный": nearly_sorted(1000, 50, seed=42),
        "Много дубликатов": many_duplicates(1000, k_unique=10, seed=42),
        "Убывающий": reverse_sorted(1000),
        "Случайный (float)": rand_float_array(1000, 0.0, 1.0, seed=42)
    }

    print("Запуск сортировок и замер времени...")
    int_arrays = {k: v for k, v in arrays.items() if isinstance(v[0], int)}
    float_arrays = {k: v for k, v in arrays.items() if isinstance(v[0], float)}

    print("\n--- Результаты для целочисленных массивов ---")
    int_results = benchmark_sorts(int_arrays, {"Bubble Sort": bubble_sort, "Count Sort": counting_sort})
    print_results(int_results)

    print("\n--- Результаты для вещественных массивов ---")
    float_results = benchmark_sorts(float_arrays, {"Bucket Sort": lambda arr: bucket_sort(arr)})
    print_results(float_results)

def print_results(results: dict):
    for algo_name, timings in results.items():
        print(f"\n{algo_name}:")
        for array_name, time_taken in timings.items():
            if time_taken == float('inf'):
                print(f"  {array_name}: ОШИБКА ВЫПОЛНЕНИЯ")
            else:
                print(f"  {array_name}: {time_taken:.6f} секунд")


if __name__ == "__main__":
    main()
