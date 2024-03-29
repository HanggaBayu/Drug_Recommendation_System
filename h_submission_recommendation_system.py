# -*- coding: utf-8 -*-
"""H_Submission_Recommendation_System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eyYcW1Rxpu-NS_eMaEKnfTu9cWrH5CrF

# Submission Dicoding - Recommendation System

## Drug Recommendation Solutions

Nama = Hangga Bayu

Dataset link : https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018

# IMPORT AND LOADING DATA
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive

drive.mount('/content/drive/')

data_train = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Bangkit Mentor 23/Machine Learning Terapan/UC_ML_Drug/drugsComTrain_raw.csv')
data_test = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Bangkit Mentor 23/Machine Learning Terapan/UC_ML_Drug/drugsComTest_raw.csv')

data_train.shape, data_test.shape

data_train.head()

data_test.head()

"""We only use test_data because the limitation of computation resource, test data is enough to explain recommenation system"""

# data_combine = pd.concat([data_train, data_test])
data_combine = data_test[:10000]

"""# EXPLORATORY DATA ANALYST"""

data_combine.head()

"""Berikut adalah penjelasan untuk setiap kolom yang disebutkan:

uniqueID: Ini adalah identifikasi unik atau kode yang digunakan untuk membedakan setiap baris atau entri dalam dataset. Kolom ini membantu dalam pengelompokan, pengurutan, atau pengaksesan data secara individual.

drugName: Kolom ini berisi nama obat yang direkomendasikan atau diulas oleh pengguna. Nama obat ini dapat mencakup nama generik atau nama merek dari obat yang diresepkan.

condition: Atribut ini menyediakan informasi tentang kondisi medis atau penyakit yang diobati dengan menggunakan obat yang disebutkan dalam baris tertentu. Misalnya, kondisi seperti diabetes, hipertensi, atau depresi.

review: Ini adalah kolom yang berisi ulasan atau pendapat dari pengguna terkait dengan pengalaman mereka menggunakan obat yang tercantum. Ulasan ini dapat mencakup berbagai aspek seperti efektivitas, efek samping, atau pengalaman penggunaan secara umum.

rating: Kolom ini mengindikasikan peringkat atau penilaian yang diberikan oleh pengguna terhadap obat yang mereka gunakan. Penilaian ini seringkali diberikan dalam bentuk angka atau bintang, di mana nilai yang lebih tinggi menunjukkan kepuasan atau efektivitas yang lebih baik.

date: Atribut ini menunjukkan tanggal ulasan atau tanggal ketika ulasan obat diberikan oleh pengguna. Informasi ini dapat digunakan untuk melacak tren atau pola penggunaan obat dari waktu ke waktu.

usefulCount: Kolom ini menghitung jumlah pengguna yang menemukan ulasan suatu obat berguna atau bermanfaat. Ini dapat digunakan sebagai metrik untuk mengevaluasi popularitas atau kepercayaan terhadap ulasan yang diberikan. Semakin tinggi nilai usefulCount, semakin banyak pengguna yang menilai ulasan tersebut bermanfaat.
"""

data_combine.shape

print(' Number of unique drugs : ', len(data_combine.drugName.unique()))
print(' Number of unique condition : ', len(data_combine.condition.unique()))

data_combine['condition'].value_counts().head(20)

data_combine['drugName'].value_counts().head(20)

data_combine.info()

data_combine.describe()

"""## Univariate Analysis

### Display Top 30 Conditions
"""

data_combine['condition'].value_counts().head(10)

top_10_conditions = data_combine['condition'].value_counts().head(30)

plt.figure(figsize=(10, 6))
top_10_conditions.plot(kind='bar', color = 'green')
plt.title('Top 30 Common Conditions', fontsize = 20)
plt.xlabel('Condition')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

"""Pada gambar, dapat dilihat birth control mendominasi data 'condition' dengan jumlah hampir sekitar 40.000

### Top 30 Popular Drugs
"""

data_combine.drugName.value_counts().head(10)

top_30_conditions = data_combine['drugName'].value_counts().head(30)

plt.figure(figsize=(10, 6))
top_30_conditions.plot(kind='bar', color = 'green')
plt.title('Top 30 Popular Drugs', fontsize = 20)
plt.xlabel('Condition')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

""" Gambaran umum mengenai distribusi n kondisi atau penyakit tertentu. Ditemukan bahwa sebagian besar ulasan berkaitan dengan obat-obatan untuk kontrasepsi (Birth Control), depresi (Depression), dan penghilang rasa sakit (Pain), dengan jumlah ulasan yang signifikan."""

from wordcloud import WordCloud
from wordcloud import STOPWORDS

stopwords = set(STOPWORDS)


# Create a WordCloud
wordcloud = WordCloud(
    stopwords = stopwords,
    background_color='white',
    width=1200,
    height=800
).generate_from_frequencies(data_combine['drugName'].value_counts().head(100))


plt.figure(figsize=(10, 10))
plt.title('Top 100 Most Popular Drugs', fontsize=20, y = 1.06)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

"""Jenis obat Levonorgestrel mendominasi dengan jumlah sekitar 4800-an"""

# data_combine.groupby(['condition'])['drugName'].nunique().sort_values(ascending=False).head(10)

"""### Mengecek jumlah variasi jenis obat untuk tiap-tiap kondisi"""

data_combine.groupby('condition')['drugName'].value_counts().groupby('condition').count().sort_values(ascending=False).head(10)

data_combine.groupby('condition')['drugName'].value_counts().groupby('condition').count().sort_values(ascending=False).head(20).plot.bar(figsize=(10, 5), color='blue')

