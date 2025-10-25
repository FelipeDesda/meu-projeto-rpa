import PyPDF2

with open('documento.pdf', 'rb') as arquivo:
    leitor = PyPDF2.PdfReader(arquivo)
    
    num_paginas = len(leitor.pages)
    print(f'O documento tem {num_paginas} páginas.')

    pagina = leitor.pages[0]
    texto = pagina.extract_text()
    print(texto)