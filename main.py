

import sys
import yaml
from exercises import FillTheGap

## relative path here
with open("/home/alessandro/myProjects/lingoLearnPorting/LingoLearn/configurations.yaml", 'r') as stream:
    configurations = yaml.load(stream)

idFile = configurations['file_id']
numberOfTest = configurations['test_to_print']
numberOfQuestions = configurations['questions']

FillTheGap.generate( numberOfTest, numberOfQuestions , idFile )
