import psutil
import csv
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434"

def get_sentiment(comment):
    """Sends a comment to Ollama for sentiment analysis."""
    payload = {
        "model": "llama3",  # Replace with your desired Ollama model
        "prompt": f"<<Comment: {comment}>> from this phrase, determine and only answer whether it is Sad, Angry, Happy, Surprised, or Normal. ONLY ONE WORD WITHOUT ANY ADDITIONAL SYMBOL OR CHARACTER",
        "stream": False  # Tell Ollama to disable streaming responses
    }

    response = requests.post(f"{OLLAMA_API_URL}/api/generate", json=payload)

    if response.status_code == 200:
        response_json = response.json()  # Use response.json() directly
        sentiment = response_json['response'].strip()
        return sentiment
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def analyze_comments(filename):
    """Analyzes comments from a CSV file and outputs sentiments."""
    comments = []
    sentiments = []

    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comment = row.get("commentText")
            if comment:  # Analyze only if 'commentText' is present
                sentiment = get_sentiment(comment)
                if sentiment:
                    comments.append(comment)
                    sentiments.append(sentiment)
                    print(f"Comment: {comment}")
                    print(f"Sentiment: {sentiment}")
                    print("-" * 20)

    # Create a DataFrame from the comments and sentiments
    df = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})

    # Plot the sentiment distribution
    sentiment_counts = df['Sentiment'].value_counts()
    sentiment_counts.plot(kind='bar')
    plt.xlabel('Sentiment')
    plt.ylabel('Frequency')
    plt.title('Sentiment Analysis of Comments')
    plt.show()

    # Monitor CPU usage
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")

    return df


if __name__ == "__main__":
    filename = "commentsEng.csv"  # Replace with your CSV file name
    sentiment_df = analyze_comments(filename)
    # Now sentiment_df contains the comments and their corresponding sentiments
