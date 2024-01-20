import os
import time

def write_in_file(fl_name):
    line_number = 1
    with open(f"{fl_name}.txt", 'w') as f:
        write_accept = input("Вы хотите ввести что-то в файл? y-yes/n-no\t")
        if write_accept == "y":
            lines_count = int(input("Введите кол-во строк: "))
            while lines_count != 0:
                user_input = input(f"Введите {line_number}-ю строку\t\n")
                f.write(f"{user_input}\n")
                line_number += 1
                lines_count -= 1
        else:
            f.close()
            
def read_file(fl_name):
    with open(f"{fl_name}.txt", 'r') as f:
        print(f.read())
        
def rename_file(fl_name):
    new_name = input("Введите новое имя файла: ")
    os.rename(f"{fl_name}.txt", f"{new_name}.txt")

def date_of_create(fl_name):
    ti_c = os.path.getctime(f"{fl_name}.txt")
    c_ti = time.ctime(ti_c)
    print(c_ti)
    
def main():
    file_name = input("Введите название файла: ")
    choose_variants = ["1. Создать и заполнить файл", "2. Просмотреть существующий файл", "3. Переименовать существующий файл", "4. Когда был создан файл"]
    while(True):
        print('\n'.join(choose_variants))
        accept = input("Что вы хотите сделать? ")
        if accept == "1":
            write_in_file(file_name)
        elif accept == "2":
            read_file(file_name)
        elif accept == "3":
            rename_file(file_name)
        elif accept == "4":
            date_of_create(file_name)
        else:
            print("Неверный ввод!")
        continue_program = input("Вы хотите продолжить работу? y-yes/n-no\t")
        if continue_program == "y":
            continue
        else:
            print("Программа закончена")
            break
        
if __name__ == "__main__":
    main()