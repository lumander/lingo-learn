import random
from os import listdir

def rndRemove( phrase ):
	'''
	This function takes a phrase in the form of a list of 
	strings and returns the same list without a random element, e.g \n
	INPUT: phrase=[I,am,a,butcher,.] \n
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
	This function returns the hints for filling the gap \n
	
	INPUT: phrase=['I', 'am', 'a', ,.] \n
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
	the entry provided by searching into a dictionary of already classified words\n

    INPUT: 'foo' \n 

    \tdictionary={ 'adjectives':{ 0:'foo',1:... }, 'verbs':{} } \n

    OUTPUT: { 0:'foo',1:... } \n
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
	given a topic as input \n
    INPUT: 'modal verbs' \n 

    \texamples={ 0:'Shall I compare thee to a summer's day?,1:... } } \n

    OUTPUT: ['Shall ', 'I ', 'compare ', 'thee ', 'to ', 'a ' , 'summer','\'','s', 'day'] \n

	'''
	## POSSIBLE IMPROVEMENT - IMPLEMENTATION OF LEVELS OF DIFFICULTY

    topic_file = 'phrases_db/' + topic
	examples={}
	
	with open( topic_file, 'r' ) as stream:
    		examples.update( yaml.load( stream ) )
	
	num_examples = len(examples)
    choice = random.randint( 0, num_examples - 1 )

	return examples[choice]


public static void generate( int numberOfTest, int numberOfQuestion, int idFile ){
	
	int test, questions;
	String text = null;
	String tempDirectory = "C:\\Users\\Alessandro Lumino\\Documents\\FillTheGap";
	String tempFileName = "unit14A_Phrases"+ idFile;
	
	String newLineWithSeparation = System.getProperty("line.separator")+System.getProperty("line.separator");
	
	text = "";
	text += "\\documentclass[a4paper, 10pt]{article}" + newLineWithSeparation;
	text += "\\usepackage[T1]{fontenc}" + newLineWithSeparation;
	text += "\\usepackage[utf8]{inputenc}" + newLineWithSeparation;
	text += "\\usepackage[english]{babel}" + newLineWithSeparation;
	text += "\\usepackage{layaureo,graphicx}" + newLineWithSeparation;
	text += "\\begin{document}" + newLineWithSeparation;
	text += "\\pagestyle{empty}" + newLineWithSeparation;
	
		
	for( test = 1; test <= numberOfTest; test++ ){
		String content="";
		text +=  "\\section*{Test " + test + "}"  + newLineWithSeparation + "\\bigskip \\medskip  " + newLineWithSeparation;
		text += "\\textbf{Name: } \\qquad \\qquad \\qquad \\qquad \\qquad " ;
		text += "\\textbf{Surname: } \\qquad \\qquad \\qquad \\qquad " ;
		text += "\\qquad \\textbf{Date: } " + newLineWithSeparation + "\\bigskip  \\smallskip " + newLineWithSeparation;
		text += "\\begin{enumerate}";
		
		 
		  
			for( questions = 1; questions <= numberOfQuestion; questions++ ){
				content += rndRemove( selectPhrase(), questions ) + newLineWithSeparation;
			}
			text += content + newLineWithSeparation;
			text += "\\end{enumerate}" + newLineWithSeparation;
			text += "\\newpage";
		 
	 	}
	
	text += newLineWithSeparation + "\\end{document}";
	
	createTex( tempDirectory, tempFileName, text );
	
	executeTex( tempFileName, tempDirectory );
	
	showPdf(tempFileName, tempDirectory);

	}

public static void createTex( String tempDirectory, String tempFileName, String content ){
	
		FileWriter writer = null;
	
    	try {
        writer = new FileWriter( tempDirectory + "\\" + tempFileName + ".tex", false );
        writer.write( content, 0, content.length() );
        writer.close();
    	} catch (IOException ex) {
        ex.printStackTrace();
    	}
    
	}

public static void executeTex( String tempFileName , String tempDirectory ){

	 ProcessBuilder pb = new ProcessBuilder("pdflatex", "-shell-escape", tempFileName + ".tex");
     pb.directory(new File( tempDirectory ));
     try {
         Process p = pb.start();
         StreamPrinter fluxSortie = new StreamPrinter(p.getInputStream(), true);
         StreamPrinter fluxErreur = new StreamPrinter(p.getErrorStream(), true);
         new Thread(fluxSortie).start();
         new Thread(fluxErreur).start();
         p.waitFor();
     } catch (IOException | InterruptedException ex) {
         ex.printStackTrace();
     }
	
    
     
	}

public static void showPdf( String tempFileName , String tempDirectory ){
	
	ProcessBuilder pb = new ProcessBuilder("cmd.exe", "/C", "start", tempFileName + ".pdf");
    pb.directory(new File( tempDirectory ));
    try {
        Process p = pb.start();
        StreamPrinter fluxSortie = new StreamPrinter(p.getInputStream(), false);
        StreamPrinter fluxErreur = new StreamPrinter(p.getErrorStream(), false);
        new Thread(fluxSortie).start();
        new Thread(fluxErreur).start();
        p.waitFor();
    } catch (IOException | InterruptedException ex) {
        ex.printStackTrace();
    }
	
	}

}