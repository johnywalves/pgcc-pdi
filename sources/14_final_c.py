from PIL import Image
import colorsys

# Abrir a imagem
caminho_imagem = "img/Mandrill.jpg"
imagem = Image.open(caminho_imagem)

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
imagem_final.show()
# imagem_final.save("saida.jpg")  # Descomente esta linha para salvar a imagem
