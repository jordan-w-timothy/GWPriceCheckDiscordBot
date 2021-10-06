import discord
import os
import requests
import json
import random
import io
import aiohttp
import datetime
import time

client = discord.Client()



def convertTime(timeStamp):
    # now = date.now()
    # Timestamp comes in millisceonds so must be converted to seconds.
    postTime =  timeStamp / 1000
    

    return  datetime.datetime.fromtimestamp(postTime)
    

def calcTimeSense(timeStamp):
    hours = 0
    # Timestamp comes in millisceonds so must be converted to seconds.
    postTime =  timeStamp / 1000
    # Get the currentTime timestamp.
    currentTime = time.time()
    # print("CurrentTime " + str(currentTime) + " | " + str(datetime.datetime.fromtimestamp(currentTime)))
    # print("Post Time " + str(postTime) + " | " +  str(datetime.datetime.fromtimestamp(postTime)))
    #Calculate the diff between currentTime and postTime in seconds.
    timeDiff = currentTime - postTime
    # print("Time Diff in seconds " + str(timeDiff))
    #Check if longer than an hour if so get number of hours and store remainder.
    if timeDiff > 60.0:
        hours = timeDiff // 3600
        hours = int(hours)
        afterHour = timeDiff % 3600
        timeDiff = afterHour
    #Calculate the number of minutes since the postTime to currentTime.
    mins = timeDiff // 60
    mins = int(mins)
    # print("Diff(Minutes) " + str(mins))
    #Calculate the seconds left after getting minutes.
    seconds = timeDiff % 60
    seconds = int(seconds)
    # print("Diff(Seconds) " + str(seconds))
    expiredTime = [hours, mins, seconds]
    return expiredTime



# myTime = convertTime(1633485427152)
# print(myTime)

# expiredTime = calcTimeSense(1633485427152)
# print(expiredTime)


def getKamadanTrade(searchWord):
  pNum = searchWord
  response = requests.get("https://kamadan.gwtoolbox.com/s/{}/0/0".format(pNum))
  
  json_data = json.loads(response.text)
#   print(json_data[0])
  #Get the Current Time.
  currentTime = datetime.datetime.fromtimestamp(time.time())
  responseText = "Current Time: " + str(currentTime) + " EST"
  responseText += "\n"
  count = 0
  for i in json_data:
      if count < 10 :
            # timeStamp = 1633447931249
            # dt_object = time.ctime(1633447931249)
            # print(dt_object)
            #Get the time of the post.
            postTime = convertTime(i['t'])
            #Get the minutes expired since post.
            timeDiff = calcTimeSense(i['t']) 
            if timeDiff[0] < 1:
                # print(str(timeDiff[0]) + " in if ")
                # responseText += "\n" + "Time of Post: " + str(postTime) +   "\nName:  " +  str(i['s'] + " \n" +  str(i['m']) + "\n" + str(timeDiff[0]) + " Hours and "  + str(timeDiff[1]) + " minutes and " + str(timeDiff[2]) + " seconds ago.")
                responseText += "\nName:  " +  str(i['s'] + " \n" +  str(i['m']) + "\n"  + str(timeDiff[1]) + " minutes and " + str(timeDiff[2]) + " seconds ago.")
                responseText += "\n"
            else:
                # print(str(timeDiff[0]) + " not in if")
                responseText += "\nName:  " +  str(i['s'] + " \n" +  str(i['m']) + "\n" + str(timeDiff[0]) + " Hours and "  + str(timeDiff[1]) + " minutes and " + str(timeDiff[2]) + " seconds ago.")
                responseText += "\n"
            # print(i['t'])
            count+=1
      
     

  tradeList = responseText
  return(tradeList)

def getAscalonTrade(searchWord):
  pNum = searchWord
  response = requests.get("https://ascalon.gwtoolbox.com/s/{}/0/0".format(pNum))
  
  json_data = json.loads(response.text)
#   print(json_data[0])
  #Get the Current Time.
  currentTime = datetime.datetime.fromtimestamp(time.time())
  responseText = "Current Time: " + str(currentTime) + " EST"
  responseText += "\n"
  count = 0
  for i in json_data:
      if count < 10 :
            # timeStamp = 1633447931249
            # dt_object = time.ctime(1633447931249)
            # print(dt_object)
            #Get the time of the post.
            postTime = convertTime(i['t'])
            #Get the minutes expired since post.
            timeDiff = calcTimeSense(i['t']) 
            if timeDiff[0] < 1:
                # print(str(timeDiff[0]) + " in if ")
                # responseText += "\n" + "Time of Post: " + str(postTime) +   "\nName:  " +  str(i['s'] + " \n" +  str(i['m']) + "\n" + str(timeDiff[0]) + " Hours and "  + str(timeDiff[1]) + " minutes and " + str(timeDiff[2]) + " seconds ago.")
                responseText += "\nName:  " +  str(i['s'] + " \n" +  str(i['m']) + "\n"  + str(timeDiff[1]) + " minutes and " + str(timeDiff[2]) + " seconds ago.")
                responseText += "\n"
            else:
                # print(str(timeDiff[0]) + " not in if")
                responseText += "\nName:  " +  str(i['s'] + " \n" +  str(i['m']) + "\n" + str(timeDiff[0]) + " Hours and "  + str(timeDiff[1]) + " minutes and " + str(timeDiff[2]) + " seconds ago.")
                responseText += "\n"
            # print(i['t'])
            count+=1
      
     

  tradeList = responseText
  return(tradeList)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('-pc -k $'):
        print("Message Recieved \n" + message.content)
        inputMessage = str(message.content)

        # print("The inputMessage is: ", inputMessage)

        searchTerm = inputMessage.split("$")
        print(" SearchTerm is  " + searchTerm[1])
        
        pokemon = getKamadanTrade(searchTerm[1])
        await message.channel.send(pokemon)

    if message.content.startswith('-pc -a $'):
        print("Message Recieved \n" + message.content)
        inputMessage = str(message.content)

        # print("The inputMessage is: ", inputMessage)

        searchTerm = inputMessage.split("$")
        print(" SearchTerm is  " + searchTerm[1])
        # print(" SearchTerm is  " + searchTerm[1])
        
        pokemon = getAscalonTrade(searchTerm[1])
        await message.channel.send(pokemon)

    

client.run("ODk1MTU1NzE1MzQwMTIwMDc0.YV0cuQ.RiN59NXX_KNwZLG-iDDdC7rKLUg")