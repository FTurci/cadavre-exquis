from random import choices, randint
from math import log, floor

class State:

	'''Given either an array or a number, defines a state of the game.
	Specify fast = False for a game without removal of double lines.
	Specify plus = False for a traditional Nim game.
	These properties will be inherited by all of the following states.'''

	def __init__(self, code, fast = True, plus = True):
		
		self.fast = fast
		self.plus = plus
		
		if type(code) is list:
			if fast:
				self.array = clean(parity(code))
				self.number = int(''.join([str(i) \
				for i in self.array]), 2)
			else:
				self.array = clean(code)
				self.number = None
		elif type(code) is int:
			self.fast = True
			self.array = clean([int(i) for i in bin(code)[2:]])
			self.number = code
		
		self.name = ','.join([str(i) for i in self.array])
		self.length = len(self.array)
		
	def __hash__(self):
	
		return hash(self.name)

	def __eq__(self, other):

		return True if self.name == other.name else False

	def winning(self):
	
		'''For Nim and Nim+, returns True if state is winning, else False,
		according to Nim-sum criterion.'''
	
		array = self.array.copy()
		l = self.length	
		nimsum = 0
		for i in range(len(array)):
			if array[i] % 2 != 0:	
				nimsum ^= l-i
					
		return False if nimsum == 0 else True
		
	def winning_antinim(self):
	
		'''For anti-Nim, returns True if state is winning, else False,
		according to Mattia Leogatti's criterion, to be checked.'''
		
		array = self.array.copy()
		l = self.length	
		if l == 1:
			return True if array[0] % 2 == 0 else False
		elif l == 2 and array[1] == 1:
			return True
		else:
			return self.winning()

	def config(self):
	
		'''Defines the configuration associated to the state.
		Not currently in use, may be useful for graphical visualization purpopses.'''

		config = []	
	
		for i in range(self.length):
			for j in range(self.array[-i-1]):
				config.append([k for k in range(i+1)])

		return config
					
	def set_avail(self, best = False):
	
		'''Given a state, stores in the avail attribute the states reachable from it
		according to the game specifics fast, plus.
		Specify best = True to only select the good moves
		(those that lead to losing states for the adversary).'''

		self.avail = []
		l = self.length

		for i in range(l):
			if self.array[i] != 0:
				for k1 in range(l-i+1):
					for k2 in range(k1,l-i-k1):
						newa = self.array.copy()
						newa[i] -= 1
						if k1 != 0:
							newa[l-k1] += 1
							if not self.plus:
								news = State(newa, \
								self.fast, self.plus)
								news.include(self.avail, best)
								break
						if k2 != 0:
							newa[l-k2] += 1
						news = State(newa, self.fast, self.plus)
						news.include(self.avail, best)

	def include(self, avail, best = False):
	
		'''Includes a state in .avail given the game specifics.'''
	
		if (best and not self.winning()) or not best:
			if self.fast or not self.plus:
				if self not in avail:
					avail.append(self) 
			else:
				avail.append(self)
				
	def reorder(self):
	
		if self.fast:
	
			newavail = []
			for i in range(self.number):
				for j in self.avail:
					if j.number == i:
						newavail.append(j)
			self.avail = newavail	
				
	def expected(self, alice, bob):
	
		'''Returns the probability that the first player has of winning starting from that state.'''
		
		counter = Counter()
		if self.number > 62:
			pass
		else:
			recursive(self, bob, alice, counter)
		return sum(counter.problist)

class Player:

	'''Attributes:
	- notebook is a dictionary of how many times moves are played. THIS CAN BE SIMPLIFIED!
	- latest is the latest meaningful move played in a match (i.e. which had more than one choice)
	- last is the last move played in a match
	'''

	def __init__(self, reinforces = False, prunes = False, \
	trims = False, spies = True, beads = 42):

		self.reinforces = reinforces
		self.prunes = prunes
		self.trims = trims
		self.spies = spies
		self.beads = beads

		self.wins = 0
		self.notebook = {}
		self.latestmove = None
		self.lastmove = None
		self.boxes = {}
		self.incentives = {}

	def set_boxes(self, state):
	
		if not hasattr(state, 'avail'):
			state.set_avail()

		for newstate in state.avail:
			if (state, newstate) not in self.boxes:
				self.boxes[(state, newstate)] = self.beads			
	
	def learns(self, winner, loser):
	
		if self.reinforces: reinforce(self, winner, loser)
		if self.prunes: prune(self, loser)
		if self.trims: trim(self, winner)
		
	def goodmoves(self, state):
	
		'''Starting from state, returns a list of reachable states
		that the player considers to be good choices'''

		goodmoves = []
		state.set_avail()
		
		for newstate in state.avail:
			beads = self.boxes.get((state, newstate), 0)	
			if beads > self.beads:
				goodmoves.append(newstate)

		return goodmoves

