import os
import time

def animate_Ball():
  distanceToBotm = 0
  while True:
    print("\n" * distanceToBotm)
    print("          (0)        ")
    
    time.sleep(0.2)
    os.system('clear')  
    distanceToBotm += 1
    if distanceToBotm <10:
      distanceToBotm += 0
    

  
#Main Program Starts Here....
animate_Ball()
