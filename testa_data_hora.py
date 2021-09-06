from datetime import datetime, timedelta
from data_hora import DatasBr

# cadastro = DatasBr()
# print(cadastro.dia_semana())

# cadastro = DatasBr()
# print(cadastro.format_data())

# hoje = datetime.today()
# hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
# print(hoje)
# print(hoje_formatada)

# numero = 1
# string = "um"
#
# print(len(string))
# print(len(numero))

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1, hours=20)
#
# print(amanha - hoje)

hoje = DatasBr()
print(hoje.tempo_cadastro())