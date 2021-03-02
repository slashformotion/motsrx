# Twitter dictionary bot

## Requirements

Python 3.7 or higher

### Python Dependance

- tweepy
- larousse-api-sunbro

To install :
- avec pip:
```
$ pip install tweepy larousse-api-sunbro
```

- avec pipenv:
```
$ pipenv install tweepy larousse-api-sunbro && pipenv check
```

## How to set up

```
$ git clone https://github.com/slashformotion/motsrx
$ cd motsrx
$ touch .env
```

Edit `.env` to add the environnment variables :

```
CONSUMER_KEY=...
CONSUMER_SECRET=...
ACCESS_TOKEN=...
ACCESS_TOKEN_SECRET=...
ACCOUNT=...
```

## Run 

```
$ python3 bot.py
```

Result : 

![](assets/exemple.png)