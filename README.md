# web-to-epub

python script to convert web page(s) as epub book

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

    python main.py --output-file /tmp/example.epub --input-urls http://www.example.com http://www.example.org

    python main.py --output-file /tmp/example.epub --urls-file /tmp/example_urls.txt

or 

    python main.py -o /tmp/example.epub -i http://www.example.com http://www.example.org

    python main.py -o /tmp/example.epub -f /tmp/example_urls.txt
    
### Verify flake8

    make flake8
    
### Create requirements.txt

    make requirements
