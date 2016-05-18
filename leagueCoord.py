import requests

# define request url for Riot API
url = 'https://na.api.pvp.net/api/lol/na/v2.2/match/2108173564?includeTimeline=true&api_key=[API KEY HERE]'


response = requests.get(url)
response_json = response.json()
data = []

# pull out position data for each player at every time step (every 60s)
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
    	print("position DNE")
    	

print(data)


