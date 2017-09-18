import unittest
from SI507F17_project1_cards import *

class JackTests(unittest.TestCase):
	def setUp(self):
		self.card = Card(2, 3)
		self.jackofhearts = Card(2, 11)
		self.jackofspades = Card(3, 11)
	
	def test_one(self):
		self.assertEqual(type(self.card.suit),str, "should be a string")
	def test_two(self):
		self.assertEqual(self.jackofhearts.suit,'Hearts',"checking if hearts") 
	def test_three(self):
	 	self.assertEqual(self.jackofhearts.rank, 'Jack', "checking if card is Jack")
	def test_four(self):
		self.assertEqual(self.jackofhearts.rank_num, 11, "checking if rank of Jack is num 11")
	def test_five(self):
		self.assertEqual(self.jackofspades.suit,'Spades',"checking if spades")
	def test_six(self):
		self.assertEqual(self.jackofhearts.__str__(), 'Jack of Hearts', "checking string method") 
		
	
class QueenTests(unittest.TestCase):          
	def setUp(self):
		self.queenofspades=Card(3,12)
		self.queenofhearts=Card(2,12)	

	
	def test_one(self):
		self.assertEqual(self.queenofspades.rank,'Queen', "checking if card is Queen")
	def test_two(self):
		self.assertEqual(self.queenofhearts.rank,'Queen', "checking if card is Queen")
	def test_three(self):
		self.assertEqual(self.queenofspades.suit, 'Spades', "checking if suit is spades")
	def test_four(self):
		self.assertEqual(self.queenofspades.__str__(), 'Queen of Spades', "checking string method") 		

class AceTests(unittest.TestCase):          
	def setUp(self):
		self.aceofdiamonds=Card(0,1)

	
	def test_one(self):
		self.assertEqual(self.aceofdiamonds.rank,'Ace', "checking if card is Ace")
	def test_two(self):	
		self.assertEqual(self.aceofdiamonds.rank_num,1, "checking rank of Ace is 1")
	def test_three(self):
		self.assertEqual(self.aceofdiamonds.__str__(), 'Ace of Diamonds', "checking string method") 	


class NumberCardTests(unittest.TestCase):          
	def setUp(self):
		self.fiveofclubs=Card(1,5)

	def test_one(self):
		self.assertEqual(self.fiveofclubs.rank,5, "checking if card is five")
	def test_two(self):	
		self.assertEqual(self.fiveofclubs.rank_num,5, "checking rank num is five")
	def test_three(self):
		self.assertEqual(self.fiveofclubs.__str__(), '5 of Clubs', "checking string method")

class CardDeckTests(unittest.TestCase):          
	def setUp(self):
		self.mydeck=Deck()

	def test_one(self):
		self.assertEqual(len(self.mydeck.cards),52, "testing number of cards in full deck")
	def test_two(self):
		self.assertEqual(type(self.mydeck.pop_card().suit), str, "Checking to make sure suit is a string")	
	def test_three(self):
		self.assertEqual(len(self.mydeck.cards),51, "testing that deck popped off one card")

class DealDeckTests(unittest.TestCase):
	def setUp(self):
		self.mydeck=Deck()

	def test_one(self):
		self.assertEqual(len(self.mydeck.cards),52, "testing number of cards in full deck")
	def test_two(self):
		self.assertEqual(len(self.mydeck.deal_hand(5)),5, "testing that 5 cards are dealt")		
	def test_three(self):
		self.assertEqual(len(self.mydeck.cards),47, "testing that now my deck has 47 cards")




if __name__=='__main__':
	unittest.main(verbosity=2)
