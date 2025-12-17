#Зайцев Степан
with open("C:/Users/ZaytsSte_89/Desktop/ИПО/lr5/text.txt", "r", encoding = "UTF-8") as file: # Открываю файл для чтения
    text = file.readline() # Заношу в переменную 1-ю строку
    text_list = text.split() # Убираю пробелы
with open("C:/Users/ZaytsSte_89/Desktop/ИПО/lr5/output.txt", "w", encoding = "UTF-8") as file: # Открываю файл для записи
    for i in text_list:
        if len(i) >= 5: # Проверяем длину слова
            file.write(i + " ") # Заносим слово в файл
