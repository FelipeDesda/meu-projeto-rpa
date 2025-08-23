# Abrir um arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)    
# Escrever em um arquivo
with open('saida.txt', 'w') as arquivo:
    arquivo.write('Olá, Mundo!')
# Adicionar conteúdo
with open('log.txt', 'a') as arquivo:
    arquivo.write('Erro Código\n')