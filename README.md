# conversor-de-imagem
🖼️ Conversor de Imagens para Tons de Cinza

Projeto simples em Python que converte imagens coloridas para tons de cinza (grayscale) utilizando a biblioteca Pillow (PIL).

🚀 Funcionalidades

Converte qualquer imagem suportada pelo Pillow (JPEG, PNG, etc.) para tons de cinza.

Permite salvar a saída com o mesmo nome da imagem + sufixo _gray.

Uso simples em linha de código.

📂 Estrutura do Projeto
├── converter.py   # Função principal de conversão
├── __init__.py    # Inicializa o módulo

🛠️ Tecnologias Utilizadas

Python 3.x

Pillow (PIL)

📦 Instalação

Clone o repositório e instale as dependências:

git clone https://github.com/seu-usuario/conversor-imagem.git
cd conversor-imagem
pip install pillow

▶️ Como Usar

Exemplo de uso em Python:

from converter import convert_to_grayscale

# Converter imagem e salvar no mesmo diretório
convert_to_grayscale("exemplo.jpg")

# Converter imagem e salvar com outro nome
convert_to_grayscale("exemplo.jpg", "saida_cinza.png")


Após a execução, a imagem convertida será salva no diretório especificado.

📌 Exemplo de Saída

Entrada (exemplo.jpg) → Saída (exemplo_gray.jpg)

📝 Licença

Este projeto está sob a licença MIT – fique à vontade para usar e modificar.
