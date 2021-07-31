import requests
import csv
import json
import time

# Convert a curl request into a python request
# https://curl.trillworks.com

allData = []
uniqueData = []
token =""

def create_unique_list():
	for row in allData:
		if not(row in uniqueData):
			uniqueData.append(row)


def get_token():
	f = open("token.txt", "r")
	return f.read()



class Song:
	def __init__(self, artist, album, track, time):
		self.track = track
		self.artist = artist
		self.album = album
		self.time = time


	def __eq__(self, other):
		if isinstance(other, Song):
			return (self.track == other.track and self.artist == other.artist and self.album == other.album)
		return False

	def __str__(self):
		string = "Song = "+self.track+"\n\t artist = "+self.artist+"\n\t album = "+self.album
		return string



token = get_token();

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+token,
}

with open('dataMin.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		s = Song(row[0],row[1],row[2],row[3])
		allData.append(s)


create_unique_list()

for row in uniqueData:

	
	##params = (('q', 'artist: Velvet Revolver track:Fall to Pieces album:Contraband'),('type', 'track'),)
	#print(params)
	params = (('q', 'artist:'+row.artist+' track:'+row.track+' album:'+row.album),('type', 'track'),)
	print(params)
	response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
	print(response.text)
	data = response.json();
	
	#print(dir(data))
	#print(data.items)
	print("\n\n")
	time.sleep(1)

	

'''
print("Size of allData = "+str(len(allData)))
create_unique_list()
print("Size of uniqueData = "+str(len(uniqueData)))'''






'''
response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)


print(response)
data = response.json();
print(data)'''