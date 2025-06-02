from xmlrpc.server import SimpleXMLRPCServer
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def obter_previsao(cidade: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if resposta.status_code == 200:
            previsao = {
                "temperatura": dados['main']['temp'],
                "umidade": dados['main']['humidity'],
                "condicao": dados['weather'][0]['description'].capitalize()
            }
        else:
            previsao = {
                "temperatura": "Não disponível",
                "umidade": "Não disponível",
                "condicao": dados.get('message', 'Cidade não encontrada')
            }
    except Exception as e:
        previsao = {
            "temperatura": None,
            "umidade": None,
            "condicao": str(e)
        }
    return previsao

servidor = SimpleXMLRPCServer(("localhost", 8000))
servidor.register_function(obter_previsao, "obter_previsao")
print("Servidor de clima rodando na porta 8000 (consultando OpenWeatherMap)...")
servidor.serve_forever()
