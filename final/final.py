import nltk
import ebooklib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ebooklib import epub

# nltk.download('stopwords')
# nltk.download('punkt')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]
    return ' '.join(filtered_tokens)

def process_epub_file(file_path):
    book = epub.read_epub(file_path)
    processed_text = ''

    for item in book.get_items():
        if item.get_type() == epub.EpubHtml:
            html_content = item.get_content()
            text = epub.utils.decode_html(html_content)
            processed_text += remove_stopwords(text) + ' '

    return processed_text

# Usage example
epub_file_path = 'books/sample1.epub'
processed_text = process_epub_file(epub_file_path)
print(processed_text)
