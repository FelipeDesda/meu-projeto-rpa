# Função sem Retorno
def saudacao(nome):
    """Exibe uma saudação personalizada."""
    print(f"Olá, {nome}! Seja bem-vindo(a)!")
    # Chamando a função
saudacao("Mundo")


# Adicionando um item à lista

x=[]
fruta = "maçã"

def adicionar_item(lista, item):
    """Adiciona um item à lista fornecida e mostra mensagem."""
    lista.append(item)
    print(f"Item '{item}' foi adicionado à lista.")
    
adicionar_item(x, fruta) 

# Função com Retorno    
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas) 

## Chamando a função com retorno
media_calculada = calcular_media([7.5, 8.0, 9.5])
print(f"A média das notas é: {media_calculada}")

# Função com múltiplos valores

def obter_info():
    """Retorna múltiplos valores como tupla"""
    return "Felipe", 20, "ADS"
y=obter_info()
print(f"{y[0]}, {y[1]}, {y[2]}")

# Função com Posicionais

def exibir_dados(nome, idade, curso):
    """Exibe os dados fornecidos."""
    print(f"{nome}, {idade}, {curso}")

## Chamando a função com argumentos posicionais
exibir_dados("Ana", 22, "Engenharia")

# Função com Nomeados
## Mesma função, ordem diferente
exibir_dados(
    curso="Medicina",
    nome="Carlos",
    idade=23)

# Função com Parâmetros Padrão
def cadastrar(nome, idade, curso="Python"):
    print(f"{nome}, {idade}, {curso}")
cadastrar("Maria", 19) # Usa o valor padrão "Python"
cadastrar("João", 25, "Java")  # Sobrescreve o valor padrão com "Java"

# Função com Argumentos Variáveis
def media(*notas):
    """Calcula a média de uma sequência de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)
print(media(7, 8, 9, 10))  
print(media(5, 6))

def perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    return dados    

z = perfil(nome="Jorge", idade=30, curso="Direito")
print(z)        

# Importando o módulo completo
import math
resultado = math.sqrt(16)
print(f"A raiz quadrada de 16 é: {resultado}")

# Importando função específica
from math import sqrt
resultado = sqrt(25)
print(f"A raiz quadrada de 25 é: {resultado}")

# Importando com alias
import math as m
resultado = m.factorial(5)
print(f"O fatorial de 5 é: {resultado}")

# Importando módulo próprio
## Em arquivo ultils.py
def validar_cpf(cpf): # Lógica de validação 
    return True
## Em arquivo principal
from utils import validar_cpf

validacao = validar_cpf("123.456.789-09")
print(validacao)