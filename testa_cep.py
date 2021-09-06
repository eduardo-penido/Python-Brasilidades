import requests
from acesso_cep import BuscaEndereco

cep = 27410350
objeto_cep = BuscaEndereco(cep)
# print(objeto_cep)

r = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
print(r.text)

a = objeto_cep.acessa_via_cep()
# print(a.text) #str
# print(a.json()) #dict
# print(a.json()['bairro'])

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)