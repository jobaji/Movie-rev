import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob
import streamlit as st

# App title
st.title("🎥 Movie Review Sentiment Analysis App")

# Load the trained Random Forest model and vectorizer
try:
    rf_model = pk.load(open('rf_model.pkl', 'rb'))
    vectorizer = pk.load(open('vectorizer.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: Model or vectorizer files not found. Ensure 'rf_model.pkl' and 'vectorizer.pkl' are in the same directory.")

# Input section for movie review
review = st.text_area("Enter your movie review below:")

if st.button("Analyze"):
    if review.strip():
        # Analyze polarity with TextBlob
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Transform the review using the TF-IDF vectorizer
        transformed_review = vectorizer.transform([review])

        # Predict sentiment using the Random Forest model
        prediction = rf_model.predict(transformed_review)

        # Map prediction to sentiment
        if prediction[0] == 0:
            sentiment_label = "Negative Review"
            emotion = "Sad 😢"
            image_path = "sad.png"  # Replace with actual path to your sad image
        else:
            sentiment_label = "Positive Review"
            emotion = "Happy 😊"
            image_path = "happy.jpg"  # Replace with actual path to your happy image

        # Display results
        st.subheader(f"Sentiment: {sentiment_label}")
        st.write(f"Emotion: {emotion}")
        st.image(image_path, width=150)

        # Display polarity and subjectivity
        st.write(f"**TextBlob Polarity:** {polarity:.2f}")
        st.write(f"**TextBlob Subjectivity:** {subjectivity:.2f}")
    else:
        st.warning("Please enter a valid review.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")