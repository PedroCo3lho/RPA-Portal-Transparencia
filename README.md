# Robô RPA - Portal da Transparência 🕵️‍♂️🇧🇷

Projeto em Python + Selenium para automação de coleta de dados no [Portal da Transparência](https://portaldatransparencia.gov.br/pessoa/visao-geral), focado em beneficiários de programas sociais.

---

## 🧠 Objetivo

| Tarefa                                                                 | Status   |
|------------------------------------------------------------------------|----------|
| Navegar até a seção de "Pessoas Físicas e Jurídicas"                   | 50% Apenas Pessoas Físicas |
| Inserir parâmetros de busca (nome, CPF ou NIS)                         |  ✅     |
| Aplicar o filtro obrigatório: **"BENEFICIÁRIO DE PROGRAMA SOCIAL"**    | ❌      |
| Coletar os dados dos **10 primeiros resultados**                       | ✅      |
| Capturar screenshot da tela e converter em **Base64**                  | ✅      |
| Coletar detalhes dos benefícios (Auxílio Brasil, Emergencial, Bolsa Família) |  50% Apenas o link de cada     |
| Exportar os dados em um arquivo **JSON**                               | ✅      |
| Operar em **modo headless** e suportar execuções simultâneas           | ❌      |

---

## ⚙️ Tecnologias

- Python
- Selenium
- Base64 (para imagens)
- JSON (estrutura de saída)

---

## 📁 Estrutura do Projeto

```bash
rpa-bot/
├── modules/
│   ├── main.py                  # Script principal de execução
│   ├── bot/
│   │   ├── __init__.py          
│   │   ├── driver.py            # Configuração do Selenium WebDriver
│   │   ├── navigator.py         # Navegação e interação com a página
│   │   ├── extractor.py         # Extração de dados da página
│   │   ├── screenshot.py        # Captura de tela e conversão para Base64
│   │   └── serializer.py        # Serialização e exportação de dados em JSON
├── data/
│   └── outputs/                 # Diretório para salvar os arquivos JSON gerados
├── README.md                    # Documentação do projeto
└── requirements.txt             # Dependências do projeto
```

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o robô:

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/PedroCo3lho/RPA-Portal-Transparencia.git
    cd RPA-Portal-Transparencia
    ```

2. **Configuração de ambiente**:
    - Certifique-se de ter o Microsoft Edge e o Python instalado.

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute o script principal**:

    ```bash
    cd bot
    python main.py --search "<Nome|CPF|NIS>"
    ```

5. **Verifique os resultados**:
    - Os arquivos JSON gerados estarão no diretório `data/outputs/`.
    - Logs e mensagens de execução serão exibidos no terminal.

## 🛠️ Dificuldades Enfrentadas

1. **Erro em relação ao Headless**:
    - Durante a codificação, enfrentei erros de execução em que o Python não conseguia interpretar os elementos da página. Aparentemente, o problema está relacionado ao meu hardware ou SO. Planejo testar em um ambiente na nuvem para implementar a concorrência e o modo headless.

## 📚 Referências

- [Portal da Transparência - API e Dados](https://portaldatransparencia.gov.br/pessoa/visao-geral)
- [Documentação do Selenium](https://www.selenium.dev/documentation)
- [GitHub - Selenium Python Exemples](https://github.com/SeleniumHQ/seleniumhq.github.io/tree/trunk/examples/python)
