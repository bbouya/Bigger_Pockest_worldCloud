"""
Created ub 28/03/2022
"""


import re
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import requests
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

import matplotlib.pyplot as plt 
from PIL import Image
from os import path, getcwd
import numpy as np

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize


def get_soup(html):
    """Get data from web page"""

    resp = requests.get(html)
    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None  
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, from_encoding = encoding)
    return soup

def get_links(soup):
    """get links from a web page"""
    http_link_list = []
    for link in soup.find_all('a', href = True):
        if link['href'][0] != '/':
            http_link_list.append(link['href'].strip("'"))
    return http_link_list

def get_ps(soup):
    """get <p> tags from web page"""
    http_link_list = []
    for link in soup.find_all('p'):
        http_link_list.append(link.get_text())
    return http_link_list

def get_text(text_array):
    """ get tect from an array of text"""
    text = " ".join(text_array)
    return text
def get_episode_text(episode_list):
    """get text from all episode in list"""
    text_return = []
    for i in episode_list:
        print(i)
        soup= get_soup(i)
        text_array = get_ps(soup)
        full_text = get_text(text_array)
        text_return.append(full_text)
    return text_return

def punctuation_stop(text):
    """remove punctuation and stop words"""
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_takens = word_tokenize(text)
    for w in word_takens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())

    return filtered