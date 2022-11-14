import string
import turtle

from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
# word_tokenize is faster than split()
tokenized_words = word_tokenize(cleaned_text, "english")
# Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
# lemmatization
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    s = turtle.Screen()
    t = turtle.Turtle(shape='turtle')
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
        t.color('black', 'red')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.penup()
        t.color('black', 'red')
        t.goto(30, 135)
        t.pendown()
        t.dot(25)
        t.penup()
        t.goto(-30, 135)
        t.pendown()
        t.dot(25)
        t.penup()
        t.goto(60, 60)
        t.pendown()
        t.setheading(120)
        t.circle(70, 120)
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
        t.color('black', 'lime green')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.penup()
        t.color('black', 'red')
        t.goto(30, 135)
        t.pendown()
        t.dot(25)
        t.penup()
        t.goto(-30, 135)
        t.pendown()
        t.dot(25)
        t.penup()
        t.goto(-60, 60)
        t.pendown()
        t.setheading(-60)
        t.circle(70, 120)

    else:
        print("Neutral Sentiment")
        t.color('orange', 'yellow')
        t.begin_fill()
        t.circle(100)
        t.end_fill()
        t.penup()
        t.color('black', 'red')
        t.goto(30, 135)
        t.pendown()
        t.dot(25)
        t.penup()
        t.goto(-30, 135)
        t.pendown()
        t.dot(25)
        t.penup()
        t.color('black')
        t.goto(-60, 60)
        t.pendown()
        t.setheading(0)
        t.forward(120)

sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()