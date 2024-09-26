import json
import re
from openai import OpenAI
from scrapy.utils.python import List
from datetime import datetime

# Uncomment for local development
# from dotenv import load_dotenv
# load_dotenv()

client = OpenAI()

MD_EXAMPLE = (
    '''---
    title: "As Vantagens dos Carros Elétricos"
    description: "Entenda os principais benefícios de adotar veículos elétricos"
    tags: [carros elétricos, veículos elétricos, sustentabilidade]
    thumbnail: "img/cyber.png"
    slug: "vantagens-carros-eletricos"
    author: "John Doe"
    date: "26/09/2024 00:12"
    ---
    
    
    Os carros elétricos oferecem uma série de vantagens que estão atraindo cada vez mais consumidores ao redor do mundo. Aqui estão os principais benefícios:
    
    ## 1. Redução de Emissões
    Uma das maiores vantagens dos carros elétricos é a ausência de emissões de gases poluentes durante a condução. Ao contrário dos veículos a combustão, que emitem dióxido de carbono (CO2) e outros gases nocivos, os carros elétricos são mais amigáveis ao meio ambiente. Essa redução de emissões é crucial na luta contra as mudanças climáticas e a poluição do ar.
    
    ## 2. Menor Custo de Manutenção
    Carros elétricos têm menos peças móveis do que veículos a gasolina ou diesel. Não há necessidade de trocar óleo, filtros de combustível ou realizar manutenção no sistema de escape. Como resultado, os custos de manutenção são significativamente menores ao longo da vida útil do veículo.
    
    ## 3. Economia de Combustível
    Embora o preço inicial de um carro elétrico possa ser maior, o custo por quilômetro rodado é muito mais baixo. O preço da eletricidade é, em geral, muito mais barato que o da gasolina ou diesel, e em alguns países, é possível carregar o carro em estações públicas gratuitamente.
    
    ## 4. Incentivos Governamentais
    Muitos governos oferecem incentivos fiscais, descontos e isenção de impostos para proprietários de veículos elétricos. Além disso, cidades ao redor do mundo estão criando áreas de baixa emissão, onde veículos a combustão são proibidos ou cobrados com taxas adicionais, enquanto carros elétricos têm livre acesso.
    
    ## 5. Condução Silenciosa e Confortável
    Os carros elétricos oferecem uma experiência de condução incrivelmente suave e silenciosa. Como os motores elétricos geram torque instantaneamente, os veículos oferecem aceleração rápida e suave, sem o barulho de um motor de combustão interna. Isso também contribui para a redução da poluição sonora nas cidades.
    
    O futuro do transporte é, sem dúvida, elétrico. Com a rápida evolução das tecnologias de bateria e a expansão da infraestrutura de recarga, os carros elétricos estão se tornando uma escolha cada vez mais acessível e vantajosa.
'''
)

def read_json(file) -> List[dict]:
    with open(file, 'r') as file:
        data = json.load(file)
        
    return data
    
def choose_posts(posts, n):
    used_links = read_json('processed_links.json')
    posts = [post for post in posts if post['url'] not in used_links]
    new_posts = posts[:n]
    
    update_processed_links(used_links, [post['url'] for post in new_posts])
    
    return new_posts
    
def update_processed_links(processed, new):
    for link in new:
        processed.append(link)
        
    with open('processed_links.json', 'w') as file:
        json.dump(processed, file, indent=4)

def translate_post(post):
    text = post['text']
    title = post['title']

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a text in English, and your task is to translate it into Brazilian Portuguese."
            },
            {
                "role": "user",
                "content": f"Given the following text and title, translate it into Brazilian Portuguese:\nTitle: {title}\nText: {text}"
            }
        ]
    )
    
    message = response.choices[0].message.content
    return message
    
def format_text(text, img, author, url):
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a text in Brazilian Portuguese, and your task is to improve it and make it compatible with the Markdown format."
            },
            {
                "role": "user",
                "content": (
                    f"Given the following text and title, improve it and make it compatible with the Markdown format."
                    f"You also must include the Front Matter with the following informations: title, description, tags, slug, author({author}) and date/time({now})."
                    "The date and time should be in the following format: DD/MM/YYYY HH:MM."
                    f"The thumbnail should also be set, but with the following url:{img} ." 
                    "For improving the text itself, consider that it is a text related to electric cars news, and should be informative and engaging."
                    "Try using different headers, bullet points and other Markdown features to make the text more readable."
                    "Dont use the ``` markers in the markdown text, as they are not necessary in this context and will make the post page fail."
                    "Just send the text that will be inside of the Markdown file."
                    f"Also, include in the end of the text that the post was based on this other website (take a look at the url to get it's name) post and author: "
                    f"URL: {url} Author: {author}."
                    f"\nText:\n{text}"
                )
            },
            {
                "role": "assistant",
                "content": f"The text should be formatted as the flowing Markdown example: {MD_EXAMPLE}"
            }
        ]
    )
    
    message = response.choices[0].message.content
    return message
    
def write_md(text):
    match = re.search(r'slug:\s*"([^"]+)"', text)
    slug = match.group(1)
    
    with open(f'../content/posts/{slug}.md', 'w') as file:
        file.write(text)

def main():
    sources = ['electrek.json', 'insideevs.json']
    for source in sources:
        scraped_posts = read_json(source)
        chosen_posts = choose_posts(scraped_posts, len(scraped_posts))
    
        for post in chosen_posts:
            translated_post = translate_post(post)
            formated_post = format_text(translated_post, post['image'], post['author'], post['url'])
            write_md(formated_post)


if __name__ == '__main__':
    main()
