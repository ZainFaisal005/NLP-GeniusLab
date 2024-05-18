import re
import string
from spellchecker import SpellChecker
import nltk
from nltk.corpus import stopwords
import emoji


class TextPreprocessing:
    def __init__(self,text='No Text Provided'):
        self.lowercasing(text)
        self.remove_html_tags(text)
        self.remove_urls(text)
        self.remove_punctuation(text)
        self.expand_chat_words(text)
        self.correct_spelling(text)
        self.remove_stop_words(text)
        self.replace_emojis_with_meanings(text)
    
    def lowercasing(self,text):
        return text.lower()
    
    def remove_html_tags(self,text):
        clean_text = re.sub('<.*?>', '', text)
        return clean_text
    
    def remove_urls(self,text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        clean_text = re.sub(url_pattern, '', text)
        return clean_text
    
    def remove_punctuation(self,text):
        punctuation = string.punctuation
        clean_text = text.translate(str.maketrans('', '', punctuation))
        return clean_text
    

    def expand_chat_words(self,text):
        chat_words_mapping = {
        "lol": "laughing out loud",
        "brb": "be right back",
        "btw": "by the way",
        "afk": "away from keyboard",
        "rofl": "rolling on the floor laughing",
        "ttyl": "talk to you later",
        "np": "no problem",
        "thx": "thanks",
        "omg": "oh my god",
        "idk": "I don't know",
        "np": "no problem",
        "gg": "good game",
        "g2g": "got to go",
        "b4": "before",
        "cu": "see you",
        "yw": "you're welcome",
        "wtf": "what the f*ck",
        "imho": "in my humble opinion",
        "jk": "just kidding",
        "gf": "girlfriend",
        "bf": "boyfriend",
        "u": "you",
        "r": "are",
        "2": "to",
        "4": "for",
        "b": "be",
        "c": "see",
        "y": "why",
        "tho": "though",
        "smh": "shaking my head",
        "lolz": "laughing out loud",
        "h8": "hate",
        "luv": "love",
        "pls": "please",
        "sry": "sorry",
        "tbh": "to be honest",
        "omw": "on my way",
        "omw2syg": "on my way to see your girlfriend",
        }
        words = text.split()
        expanded_words = [chat_words_mapping.get(word.lower(), word) for word in words]
        return ' '.join(expanded_words)
    
    def correct_spelling(self,text):
        spell = SpellChecker()
        corrected_words = []
        for word in text.split():
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word if corrected_word is not None else word)
        corrected_text = ' '.join(corrected_words)
        return corrected_text
    
    def remove_stop_words(self,text):
        tokens = nltk.word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]
        preprocessed_text = ' '.join(filtered_tokens)
        return preprocessed_text
    
    def remove_emojis(self,text):
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"
                                u"\U0001F300-\U0001F5FF"
                                u"\U0001F680-\U0001F6FF"
                                u"\U0001F1E0-\U0001F1FF"
                                u"\U00002500-\U00002BEF"
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        cleaned_text = emoji_pattern.sub(r'', text)
        return cleaned_text
    

    def replace_emojis_with_meanings(self,text):
        def replace(match):
            emoji_char = match.group()
            emoji_meaning = emoji.demojize(emoji_char)
            return emoji_meaning

        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"
                                u"\U0001F300-\U0001F5FF"
                                u"\U0001F680-\U0001F6FF"
                                u"\U0001F1E0-\U0001F1FF"
                                u"\U00002500-\U00002BEF"
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        text_with_meanings = emoji_pattern.sub(replace, text)
        return text_with_meanings