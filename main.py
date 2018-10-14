import sys
import yaml
#from exercises import FillTheGap

## relative path here
with open("configurations.yaml", 'r') as stream:
    configurations = yaml.load(stream)

idFile = configurations['file_id']
numberOfTest = configurations['test_to_print']
numberOfQuestions = configurations['questions']
print(idFile)
#sFillTheGap.generate( numberOfTest, numberOfQuestions , idFile )
