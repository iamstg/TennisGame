##Comments: Deuce will be printed as 40 - 40
##	    Advantage will be printed as 40 - Advantage or Advantage - 40
##          Winner is neither decided by set of three or five as it was not specified
##          At the EOF, winner will be printed on the basis of higher scores
## 	    if scores are equal, match will be considered tie
#!/usr/bin/python
import sys
import os
import re
from sys import stdin
os.system('clear')
iteration = 1
playerturn = 1
serveturn = 1
P1score=0
P1set=0
P1game=0
P2score=0
P2set=0
P2game=0
P1tb=0
P2tb=0
itr = 0
def printIteration():
	global itr
	itr += 1
	print "Iteration : "+str(itr)

def compareString(job,string):
	x=re.compile(job)
	r=x.match(string)
	if r is None:
		return 1
	else:
		return 0

def changeServe():
	global serveturn
	if serveturn == 1:
		serveturn = 2
	else:
		serveturn = 1

class Count:
	"""TODO: Reduce global variables."""
	global playerturn
	global P1set
	global P1game
	global P1score
	global P1tb
	global P2set
	global P2game
	global P2score
	global P2tb
	def __init__(self,playerturn,setwon,gamewon,score,tiebreaker):
		self.player=playerturn
		self.sets=setwon
		self.game=gamewon
		self.score=score
		self.tb=tiebreaker

	def IncrementSetCount(self):
	 	self.sets = self.sets + 1

	def IncrementTiebreaker(self):
		global playerturn
		global P1set
		global P1game
		global P1score
		global P1tb
		global P2set
		global P2game
		global P2score
		global P2tb
		if self.tb >= 0 and self.tb<=5:
			self.tb = self.tb + 1
		elif self.tb >= 6 and self.player == 1 and P2tb <= (self.tb-1):
			P1tb=0
			P2tb=0
			P1game=0
			P2game=0
			self.IncrementSetCount()
		elif self.tb >= 6 and self.player == 2 and P1tb <= (self.tb-1):
			P1tb=0
			P2tb=0
			P1game=0
			P2game=0
			self.IncrementSetCount()
		elif self.tb >= 6 and self.player == 1 and P2tb >= self.tb:
			self.tb = self.tb + 1
		elif self.tb >= 6 and self.player == 2 and P1tb >= self.tb:
			self.tb = self.tb + 1

	def IncrementGameCount(self):
		global playerturn
		global P1set
		global P1game
		global P1score
		global P1tb
		global P2set
		global P2game
		global P2score
		global P2tb
		if self.game >= 0 and self.game < 5:
	 		self.game = self.game + 1
	 	elif self.game == 5 and self.player == 1 and P2game<5:
	 		P1game=0
	 		P2game=0
	 		self.IncrementSetCount()
	 	elif self.game == 5 and self.player == 2 and P1game<5:
	 		P1game=0
	 		P2game=0
	 		self.IncrementSetCount()
	 	elif self.game == 5 and self.player == 1 and P2game==5:
	 		self.game=6
	 	elif self.game == 5 and self.player == 2 and P1game==5:
	 		self.game=6
	 	elif self.game == 6:
	 		P1game=0
	 		P2game=0
	 		self.IncrementSetCount()
	 	
	def IncrementScore(self):
		global playerturn
		global P1set
		global P1game
		global P1score
		global P1tb
		global P2set
		global P2game
		global P2score
		global P2tb
		if self.game == 6 and self.player == 1 and P2game == 6:
			IncrementTiebreaker()
		elif self.game == 6 and self.player == 2 and P1game == 6:
			IncrementTiebreaker()
	 	elif self.score == 0:
	 		self.score = 15
	 	elif self.score == 15:
	 		self.score = 30
	 	elif self.score == 30:
	 		self.score = 40
	 	elif self.score == 40 and self.player == 1 and P2score < 40:
			P1score=0
			P2score=0
			changeServe()
	 		self.IncrementGameCount()
		elif self.score == 40 and self.player == 2 and P1score < 40:
		 	P1score=0
		 	P2score=0
		 	changeServe()
		 	self.IncrementGameCount()
		elif self.score == 40 and self.player == 1 and P2score == 40:
		 	self.score = "Advantage"
		elif self.score == 40 and self.player == 2 and P1score == 40:
		 	self.score = "Advantage"
		elif self.score == "Advantage":
		 	P1score=0
		 	P2score=0
		 	changeServe()
		 	self.IncrementGameCount()

