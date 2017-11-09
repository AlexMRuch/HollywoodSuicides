# extractor.py
# Written by Alexander M. Ruch (amr442@cornell.edu)
# Co-authors: Reid Ralston, Benjamin Cornwell
# Last update: November 6, 2017

# Stage 1 deliverables:
# TODO: Extract Dataset A: actor/actress data
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
link_malesu = 'https://en.wikipedia.org/wiki/Category:Male_actors_who_committed_suicide'
link_femsu = 'https://en.wikipedia.org/wiki/Category:American_actresses_who_committed_suicide'
link_malenosu = 'https://en.wikipedia.org/wiki/Category:American_male_film_actors'
link_femnoso = 'https://en.wikipedia.org/wiki/Category:American_film_actresses'
wikies_su = [link_malesu, link_femsu]
wikies_nosu = [[link_malenosu], [link_femnoso]]
linkroot = 'https://en.wikipedia.org'

# Initialize dict for datasetA
datasetA = {}

def getactsu(wikies_su = wikies_su):
    '''Extracts names, wiki links, and suicide status. Input wikies_su is a link
    to the Wikipedia page for film actors/actresses who committed suicide.'''
    # Get links of actors and actresses who committed suicide
    for wiki in wikies_su:
        try:
            page = urlopen(wiki)
        except:
            print('EXCEPTION: urlopen() failed. Processing ended on', wiki)
        soup = BeautifulSoup(page, 'html.parser')
        names_box = soup.find_all("div", class_="mw-category-group")
        box = -1
        while box < len(names_box) - 1:
            box += 1
            for l in names_box[box].find_all('a'):
                name = l.text  # A's name
                namelink = linkroot + l.get('href')  # A's wiki link
                datasetA[name] = {}
                datasetA[name]['namelink'] = namelink
                datasetA[name]['suicide'] = True


wikies_nosu = [[link_malenosu], [link_femnoso]]  # groups list of lists
links = []  # initialze empty links list
def getactnosu(wikies_nosu = wikies_nosu):
    '''Extracts names, wiki links, and no suicide status. Input wikies_nosu is a
    link to the Wikipedia page for film actors/actresses who did not commit suicide.'''
    for gender in wikies_nosu:  # start groups loop (L0)
        print('Begin loop in', gender)
        for wiki in gender:  # start wiki loop (L1) in current group loop (L0)
            try:
                page = urlopen(wiki)
            except:
                print('EXCEPTION: urlopen() failed. Processing ended on', wiki)
            soup = BeautifulSoup(page, 'html.parser')
            names_box = soup.find_all("div", class_="mw-content-ltr")[2]  # get names/links
            names_box = names_box.find_all('a')
            box = -1
            while box < len(names_box) - 1:  # start name group loop (L2)
                box += 1
                for l in names_box[box].find_all('a'):  # start within name loop (l3)
                    name = l.text  # get name
                    namelink = linkroot + l.get('href')  # get namelink
                    datasetA[name] = {}  # add name to datasetA
                    datasetA[name]['namelink'] = namelink  # add namelink to name dict
                    datasetA[name]['suicide'] = False  # add suicide to name dict
            try:
                nextlink = soup.find_all("div", id="mw-pages")  # get all nextlink tag
                nextlink = str(mwpages)[str(mwpages).rfind('/w/'):]  # get start of nextlink str
                if "previous page" in nextlink:  # True if "next page" is inactive (last page)
                    print('BREAKING: Last page processed or next page link not extracted')
                    print("'nextlink' =", nextlink, '. Check previous/next pages')
                    break
                nextlink = nextlink[:nextlink.index('"')]  # get end to slice nextlink
                nextlink = linkroot + nextlink  # append nextlink end to linkroot
                wikies_nosu[gender].append(nextlink)
            except:
                print('EXCEPTION: Processing ended on the following page:')
                print(wiki)
                break


def getactdata(datasetA = datasetA):
    '''Extracts wiki content, including biography, key dates, and career data.
    NOTE: Must run getactsu() and getactnosu() first to extract names/links.
    NOTE: datasetA is a dict of of dicts of names and wiki links.'''
    # Use wiki links to access life info table class = "infobox biography vcard"
    assert(len(datasetA) > 0), "NOTE: Must run getactsu() and getactnosu() first"


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
