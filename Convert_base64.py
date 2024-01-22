import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

def main():
    image_path = 'C:/Users/gleis/OneDrive/Documentos/GitHub/About_Me/solo.jpg'
    
    try:
        encoded_image = encode_image_to_base64(image_path)
        print("\nImagem codificada em base64:\n")
        print("data:image/jpeg;base64," + encoded_image)
    except FileNotFoundError:
        print("Arquivo não encontrado. Certifique-se de fornecer um caminho de imagem válido.")

if __name__ == "__main__":
    main()
