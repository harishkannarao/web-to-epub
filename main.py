import sys
from ebooklib import epub

print(sys.argv)
book = epub.EpubBook()

book.set_identifier('sample123456')
book.set_title('Sample book')
book.set_language('en')

book.add_author('Sample Author')

# intro chapter
c1 = epub.EpubHtml(title='Introduction',
                   file_name='intro.xhtml',
                   lang='en')
c1.set_content(u'<html><body><h1>Introduction</h1><p>Introduction paragraph.</p></body></html>')

# about chapter
c2 = epub.EpubHtml(title='About this book',
                   file_name='about.xhtml')
c2.set_content('<h1>About this book</h1><p>This is a book.</p>')

book.toc = (c1, c2)

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

epub.write_epub('test.epub', book)
