cadastros = []
def cadastrar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cadastro = {"nome": nome, "idade": idade}
    cadastros.append(cadastro)
    print("Cadastro realizado com sucesso!")
          
def listar():
    for i, pessoa in enumerate(cadastros):
        print(f"{i+1}. Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")
                                                           
def menu():
    print("\nMenu")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
          
while True:
    menu()
    opcao = input("Escolha: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        print("Saindo...")
    break
else:
        print("Opção inválida.")