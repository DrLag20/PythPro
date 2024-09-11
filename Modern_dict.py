modern_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso.",
            "LOL": "Una respuesta común a algo gracioso.",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL.",
            "AGGRO": "Ponerse agresivo o enojado.",
            "KLK": "Forma de saludo, como decir: ¿Qué pasa?",
            "CREEPY": "Aterrador, siniestro.",

            } 

word = input("Escribe una palabra moderna que no entiendas (EN MAYÚSCULAS):")

if word in modern_dict.keys():
    print(modern_dict[word])
else:
    print("Esta palabra aún no está en la base de datos.")
