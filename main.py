import openai
import requests

prompt = input("Digite o que você deseja para a imagem: ")

response = openai.Image.create(
    api_key='your_api_key',
    prompt= prompt,
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
image_data = requests.get(image_url).content
filename = prompt.replace(" ", "_") + ".jpg"
path = "images"
with open(path + filename, "wb") as f:
    f.write(image_data)
print(f"A imagem foi salva em {filename}.")

# def generate_and_save_image(prompt):
#     response = openai.Image.create(
#         api_key='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',
#         prompt=prompt,
#         n=1,
#         size="1024x1024"
#     )
#     image_url = response['data'][0]['url']
#     image_data = requests.get(image_url).content
#     print(image_data)
    # filename = prompt.replace(" ", "_") + ".jpg"
    # path = "Imagens/"
    # with open(path + filename, "wb") as f:
    #     f.write(image_data)
    # print(f"A imagem foi salva em {path + filename}.")

# prompt = input("Digite o que você deseja para a imagem: ")
# generate_and_save_image(prompt)
