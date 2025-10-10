with open("C:/Users/ZaytsSte_89/Desktop/ИПО/lr5/text.txt", "r", encoding = "UTF-8") as file: # Открываю файл для чтения
    text = file.readline() # Заношу в переменную 1-ю строку
    num = text.split() # Убираю пробелы
    print(len(num))
