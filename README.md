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
