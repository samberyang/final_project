import ebooklib
from ebooklib import epub
book = epub.read_epub('books/sample1.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        print('==================================')
        print('NAME : ', item.get_name())
        print('----------------------------------')
        print(item.get_content())
        print('==================================')
