# web-to-epub

python script to convert web page(s) as epub book.

This script is built around Alan Turing Institute's [Readabilipy](https://github.com/alan-turing-institute/ReadabiliPy) python library, which in turn is a wrapper around Mozilla's [Readability](https://github.com/mozilla/readability) Node.js package. Hence you need to have a working [Node.js](https://nodejs.org/en/download/) installation of version 10 or higher. Make sure to install Node.js before running this script, as this ensures Readability.js will be installed.

Credit goes to the authors and contributors of the following repositories:

* [alan-turing-institute/ReadabiliPy](https://github.com/alan-turing-institute/ReadabiliPy)
* [mozilla/readability](https://github.com/mozilla/readability)
* [aerkalov/ebooklib](https://github.com/aerkalov/ebooklib)

## Tools Required

* python `3.9`
* node `12.0.0` or `latest`
* make `3.81`
* git `latest`
* pycharm `latest`

## Commands

### Install dependencies

    make init

### Run python script to convert web page(s) to epub

    pipenv run python main.py --output-file /tmp/example.epub --input-urls http://www.example.com http://www.example.org

    pipenv run python main.py --output-file /tmp/example.epub --urls-file /tmp/example_urls.txt

or 

    pipenv run python main.py -o /tmp/example.epub -i http://www.example.com http://www.example.org

    pipenv run python main.py -o /tmp/example.epub -f /tmp/example_urls.txt
    
### Verify flake8

    make flake8
    
### Create requirements.txt

    make requirements
