from ebooklib import epub

book = epub.EpubBook()

# add metadata
book.set_identifier('sample123456')
book.set_title('Sample book')
book.set_language('en')

book.add_author('Sample Author')

# intro chapter
c1 = epub.EpubHtml(title='Introduction', file_name='intro.xhtml', lang='en')
c1.content = u'<html><head></head><body><h1>Introduction</h1><p>Introduction paragraph where i explain what is happening.</p></body></html>'

# about chapter
c2 = epub.EpubHtml(title='About this book', file_name='about.xhtml', lang='en')
c2.content = '<h1>About this book</h1><p>http://www.example.com<br/>http://www.example.org</p>'

# add chapters to the book
book.add_item(c1)
book.add_item(c2)

# create table of contents
book.toc = (c1, c2)

# add navigation files
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# create spine
book.spine = [c1, c2]

# create epub file
epub.write_epub('test.epub', book, {})
