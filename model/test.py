import pandas as pd

df = pd.read_csv(r'dataset\test2.csv')

print(df.head(10))

# Basic preprocessing
# Remove tags
# lowercase
# remove stopwords

import re
def remove_tags(row_text):
    cleaned_text=re.sub(re.complile('<.*?>'),'',raw_text)
    return cleaned_text


### POS Tagging

pip install spacy
import spacy
nlp = spacy.load('en_core_web_sm')
