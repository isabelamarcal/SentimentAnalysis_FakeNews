import tweepy
import csv
import time
import io


consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

arq = csv.writer(open("base_teste.csv","w", encoding="utf-8"))
arq2 = io.open("base_teste_json.json","w", encoding="utf-8")

row = []

statuses = tweepy.Cursor(api.search, q='politica', since='2018-06-20', until='2018-06-26', lang='pt').items()


while True:
    try:
        status = statuses.next()
        row = str(status.user.screen_name),str(status.created_at),str(status.text)

        arq.writerow(row)
        arq2.write(str(status))
        arq2.write("\n")
       #exit()

    except tweepy.TweepError:
        print('wait 15 min')
        time.sleep(60*15)
        continue
    except StopIteration:
        print('acabou é hexa')
        break


