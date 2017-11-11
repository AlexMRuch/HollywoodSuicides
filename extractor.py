# extractor.py
# Written by Alexander M. Ruch (amr442@cornell.edu)
# Co-authors: Reid Ralston, Benjamin Cornwell
# Last update: November 9, 2017

# Stage 1 deliverables:
# TODO: Extract Dataset A: actor/actress data
    # TODO: use getactnames() to get actor/actress names/links
    # TODO: use wikipedia.py to get actor/actress data
# TODO: Extract Dataset M: movie data
# TODO: Identify and extract Dataset O: other relevant data
    # TODO: Extract race (by text or pics)
# TODO: Determine data structure(s)
# TODO: Create Joined Dataset: joined Datasets A, M, O


# Import data extraction packages
import requests
import json
import time
import wikipedia  # https://pypi.python.org/pypi/wikipedia
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Import data structuring packages
import numpy as np
import datetime as dt
# Import output packages
import pickle
import os.path


'''PART 1: EXTRACT ACTOR/ACTRESS DATA AND GENERATE DATASET A '''
# Initialize dict for datasetA
datasetA = {}

# Set links for main pages
male_su = 'Category:American_male_actors_who_committed_suicide'
fem_su = 'Category:American_actresses_who_committed_suicide'
male_nosu = 'Category:American_male_film_actors'
fem_noso = 'Category:American_film_actresses'
namesdict = {
    male_su:{'male':1, 'suicide':1},
    fem_su:{'male':0, 'suicide':1},
    male_nosu:{'male':1, 'suicide':0},
    fem_noso:{'male':0, 'suicide':0},
}

def getactnames(namesdict = namesdict):
    '''Extracts actors'/actresses' names and Wiki ids. Input is dict of dicts of
    lists with Wiki category links, sex, and suicide status of actors/actresses.
    This is a modified example of www.mediawiki.org/wiki/API:Query#Sample_query.'''
    if os.path.isfile(data/actnames.pickle):
        run = input('actnames.pickle detected. Continue to run getactnames()? (Y/N): )')
        if (run.lower() == 'y') or (run.lower() == 'yes'):
            continue
    # L0: Loop through Wiki categories
    for group in namesdict:
        print('Begin reqesting', group)
        api = 'https://en.wikipedia.org/w/api.php'
        params = {
            'action':'query',
            'list':'categorymembers',
            'cmtitle':group,
            'cmlimit':'max',
            'cmcontinue':'',
            'continue':'',
            'format':'json'
        }
        headers = {'User-agent':'amr442@cornell.edu', 'request-delay':'1s'}
        timeout = 10
        call = -1
        # L1: Keep calling until all group data extracted (500 results per call)
        while True:
            call += 1
            print('Call request', call)
            time.sleep(1)
            result = requests.get(api, params=params, headers=headers, timeout=timeout)
            if result.raise_for_status() != None:
                raise Error(result.raise_for_status())
            result = result.json()
            if 'error' in result:
                raise Error(result['error'])
            if 'warnings' in result:
                print(result['warnings'])
            if 'query' in result:
                member = -1  # initialize member index
                # L2: start looping through members in categorymembers query
                while member < len(result['query']['categorymembers']) - 1:
                    member += 1
                    title = result['query']['categorymembers'][member]['title']
                    pageid = result['query']['categorymembers'][member]['pageid']
                    datasetA[title] = {}  # add title:dict pair to datasetA
                    print('Get data for', title)
                    datasetA[title]['pageid'] = pageid
                    print('    pageid:', pageid)
                    if namesdict[group]['male'] == 1:
                        datasetA[title]['male'] = 1
                        print('    male')
                    if namesdict[group]['male'] == 0:
                        datasetA[title]['male'] = 0
                        print('    female')
                    if namesdict[group]['suicide'] == 1:
                        datasetA[title]['suicide'] = 1
                        print('    suicide')
                    if namesdict[group]['suicide'] == 0:
                        datasetA[title]['suicide'] = 0
                        print('    no suicide')
            if 'continue' not in result:
                break
            params['cmcontinue'] = result['continue']['cmcontinue']
            params['continue'] = result['continue']['continue']
        # Reset continue parameters
        print('Finished requests in group', group)
        params['cmcontinue'] = ''
        params['continue'] = ''
    print('Finished all requests for all groups. Saving as data/actnames.pickle.')
    with open('data/actnames.pickle', 'wb') as f:
        pickle.dump(datasetA, f, pickle.HIGHEST_PROTOCOL)
    print('Save complete. Function finished.')


