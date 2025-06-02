# Sistema de Previsão do Tempo

Este projeto implementa um sistema distribuído de previsão do tempo usando XML-RPC, com um servidor que consulta a API do OpenWeatherMap e um cliente web Flask.

## Arquitetura

- **Servidor XML-RPC** (`servidor_clima.py`): Consulta a API do OpenWeatherMap e expõe os dados via XML-RPC
- **Cliente Web** (`cliente_web.py`): Interface web Flask que consome o serviço XML-RPC
- **Frontend**: Interface HTML para consulta de previsão do tempo

## Pré-requisitos

- Python 3.7+
- Conta no OpenWeatherMap (para obter API key gratuita)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/thiagoserafina/trabalho_previsao.git
cd trabalho_previsao
```

2. Instale as dependências:
```bash
pip install requests flask python-dotenv
```
- ou usando o arquivo requirements.txt:
```bash
pip install -r requirements.txt
```


3. Configure a API key do OpenWeatherMap:
   - Crie uma conta em [OpenWeatherMap](https://openweathermap.org/api)
   - Obtenha sua API key gratuita
   - Crie um arquivo `.env` na raiz do projeto:
```bash
echo "OPENWEATHER_API_KEY=sua_api_key_aqui" > .env
```

## Como usar

### 1. Iniciar o servidor XML-RPC

```bash
python servidor_clima.py
```

O servidor ficará rodando em `localhost:8000`

### 2. Iniciar o cliente web

Em outro terminal:

```bash
python cliente_web.py
```

O cliente web ficará disponível em `http://localhost:5000`

### 3. Usar a aplicação

1. Acesse `http://localhost:5000` no navegador
2. Digite o nome de uma cidade
3. Visualize as informações de previsão do tempo

## Funcionalidades

O sistema retorna as seguintes informações meteorológicas:

- **Temperatura atual** (°C)
- **Temperatura máxima** (°C)
- **Temperatura mínima** (°C)
- **Sensação térmica** (°C)
- **Umidade** (%)
- **Condição climática** (descrição em português)

## Estrutura do Projeto

```
trabalho_previsao/
├── servidor_clima.py      # Servidor XML-RPC
├── cliente_web.py         # Cliente web Flask
├── templates/
│   └── index.html        # Interface web
├── .env                  # Configurações (API key)
├── .gitignore
└── README.md
```

## API

### Servidor XML-RPC

**Método:** `obter_previsao(cidade: str)`

**Parâmetros:**
- `cidade`: Nome da cidade (string)

**Retorno:**
```python
{
    "temperatura": float,
    "maxima": float,
    "minima": float,
    "sensacao": float,
    "umidade": int,
    "condicao": str
}
```

### Cliente Web

**Endpoint:** `POST /previsao`

**Body:**
```json
{
    "cidade": "São Paulo"
}
```

**Response:**
```json
{
    "temperatura": 25.5,
    "maxima": 28.0,
    "minima": 22.0,
    "sensacao": 26.2,
    "umidade": 65,
    "condicao": "Céu limpo"
}
```

## Tratamento de Erros

O sistema trata os seguintes cenários de erro:

- Cidade não encontrada
- Problemas de conectividade com a API
- Servidor XML-RPC indisponível
- API key inválida ou expirada

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal
- **XML-RPC**: Protocolo de comunicação entre servidor e cliente
- **Flask**: Framework web para o cliente
- **OpenWeatherMap API**: Fonte dos dados meteorológicos
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.