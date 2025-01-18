import streamlit as st

def main():
    # Title and Introduction
    st.title("🎬 Movie Review Sentiment Analyzer")
    st.write("""
    Welcome to the Movie Review Sentiment Analyzer! 🎉
    This application uses machine learning and natural language processing to analyze the sentiment of movie reviews.
    
    #### Key Features:
    - Classify reviews as **Positive** or **Negative** using a trained Random Forest model.
    - Analyze the **Polarity** and **Subjectivity** of the review using TextBlob.
    - Get an intuitive output with text labels, emojis, and more!
    
    #### How to Use:
    1. Go to the **Sentiment Analysis** page (if multi-page setup is used).
    2. Enter a movie review in the text box.
    3. Click the "Analyze" button to see the results.
    """)
    
    # Add a call to action or extra information
    st.info("Ready to get started? Head over to the analysis section and try it out!")

    # Footer or Credits
    st.write("Developed by [Your Name] | Powered by Streamlit 🚀")

if __name__ == "__main__":
    main()
