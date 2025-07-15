from scholarly import scholarly
import pandas as pd
import time
import openpyxl



# Executa a busca e limita o número de resultados
query = artigos_encontrados = scholarly.search_pubs("ergonomia em TI LER") # Insira as palavras-chave desejadas

# Exibir resultados dentro do intervalo temporal desejado
resultados = []

print("Buscando artigos...")

def to_xlsx(x): # Função para salvar os resultados em um arquivo Excel
    if x:
        df = pd.DataFrame(x)
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ")
        df.to_excel(f"{nome_arquivo}.xlsx", index=False, engine='openpyxl')
        print(f"Os resultados foram salvos em {nome_arquivo}.xlsx")

            
        
for i, artigo in enumerate(artigos_encontrados):
    
    if i >= 20: # ALTERE AQUI A QUANTIDADE DE ARTIGOS A SEREM EXIBIDOS
        
        break  # Sai do loop após 20 artigos
    
    time.sleep(3)
    
    pub_year = artigo.get('pub_year', '0')  
    try:
        pub_year = int(pub_year)
    except ValueError:
        continue
        
    if 2018 >= pub_year <= 2024:
        resultados.append({
            'Título': artigo['bib']['title'],
            'Autor(es)': artigo['bib'].get('author', 'Não disponível'),
            'Resumo': artigo['bib'].get('abstract', 'Não disponível'),
            'Ano:': artigo['bib'].get('pub_year','Não disponível'),
            'Link': artigo.get('pub_url', 'Link não disponível')
        })        
        

print(resultados) # Printa os resultados encontrados para conferencia de retorno
print("Salvando resultados...")
to_xlsx(resultados)
    
