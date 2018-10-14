import random

def rndRemove( phrase ):
	'''
	This function takes a phrase in the form of a list of 
	strings and returns the same list without a random element, e.g \n
	INPUT -> phrase=[I,am,a,butcher,.] \n
	OUTPUT -> gapped_phrase=[I,am,a, ,.]
	'''

	length_phrase = len(phrase)
	
	choice = random.randint( 0, length_phrase - 2 )
	gapped_phrase = []
	blank = '_______'
	double_separator = '\n\n'
	
	
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
	




public static String showHelp( int choice , ArrayList<String> phrase ){ // questa e' una funzione cazzuta
	
	Properties names = new Properties();
	Properties verbs = new Properties();
	Properties adjectives = new Properties();
	Properties adverbs = new Properties();
	Properties pronouns = new Properties();
	Properties prepositions = new Properties();
	boolean sentinel = false;
	String output = null;
	String newLineWithSeparation = System.getProperty("line.separator")+System.getProperty("line.separator");
	
			 
			try {
				InputStream input = new FileInputStream("src\\words\\commonNames.properties");
				names.load(input);
				input.close();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
			try {
				InputStream input = new FileInputStream("src\\words\\commonVerbs.properties");
				verbs.load(input);
				input.close();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
			try {
				InputStream input = new FileInputStream("src\\words\\commonAdjectives.properties");
				adjectives.load(input);
				input.close();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
			try {
				InputStream input = new FileInputStream("src\\words\\commonAdverbs.properties");
				adverbs.load(input);
				input.close();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
						
			try {
				InputStream input = new FileInputStream("src\\words\\commonPronouns.properties");
				pronouns.load(input);
				input.close();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
			try {
				InputStream input = new FileInputStream("src\\words\\commonPrepositions.properties");
				prepositions.load(input);
				input.close();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			
//try {
//	
//	FileReader verbsInput = new FileReader( "C:\\Users\\Alessandro Lumino\\Documents\\commonVerbs.txt" ); // qui bisognerebbe scegliere il livello di difficolta'
//			
//	Scanner s = new Scanner( new BufferedReader( verbsInput ) );
//	
//	s.useDelimiter("\n");
//	
//	while(s.hasNext()){
//		verbs.add(s.next());
//	}
//	
//	if( s != null )
//		s.close();
//} catch (FileNotFoundException e) {
//	
//	e.printStackTrace();
//}
//


  if ( findCategory( phrase.get(choice), names ) && sentinel == false ) {
	  
	  int choice1 = (int) ( Math.random() * names.size() );
	  int choice2 = (int) ( Math.random() * names.size() );
	  int choice3 = (int) ( Math.random() * names.size() );
	  int choice4 = (int) ( Math.random() * names.size() );
	
	  
	  
	  output = newLineWithSeparation + "\\medskip ";
	  output += "\\emph{" + phrase.get( choice ).toLowerCase() + " - " + 
			  names.getProperty( String.valueOf(choice1) ).trim().toLowerCase() + " - " + 
			  names.getProperty( String.valueOf(choice2) ).trim().toLowerCase() + " - " + 
			  names.getProperty( String.valueOf(choice3) ).trim().toLowerCase() + " - " + 
			  names.getProperty( String.valueOf(choice4) ).trim().toLowerCase() + "}";
	  output += newLineWithSeparation + "\\medskip ";
	  
	  sentinel = true;
	  
  } 
  
  if ( findCategory( phrase.get(choice), verbs ) == true && sentinel == false ) {
	  
	  int choice1 = (int) ( Math.random() * verbs.size() );
	  int choice2 = (int) ( Math.random() * verbs.size() );
	  int choice3 = (int) ( Math.random() * verbs.size() );
	  int choice4 = (int) ( Math.random() * verbs.size() );
	  
	  output = newLineWithSeparation + "\\medskip ";
	  output += "\\emph{" + phrase.get( choice ).toLowerCase() + " - " + 
			  verbs.getProperty( String.valueOf(choice1) ).trim().toLowerCase() + " - " + 
			  verbs.getProperty( String.valueOf(choice2) ).trim().toLowerCase() + " - " + 
			  verbs.getProperty( String.valueOf(choice3) ).trim().toLowerCase() + " - " + 
			  verbs.getProperty( String.valueOf(choice4) ).trim().toLowerCase() + "}";
	  output += newLineWithSeparation + "\\medskip ";
	  
	  sentinel = true;	  
	  
  } 

  if ( findCategory( phrase.get(choice), adjectives ) == true && sentinel == false ) {
	  
	  int choice1 = (int) ( Math.random() * adjectives.size() );
	  int choice2 = (int) ( Math.random() * adjectives.size() );
	  int choice3 = (int) ( Math.random() * adjectives.size() );
	  int choice4 = (int) ( Math.random() * adjectives.size() );
	  
	  output = newLineWithSeparation + "\\medskip ";
	  output += "\\emph{" + phrase.get( choice ).toLowerCase() + " - " + 
			  adjectives.getProperty( String.valueOf(choice1) ).trim().toLowerCase() + " - " + 
			  adjectives.getProperty( String.valueOf(choice2) ).trim().toLowerCase() + " - " + 
			  adjectives.getProperty( String.valueOf(choice3) ).trim().toLowerCase() + " - " + 
			  adjectives.getProperty( String.valueOf(choice4) ).trim().toLowerCase() + "}";
	  output += newLineWithSeparation + "\\medskip ";
	  
	  sentinel = true;
  } 
  
  if ( findCategory( phrase.get(choice), adverbs ) == true && sentinel == false ) {
	  
	  int choice1 = (int) ( Math.random() * adverbs.size() );
	  int choice2 = (int) ( Math.random() * adverbs.size() );
	  int choice3 = (int) ( Math.random() * adverbs.size() );
	  int choice4 = (int) ( Math.random() * adverbs.size() );
	  
	  output = newLineWithSeparation + "\\medskip ";
	  output += "\\emph{" + phrase.get( choice ).toLowerCase() + " - " + 
			  adverbs.getProperty( String.valueOf(choice1) ).trim().toLowerCase() + " - " + 
			  adverbs.getProperty( String.valueOf(choice2) ).trim().toLowerCase() + " - " + 
			  adverbs.getProperty( String.valueOf(choice3) ).trim().toLowerCase() + " - " + 
			  adverbs.getProperty( String.valueOf(choice4) ).trim().toLowerCase() + "}";
	  output += newLineWithSeparation + "\\medskip ";
	
	  sentinel = true;
	  
  } 
  
  if ( findCategory( phrase.get(choice), pronouns ) && sentinel == false ) {
	  
	  int choice1 = (int) ( Math.random() * pronouns.size() );
	  int choice2 = (int) ( Math.random() * pronouns.size() );
	  int choice3 = (int) ( Math.random() * pronouns.size() );
	  int choice4 = (int) ( Math.random() * pronouns.size() );
	  String str0,str1,str2,str3,str4;
	  
	  str0 = ( phrase.get( choice ).trim().equals("I") ) ? phrase.get( choice ).trim() : phrase.get( choice ).trim().toLowerCase();
	  str1 = ( pronouns.getProperty( String.valueOf(choice1) ).trim().equals("I") ) ? pronouns.getProperty( String.valueOf(choice1) ).trim() : pronouns.getProperty( String.valueOf(choice1) ).trim().toLowerCase();
	  str2 = ( pronouns.getProperty( String.valueOf(choice2) ).trim().equals("I") ) ? pronouns.getProperty( String.valueOf(choice2) ).trim() : pronouns.getProperty( String.valueOf(choice2) ).trim().toLowerCase();
	  str3 = ( pronouns.getProperty( String.valueOf(choice3) ).trim().equals("I") ) ? pronouns.getProperty( String.valueOf(choice3) ).trim() : pronouns.getProperty( String.valueOf(choice3) ).trim().toLowerCase();
	  str4 = ( pronouns.getProperty( String.valueOf(choice4) ).trim().equals("I") ) ? pronouns.getProperty( String.valueOf(choice4) ).trim() : pronouns.getProperty( String.valueOf(choice4) ).trim().toLowerCase();
	  
	  
	  output = newLineWithSeparation + "\\medskip ";
	  output += "\\emph{" + str0 + " - " + str1 + " - " + str2 + " - " + str3 + " - " + str4 + "}";
	  output += newLineWithSeparation + "\\medskip ";
	
	  sentinel = true;
	  
  } 
  

  
  if ( findCategory( phrase.get(choice), prepositions ) == true && sentinel == false ) {
	  
	  int choice1 = (int) ( Math.random() * prepositions.size() );
	  int choice2 = (int) ( Math.random() * prepositions.size() );
	  int choice3 = (int) ( Math.random() * prepositions.size() );
	  int choice4 = (int) ( Math.random() * prepositions.size() );
	  
	  output = newLineWithSeparation + "\\medskip ";
	  output += "\\emph{" + phrase.get( choice ).toLowerCase() + " - " + 
			  prepositions.getProperty( String.valueOf(choice1) ).trim().toLowerCase() + " - " + 
			  prepositions.getProperty( String.valueOf(choice2) ).trim().toLowerCase() + " - " + 
			  prepositions.getProperty( String.valueOf(choice3) ).trim().toLowerCase() + " - " + 
			  prepositions.getProperty( String.valueOf(choice4) ).trim().toLowerCase() + "}";
	  output += newLineWithSeparation + "\\medskip ";
	
	  sentinel = true;
	  
  } 
  
  if( !sentinel ) {
	  output = newLineWithSeparation + "\\medskip ";
	output +=  "\\emph{" + "Clue not found! }";
	output += newLineWithSeparation + "\\medskip ";
  }
  
  return output;

	}

public static boolean findCategory( String findMe, Properties basket ){
	
	boolean flag = false;
	
	for ( int k = 0; k < basket.size() ; k++ ){
		
		if( findMe.toLowerCase().equals( basket.getProperty( String.valueOf(k) ).trim().toLowerCase() ) ){
			flag = true;
			break;
			
		}
			
		
	}
	
	return flag;
}

public static ArrayList<String> selectPhrase(){
	
	Properties examples = new Properties();
	ArrayList<String> phrase = new ArrayList<String>(4);
	Scanner s = null;
	
	try {
		InputStream input = new FileInputStream("src\\examples\\unit01A.properties");
		examples.load(input);
		input.close();
	} catch (IOException e1) {
		// TODO Auto-generated catch block
		e1.printStackTrace();
	}
	
//	try {
//		
//		FileReader input = new FileReader( "C:\\Users\\Alessandro Lumino\\Documents\\unit14A_Phrases.txt" ); // qui bisognerebbe scegliere il livello di difficolta'
//				
//		s = new Scanner( new BufferedReader( input ) );
//		
//		s.useDelimiter("\n");
//		
//		while(s.hasNext()){
//			examples.add(s.next());
//		}
//		
//		if( s != null )
//			s.close();
//	} catch (FileNotFoundException e) {
//		
//		e.printStackTrace();
//	}
	
	int choice = (int) ( Math.random()*examples.size() );
	

		s = new Scanner( examples.getProperty( String.valueOf(choice) ) );
		s.useDelimiter(" ");
		while(s.hasNext()){
			phrase.add(s.next());
		}
		if( s != null )
			s.close();
		s.close();
		
		return phrase;
		
	}

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