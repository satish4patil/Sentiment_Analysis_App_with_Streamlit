
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("Sentiment Analysis App")

# Text Input
user_input = st.text_area("Enter text for sentiment analysis:")

# Button to analyze sentiment
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform Sentiment Analysis
        sentiment_scores = analyzer.polarity_scores(user_input)

        # Determine sentiment label
        compound_score = sentiment_scores["compound"]
        if compound_score > 0.05:
            sentiment = "Positive"
            color = "green"
        elif compound_score < -0.05:
            sentiment = "Negative"
            color = "red"
        else:
            sentiment = "Neutral"
            color = "blue"

        # Display Results
        st.markdown(f"### **Sentiment:** <span style='color:{color}'>{sentiment}</span>", unsafe_allow_html=True)
        st.write(f"**Compound Score:** {compound_score:.2f}")

        # Extract individual sentiment scores
        labels = ['Positive', 'Neutral', 'Negative']
        values = [sentiment_scores['pos'] * 100, sentiment_scores['neu'] * 100, sentiment_scores['neg'] * 100]

        # Visualization: Bar Chart
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=['green', 'blue', 'red'])
        ax.set_ylabel("Sentiment Score (%)")
        ax.set_ylim([0, 100])  # Set y-axis limit from 0 to 100 for consistency
        ax.set_title("Sentiment Score Distribution")

        st.pyplot(fig)

    else:
        st.warning("Please enter some text for analysis.")