class PrintScore:
	def __init__(self,player,score,sets,game,work):
		self.player=player
		self.sets=sets
		self.game=game
		self.score=score
		self.work=work
	def printinitial(self):
		print "Player"+str(self.player)+" : "+str(self.work)
	def printscore(self):
	 	print "P"+str(self.player)+" Score: "+str(self.score)
	def printgame(self):
		print "P"+str(self.player)+" Game Win Count: "+str(self.game)
	def printset(self):
		print "P"+str(self.player)+" Set Win Count: "+str(self.sets)

def PlayGame():
	global playerturn
	global P1set
	global P1game
	global P1score
	global P1tb
	global P2set
	global P2game
	global P2score
	global P2tb
	global serveturn
	global job
	C1=Count(1,P1set,P1game,P1score,P1tb)
	C2=Count(2,P2set,P2game,P2score,P2tb)
	printIteration()

	if job == "Fault" and playerturn == 1:
		C2.IncrementScore()
	elif job == "Fault" and playerturn == 2:
		C1.IncrementScore()
	elif job.find("PointLost")>=0 and playerturn == 1:
		C2.IncrementScore()
	elif job.find("PointLost")>=0 and playerturn == 2:
		C1.IncrementScore()
	elif job == "Nets" and playerturn == 1:
		C2.IncrementScore()
	elif job == "Nets" and playerturn == 2:
		C1.IncrementScore()
	elif job == "Ace" and playerturn == 1:
		C1.IncrementScore()
	elif job == "Ace" and playerturn == 2:
		C2.IncrementScore()

	if P1game!=C1.game or P2game!=C2.game:
		C1.score=0
		C2.score=0
	if P1set!=C1.sets or P2set!=C2.sets:
		C1.game=0
		C2.game=0
		C1.score=0
		C2.score=0

	P1=PrintScore(1,C1.score,C1.sets,C1.game,job)
	P2=PrintScore(2,C2.score,C2.sets,C2.game,job)
	P1set=C1.sets
	P1game=C1.game
	P1score=C1.score
	P1tb=C1.tb
	P2set=C2.sets
	P2game=C2.game
	P2score=C2.score
	P2tb=C2.tb
	if playerturn == 1:
		P1.printinitial();
	if playerturn == 2:
		P2.printinitial();
	P1.printscore()
	P2.printscore()
	P1.printgame()
	P2.printgame()
	P1.printset()
	P2.printset()
	print "\n"
	 	
total = len(sys.argv)
if total == 1:
	print "Insufficient arguments provided!! Also enter input file"
	os._exit(1)
if total > 2:
	print "More than 2 arguments!!Enter only one input file"
	os._exit(1)
if total == 2:
	inputfile = str(sys.argv[1])

with open(inputfile,"r") as f:
	for x in f:
		x=x.rstrip()
		if not x: continue
		time,job = x.split()
		if (job.find("Fault")==0 or job.find("Ace")==0) and playerturn == 2:
			playerturn = 1
		elif (job.find("Fault")==0 or job.find("Ace")==0) and playerturn == 1:
			playerturn = 2
		elif job.find("Serve")==0:
			playerturn = serveturn
		PlayGame()
		if playerturn == 1:
			playerturn = 2
		else:
			playerturn = 1

if P1set > P2set:
	print "P1 is the Winner!!"
elif P2set > P1set:
	print "P2 is the Winner!!"
elif P1set == P2set and P1game > P2game:
	print "P1 is the Winner!!"
elif P1set == P2set and P2game > P1game:
	print "P2 is the Winner!!"
elif P1set == P2set and P1game == P2game and P1score > P2score:
	print "P1 is the Winner!!"
elif P1set == P2set and P2game==P1game and P2score > P1score:
	print "P2 is the Winner!!"
elif P1set == P2set and P2game==P1game and P2score == P1score:
	print "Match Tied"
	
