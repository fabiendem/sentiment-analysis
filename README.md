## Setup

Only tested with Python 3.x

### Add ENV vars

Export the following ENV vars:

Bash

```sh
export FLASK_APP=index.py
export ASK_ENV=development
export NLTK_DATA ~/Projects/sentiment/nltk
```

:fish:

```sh
set --export FLASK_APP index.py
set --export FLASK_ENV development
set --export NLTK_DATA ~/Projects/sentiment/nltk
```

### Setup the environment

```sh
python3 -m venv venv
```

Activate it

```
. venv/bin/activate
```

### Install deps

```sh
pip install -r requirements.txt
python3 -m textblob.download_corpora
```

### Run server

```sh
flask run
```

Tunnel with ngrok

```
/Applications/ngrok http 5000
```
