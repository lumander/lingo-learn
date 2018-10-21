import random
from os import listdir
import yaml
from pylatex import Document, PageStyle, Head, Foot, MiniPage, StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, LineBreak, NewPage, Tabularx, TextColor, simple_page_number
from pylatex.utils import bold, NoEscape

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



	#output += showHelp( choice, phrase );
	
def show_help( entry, phrase ):
	'''
	This function returns the hints for filling the gap 

	INPUT: phrase=['I', 'am', 'a', ,.] 
	OUTPUT:helper=['plumber', 'butcher'.,]	
	'''

	# TO DO
	# HANDLE SPECIAL CASES SUCH AS I ( pronoun )	

	helper=[]
	num_words = 5 ## a phrase may contain dots or marks at its ending
	dictionary = return_category( entry )
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
			helper.append( str( category[ i ] ) + '  ' )
	
	

	return helper

  

def return_category( entry ):
	'''
	This function returns a relevant category of words upon
	the entry provided by searching into a dictionary of already classified words

	INPUT: 'foo' 
	dictionary={ 'adjectives':{ 0:'foo',1:... }, 'verbs':{} } 

	OUTPUT: { 0:'foo',1:... }
	'''

	dictionary_path = 'words_db/'
	category_files = listdir( dictionary_path )
	
	dictionary = {}
	check = False
	
	for file in category_files:
		with open( dictionary_path + file, 'r' ) as stream:
			dictionary.update( yaml.load( stream ) )
	
	categories = dictionary.keys()
	output={}
	for category in categories:
		for key in range( len( dictionary[ category ] ) ):
			if dictionary[ category ][ key ] == entry.lower() :
				check = True
				output['key']=key
				output['category']=dictionary[category]
				return output
	
	if check == False:
		output['key'] = -1
		output['category'] = entry + ' not found!'
		return output
			




def select_phrase( topic ):
	'''
	This function randomly returns a phrase from a list of examples
	given a topic as input 
	INPUT: 'modal verbs' 
	examples={ 0:'Shall I compare thee to a summer's day?,1:... } }
	OUTPUT: ['Shall ', 'I ', 'compare ', 'thee ', 'to ', 'a ' , 'summer','\'','s', 'day']
	'''
	## POSSIBLE IMPROVEMENT - IMPLEMENTATION OF LEVELS OF DIFFICULTY

	topic_file = 'phrases_db/' + topic + '.yaml'
	examples={}
	
	with open( topic_file, 'r' ) as stream:
		examples.update( yaml.load( stream ) )

	num_examples = len(examples)
	choice = random.randint( 0, num_examples - 1 )

	return examples[choice].split(' ')

def question_with_help( phrase ):
	output = ''
	test=rnd_remove( phrase )
	gapped_phrase = test['phrase']
	entry = phrase[ test['entry'] ]
	output += to_string( gapped_phrase )
	output += '\n'
	output +=  to_string(show_help( entry, phrase ) )
	return output

def to_string( array ):
	string=''
	for i in range( len( array ) ):
		string += array[i]
	return string



#def generate( numberOfTest, numberOfQuestions ):
topic='unit14A'
for test in range( 2 ):
	print(str(test) + '\n')
	content=''
	for questions in range( 10 ):
		phrase = select_phrase( topic )
		content += question_with_help( phrase )
		content += '\n\n'	
	print(content)