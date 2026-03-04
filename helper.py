'''How many messages were sent?

Who is the most active user?

What words are used most?

Which emojis appear most?'''


import pandas as pd
from collections import Counter
from urlextract import URLExtract
import emoji 

extract =URLExtract()

def fetch_stats(df):
    # total msg
    num_message = df.shape[0]

    # total words 
    words = []
    for message in df['message']:
        words.extend(message.split())

    # Media msg
    num_media_message = df[df['message']== '<Media omitted>\n'].shape[0]

    # Links
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_message,len(words),num_media_message,len(links)



# to find most active users
def most_activate_users(df):
    x = df['user'].value_counts().head()
    
    df_percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()
    df_percent.columns = ['user', 'percent']

    return x,df_percent

# function to count words frequency
def most_common_words(df):

    words = []

    for message in df['message']:
        for word in message.lower().split():
            words.append(word)

    most_common = Counter(words).most_common(20)

    return most_common

# Emoji Analysis
def emoji_analysis(df):
    emojis = []

    for message in df['message']:
        for char in message:
            if char in emoji.EMOJI_DATA:
                emojis.append(char)

    emoji_counts = Counter(emojis).most_common(10)
    
    return emoji_counts


