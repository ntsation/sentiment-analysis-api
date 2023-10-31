import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')


# Initialize the NLTK sentiment analyzer
sia = SentimentIntensityAnalyzer()

# real-time data analysis pipeline main loop
while True:
   #Simulate real-time message ingestion from an external source
   message = input("Enter a message (or 'quit' to exit):")

   if message.lower() == 'quit':
      break

   # Analyze the sentiment of the message
   sentiment_score = sia.polarity_scores(message)

   # Print the results or perform other actions with them
   print(f'Message: {message}')
   print(f'Sentiment: {sentiment_score}')