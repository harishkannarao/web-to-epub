from ebooklib import epub
import requests
from readabilipy import simple_json_from_html_string, simple_tree_from_html_string

# req = requests.get('https://en.wikipedia.org/wiki/Readability')
req = requests.get('https://blogs.harishkannarao.com/2021/03/reactjs-nodejs-for-java-developers.html')
article = simple_json_from_html_string(req.text, use_readability=True)['plain_content']

book = epub.EpubBook()

# add metadata
book.set_identifier('sample123456')
book.set_title('Sample book')
book.set_language('en')

book.add_author('Sample Author')

# intro chapter
c1 = epub.EpubHtml(title='Introduction', file_name='intro.xhtml', lang='en')
c1.content = article

# about chapter
c2 = epub.EpubHtml(title='About this book', file_name='about.xhtml', lang='en')
c2.content = '<h1>About this book</h1><p>http://www.example.com<br/>http://www.example.org</p>'

chapters = [c1, c2]

# add chapters to the book
for chapter in chapters:
    book.add_item(chapter)

# create table of contents
book.toc = chapters

# add navigation files
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# create spine
book.spine = chapters

# create epub file
epub.write_epub('test.epub', book, {})
