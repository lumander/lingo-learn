import sys
import yaml
from fillthegap import generate

from os import listdir

## relative path here
with open("configurations.yaml", 'r') as stream:
    configurations = yaml.load( stream )

topic = configurations['topic']
numberOfTests = configurations['test_to_print']
numberOfQuestions = configurations['questions']

def get_topic( topic ):
	topic_file = 'phrases_db/' + topic + '.yaml'
	
	examples={}

	with open( topic_file, 'r' ) as stream:
		examples.update( yaml.load( stream ) )

	return examples

def get_vocabulary():
	vocabulary={}
	vocabulary_path = 'words_db/'
	category_files = listdir( vocabulary_path )
	for file in category_files:
		with open( vocabulary_path + file, 'r' ) as stream:
			vocabulary.update( yaml.load( stream ) )
	return vocabulary



vocabulary = get_vocabulary()
examples = get_topic( topic )





if __name__ == '__main__':
    generate(  topic, numberOfTests, numberOfQuestions, vocabulary, examples )
               
    
    