def opendata(file):
    with open('data/' + str(file), 'rb') as f:
        data = input('Name data object (eg, datasetA, datasetM, datasetO): ')
        data = pickle.load(f)


def getactdata(datasetA = datasetA):
    '''Extracts wiki content, including biography, key dates, and career data.
    NOTE: Must run getactsu() and getactnosu() first to extract titles/links.
    NOTE: datasetA is a dict of of dicts of titles and wiki links.'''
    # Use wiki links to access life info table class = "infobox biography vcard"
    if len(datasetA) == 0:
        print('NOTE: datasetA is empty.')
        if os.path.isfile(data/actnames.pickle):
            get = input('actnames.pickle detected. Open it as datasetA? (Y/N): )')
            if (get.lower() == 'y') or (get.lower() == 'yes'):
                with open('data/actnames.pickle', 'rb') as f:
                    datasetA = pickle.load(f)
            else:
                raise Error('Must run getactnames() first.')
        else:
            raise Error('Must run getactnames() first.')
    # Use wikipedia.py package to get actors/actresses wikipedia page data


def cleanactdata(datasetA = datasetA):
    # Delete "Category" titled keys
    ## ['category' in m.lower() for m in list(ex.datasetA.keys())]
    # Rename '(Actor)' and '(Actress)' from titles
    ## [print(m) for m in list(ex.datasetA.keys()) if '(' in m.lower() or ')' in m.lower()]



''' PART 2: EXTRACT MOVIE DATA AND GENERATE Dataset M '''
# Initialize dict for datasetM
datasetM = {}


''' Part 3: EXTRACT OTHER RELEVANT DATA AND GENERATE Dataset O '''
# Initialize dict for datasetO
datasetO = {}


''' Part 4: RESTRUCTURE DATA '''
#


''' Part 5: JOIN Datasets A, M, O '''
#




################################################################################
################################################################################
''' Extracts titles, Wiki links, sex, and suicide. Input wikies_su is a list
    of Wikipedia category pages for film actors/actresses who committed suicide.
def getactsu(wikies_su = wikies_su):
    male = 2  # initialize sex indicator (1=male, 0=female)
    # L0: start group look
    for wiki in wikies_su:
        male -= 1
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
                title = l.text  # get title
                print('Get title:', title)
                pageid = linkroot + l.get('href')  # get pageid
                print('    Get pageid:', pageid)
                datasetA[title] = {}  # add title to datasetA
                datasetA[title]['pageid'] = pageid  # add pageid to title dict
                datasetA[title]['suicide'] = True  # add suicide to title dict
                if male == 1:
                    datasetA[title]['male'] = 'male'
                    print('    Get sex: male')
                if male == 0:
                    datasetA[title]['male'] = 'female'
                    print('    Get sex: female')
        time.sleep(1)
'''

''' Extracts titles, Wiki links, sex, and no suicide. Input wikies_nosu is a
    list of lists with links to Wikipedia pages for film actors/actresses who
    did not commit suicide.
def getactnosu(wikies_nosu = wikies_nosu):
    male = 2 # initialize sex indicator (0=male, 1=female): get list's lists
    # L0: start genderlist loop
    for genderlist in wikies_nosu:
        male -= 1
        print('Begin loop in', genderlist)
        # L1: start looping through link pages of genderlist: get list elements
        for link in genderlist:
            try:
                # Make API request; receive event node field and/or edge data response
                time.sleep(1)
                print('Opening:', link)
                req = requests.get(link)
                req = req.json()
            except:
                print('EXCEPTION: requests() failed at', link)
            soup = BeautifulSoup(page, 'html.parser')
            names_box = soup.find_all("div", class_="mw-content-ltr")[2]  # get titles/links
            names_box = names_box.find_all('a')
            box = -1  # initialize name group index
            # L2: loop through name groups on link page
            while box < len(names_box) - 1:
                box += 1
                print('Processing name box', str(box), 'of', str(len(names_box)-1))
                # L3: start within name loop
                for l in names_box[box].find_all('a'):
                    title = l.text  # get title
                    print('Get title:', title)
                    pageid = linkroot + l.get('href')  # get pageid
                    print('    Get pageid:', pageid)
                    datasetA[title] = {}  # add title to datasetA
                    datasetA[title]['pageid'] = pageid  # add pageid to title dict
                    datasetA[title]['suicide'] = False  # add suicide to title dict
                    if male == 1:
                        datasetA[title]['male'] = 'male'
                        print('    Get sex: male')
                    if male == 0:
                        datasetA[title]['male'] = 'female'
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
'''
