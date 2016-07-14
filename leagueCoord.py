import requests, time


def getSummonerId(username):
	# username : the username used by the player to sign onto League of Legends
	#
	# returns : summonerId , id number corresponding to given username

	# get summoner ID
	url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + username + '?api_key=[API KEY HERE]'
	response = requests.get(url)
	response_json = response.json()
	#print("SummonerId: " + str(summonerId))

	summonerId = response_json[username]['id']
	return summonerId
	

def getMatchIds(summonerId):
	# summonerId : id number for the given player username, use getSummonerId to get this value
	#
	# returns : matchIds , a list of all matchId numbers for every ranked game played by the player
	# get Match IDS
	url = 'https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/' + str(summonerId) + '?api_key=f70f9a95-b58f-4784-aa28-cf2b6d7724b6'
	response = requests.get(url)
	response_json = response.json()

	matchIds = []
	for item in response_json['matches']:
		matchIds.append(item['matchId'])

	#print("Number of ranked matches played: " + str(len(matchIds)))

	return matchIds
	

def getPositionData(matchIds, data):
	# matchIds : list of match Ids
	# data : list in which to put the data into (should be initialized in main() )
	#
	# returns : data  , a list containing all the position data for each player for every ranked game the player has played

	# Calculate runtime and set delay so too rate limit for API isn't exceeded
	delay = 1.5
	loopTime = 2
	timeToRun = len(matchIds) * ( delay + loopTime )
	print("Estimated time to run : " + str(timeToRun))

	# get position data [x,y] for every player for each match ID and append it to data list
	for matchId in matchIds:
		# build url for API request

		#print(matchId)
		url = 'https://na.api.pvp.net/api/lol/na/v2.2/match/' + str(matchId) + '?includeTimeline=true&api_key=f70f9a95-b58f-4784-aa28-cf2b6d7724b6'
		#print(url)
		response = requests.get(url)
		response_json = response.json()
		#data.append('START OF MATCH: ' + str(matchId))

		# Getting errors on certain matches, use try to skip these. Not sure why but error will be given on different matches when script is rerun. 
		# Might be something to do with API server
		try: 

			for frame in response_json['timeline']['frames']:
				# sometimes the last frame of a game does not contain position data, use try for error checking
			    try:
				    data.append([frame['participantFrames']['1']['position']['x'] , frame['participantFrames']['1']['position']['y']])
				    data.append( [frame['participantFrames']['2']['position']['x'] , frame['participantFrames']['2']['position']['y'] ] )
				    data.append( [frame['participantFrames']['3']['position']['x'] , frame['participantFrames']['3']['position']['y'] ] )
				    data.append( [frame['participantFrames']['4']['position']['x'] , frame['participantFrames']['4']['position']['y'] ] )
				    data.append( [frame['participantFrames']['5']['position']['x'] , frame['participantFrames']['5']['position']['y'] ] )
				    data.append( [frame['participantFrames']['6']['position']['x'] , frame['participantFrames']['6']['position']['y'] ] )
				    data.append( [frame['participantFrames']['7']['position']['x'] , frame['participantFrames']['7']['position']['y'] ] )
				    data.append( [frame['participantFrames']['8']['position']['x'] , frame['participantFrames']['8']['position']['y'] ] )
				    data.append( [frame['participantFrames']['9']['position']['x'] , frame['participantFrames']['9']['position']['y'] ] )
				    data.append( [frame['participantFrames']['10']['position']['x'] , frame['participantFrames']['10']['position']['y'] ] )
			    except KeyError:
			    	continue

		except KeyError:
			continue

		# delay loop so API request limit is not exceeded
		time.sleep(delay)

	return data

def writeToFile(data):
	# writes the data to file
	# data : list containing all position data
	#
	# creates a text file with the data in the same directory as the script
	textFile = open("heatMapData.txt", "w")
	textFile.write(data)
	textFile.close()


def main():
	username = 'andhint'
	summonerId = getSummonerId(username)
	matchIds = getMatchIds(summonerId)
	#testMatchIds = matchIds[0:15]
	#print(matchIds)
	data = []
	data = getPositionData(matchIds, data)
	writeToFile(str(data))
	


main()