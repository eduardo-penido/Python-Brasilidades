from telefones_br import Telefones_Br
import re

# molde = "(xx)aaaa-wwww"
# padrao_fixo = "[0-9}{0,2}[0-9]{4,5}[0-9]{4,6}"
# texto_tel = "Eu gosto do numero 2126451234 demais e gosto também do 21999562345"
# resposta = re.findall(padrao_fixo, texto_tel)
# print(resposta)

texto_telefone = "Eu gosto do numero 552126451234 demais e gosto também do 5521999562345"

telefone_objeto = Telefones_Br(texto_telefone)
telefone_objeto.formata_numero()