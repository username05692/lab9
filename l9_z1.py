def Open(file_name, mode):
    """
    Функція для відкриття файлу з перевіркою.
    """
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


file1_name = "TF11_1.txt"
file2_name = "TF11_2.txt"

# а) Створення файлу TF11_1 із символьних рядків однакової довжини
file_1_w = Open(file1_name, "w")

if file_1_w is not None:
    lines = [
        "a1b2c3d4",
        "123abc456",
        "hello7890",
        "42world99"
    ]
    for line in lines:
        file_1_w.write(line + "\n")
    print("Information was successfully added to", file1_name)
    file_1_w.close()
    print("File", file1_name, "was closed!")

# б) Обробка файлу TF11_1 і запис результату у TF11_2
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r is not None and file_2_w is not None:
    line_length = 10  # Задана довжина рядка
    for line in file_1_r:
        # Залишаємо лише цифри
        numbers_only = ''.join(char for char in line if char.isdigit())
        # Доповнюємо рядок пробілами
        padded_line = numbers_only.ljust(line_length)
        file_2_w.write(padded_line + "\n")
    print("File", file2_name, "was successfully created!")
    file_1_r.close()
    file_2_w.close()
    print("Files were closed!")

# в) Читання і друк вмісту файлу TF11_2
print("New sequence:")
file_2_r = Open(file2_name, "r")

if file_2_r is not None:
    for line in file_2_r:
        print(line.strip())
    print("File", file2_name, "was closed!")
    file_2_r.close()
