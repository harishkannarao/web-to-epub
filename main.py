from ebooklib import epub
import requests
from readabilipy import simple_json_from_html_string
import argparse


def read_file(file_name):
    lines = []
    with open(file_name) as file:
        for line in file:
            lines.append(line.rstrip('\n'))
    return lines


my_parser = argparse.ArgumentParser(description='Convert web page(s) as epub')
my_parser.add_argument('--input-urls', '-i', action='store', nargs='+', type=str, required=False)
my_parser.add_argument('--urls-file', '-f', action='store', type=str, required=False)
my_parser.add_argument('--output-file', '-o', action='store', type=str, required=True)

args = my_parser.parse_args()

urls = []
if args.urls_file is not None:
    urls = read_file(args.urls_file)
else:
    urls = args.input_urls

book = epub.EpubBook()

# add metadata
book.set_identifier('web-to-epub')
book.set_title('Book created with web-to-epub')
book.set_language('en')
book.add_author('Computer Program')

chapters = []
for num, url in enumerate(urls, start=1):
    req = requests.get(url)
    article = simple_json_from_html_string(req.text, use_readability=True)
    content = f"<h1>Chapter {num}</h1>"
    content += f"<h1>{article['title']}</h1>"
    content += article['plain_content']
    title = f"{num} - {article['title']}"
    chapter = epub.EpubHtml(title=title, file_name=f"{num}.xhtml", lang='en')
    chapter.content = content
    chapters.append(chapter)

source_url_content = '<h1>Source URLs</h1>'
for url in urls:
    source_url_content += f"<br/>{url}"
source_url_chapter = epub.EpubHtml(title='Source URLs', file_name='source_urls.xhtml', lang='en')
source_url_chapter.content = source_url_content
chapters.append(source_url_chapter)

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
epub.write_epub(args.output_file, book, {})
