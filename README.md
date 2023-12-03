# Real-Time Sentiment Analysis 📊

This project demonstrates a real-time sentiment analysis pipeline using the NLTK (Natural Language Toolkit) Sentiment Analyzer and Python. The code allows you to choose between entering messages in real-time for sentiment analysis and analyzing text from a file.

## Requirements 🛠️

Before using this project, make sure you have the following dependencies installed:

- Python 3.x
- NLTK (Natural Language Toolkit)

## How to use with Docker 🐳

1. Clone this repository:
```
git clone https://github.com/ntsation/analyze_feelings.git
```
## Navigate to the project directory:

```
cd analyze_feelings
```

## Build the Docker image:
```
docker build -t analyze_feelings .
```
## Run the Docker container interactively:
```
docker run -it --rm analyze_feelings
```
This will start the sentiment analysis application in interactive mode.

## Choose an option:

Enter messages into the console for real-time sentiment analysis.
Analyze the sentiment of a text file by providing its path.
### Message Examples 📝
Positive message 😃:
```
I love this product, it's amazing!
```
Negative message 😞:
```
This movie is terrible, I don't recommend it.
```
Neutral message 😐:
```
The weather is pleasant today.
```

## Contribution 💬
Feel free to contribute, open issues, and improve this project. All types of contributions are welcome!