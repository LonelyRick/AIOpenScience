import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import os
from grobid_client_python.grobid_client.grobid_client import GrobidClient

# Conexión con API de Grobid
grobid_url = 'http://localhost:8070/api/processFulltextDocument'
headers = {'Accept': 'application/xml'}
client = GrobidClient(config_path="./config.json")

pdfs=[]
names =[]
def getPDF():
    #Lista de PDFs a evaluar
    folder= './shared'  
    for f in os.listdir(folder):
        if f.endswith('.pdf'):  
            pdfs.append(folder+'/'+f)
            names.append(f)


#Obtención del html mediante Grobid
def getGrobid(pdf):
    try:
        with open(pdf, 'rb') as file:
            reader = file.read()
            respuesta =client.post(grobid_url, headers=headers, files={'input': ('input.pdf', reader)})
            if str(respuesta[0]) == "<Response [200]>" : 
                fres = respuesta[0].text.encode("utf-8")
            else:
                print('Error:', respuesta[0])
            return str(fres)
    except FileNotFoundError:
        print("El fichero no existe o no se encuentra")

#Obtención de abstracto
def getAbstract(respuesta):
    abstract = re.findall(r"<abstract>(.*?)</abstract>", respuesta, re.DOTALL)
    cleanAbstract = abstract[0].encode('utf-8')  
    return cleanAbstract

#Obtención de figuras
def getNumFigures(respuesta):
    figures = len(re.findall(r"<figure(.*?)</figure>", respuesta, re.DOTALL))
    return figures

#Obtención de links
def getLinks(respuesta):
    links = re.findall(r'<ptr target="([^"]+)"', respuesta, re.DOTALL)
    return links


#Generación de WordCloud
def getWordCloud(abstract):
    try:
        wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(abstract)
        return wordcloud
    except ValueError:
        print("Se necesita al menos 1 palabra para generar el WordCloud")

def pintar(wordcloud,pdf):
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    wordcloud.to_file(f'{pdf}wordcloud.png')

def grafica(figures):
    plt.figure()
    plt.bar(range(len(figures)), figures)
    plt.xticks(range(len(figures)), [name for name in names], ha='right',fontsize=5)
    plt.xlabel('Paper')
    plt.ylabel('Number of Figures')
    plt.show()
    plt.savefig("graficalinks.png")

def listado(links, pdf):
    name = pdf.split('.p')[0]
    filename = f"{name}_links.txt" 
    print(f'Links found in {pdf}:')
    with open(filename, 'w') as f: 
        for link in links:
            url = link[0:-1]
            f.write(url + '\n') 
    print(f'Links saved in {filename}')
    
def main():
    num_figures = []
    getPDF()
    for pdf in pdfs:
        print(pdf)
        respuesta = getGrobid(pdf)
        abstracto = getAbstract(respuesta)
        wordcloud = getWordCloud(str(abstracto))
        pintar(wordcloud,pdf)
        figures = getNumFigures(respuesta)
        num_figures.append(figures)
        links = getLinks(respuesta)
        listado(links,pdf)
    grafica(num_figures)


if __name__ == '__main__':
    main()


