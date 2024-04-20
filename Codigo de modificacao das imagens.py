from PIL import Image
import os


folder_path = 'Imagens que serão alteradas'

paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

path_save = 'Imagens - Pistas/Imagens de cabeca para baixo'

for path in paths:
    try:

        imagem = Image.open(path)


        imagem_rgb = imagem.convert('RGB')


        imagem_girada = imagem.rotate(180)


        nome_arquivo, extensao = os.path.splitext(os.path.basename(path))


        caminho_nova = os.path.join(path_save, f"{nome_arquivo}_modificada.jpg")


        imagem_girada.save(caminho_nova)
        print(f'Imagem rotacionada e salva em: {caminho_nova}')

    except Exception as e:
        print(f"Erro ao processar a imagem {path}: {str(e)}")

print('Processo concluído.')
