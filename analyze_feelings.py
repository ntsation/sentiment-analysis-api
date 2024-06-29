import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Inicializa o analisador de sentimento do NLTK
sia = SentimentIntensityAnalyzer()


def analisar_sentimento(texto):
    pontuacao_sentimento = sia.polarity_scores(texto)
    print(f'Mensagem: {texto}')
    print(f'Sentimento: {pontuacao_sentimento}')


def analisar_sentimento_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            mensagem = arquivo.read().strip
            if not mensagem:
                print('O arquivo está vazio.')
                return
            analisar_sentimento(mensagem)
    except FileNotFoundError:
        print('Arquivo não encontrado. Por favor, tente novamente.')
    except PermissionError:
        print('Permissão negada para acessar o arquivo. Por favor, verifique '
              'as permissões e tente novamente.')
    except Exception as e:
        print(f'Ocorreu um erro: {str(e)}')


def menu_principal():
    while True:
        print('Escolha uma opção:')
        print('1. Digitar uma mensagem para analisar')
        print('2. Analisar uma mensagem de um arquivo')
        print('3. Sair')

        escolha = input('Digite sua escolha: ')

        if escolha == '1':
            mensagem = input('Digite uma mensagem: ')
            analisar_sentimento(mensagem)
        elif escolha == '2':
            caminho_arquivo = input('Digite o caminho do arquivo: ')
            analisar_sentimento_arquivo(caminho_arquivo)
        elif escolha == '3':
            print('Saindo...')
            break
        else:
            print('Escolha inválida. Por favor, tente novamente.')


if __name__ == '__main__':
    menu_principal()
