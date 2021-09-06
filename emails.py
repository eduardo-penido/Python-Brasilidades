import re

class Emails:
    def __init__(self,email):
        if self.valida_email(email):
            self.texto = email
        else:
            raise ValueError ("e-mail incorreto!!")

    def valida_email(self,email):
        padrao_email = "\S{5,50}@\w{3,15}.\w{2,3}.\w{0,3}"
        resposta = re.findall(padrao_email, email)
        if resposta:
            print(resposta)
            return True
        else:
            return False