# Instalar pacote com `pip3 install pillow`
from PIL import Image

# Abrir a imagem
imagem = Image.open("./images_original/14/Mandrill.jpg")

# Converter a imagem para o espaço de cores HSV
imagem_hsv = imagem.convert("HSV")

# Realizar a manipulação no componente de cor
deslocamento_tonalidade = 90  # Valor de deslocamento de exemplo, ajuste conforme necessário
dados = imagem_hsv.getdata()
dados_atualizados = []
for item in dados:
    tonalidade, saturacao, valor = item
    # Deslocar o valor da tonalidade
    tonalidade = (tonalidade + deslocamento_tonalidade) % 256
    dados_atualizados.append((tonalidade, saturacao, valor))

# Criar uma nova imagem com os dados atualizados
imagem_atualizada = Image.new("HSV", imagem_hsv.size)
imagem_atualizada.putdata(dados_atualizados)

# Converter a imagem de volta para o espaço de cores RGB
imagem_final = imagem_atualizada.convert("RGB")

# Exibir ou salvar a imagem final
imagem_final.save('./images_generate/14/atividadefinal_c.png')
