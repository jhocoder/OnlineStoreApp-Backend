import logging



loggerApp = logging.getLogger("loggerTienda")
loggerApp.setLevel(logging.DEBUG)


consolaLogger = logging.StreamHandler()
consolaFichero = logging.FileHandler("app.log", mode="a", encoding="utf-8")

formatterConsola = logging.Formatter("{levelname} - {message} - {asctime}", style="{")

formatterFichero = logging.Formatter("{levelname} - {message} - {process}", style="{", datefmt='%Y-%m-%d %H:%M')

consolaLogger.setFormatter(formatterConsola)
consolaFichero.setFormatter(formatterFichero)

loggerApp.addHandler(consolaFichero)








