import regex as re
import pandas as pd
import numpy as np

class PreprocessTransformer:
    
    def __init__(self):
        pass
    
    
    def fit(self):
        #figure out the number of weird character
        pass
    
    
    def transform(self, df):
        
        
        #--------------------------------------------------------
        # replace diacritical marks like ö -> o
        #--------------------------------------------------------

        df["title"] = df["title"].map(self.replace_diacritics)
        
        #--------------------------------------------------------
        # add a column for number of weird characters in the post
        #--------------------------------------------------------
        
        # based on EDA I identified the most common punctuation
        # so anything not in this, is considered 'weird'. This only works for English text obv
        weird_chars_regex = r"[^A-Za-z \.\,\!\d\'\’\"\%\“\”\-\/\(\)\$\:\?]"
        
        
        df["has_weird_chars"] = df["title"].map(lambda s: len(re.findall(weird_chars_regex, s))!=0)
        
        #
        #--------------------------------------------------------
        # Add column for # of words in post title
        #--------------------------------------------------------
        
        df["sentence_len"] = df["title"].map(self.sentence_len)
        
        
        # Remove all punctuation, then lowercase.etc
        df["title"] = df["title"].map(self.only_chars_and_lowercase)
        
        return df
        
    def replace_diacritics(self, text):
    
        # Found some common ones here
        # https://www.thoughtco.com/what-is-a-diacritic-mark-1690444
        common_letters = {'é' : 'e',
                          'ç' : 'c',
                          'à' : 'a',
                          'ô' : 'o',
                          'ë' : 'e',
                          'ö' : 'o',
                          'ï' : 'i',
                          'è' : 'e',
                          'ā' : 'a',
                          'ñ' : 'n',
                          'ã' : 'a'}
        for key, value in common_letters.items():
            if key not in text:
                continue
            text = text.replace(key, value)
        return text


    def sentence_len(self, text):
        only_chars = r"[^A-Za-z]"

        text = re.sub(only_chars, " ", text)

        return len(text.split())
    
    def only_chars_and_lowercase(self, text):
        
        regex_str = r"[^A-Za-z\'\’]"
        
        # word like 'doesn't' should become 'doesnt'
        regex_apostrophe = "[\’\']"
        
        text = re.sub(regex_str, " ", text)
        text = re.sub(regex_apostrophe, "", text)
        
        # split into individual words
        # 
        text_split = text.split()
        
        # make it lowercase
        text_split = [s.lower() for s in text_split]
        
        # combine the words
        return " ".join(text_split)
        