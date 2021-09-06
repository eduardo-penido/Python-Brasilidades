import re
from emails import Emails

# padrao_email = "\w{5,50}@\w{3,15}.\w{2,3}.\w{0,3}"
# texto_email = "aaabbbccc eduardo@gmail.com"
# resposta = re.search(padrao_email, texto_email)
# print(resposta.group())

texto_email = "O meu e-mail mais utilizado é o email.doduda@hotmail.com , mas também tenho o eduardospenido@gmail.com"

email_objeto = Emails(texto_email)

