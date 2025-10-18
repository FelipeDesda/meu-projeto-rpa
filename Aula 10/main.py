import requests
from bs4 import BeautifulSoup

def extrair_noticias(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200:
        return f"Erro ao acessar o site. Código: {resposta.status_code}"
    
    soup = BeautifulSoup(resposta.content, 'html.parser')
    titulos = soup.select('.feed-post-linl')
    return [titulo.text for titulo in titulos]

noticias = extrair_noticias('https://g1.globo.com/')
for i, noticia in enumerate(noticias, 1):
    print(f"{i}. {noticia}")