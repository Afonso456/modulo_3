def saudacao(texto= "Mundo"):
    print(f"Ola, {texto}")
def saudacao2(nome, parte_dia="Bomd dia"):
    print(f"{parte_dia}, {nome}")

saudacao()
saudacao("Joaquim")
saudacao2(parte_dia="Bom dia", nome="Joaquim")
saudacao2(parte_dia="Bao tarde", nome="Maria")
saudacao2(nome="Joaquim")