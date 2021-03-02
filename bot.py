import tweepy
import logging
from config import create_api, get_account
import time
import dictionaire as dico
from larousse_api import larousse
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    api = create_api()
    since_id = max([i.id for i in api.mentions_timeline()])
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(5)


def send_reply(msg, tweet, api):
    api.update_status(status=msg,in_reply_to_status_id=tweet.id)

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in api.mentions_timeline(since_id=since_id):
        # on met à jour l'index
        new_since_id = max(tweet.id, new_since_id)

        # on regarde quel est le tweet
        logger.info(f"{tweet.user.screen_name} said: '{tweet.text}'")
        texte = tweet.text

        # on vérifie si  le tweet n'est pas vide
        if texte == "" :
            logger.info(f"SKIPPED : tweet empty")
            continue

        # if os.getenv('ACCOUNT') == tweet.in_reply_to_screen_name:
        #     logger.info(f"SKIPPED : in_reply_to_myself")
        #     continue
    
        # on vérifie que le tweet est en français
        # if not tweet.lang == 'fr':
        #     logger.info("WARNING : tweet in foreign language")
        #     send_reply("We only use french word my friend ! ", tweet, api)
        #     continue

        # traitment du texte 
        texte = texte.replace(get_account(), "")
        terms = texte.strip().lower().split(" ")

        logger.info(f"--terms found : {terms}")
        logger.info(f"--term retained : {terms[0]}")

        results = larousse.get_definitions(terms[0])
        if len(results)==0:
            send_reply(f"Définition pour '{terms[0]}' non trouvée", tweet, api)
            logger.info(f"SKIPPED : définition for '{terms[0]}' not found")
            continue

        trunc_result = results[0][0:247-4-len(terms[0])]
        reply = f"{terms[0]}: {trunc_result}"
        send_reply(
            reply,
            tweet,
            api
        )
        logger.info(f"Response sent:{reply}")
    return new_since_id



if __name__ == "__main__":
    # api = create_api()
    # from pprint import pprint
    # pprint()
    
    main()
    # print(type(get_account()))