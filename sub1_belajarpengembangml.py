# -*- coding: utf-8 -*-
"""Sub1_BelajarPengembangML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wo_CgX7EKLBzJ_6EfO-JYJZ4kj_CZ0xa

Submission 1 - Belajar Pengembang Machine Learning Dicoding

Menggunakan dataset bbc-news-data yang diunduh pada Kaggle yang diunduh melalui link https://www.kaggle.com/hgultekin/bbcnewsarchive
"""

# Mengambil data melalui google drive
# Dengan melekukan autentikasi akun gmail
from google.colab import drive
drive.mount('/content/drive/')

!ls '/content/drive/My Drive/Dataset Latihan Pengembang ML'

import pandas as pd
df = pd.read_csv('/content/drive/My Drive/Dataset Latihan Pengembang ML/bbc-news-data.csv', sep='\t')
df.info()

df.head(10)

# Kolom filename tidak relevan sehingga dapat di drop saja

df_baru = df.drop(columns=['filename'])

df_baru.head(10)

# Import library yang dibutuhkan untuk melakukan preprocessing dan
# pembuatan model machine learning

import nltk, os, re, string
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

# Melakukan pengecilan untuk semua huruf yang ada pada data

df_baru.content = df_baru.content.apply(lambda x: x.lower())
df_baru.title = df_baru.title.apply(lambda x: x.lower())

# Fungsi membersihkan data

def bersih(data):
    return(data.translate(str.maketrans('','', string.punctuation)))
    df_baru.title = df_baru.title.apply(lambda x: bersih(x))
    df_baru.content = df_baru.content.apply(lambda x: kelompok(x))

# Fungsi pengelompokan kata yang sesuai

kelompokan = WordNetLemmatizer()
def kelompok(data):
    pos_dict = {'N': wn.NOUN, 'V': wn.VERB, 'J': wn.ADJ, 'R': wn.ADV}
    return(' '.join([kelompokan.lemmatize(w,pos_dict.get(t, wn.NOUN)) for w,t in nltk.pos_tag(data.split())]))
    df_baru.title = df_baru.title.apply(lambda x: kelompok(x))
    df_baru.content = df_baru.content.apply(lambda x: kelompok(x))

# Fungsi pengenalan angka pada data

def angka(data):
    return re.sub('[0-9]+','',data)
    df_baru['title'].apply(angka)
    df_baru['content'].apply(angka)

stop_kata = stopwords.words()
def stopkata(data):
    return(' '.join([w for w in data.split() if w not in stop_kata ]))
    df_baru.title = df_new.title.apply(lambda x: stopkata(x))
    df_baru.content = df_new.content.apply(lambda x: kelompok(x))

df_baru.head(10)

# Penyesuaian kategori untuk multiclass

category = pd.get_dummies(df_baru.category)
df_baru = pd.concat([df_baru, category], axis=1)
df_baru = df_baru.drop(columns=['category'])

df_baru.head(10)

content = df_baru['title'].values + '' + df_baru['content'].values
label = df_baru[['business', 'entertainment', 'politics', 'sport', 'tech']].values

# Library untuk mengelola dan membuat model

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping

# Split data latih dan data uji

content_latih, content_uji, label_latih, label_uji = train_test_split(content, label, test_size = 0.2)

tokenizer = Tokenizer(num_words=4000, oov_token='_')

tokenizer.fit_on_texts(content_latih)
tokenizer.fit_on_texts(content_uji)

sequence_latih = tokenizer.texts_to_sequences(content_latih)
sequence_uji = tokenizer.texts_to_sequences(content_uji)

padd_latih = pad_sequences(sequence_latih) 
padd_uji = pad_sequences(sequence_uji)

# Build model NLP

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=5000, output_dim=16),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',    
              metrics=['accuracy'])

# Fungsi Callback untuk menghentikan training model pada 85%

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.8 and logs.get('val_accuracy')>0.85):
      self.model.stop_training = True
      print("\nThe accuracy of the training set and the validation set has reached > 85%!")
callbacks = myCallback()

num_epochs = 40
history = model.fit(padd_latih,
                    label_latih,
                    epochs=num_epochs,
                    validation_data = (padd_uji, label_uji),
                    verbose=2,
                    callbacks = [callbacks])

# Visualisasi Hasil Akurasi dan Loss Model ML

import matplotlib.pyplot as plt

# Visualisasi Plot Loss Model

plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper right')
plt.show()

# Visualisasi Plot Accuracy Model

plt.plot(history.history['accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper right')
plt.show()