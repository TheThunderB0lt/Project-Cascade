# Racing-Fury 2D Car Game!

This is a 2D car game which is developed in Python using Pygame.

## Setup Guide

### Requirements

To be able to successfully run this desktop application there are few requirements that have to be 
satisfied and these include :

- Python 3.7 or higher 
  which you can obtain [here](https://www.python.org/downloads/)
  
- You can also refer pygame documentation 
  which you can obtain [here](https://www.pygame.org/contribute.html)
  
- Pygame using
    
  ```
  pip install pygame
  ```

 - Clone the repo or fork it.

 - Move into **Racing-Fury**.
 
 ## For Images
 
 You must change directory or path.
 
 ## Instruction for this game
 
 - Move Right : D
 - Move Leftt : A
 - Accelerator : W
 - Brake : D
 
Function used:

pygame.init(): This command is used to initiate the pygame module.
pygame.display.set_mode((500,500)): This command is used to make a window of desired size, (width, height). The return value is a Surface Object which is the object where we perform different graphical operations.
pygame.display.set_caption(title = “”): This command is used to set the title of the window/ board.
pygame.event.get(): This is used to empty the event queue. If we do not call this, the window messages will start to pile up and, the game will become unresponsive in the opinion of the operating system.
pygame.QUIT: This is used to terminate the event when we click on the close button at the corner of the window.
