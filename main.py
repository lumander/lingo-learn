import sys
import yaml
import fillthegap
from utils import generate

## relative path here
with open("configurations.yaml", 'r') as stream:
    configurations = yaml.load(stream)

idFile = configurations['file_id']
numberOfTests = configurations['test_to_print']
numberOfQuestions = configurations['questions']


#FillTheGap.generate( numberOfTest, numberOfQuestions , idFile )
