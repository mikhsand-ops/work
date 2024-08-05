import tweepy
import openai
import time
import datetime
import random
import pytz
import requests


import logging
import logging.handlers
# create logger
appname = 'auto_replytoaccNretweet'
logger = logging.getLogger(appname)
logger.setLevel(logging.INFO)

# create Timed Rotating Fle handler and set level to WARNING

filename = f"log/{appname}.log"
ch = logging.handlers.TimedRotatingFileHandler(filename,'midnight',1)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

test = 0
tags = "PTPNPalmCo"
tanyagambar = "jelaskan dengan satu kalimat singkat bagaimana kebijakan Pemerintah Indonesia pada penggabungan 13 perusahaan di bawah Holding Perkebunan Nusantara, menjadi dua Sub Holding, yakni PalmCo dan SupportingCo terhadap ketahanan ekonomi Indonesia dan hilirisasi produk kelapa sawit."
peranjawab = "anda adalah seorang juru bicara pemerintahan Indonesia yang membahas tentang penggabungan 13 perusahaan di bawah Holding Perkebunan Nusantara, menjadi dua Sub Holding, yakni PalmCo dan SupportingCo . Penggabungan ini dipercaya mampu berkontribusi meningkatkan produksi CPO nasional dan minyak goreng dalam negeri. PTPN memperkirakan, produksi minyak gorengnya akan meningkat dari 460.000 ton/tahun di 2021 menjadi 1,8 juta ton/tahun (4 kali lipat) di 2026. Tujuan besarnya adalah memaksimalkan nilai aset landbank untuk mendapatkan nilai tambah, peningkatan margin EBITDA dalam 5 tahun mendatang, peningkatan ESG dan ketahanan pangan, peningkatan ekuitas, hingga peningkatan leadership. berikan komentar singkat dan jelas dalam satu kalimat."
medianame = "PTPNPalmCo"
medianum = 8
account_to_reply = "standwrt"
servernamereadfile = "minji"

acctname = "GastonHarl58608"
DSApiKey = "NIMK9fA4v8tKKefptVVb285Or"
DSAPISecret = "sPrH8NSSRC3ICgCbxLkKRcRByTcUd3EVR4jCLvriO6ZZvBOLMS"
DSBearer = "AAAAAAAAAAAAAAAAAAAAALNbrgEAAAAA1n%2BPqGUmgLPoBqaa1eueTrtO4s0%3D0H7hjoq4SJATVMRqn4vroOCUIyVHI6R1ZVWIuIqb5YGOEQbqGd"
DSToken = "1730221626048823296-mwvXOStxUT5Z2kLn2sc4VLz4KxfCjd"
DSTokenSecret = "7bQolkNGezUZEjjb8Nlhr6VxmLsinbucsJlzfnnD4Trnd"

gambar  = 0
twitcount = 0
getout = 0


