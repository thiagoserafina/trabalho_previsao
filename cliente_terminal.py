import xmlrpc.client

servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")
cidade = input("Digite o nome da cidade para consultar a previsão do tempo: ")
previsao = servidor.obter_previsao(cidade)
print(f"\nPrevisão do tempo para {cidade}:")
print(f"Temperatura: {previsao['temperatura']}°C")
print(f"Temperatura Máxima: {previsao['maxima']}°C")
print(f"Temperatura Mínima: {previsao['minima']}°C")
print(f"Sensação Térmica: {previsao['sensacao']}°C")
print(f"Umidade: {previsao['umidade']}%")
print(f"Condição: {previsao['condicao']}")
