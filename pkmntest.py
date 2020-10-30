#import sys
#sys.path.insert(0,'Labs/pkmntest.py')
#from Labs import pkmntest
#import pkmntest
#pkmntest.poke()

reset = u"\u001B[0m"
red = u"\u001B[31m"
blue = u"\u001B[34m"

def poke():
  print ("Which game do you prefer, Pokemon Sword or Shield?")
  game = input()
  print ("So you like Pokemon " + game + " huh?")
  if game == "Sword" or "sword":
    print("I agree.")
    print("                    /   ")                   
    print("                   /.// ")                    
    print("               ////////// ")                 
    print("         ////////////////// ")               
    print("            ,   ///////////// ")              
    print("          ***  ********///  ")               
    print("                *********  ")               
    print("          ,******************,  ")          
    print(" ************************************** ")   
    print(" *****,     *****************    ,***** ") 
    print("   *        *****************       * ")
    print("            ,,,,,,,,,,,,,,,,,  ")      
    print("            ,,,,,,,,,,,,,,,,,    ")    
    print("            ,,,,,,,,,,,,,,,,,      ") 
    print("            ,,,,,,,,,,,,,,,,,   ")
    print("            ,,,,,,,,,,,,,,,,,     ")   
    print("            ,,,,,,,,,,,,,,,,,       ") 
    print("            ,,,,,,,,,,,,,,,,,        ")
    print("            ,,,,,,,.,........       ")
    print("            ,................      ")
    print("            .................        ")
    print("            .................        ")
    print("            .................       ")
    print("             ...............         ")
    print("              ............           ")
    print("               ..........            ")
    print("                .......             ")
    print("                 .... ")                 
    print("                   .  ")
  if game == "Shield" or "shield":
    print("Yeah, that's pretty good too.")
    print( )