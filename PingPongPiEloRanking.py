import math

K = 32

def CalculateElo(p1ID, p2ID, p1Score, p2Score):
	oldRating1 = math.pow(10, GetElo(p1ID) / 400)
	oldRating2 = math.pow(10, GetElo(p2ID) / 400)

	expected1 = oldRating1 / (oldRating1 + oldRating2)
	expected2 = oldRating2 / (oldRating1 + oldRating2)

	result1 = 0.5 + (0.5 * ((p1Score - p2Score) / 11))
	result2 = 0.5 + (0.5 * ((p2Score - p1Score) / 11))

	newRating1 = GetElo(p1ID) + (K * (result1 - expected1))
	newRating2 = GetElo(p2ID) + (K * (result2 - expected2))

	RecordGame(p1ID, p2ID, p1Score, p2Score, round(newRating1, 2) - GetElo(p1ID), round(newRating2, 2) - GetElo(p2ID))

	SetElo(p1ID, round(newRating1, 2))
	SetElo(p2ID, round(newRating2, 2))

	return GetData()

def RecordGame(p1ID, p2ID, p1Score, p2Score, p1EloChange, p2EloChange):
	hist = open("RankedHistory.txt", "a")
	if p1Score > p2Score:
		hist.write(p1ID + "(+" + str(round(p1EloChange, 2)) + ") " + str(p1Score) + " - " + str(p2Score) + " " + p2ID + "(" + str(round(p2EloChange, 2)) + ")\n")
	else:
		hist.write(p2ID + "(+" + str(round(p2EloChange, 2)) + ") " + str(p2Score) + " - " + str(p1Score) + " " + p1ID + "(" + str(round(p1EloChange, 2)) + ")\n")

	hist.close()

def SetElo(pID, pElo):
	data = GetData()
	if pID in data:
		data[pID] = pElo
		SetData(data)

def GetElo(pID):
	data = GetData()
	if pID in data:
		return data[pID]

def SetData(data):
	elo = open("EloRanking.txt", "w+")
	elo.seek(0, 0)
	for k in data:
		elo.write(k + "\n" + str(data[k]) + "\n")
	elo.close()

def GetData():
	elo = open("EloRanking.txt", "r")
	elo.seek(0, 0)

	data = {elo.readline().strip():elo.readline().strip(), elo.readline().strip():elo.readline().strip(), elo.readline().strip():elo.readline().strip()}
	for i in data:
		data[i] = round(float(data[i]), 2)

	elo.close()

	return data