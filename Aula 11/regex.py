import re

texto = """Contatos:
João Silva - joao.silva@empresa.com.br - (11) 91234-5678
Maria Oliveira - maria@tech.org - (21) 99876-5432
Pedro Santos - pedro.s@consultoria.net - (31) 98765-4321"""

padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
primeiro_email = re.search(padrao_email, texto)
if primeiro_email:
    print("Primeiro email encontrado:", primeiro_email.group())


todos_emails = re.findall(padrao_email, texto)
print("Todos os emails encontrados:", todos_emails)

padrao_telefone = r'\(\d{2}\) \d{5}-\d{4}'
telefones = re.findall(padrao_telefone, texto)
print("Telefones encontrados:", telefones)

novo_texto = re.sub(padrao_telefone, '[TELEFONE]', texto)
print(novo_texto)