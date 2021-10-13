# Simple test of spaCy for document parsing

* Simple test that reads in a pdf, parses the text with spaCy using a set of defined keywords, and outputs a pretty result.
* Output can be visualized at `localhost:5000`.


## Setup

**Requirement:** python3

0. Set up python virtual environment

I have been running this in a python virtual environment and this seems to work well to avoid shenanigans with other python versions/libraries on my local machine.
But this is not a strict requirement - you do you.


To set up the virutal env in your working directory:
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

When you are finished in the virtual environment, you can exit it with
```
$ deactivate
```

1. Make sure pip is up to date:
```
$ python3 -m pip install --upgrade pip
```


2. Install required packages:
```
$ python3 -m pip install -U pip setuptools wheel
$ python3 -m pip install spacy
$ python3 -m spacy download en_core_web_sm
$ python3 -m pip install pdfplumber
```

3. Run it an behold the results at `localhost:5000` !
```
$ python3	process-pdf.py Sample-Contract.pdf
```
