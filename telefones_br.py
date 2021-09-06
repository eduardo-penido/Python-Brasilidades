import re

class Telefones_Br:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError ("Número incorreto!!")

    def __str__(self):
        return self.formata_numero()

    def valida_telefone(self,telefone):
        padrao_tel = "([0-9]{2,3})?([0-9}{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao_tel, telefone)
        if resposta:
            print(resposta)
            return True
        else:
            return False

    def formata_numero(self):
        padrao_tel = "([0-9]{2,3})?([0-9}{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao_tel,self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(0),
            resposta.group(1),
            resposta.group(2),
            resposta.group(3)
        )
        return numero_formatado