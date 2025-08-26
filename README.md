# 📋 Sistema de Ordem de Serviço e Orçamento

Uma aplicação web moderna e intuitiva para gerenciamento de ordens de serviço e orçamentos, desenvolvida com Streamlit e Python.

## ✨ Funcionalidades

- **📝 Criação de Registros**: Suporte para Pedidos e Orçamentos
- **👤 Gestão de Clientes**: Cadastro completo com dados adicionais
- **📦 Controle de Itens**: Tabela dinâmica para materiais e valores
- **📄 Exportação PDF**: Geração automática de documentos profissionais
- **📱 Interface Responsiva**: Design moderno e intuitivo

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd folha-de-orcamento
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Execute a aplicação**
```bash
streamlit run app.py
```

6. **Acesse no navegador**
```
http://localhost:8501
```

## 📁 Estrutura do Projeto

```
folha-de-orcamento/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências do projeto
├── README.md          # Documentação
├── .gitignore         # Arquivos ignorados pelo Git
└── venv/              # Ambiente virtual (não versionado)
```

## 🎯 Como Usar

### 1. **Configuração do Serviço**
- Selecione o tipo (Pedido ou Orçamento)
- Informe o número do registro
- A data de validade é calculada automaticamente (+3 dias)

### 2. **Cadastro do Cliente**
- Preencha nome e documento (CPF/CNPJ)
- Adicione dados complementares (email, telefone, CEP)
- Inclua informações adicionais conforme necessário

### 3. **Descrição do Pedido**
- Descreva detalhadamente o serviço solicitado

### 4. **Itens do Pedido**
- Adicione materiais, quantidades e valores
- Use a tabela dinâmica para inserir múltiplos itens

### 5. **Exportação PDF**
- Clique em "📄 Exportar para PDF"
- Baixe o documento gerado automaticamente

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework web para aplicações Python
- **Pandas**: Manipulação e análise de dados
- **ReportLab**: Geração de documentos PDF
- **Python**: Linguagem de programação principal

## 📋 Dependências

- `streamlit>=1.28.0`: Interface web
- `pandas>=2.0.0`: Manipulação de dados
- `reportlab>=4.0.0`: Geração de PDFs

## 🔧 Personalização

### Modificar Estilos do PDF
Edite a função `generate_pdf()` em `app.py` para personalizar:
- Cores e fontes
- Layout e espaçamento
- Cabeçalhos e rodapés
- Formatação de tabelas

### Adicionar Novos Campos
Para incluir novos campos:
1. Adicione o campo na interface Streamlit
2. Atualize a função de geração de PDF
3. Teste a funcionalidade

## 📱 Deploy

### Streamlit Cloud
1. Conecte seu repositório GitHub ao Streamlit Cloud
2. Configure as dependências em `requirements.txt`
3. Deploy automático a cada push

### Heroku
1. Crie um arquivo `Procfile` com: `web: streamlit run app.py`
2. Configure as variáveis de ambiente
3. Deploy via Heroku CLI ou GitHub integration

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou sugestões:
- Abra uma issue no GitHub
- Entre em contato via email: [carlos.heitor@outlook.com]

## 🎉 Agradecimentos

- Comunidade Streamlit
- Contribuidores do projeto
- Usuários que testaram e reportaram bugs

---

**Desenvolvido com ❤️ usando Python e Streamlit**
