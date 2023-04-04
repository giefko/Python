import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier

def main():
    nltk.download('punkt')

    # Preprocessed training data
    training_data = [
        ('I love this movie', 'positive'),
        ('This restaurant has great food', 'positive'),
        ('The service was terrible', 'negative'),
        ('I did not enjoy the concert', 'negative')
    ]

    # Tokenize and preprocess the training data
    tokenized_data = [(word_tokenize(sentence.lower()), sentiment) for (sentence, sentiment) in training_data]

    # Train the Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(tokenized_data)

    # Test the classifier on new data
    test_sentence = 'The weather today is beautiful'
    test_sentence_tokens = word_tokenize(test_sentence.lower())
    sentiment = classifier.classify(dict([token, True] for token in test_sentence_tokens))
    print(f"The sentiment of '{test_sentence}' is '{sentiment}'.")

if __name__ == '__main__':
    main()
