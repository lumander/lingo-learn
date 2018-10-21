import random
import yaml
from pylatex import Document, Section,Subsection, NewPage
from pylatex.utils import italic
from pylatex.utils import NoEscape


def rnd_remove( phrase ):
	'''
	This function takes a phrase in the form of a list of 
	strings and returns the same list without a random element, e.g 
	INPUT: phrase=[I,am,a,butcher,.] 
	OUTPUT: gapped_phrase=[I,am,a, ,.]
	'''	
	length_phrase = len( phrase )
	output={}
	choice = random.randint( 0, length_phrase - 2 )
	
	gapped_phrase = []
	blank = '_______'

	for i in range( length_phrase ):
		if i == choice:
			gapped_phrase.append( blank + ' ' )
		else:
			if i == ( length_phrase - 1 ):
				gapped_phrase.append( phrase[i] )
			else:
				gapped_phrase.append( phrase[i] + ' ' )	
	output['entry']=choice
	output['phrase']=to_string( gapped_phrase )
	return output		

	
def show_help( entry, phrase,vocabulary ):
	'''
	This function returns the hints for filling the gap 

	INPUT: phrase=['I', 'am', 'a', ,.] 
	OUTPUT:helper=['plumber', 'butcher'.,]	
	'''

	# TO DO
	# HANDLE SPECIAL CASES SUCH AS I ( pronoun )	

	helper=[]
	num_words = 5 ## a phrase may contain dots or marks at its ending
	dictionary = return_category( entry, vocabulary)
	entry_key=dictionary['key']
	category=dictionary['category']
	length_category = len( category )
	random_choices = set()
	random_choices.add( entry_key )
	while( len( random_choices ) != num_words ):
		random_choices.add( random.randint( 0, length_category - 1 )  ) # minus 1 since one clue has to be the correct one!
	
	
	if entry_key == -1:
		helper.append('Clue not found!')
	else:
		for i in random_choices:
			helper.append( str( category[ i ] ) + '    ' )
	
	

	return helper


  

def return_category( entry, vocabulary ):
	'''
	This function returns a relevant category of words upon
	the entry provided by searching into a dictionary of already classified words

	INPUT: 'foo' 
	dictionary={ 'adjectives':{ 0:'foo',1:... }, 'verbs':{} } 

	OUTPUT: { 0:'foo',1:... }
	'''

	check = False
	
	
	categories = vocabulary.keys()
	output={}
	for category in categories:
		for key in range( len( vocabulary[ category ] ) ):
			if vocabulary[ category ][ key ] == entry :
				check = True
				output['key']=key
				output['category']=vocabulary[category]
				return output
	
	if check == False:
		output['key'] = -1
		output['category'] = entry + ' not found!'
		return output
			




def select_phrase( examples ):
	'''
	This function randomly returns a phrase from a list of examples
	given a topic as input 
	INPUT: 'modal verbs' 
	examples={ 0:'Shall I compare thee to a summer's day?,1:... } }
	OUTPUT: ['Shall ', 'I ', 'compare ', 'thee ', 'to ', 'a ' , 'summer','\'','s', 'day']
	'''
	## POSSIBLE IMPROVEMENT - IMPLEMENTATION OF LEVELS OF DIFFICULTY

	num_examples = len(examples)
	choice = random.randint( 0, num_examples - 1 )

	return examples[choice].split(' ')

def question_with_help( phrase, vocabulary, doc ):
	
	dictionary=rnd_remove( phrase )
	gapped_phrase = dictionary['phrase']
	entry = phrase[ dictionary['entry'] ]
	doc.append( to_string( gapped_phrase ) )
	doc.append('\n\n')
	doc.append( italic( to_string( show_help( entry, phrase, vocabulary ) ) ) )



def to_string( array ):
	string=''
	for i in range( len( array ) ):
		string += array[i]
	return string

def generate( topic, numberOfTests, numberOfQuestions, vocabulary, examples ):

	doc = Document()
	for test in range( numberOfTests ):
		with doc.create( Section( 'Fill in the Gap', numbering = False ) ):
			with doc.create( Subsection( 'Surname:_________Name:_________Date:________ ', numbering = False ) ):
				for questions in range( numberOfQuestions ):
					phrase = select_phrase( examples )
					question_with_help( phrase, vocabulary, doc )
					doc.append('\n\n')
		doc.append(NewPage())
	
	doc.generate_pdf('full', clean_tex=False)
	
