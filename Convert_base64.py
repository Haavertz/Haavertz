from PIL import Image
import base64

# pip install pillow

caminho_da_imagem = "C:/Users/gleis/OneDrive/Documentos/GitHub/About_Me/264156.jpg"

imagem = Image.open(caminho_da_imagem)

with open(caminho_da_imagem, "rb") as imagem_arquivo:
    base64_data = base64.b64encode(imagem_arquivo.read())

base64_string = base64_data.decode('utf-8')

print(base64_string)
