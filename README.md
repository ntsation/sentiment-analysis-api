# Análise de sentimentos em tempo real 📊

Este projeto demonstra um pipeline de análise de sentimentos em tempo real usando o analisador de sentimentos e python NLTK (Language Toolkit).O código permite escolher entre inserir mensagens em tempo real para análise de sentimentos e analisar o texto de um arquivo.

## Requisitos 🛠️

Antes de usar este projeto, verifique se você tem as seguintes dependências instaladas:

- Python 3.x
- NLTK (kit de ferramentas de linguagem natural)

## Como usar com o Docker 🐳

### 1. Clone este repositório:
```
Git clone https://github.com/ntsation/analyze_feelings.git
```
### 2. Navegue até o diretório do projeto:

```
cd analyze_feelings
```

### 3. Construa a imagem do Docker:
```
docker build -t analyze_feelings .
```
### 4. Execute o contêiner do Docker interativamente:
```
docker run -it --rm analyze_feelings
```
Isso iniciará o aplicativo de análise de sentimentos no modo interativo.

## Escolha uma opção:

Digite mensagens no console para análise de sentimentos em tempo real.
Analise o sentimento de um arquivo de texto, fornecendo seu caminho.
### Exemplos de mensagens 📝
Mensagem positiva 😃:
```
Eu amo este produto, é incrível!
```
Mensagem negativa 😞:
```
Este filme é terrível, eu não recomendo.
```
Mensagem neutra 😐:
```
O tempo está agradável hoje.
```

## Contribuição 💬
Sinta -se à vontade para contribuir, abrir problemas e melhorar este projeto.Todos os tipos de contribuições são bem -vindos!