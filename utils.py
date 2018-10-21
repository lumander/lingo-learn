from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number
from pylatex.utils import bold, NoEscape

def generate( numberOfTest, numberOfQuestions ):
    for test in range( numberOfTest ):
        content=''
        for questions in range( numberOfQuestions ):
            content += rndRemove