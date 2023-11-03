import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Initialize the NLTK sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    print(f'Message: {text}')
    print(f'Sentiment: {sentiment_score}')

def main_menu():
    while True:
        print('Choose an option:')
        print('1. Type a message to analyze')
        print('2. Analyze a message from a file')
        print('3. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            message = input('Enter a message: ')
            analyze_sentiment(message)
        elif choice == '2':
            file_path = input('Enter the file path: ')
            analyze_sentiment_from_file(file_path)
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')

def analyze_sentiment_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            message = file.read()
            analyze_sentiment(message)
    except FileNotFoundError:
        print('File not found. Please try again.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    main_menu()
