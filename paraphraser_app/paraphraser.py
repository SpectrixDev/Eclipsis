import nltk

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

def split_text_into_sentences(text):
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(text)
