import webbrowser

def validator(func):
    def wrapper(url):
        if '.' in url: #если в тксте есть точка тогда выполнять
            func(url) #функцию func с передачей url
        else: #иначе
            print("Неверный URL!") #вывести текст на экран
    return wrapper #вернуть wrapper

@validator
    

def open_url(url):
    webbrowser.open(url)


open_url("https://github.com/DinislamSuperYT")