class Game:

	def __init__(self, level = 3, matches = 1, starter = None, \
	fast = True, plus = True, anti = False, record = False):
	
		self.level = level
		self.matches = matches
		self.starter = starter
		self.plus = plus
		self.fast = fast
		self.anti = anti
		self.record = record
		if self.record:
			self.history = [] if self.fast else None
		code = [1 for i in range(0, self.level)]
		self.start = State(code, fast, plus)
		
	def play(self, alice, bob):

		'''Starts a game, actuates the learning etc.
		Notice that if at the beginning of the game the players have the same faculaties
		and the boxes happen to be identical then they will stay identical for the whole game.'''
		
		if identical(alice, bob):
			alice.boxes = bob.boxes
	
		for i in range(self.matches):

			if self.starter is not None:
				player = self.starter
			else:
				player = choices([alice,bob])[0]

			other = bob if player == alice else alice
					
			winner, loser = match(player, other, self.start)
			if self.anti:
				winner, loser = loser, winner
				
			winner.wins += 1

			alice.learns(winner, loser)
			if not identical(alice, bob):
				bob.learns(winner, loser)
			
			if self.record and self.fast:
				transcript = []
				for i in alice.notebook:
					transcript.append(i[0].number)
					transcript.append(i[1].number)
				transcript.sort()
				if transcript[0] != 0:
					transcript = [0] + transcript
				if transcript[-1] != self.start.number:
					transcript += [self.start.number]
				self.history.append(transcript)
			
			alice.notebook = {}
			bob.notebook = {}
			
class Counter:

	'''This is useful to calculate expected game wins and do statisics on games.'''

	def __init__(self):
		self.turn = 0
		self.prob = 1
		self.problist = []
		
def identical(alice, bob):

	'''Returns True if Alice and Bob have the same mental faculties
	(in this case they will share boxes to save space).
	Not a class Player object identity.'''

	if alice.reinforces == bob.reinforces\
	and alice.prunes == bob.prunes\
	and alice.trims == bob.trims\
	and alice.spies == bob.spies\
	and alice.incentives == bob.incentives\
	and alice.boxes == bob.boxes:
		return True
	else:
		return False
			
def match(player, other, start):

	'''Plays a single match between Alice and Bob, starting from any given state.
	Returns winner and loser. Records all of the moves in players' notebooks
	Records the last meaningful move played by each player.'''

	state = start
		
	while state != finish:
	
		state.set_avail()
		player.set_boxes(state)
		
		if not identical(player, other):
			other.set_boxes(state)

		weights = [player.boxes[state, newstate] for newstate in state.avail]
		newstate = choices(state.avail, weights)[0]

		move = state, newstate		
		player.notebook[move] = player.notebook.get(move, 0) + 1
		
		if weights.count(0) != len(weights)-1:
			player.latestmove = move

		if newstate == finish:
			winner, loser, = player, other
			player.lastmove = move

		player, other = other, player
		state = newstate
		
	return winner, loser
	
def reinforce(learner, winner, loser):

	if learner.spies or learner == winner:

		for move in winner.notebook:
			extra = learner.incentives.get(move, 1)
			change = learner.boxes[move] + extra	
			learner.boxes[move] = change if change < 2 * learner.beads \
			               else 2 * learner.beads
			
	if learner.spies or learner == loser:

		for move in loser.notebook:
			extra = learner.incentives.get(move, 1)
			change = learner.boxes[move] - extra
			learner.boxes[move] = change if change > 0 else 1				
		
def prune(learner, loser):

	latest = loser.latestmove
	latest[0].set_avail()
	
	for i in latest[0].avail:
		if i == latest[1]:
			learner.boxes[latest[0], i] = 0
		else:
			learner.boxes[latest[0], i] += 1
	
def trim(learner, winner):

	last = winner.lastmove
	last[0].set_avail()
	
	for i in last[0].avail:
		if i == last[1]:
			learner.boxes[last[0], i] += 1
		else:
			learner.boxes[last[0], i] = 0

def clean(array):

	for i in range(len(array)):
		if array[0] == 0 and len(array) != 1:
			array.pop(0)
						
	return array
		
def parity(array):

	for i in range(len(array)):
		array[i] %= 2

	return array

def recursive(state, alice, bob, counter):

	if state == finish:
		if counter.turn % 2 == 1:
			counter.problist.append(counter.prob)
			
	else:

		if counter.turn == 0:
			alice.set_boxes(state)
			boxes = alice.boxes
		else:
			bob.set_boxes(state)
			boxes = bob.boxes

		counter.turn += 1	
		state.set_avail()
		weights = [boxes[state, newstate] for newstate in state.avail]
		normalization = sum(weights)
		weights = [i/normalization for i in weights]
		
		for newstate in state.avail:
			i = state.avail.index(newstate)		
			counter.prob *= weights[i]
			recursive(newstate, bob, alice, counter)
			counter.prob /= weights[i]			

		counter.turn -= 1

finish = State(0)

	








