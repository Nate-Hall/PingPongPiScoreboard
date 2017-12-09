def CalculateElo(p1ID, p2ID, p1Score, p2Score):
	pass

def SetElo(pID, pElo):
	pass

def GetElo(pID, pElo):
	pass

def SetData(data):
	elo = open("EloRanking.txt", "w+")
	elo.seek(0, 0)
	k = list(data.keys())
	for i in k:
		elo.write(i + "\n")
		elo.write(data[i] + "\n")

def GetData():
	elo = open("EloRanking.txt", "r")
	elo.seek(0, 0)

	data = {elo.readline().strip():elo.readline().strip(), elo.readline().strip():elo.readline().strip(), elo.readline().strip():elo.readline().strip()}
	for i in data:
		data[i] = int(data[i])

	elo.close()

	sortedData = [(k, data[k]) for k in sorted(data, key=data.get, reverse=True)]
	print(sortedData)
	return sortedData

SetData(GetData())