# extractor.py
# Written by Alexander M. Ruch (amr442@cornell.edu)
# Co-authors: Reid Ralston, Benjamin Cornwell
# Last update: November 6, 2017

# Stage 1 deliverables:
# TODO: Extract Dataset A: actor/actress data
    # TODO:
    # TODO:
# TODO: Extract Dataset M: movie data
# TODO: Identify and extract Dataset O: other relevant data
# TODO: Determine data structure(s)
# TODO: Create Joined Dataset: joined Datasets A, M, O


# Import data extraction packages
import wikipedia
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup  #crummy.com/software/BeautifulSoup/bs4/doc/
import json
import time
# Import data structuring packages
import numpy as np
import datetime as dt
# Import NLP packages
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Import visualization packages
import matplotlib.pyplot as plt
# Import output packages
import csv


''' Part 1: Extract Dataset A: actor/actress data '''
# Set links for main pages
usmalesu_link = 'https://en.wikipedia.org/wiki/Category:Male_actors_who_committed_suicide'
usfemalesu_link = 'https://en.wikipedia.org/wiki/Category:American_actresses_who_committed_suicide'
usmale_link = 'https://en.wikipedia.org/wiki/Category:American_male_actors'
usfemale_link = 'https://en.wikipedia.org/wiki/Category:American_actresses'
wikies = [usmalesu_link, usfemalesu_link, usmale_link, usfemale_link]
linkbase = 'https://en.wikipedia.org'

# Initialize dict for datasetA
datasetA = {}

for wiki in wikies:
    page = urlopen(wiki)
    soup = BeautifulSoup(page, 'html.parser')
    names_box = soup.find_all("div", class_="mw-category-group")
    for box in names_box:
        linklist_prep = names_box[box].next_element.next_element.next_element.next_element
        for l in linklist_prep.find_all('a'):
            name = l.text
            link = linkbase + l.get('href')
            datasetA[name] = link

# Use A's links to access table class = "infobox biography vcard" for life info



''' Part 2: Extract Dataset M: movie data '''
# Initialize dict for datasetM
datasetM = {}


''' Part 3: Identify and extract Dataset O: other relevant data '''
# Initialize dict for datasetO
datasetO = {}


''' Part 4: Determine data structure(s) '''
#


''' Part 5: Create Joined Dataset: joined Datasets A, M, O '''
#
