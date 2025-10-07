# **Objetivo**
**Criar uma Function HTTP em Python que converte temperaturas entre Celsius e Fahrenheit.**

## **Pré-requisitos**
- **Azure Functions Core Tools v4**
- **Python 3.12+**
- **VS Code com extensões: Python e Azure Functions**
- **pip instalado**
- **Conta GitHub autenticada (para push remoto)**

## **Criar projeto**
Caminho exemplo:
```bash
cd /mnt/c/Users/tavar/Documents/github/temperature-conversion-func
func init . --python
```

## **Dependências**
Edite requirements.txt e deixe:
```bash
azure-functions
requests
```

## **Criar template de função HTTP**
```bash
func new --name ConvertTemperatureFunc --template "HTTP trigger"
Auth level: ANONYMOUS
```

## **Estrutura final esperada:**
```bash
.
├── .gitignore
├── .vscode/extensions.json
├── function_app.py
├── host.json
├── local.settings.json
└── requirements.txt
```
## **Implementação**

A função deve:

- Aceitar query parameters temperature e unit.
- Validar que ambos foram fornecidos.
- Converter Celsius ↔ Fahrenheit.
- Retornar `HTTP 400` se os parâmetros estiverem ausentes ou inválidos.
- Retornar o valor convertido em text/plain.

Exemplo de URL para teste local:
```bash
http://localhost:7071/api/convert_temperature?temperature=34.3&unit=celsius
```
<img width="556" height="124" alt="image" src="https://github.com/user-attachments/assets/544ac37e-5749-43ab-8bb8-a742e7417bee" />
