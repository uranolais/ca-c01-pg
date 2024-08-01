import anthropic
import dotenv
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
modelo = "claude-3-5-sonnet-20240620"
# modelo = "claude-3-haiku-20240307"

def categoriza_alimento(lista_de_categorias_validas,nome_do_alimento):
    prompt_do_sistema = f"""
    Você é um categorizador de alimentos.
    Você deve assumir as categorias presentes na lista abaixo.
    Você não deve responder informações não alimentícias e/ou que fogem do seu escopo principal.

    # Lista de Categorias Válidas
    {lista_de_categorias_validas.split(",")}

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto

    # Exemplo de Saída
    Produto: Maçã
    Categoria: Frutas
    """
    prompt_do_usuario = nome_do_alimento

    message = client.messages.create(
        model=modelo,
        max_tokens=1000,
        temperature=0,
        system=prompt_do_sistema,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_do_usuario
                    }
                ]
            }
        ]
    )
    resposta = message.content[0].text
    return resposta

categorias_validas = input("Informe as categorias válidas, separando por virgula: ")

while True:
    nome_do_alimento = input("Digite o nome do alimento: ")
    texto_resposta = categoriza_alimento(categorias_validas,nome_do_alimento)
    print(texto_resposta)