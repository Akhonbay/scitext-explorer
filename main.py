#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 18:29:24 2018

@author: kenipatel
"""

import logging
from structures import Corpus
from algorithms import Algorithm
from visualization import Visualization
from itertools import chain, repeat

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    filename='scitext.log',
                    filemode='w')
'''
TODO:
# if select something (ie for PP) that doesn't work for ALG or VIZ, spit out warning
'''


corpus = Corpus('./config/data/text_files.yaml')

tokens = corpus()
tokenized_docs = []

for doc in tokens:
    tokenized_docs.append(doc)

#print(tokenized_docs)
#print('tokens')
    
doc_names = corpus.get_file_names()




token_dict = dict(zip(doc_names, chain(tokenized_docs, repeat(None))))


alg = Algorithm(tokens, './config/algorithms.yaml')



vis = Visualization( './config/visualization.yaml',alg, doc_names)


vis.run()

