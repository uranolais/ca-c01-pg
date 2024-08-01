import anthropic
import dotenv
import os

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
# modelo = "claude-3-5-sonnet-20240620"
modelo = "claude-3-haiku-20240307"
prompt_do_sistema = """
Você é um categorizador de alimentos.
Você deve assumir as categorias presentes na lista abaixo.

# Lista de Categorias Válidas
    - Frutas
    - Vegetais
    - Carnes
    - Grãos e Cereais
    - Laticínios
    - Bebidas
    - Doces e Sobremesas
    - Alimentos Processados

# Formato da Saída
Produto: Nome do Produto
Categoria: apresente a categoria do produto

# Exemplo de Saída
Produto: Maçã
Categoria: Frutas
"""
prompt_do_usuario = input("Forneça o nome do alimento: ")

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
print(resposta)