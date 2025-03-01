# ebasket-statistics
Criador de Estatísticas

## Histórico de Confrontos

Este projeto permite visualizar o histórico de confrontos entre jogadores, baseado em um banco de dados SQLite.

## Requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```
   git clone <url-do-repositorio>
   cd ebasket-statistics
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

5. Configure as variáveis de ambiente (opcional):
   - Renomeie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` conforme necessário

## Executando o Projeto

1. Execute a aplicação:
   ```
   python app.py
   ```

2. Acesse a aplicação no navegador:
   ```
   http://localhost:5000
   ```

## Estrutura do Projeto

- `app.py`: Ponto de entrada da aplicação
- `config.py`: Configurações da aplicação
- `models/`: Modelos de dados
- `routes/`: Rotas da aplicação
- `templates/`: Templates HTML
- `static/`: Arquivos estáticos (CSS, JS)
- `statistics/`: Módulo para estatísticas (futuro)

## Uso

1. Na página inicial, selecione um jogador no primeiro dropdown
2. O segundo dropdown será preenchido com jogadores que têm histórico de confrontos com o primeiro jogador
3. Selecione o segundo jogador e clique em "Ver Confrontos"
4. Visualize o histórico de confrontos entre os jogadores selecionados