plt.title('Most drugs available per Conditions', fontsize=20)
plt.xlabel('Conditions', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.show()

"""Menggambarkan sejumlah besar obat terfokus pada pengobatan kondisi kesehatan tertentu.

###  Mengecek jumlah suatu jenis obat yang dapat digunakan untuk berbagai kondisi
"""

data_combine.groupby('drugName')['condition'].value_counts().groupby('drugName').count().sort_values(ascending=False).head(20)

data_combine.groupby('drugName')['condition'].value_counts().groupby('drugName').count().sort_values(ascending=False).head(20).plot.bar(figsize=(15, 5), color='blue')

plt.title('Most Drugs can be Used for Many Conditions', fontsize=20)
plt.xlabel('Conditions', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.show()

"""Menjelaskan tentang jumlah obat untuk beberapa kondisi menunjukkan variasi dalam jenis obat yang digunakan untuk berbagai kondisi kesehatan

###  Melihat distribusi rating dan usefulCount pada data
"""

data_combine[['rating', 'usefulCount']].hist(bins = 20, figsize =(10,10))
plt.show

data_combine[data_combine['usefulCount']==949]

# Plotting a pie chart for the distribution of ratings
data_combine['rating'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, figsize=(8, 8), colors=plt.cm.Paired.colors)

plt.title('Distribution of Ratings')
plt.show()

# Categorize ratings as positive and negative sentiment
data_combine['sentiment'] = data_combine['rating'].apply(lambda x: 'Positive' if x > 5 else 'Negative')

sentiment_counts = data_combine['sentiment'].value_counts()
colors = ['blue', 'red']

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(sentiment_counts, autopct='%1.1f%%', startangle=90, colors=colors,
                                  wedgeprops=dict(width=0.4, edgecolor='w'))

plt.title('Distribution of Sentiments based on Ratings')
ax.legend(wedges, ['Positive', 'Negative'], title='Sentiment', loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()

"""Distribusi sentimen positif mendominasi dengan persentase sebesar 69.6 %

# Data Preparation

## Data Cleaning
"""

data_combine.isnull().sum()

data_combine = data_combine.dropna()

data_combine.isna().sum()

# CHECKING DUPLICATE DATA
duplicate_idx = data_combine['uniqueID'].duplicated()
duplicate_rows_id = data_combine[duplicate_idx]

print(f'Number of duplicate unique ID values: { duplicate_rows_id.shape[0]}')

data_combine

len(data_combine['uniqueID'].unique())

"""## Konversi Data Series ke List"""

unique_id = data_combine['uniqueID'].to_list()
drug_name = data_combine['drugName'].to_list()
condition = data_combine['condition'].to_list()

len(unique_id),len(drug_name), len(condition)

"""#### Membuat dataframe"""

drug_data_new = pd.DataFrame({
    'id':unique_id,
    'drug_name':drug_name,
    'condition':condition
})

drug_data_new

data = drug_data_new
data.sample(5)

df = pd.DataFrame(data)

# Check for duplicate rows based on both "drug_name" and "condition"
df_no_duplicates = df.drop_duplicates(subset=['drug_name', 'condition'])

df_no_duplicates

data_merged = df_no_duplicates.groupby('drug_name')['condition'].agg(lambda x: ', '.join(x)).reset_index()

data_merged.tail(10)

data_merged[data_merged['drug_name'] == 'Mirtazapine']

"""# Modelling - Content Based Filtering

## TF-IDF Vectorizer
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

tf.fit(data_merged['condition'])

tf.get_feature_names_out()

# Melakukan fit  transformasi ke bentuk matrix
tfidf_matrix = tf.fit_transform(data_merged['condition'])

#melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix

# Making dataset from list with index and column names
a = pd.DataFrame(
    tfidf_matrix.todense(),
    columns = tf.get_feature_names_out(),
    index = data_merged.drug_name
)

a.sample(15, axis=1).sample(15, axis=0)

"""# Cosine Similiarity"""

tfidf_matrix.todense().shape

from sklearn.metrics.pairwise import cosine_similarity

#Menghitung cosine similiarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim.shape

# Membuat dataframe dari variabel cosine_sim dengan baris kolom berupa nama obat
cosine_sim_df = pd.DataFrame(cosine_sim, index= data_merged['drug_name'], columns = data_merged['drug_name'])
print('Shape: ', cosine_sim_df.shape)

# Melihat similarty matrix pada setiap obat
cosine_sim_df.sample(10, axis=1).sample(10,axis=0)

def drug_recommendations(drug_name, similarity_data=cosine_sim_df, items=data_merged[['drug_name', 'condition']], k=5):

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,drug_name].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(drug_name, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

drug_recommendations('Abilify Discmelt')

"""# Evaluation"""

drug_recommendation = drug_recommendations('Abilify Discmelt')

drug_name = data_merged[data_merged['drug_name']=='Abilify Discmelt']

drug_name

match_condition = 0
for i in range (5):
  if drug_recommendation['condition'][i] == drug_name.iloc[0]['condition']:
    match_condition +=1

match_condition

Accuracy = match_condition/5*100
print("Accuracy of the model is", Accuracy,'%')

"""Dalam tabel hasil , kita memiliki rekomendasi obat untuk kondisi "Depression" berdasarkan obat sebelumnya yang dikonsumsi, yaitu "Abilify Discmelt." Dapat dilihat sistem memberikan rekomendasi yang sepenuhnya sesuai dengan kondisi "Depression" dan obat sebelumnya tersebut, maka kita memiliki presisi 100%"""