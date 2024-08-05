import logparser

logfile = open("/home/mid/analisa-log/log1.txt","r")

hour = {}

for line in logfile:
    
  logParts = logparser.parser(line)

  host = logParts["host"]
  
  getTime = logParts["time"].split(":")[1]
  tgl = logParts["time"].split(":")[0]
  time = tgl + '|' + getTime

  if time not in hour:
    
    hour[time] = 1
    
    # if host not in hour[time]:
      
    #   hour[time][host] = 1
    # else:
        
    #   hour[time][host] = hour[time][host] + 1
    
  else:
    # if host not in hour[time]:
        
    #   hour[time][host] = 1
    
    # else:
    #   hour[time][host] = hour[time][host] + 1
    hour[time] = hour[time] + 1  
for item in hour:
  
  # print("The date in which below details are of :-",item)
  print(f'tanggal : {item.split("|")[0]} jam : {item.split("|")[1]} count : {hour[item]}')
  # print(hour[item], "\n")
