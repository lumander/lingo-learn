import sys
import yaml
from fillthegap import generate


## relative path here
with open("configurations.yaml", 'r') as stream:
    configurations = yaml.load(stream)

topic = configurations['topic']
numberOfTests = configurations['test_to_print']
numberOfQuestions = configurations['questions']


generate( topic, numberOfTests,numberOfQuestions )
