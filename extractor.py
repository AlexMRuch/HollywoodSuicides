# extractor.py
# Written by Alexander M. Ruch (amr442@cornell.edu)
# Co-authors: Reid Ralston, Benjamin Cornwell
# Last update: November 9, 2017

# Stage 1 deliverables:
# TODO: Extract Dataset A: actor/actress data
    # TODO: add wait times
# TODO: Extract Dataset M: movie data
# TODO: Identify and extract Dataset O: other relevant data
    # TODO: Extract race (by text or pics)
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


'''Part 1: Extract Dataset A: actor/actress data'''
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
    '''Extracts names, Wiki links, sex, and suicide. Input wikies_su is a list
    of Wikipedia category pages for film actors/actresses who committed suicide.'''
    sex = -1  # initialize sex indicator (0=male, 1=female)
    # L0: start group look
    for wiki in wikies_su:
        sex += 1
        try:
            page = urlopen(wiki)
            print('Opening:', wiki)
        except:
            print('EXCEPTION: urlopen() failed. Processing ended on', wiki)
        soup = BeautifulSoup(page, 'html.parser')
        names_box = soup.find_all("div", class_="mw-category-group")
        box = -1  # initialize name group index
        # L1: start name group loop
        while box < len(names_box) - 1:
            box += 1
            print('Processing name box', str(box), 'of', str(len(names_box)-1))
            # L2: start within name look
            for l in names_box[box].find_all('a'):
                name = l.text  # get name
                print('Get name:', name)
                namelink = linkroot + l.get('href')  # get namelink
                print('    Get namelink:', namelink)
                datasetA[name] = {}  # add name to datasetA
                datasetA[name]['namelink'] = namelink  # add namelink to name dict
                datasetA[name]['suicide'] = True  # add suicide to name dict
                if sex == 0:
                    datasetA[name]['sex'] = 'male'
                    print('    Get sex: male')
                if sex == 1:
                    datasetA[name]['sex'] = 'female'
                    print('    Get sex: female')


def getactnosu(wikies_nosu = wikies_nosu):
    '''Extracts names, Wiki links, sex, and no suicide. Input wikies_nosu is a
    list of lists with links to Wikipedia pages for film actors/actresses who
    did not commit suicide.'''
    sex = -1 # initialize sex indicator (0=male, 1=female): get list's lists
    # L0: start genderlist loop
    for genderlist in wikies_nosu:
        sex += 1
        print('Begin loop in', genderlist)
        # L1: start looping through link pages of genderlist: get list elements
        for link in genderlist:
            try:
                page = urlopen(link)
                print('Opening:', link)
            except:
                print('EXCEPTION: urlopen() failed. Processing ended on', link)
            soup = BeautifulSoup(page, 'html.parser')
            names_box = soup.find_all("div", class_="mw-content-ltr")[2]  # get names/links
            names_box = names_box.find_all('a')
            box = -1  # initialize name group index
            # L2: loop through name groups on link page
            while box < len(names_box) - 1:
                box += 1
                print('Processing name box', str(box), 'of', str(len(names_box)-1))
                # L3: start within name loop
                for l in names_box[box].find_all('a'):
                    name = l.text  # get name
                    print('Get name:', name)
                    namelink = linkroot + l.get('href')  # get namelink
                    print('    Get namelink:', namelink)
                    datasetA[name] = {}  # add name to datasetA
                    datasetA[name]['namelink'] = namelink  # add namelink to name dict
                    datasetA[name]['suicide'] = False  # add suicide to name dict
                    if sex == 0:
                        datasetA[name]['sex'] = 'male'
                        print('    Get sex: male')
                    if sex == 1:
                        datasetA[name]['sex'] = 'female'
                        print('    Get sex: female')
            # After processing all names_box, get next page link
            try:
                nextlink = soup.find_all("div", id="mw-pages")  # get page links
                nextlink = str(mwpages)[str(mwpages).rfind('/w/'):]  # slice nextlink front
                if "previous page" in nextlink:  # = next page inactive, last page
                    print('CONTINUE: Last page processed or next page not extracted')
                    print("'nextlink' =", nextlink, '. Check previous/next pages')
                    continue  # Move to L1 if no next page (L2 for loop expires)
                nextlink = nextlink[:nextlink.index('"')]  # slice nextlink end
                nextlink = linkroot + nextlink  # add nextlink to linkroot
                wikies_nosu[genderlist].append(nextlink)  # append nextlnik to L1
            # If no more next page links or genderlist elements:
            except:
                print('BREAK: Processing ended on the following page:')
                print(link)
                print('Failed command: soup.find_all("div", id="mw-pages")')
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
