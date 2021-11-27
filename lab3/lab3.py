def gamma():
    dict = {"а": 1, "б": 2, "в": 3, "г": 4, "д": 5, "е": 6, "ё": 7, "ж": 8, "з": 9, "и": 10, "й": 11, "к": 12, "л": 13,
            "м": 14, "н": 15, "о": 16, "п": 17,
            "р": 18, "с": 19, "т": 20, "у": 21, "ф": 22, "х": 23, "ц": 24, "ч": 25, "ш": 26, "щ": 27, "ъ": 28,
            "ы": 29, "ь": 30, "э": 31, "ю": 32, "я": 32}
    dict2 = {v: k for k, v in dict.items()}
    gamma_ = input('Введите гамму: \n').lower()
    text = input('Введите текст для зашифровки: \n').lower()
    listofdigitsoftext = list()
    listofdigitsofgamma = list()
    for i in text:
        listofdigitsoftext.append(dict[i])
    print('Числа текста: \n', listofdigitsoftext)
    for i in gamma_:
        listofdigitsofgamma.append(dict[i])
    print('Числа гамма: \n', listofdigitsofgamma)
    listofdigetsresult = list()
    tmp = 0
    for i in text:
        try:
            a = dict[i] + listofdigitsofgamma[tmp]
        except:
            tmp = 0
            a = dict[i] + listofdigitsofgamma[tmp]
        if a >= 33:
            a = a % 33
        tmp += 1
        listofdigetsresult.append(a)
    print('Числа зашифрованного текста: \n', listofdigetsresult)
    txtencryp = ''
    for i in listofdigetsresult:
        txtencryp += dict2[i]
    print('Зашифрованный текст: \n', txtencryp)
    listofdigets = list()
    for i in txtencryp:
        listofdigets.append(dict[i])
    tmp = 0
    listofdigets_ = list()
    for i in listofdigets:
        a = i - listofdigitsofgamma[tmp]
        if a < 1:
            a = 33 + a
        listofdigets_.append(a)
        tmp += 1
    txtdecryp = ''
    for i in listofdigets_:
        txtdecryp += dict2[i]
    print('Расшифрованный текст: \n', txtdecryp)


gamma()
