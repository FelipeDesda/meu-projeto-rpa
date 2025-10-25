import pdf_pdfflumber

with pdf_pdfflumber.open("sample.pdf") as pdf:
    primeira_pagina = pdf.pages[0]
    texto = primeira_pagina.extract_text()
    tabelas = primeira_pagina.extract_tables()

    if tabelas:
        tabela = tabelas[0]
        import pandas as pd
        df = pd.DataFrame(tabela[1:], columns=tabela[0])
        print(df)