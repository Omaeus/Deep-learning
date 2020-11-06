#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import files 
from spellchecker import SpellChecker


# In[ ]:


#load default word frequency list
spell= SpellChecker()
#loads your self made dictionary
new_dict = open(r"New_dict","r+")
spell.word_frequency.load_text_file("New_dict")


# In[ ]:


#to check spelling
def checkspelling(docx):
    for word in docx:
        print("Correction = "f'{word}:{spell.correction(word)}')
        
#change "" with any text you want to check spelling of.        
checkspelling(["jchris"])


# In[ ]:


#to check possible words
def checkcandidates(docx):
    for word in docx:
        print("Candidates = "f'{word}:{spell.candidates(word)}')
        
#change "" with any text you want to check spelling of.        
checkcandidates(["bussiness"])

