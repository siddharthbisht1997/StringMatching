# -*- coding: utf-8 -*-
"""StringSimilarity.ipynb
"""

import numpy as np
from collections import Counter

def get_ngrams(s:str, ngram_size:int = 1)->list:
  ngrams = []
  idx = 0
  while idx <= len(s)- ngram_size:
    ngram = s[idx:idx+ngram_size]
    ngrams.append(ngram)
    idx += 1
  return ngrams

def jaccard(s1:str, s2:str, ngram:int = 1, marker:bool = False)->float:
  if marker:
    s1 = "$"+ s1 + "@"
    s2 = "$"+ s2 + "@"
  s1, s2 = get_ngrams(s1,ngram),get_ngrams(s2,ngram)
  s1, s2 = set(Counter(s1).keys()), set(Counter(s2).keys())
  intersection = len(s1.intersection(s2))
  union = len(s1.union(s2))
  return np.divide(intersection,union)

def sorensen_dice(s1:str, s2:str, ngram:int = 1, marker:bool = False)->float:
  if marker:
    s1 = "$"+ s1 + "@"
    s2 = "$"+ s2 + "@"
  s1, s2 = get_ngrams(s1,ngram),get_ngrams(s2,ngram)
  s1, s2 = set(Counter(s1).keys()), set(Counter(s2).keys())
  intersection = 2*len(s1.intersection(s2))
  union = len(s1) + len(s2)
  return np.divide(intersection,union)

def szymkiewicz_simpson(s1:str, s2:str, ngram:int = 1, marker:bool = False)->float:
  if marker:
    s1 = "$"+ s1 + "@"
    s2 = "$"+ s2 + "@"
  s1, s2 = get_ngrams(s1,ngram),get_ngrams(s2,ngram)
  s1, s2 = set(Counter(s1).keys()), set(Counter(s2).keys())
  intersection = len(s1.intersection(s2))
  return np.divide(intersection,min(len(s1),len(s2)))

