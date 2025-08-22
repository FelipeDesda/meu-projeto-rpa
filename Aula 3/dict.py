# Criando um dicionário com informações de um aluno
aluno = {
    "nome": "Felipe Damasceno",
    "idade": 20,
    "curso": "Análise e Desenvolvimento de Sistemas",
}

# Acessando o valor da chave

print(aluno["nome"]) # Felipe Damasceno
print(aluno("idade")) # 20

# Adicionando novo par

aluno["semestre"] = 2

print(aluno) # Imprimindo o dicionário atualizado