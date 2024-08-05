import sys

try:
    namalogfile = sys.argv[1] 
except:
    namalogfile = "autotwitreply.log"
with open(namalogfile,"r") as flog:
    lines = flog.readlines()

sessions = []
session = {
    "account":"",
    "first":"",
    "last":"",
    "count":0,
    "error":0
}
sessions.append(session)

skipnext = False
i = 0
for line in lines:
    i+=1
    if skipnext:
        skipnext = False
        continue
    logstrs = line.split(" - autotwitreply - INFO - ")
    datestr = logstrs[0]
    try:
        msg = logstrs[1]
    except:
        # print(f"error di line : {i}")
        continue
    if (msg[:10] == "twit sent "):
        continue
    elif (msg[:11] == "twit failed"):
        skipnext = True        
        session["error"]+=1
        continue
    else:
        msgstrs = msg.split(" , ",1)
        msg_account = msgstrs[0]
        if session["account"] != msg_account:
            if session["account"] == "":
                session["account"] = msg_account
                session["first"] = datestr
            else:
                session = {
                    "account":msg_account,
                    "first":datestr,
                    "last":"",
                    "count":0,
                    "error":0
                }
                sessions.append(session)
        session["count"]+=1
        session["last"]= datestr


i = 0
with open(f"summarytweet.{namalogfile.replace('.log','')}.csv","w") as flog:
    flog.write(f"no;account;first;last;count;error\n")
    print("no;account;first;last;count;error")
    for session in sessions:
        i+=1
        flog.write(f"{i};{session['account']};{session['first']};{session['last']};{session['count']};{session['error']}\n")
        print(f"{i};{session['account']};{session['first']};{session['last']};{session['count']};{session['error']} ")

