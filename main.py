# Import the TextBlob library
from textblob import TextBlob


def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get the sentiment polarity
    sentiment_polarity = blob.sentiment.polarity

    # Determine the sentiment
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":
    # Ask the user to input text for analysis
    user_input = input("Enter a sentence or review for sentiment analysis: ")

    # Analyze the sentiment of the user's input
    result = analyze_sentiment(user_input)

    # Output the result
    print(f"The sentiment of the provided text is: {result}")
