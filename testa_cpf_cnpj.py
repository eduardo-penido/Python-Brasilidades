from cpf_cnpj import Documento

from validate_docbr import CPF

# cpf = 12345678912
# cpf = str(cpf)
# tamanho_cpf = len(cpf)
# print(tamanho_cpf)

# objeto_cpf = Cpf(cpf)

# fatia_um = cpf[:3]
# fatia_dois = cpf[3:6]
# fatia_tres = cpf[6:9]
# fatia_quatro = cpf[9:]
# cpf_formatado = "{}.{}.{}-{}".format(fatia_um,fatia_dois,fatia_tres,fatia_quatro)
# print(fatia_um)
# print(fatia_dois)
# print(fatia_tres)
# print(fatia_quatro)
# print(cpf_formatado)
# print(objeto_cpf)

# cpf = CPF()
#
# print(cpf.validate("12345678912"))

exemplo_cnpj = "35379838000112"

documento = Documento.cria_documento(exemplo_cnpj)
print(documento)

cpf_um = Documento.cria_documento("09437786704")
print(cpf_um)