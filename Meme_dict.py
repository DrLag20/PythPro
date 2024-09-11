meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}

word = input("\nEscribe una palabra que no entiendas (EN MAYÚSCULAS): ")

if word in meme_dict:
        print(f"{word}: {meme_dict[word]}")
else:
        print("Lo siento, no conozco esa palabra."