while 1 :
    waktu_tidur = 120

    cc = 0
    tanya = tanyagambar
    jawab = ""



    # Authenticate to Twitter
    twitter_auth = {
        "consumer_key": DSApiKey,
        "consumer_secret": DSAPISecret,
        "bearer_token": DSBearer,
        "access_token": DSToken,
        "access_token_secret": DSTokenSecret, #TA
    }

    clientv2 = tweepy.Client(
        bearer_token=twitter_auth["bearer_token"],
        consumer_key=twitter_auth["consumer_key"],
        consumer_secret=twitter_auth["consumer_secret"],
        access_token= twitter_auth["access_token"],
        access_token_secret=twitter_auth["access_token_secret"],
        wait_on_rate_limit=False)

    # initiate tweepy clientv1
    auth = tweepy.OAuth1UserHandler(
        twitter_auth["consumer_key"],
        twitter_auth["consumer_secret"]
        )
    auth.set_access_token(
        twitter_auth["access_token"],
        twitter_auth["access_token_secret"],
    )
    clientv1 = tweepy.API(auth)

    conversation = []
    
    role = peranjawab

    print( f"pertanyaan : {tanya}" )
    conversation.append({"role": "system", "content": role})
    conversation.append({"role": "user", "content":tanya})
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=conversation#,
                        #max_tokens=60
            )

    bot_response = response.choices[0].message['content']
    print( f"bot response: {bot_response}" )


    jawab = bot_response
    #tweet = f"Q:{tanya} A: {jawab}"
    tweet = bot_response
    # Mengambil waktu saat ini
    waktu_sekarang = datetime.datetime.now()

    # Mendapatkan menit dan detik dari waktu saat ini
    menit = waktu_sekarang.minute
    detik = waktu_sekarang.second

    print(f"Menit: {menit}")
    print(f"Detik: {detik}")
    stamp = f"{menit}{detik}"
    print( stamp )



    try  :
        # Membagi tweet menjadi bagian-bagian dengan panjang maksimum, memotong pada spasi
        panjang_maksimum = 250
        tweets = []
        while len(jawab) > panjang_maksimum:
            last_space = jawab.rfind(' ', 0, panjang_maksimum)
            if last_space == -1:
                last_space = panjang_maksimum
            tweets.append(jawab[:last_space])
            jawab = jawab[last_space + 1:]
        tweets.append(jawab)



        # Menampilkan setiap tweet
        for i, tweet in enumerate(tweets):
            full_tweet = f"{i + 1}/{len(tweets)} {tweet}"
            full_tweet = stamp + "-" + full_tweet + " #" + tags
            print(full_tweet)
            print( "Sending Twit ...")
            # Kirim tweet
            coba = 0


            print( "Kirim dgn gambar ...")
            print( "Acct Name: " + acctname )

            # Lokasi file gambar yang ingin dikirim
            # upload image
            gambar = gambar % medianum
            gambar = gambar + 1
            print( f"Gambar: {gambar}" )
            medianm = medianame + str(gambar) + ".jpeg"
            print( f"Media : {medianm}")
            teks = tweet + " #" + tags

            # tweet msg with image
            msg = f"tahu gak @{account_to_reply}? {teks}"
            try :
                print( "kirim tweet gambar..." )


                if test != 1 :
                    nowlog = time.time()

                    # randrep = random.randint(1,10)
                    # if(randrep%2==0):
                    #   response = clientv2.create_tweet(text=msg,media_ids=[media_id])
                    # else:

                    media_path = medianm  #lokasi dari gambar tersebut
                    media = clientv1.media_upload(filename=media_path)
                    media_id = media.media_id
                    response = clientv2.create_tweet(text=msg, media_ids=[media_id])
                    print(response)

                    this_tweet_id = response.data["id"]

                    twitcount += 1
                    logger.info(f"twit sent with text and picture")
                    logger.info(f"{acctname} , {msg} , {media_path}")
                    time.sleep(10)

            except Exception as e:
                # Mencetak exception
                print("Terjadi error:", e)
                logger.info(f"twit failed : {nowlog}. Error : {str(e.response)}")
                logger.info(f"{acctname} , Error : {str(e.response)}")

                if("400" in str(e)):
                    continue

                if("326" in str(e)):
                    print("account banned")
                    continue

                getout = 1

                print( "error: " + str(e.response.headers) )
                print( "Limit User: " + str(e.response.headers['x-user-limit-24hour-remaining'] ))
                print( "Limit Apps: " + str(e.response.headers['x-app-limit-24hour-remaining'] ))
                limituser = int(e.response.headers['x-user-limit-24hour-remaining'] )
                limitapps = int(e.response.headers['x-app-limit-24hour-remaining'] )
                if "261" in str(e.response.headers) :
                    limitapps = 1000
                if limitapps == 0 :
                    print( "Apps Limit. Exiting ...")
                    getout = 1
                    exit()
                if limituser == 0 :
                    print( "User Limit. Next ...")
                    break
                if limitapps > 0 :
                    print( "Blocked by Twitter!!!")
                    print( "TwitCount : " + str(twitcount) )

                    waktu_sekarang = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))

                    # Mendapatkan menit dan detik dari waktu saat ini
                    jam = waktu_sekarang.hour
                    menit = waktu_sekarang.minute
                    detik = waktu_sekarang.second

                    stamp = f"Time: {jam}:{menit}:{detik}"
                    print( stamp )
                    print( "TwitCount : " + str(twitcount) )
                    getout  = 1

                    exit()


            #print(f"msg: {msg}")
            #print(f"response: {response}")
    #teks = input( "klik Enter... " )

    except Exception as e:
    # Mencetak pesan error
        print("Terjadi error lagi:", e)
        cc = 101
        if getout == 1 :
            exit()


    sukses_retweet = 0
    while(not sukses_retweet):
        print(f"try to retweet..")
        time.sleep(30)
        # readfile from minji
        url = f"https://{servernamereadfile}.cayangqu.com/{tags}.txt?a=1"

        try:
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Split the response text into lines
                lines = response.text.split('\n')
                print("success get file")

                # Iterate through each line
                for line in lines:
                    # Split each line by comma
                    if(line != ""):
                        username, rtweet_id = line.split(',')

                        # Print the separated values
                        # clientv2.retweet(tweet_id)
                        # logger.info(f"twit quote retweeted")
                        # logger.info(f"{acctname} , {tweet_id}")

                        if(username == acctname and this_tweet_id < rtweet_id):
                            print(f"Username: {username}, tweet_id: {rtweet_id}")
                            msgquote = f"#{tags}"
                            response = clientv2.create_tweet(text=msgquote, quote_tweet_id=rtweet_id)
                            logger.info(f"twit quote tweeted")
                            logger.info(f"{acctname} , {msgquote}")

                            sukses_retweet = 1
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"An error occurred: {e}")

    exit()
    # print(f"sleeping for {waktu_tidur}s")
    # time.sleep( waktu_tidur )

    #teks = input( "tunggu ...")
