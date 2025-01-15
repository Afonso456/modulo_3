"""Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
"""
def e_vogal(letra):
    """Verifica se uma letra é uma vogal."""
    vogais = "aeiouáàãâéêíóõôúü"
    return letra.lower() in vogais

def lingua_dos_p(palavra):
    """
    Converte uma palavra para a língua dos p.
    Adiciona a letra 'p' antes de cada vogal.
    """
    resultado = ""
    for letra in palavra:
        if e_vogal(letra):  # Se for vogal
            resultado += "p" + letra
        else:  # Se for consoante
            resultado += letra
    return resultado

# Exemplo de uso
palavra = input("Digite uma palavra para converter para a língua dos p: ")
resultado = lingua_dos_p(palavra)
print(f"A palavra '{palavra}' na língua dos p é: '{resultado}'")

