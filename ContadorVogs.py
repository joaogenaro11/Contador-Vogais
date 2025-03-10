def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = sum(1 for letra in frase if letra in vogais)
    return contador

frase_usuario = input("Digite uma frase: ")
print(f"Número de vogais na frase: {contar_vogais(frase_usuario)}")