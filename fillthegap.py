import random
from os import listdir

def rndRemove( phrase ):
	'''
	This function takes a phrase in the form of a list of 
	strings and returns the same list without a random element, e.g 
	INPUT: phrase=[I,am,a,butcher,.] 
	OUTPUT: gapped_phrase=[I,am,a, ,.]
	'''

	length_phrase = len( phrase )
	
	choice = random.randint( 0, length_phrase - 2 )
	gapped_phrase = []
	blank = '_______'
		
	for i in range(length_phrase):
		if i == choice:
			gapped_phrase.append( blank + ' ' )
		else:
			if i == ( length_phrase - 1 ):
				gapped_phrase.append( phrase[i] )
			else:
				gapped_phrase.append( phrase[i] + ' ' )

	return gapped_phrase		
	
	
	
	#output += showHelp( choice, phrase );
	
def showHelp( entry, category, phrase ):
	'''
	This function returns the hints for filling the gap 
	
	INPUT: phrase=['I', 'am', 'a', ,.] 
	OUTPUT:helper=['plumber', 'butcher'.,]

	'''
	# TO DO
	# HANDLE SPECIAL CASES SUCH AS I ( pronoun )

	helper=[]
	num_words = len( phrase ) - 1 ## a phrase may contain dots or marks at its ending
	length_category = len( category )
	random_choices = random.sample( range( length_category ) , num_words - 1 ) # minus 1 since one clue has to be the correct one!
	
	random_fill = random.sample( range( num_words ) , num_words ) # random order for filling the helper list
	choice = random.randint( 0, num_words - 1 ) # if the order were not random, the test would be biased

	for i in random_fill:
		if i == choice:
			helper.append( entry )
		else:
			helper.append( category[ random_choices[i] ] )

	return helper		

  

def returnCategory( entry ):
    '''
    This function returns a relevant category of words upon
	the entry provided by searching into a dictionary of already classified words

    INPUT: 'foo' 

    \tdictionary={ 'adjectives':{ 0:'foo',1:... }, 'verbs':{} } 

    OUTPUT: { 0:'foo',1:... }
    '''

	dictionary_path = 'words_db/'
	category_files = listdir( dictionary_path )
	dictionary = {} 

	for file in category_files:
		with open( file, 'r' ) as stream:
    		dictionary.update( yaml.load( stream ) )

	categories = dictionary.keys()

    for category in categories:
        for key in range( len( dictionary[ category ] ) ):
            if dictionary[ category ][ key ] == entry :
                return dictionary[category]
			else:
				return {0:'Clue not found!'}




def selectPhrase( topic ):
	'''
	This function randomly returns a phrase from a list of examples
	given a topic as input 
    INPUT: 'modal verbs' 

    examples={ 0:'Shall I compare thee to a summer's day?,1:... } }

    OUTPUT: ['Shall ', 'I ', 'compare ', 'thee ', 'to ', 'a ' , 'summer','\'','s', 'day']

	'''
	## POSSIBLE IMPROVEMENT - IMPLEMENTATION OF LEVELS OF DIFFICULTY

    topic_file = 'phrases_db/' + topic
	examples={}
	
	with open( topic_file, 'r' ) as stream:
    		examples.update( yaml.load( stream ) )
	
	num_examples = len(examples)
    choice = random.randint( 0, num_examples - 1 )

	return examples[choice]


