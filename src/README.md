# **Connect 4 Game**

## **Project Description**
This project is a functional mockup of the classic Connect 4 Board Game! You play it by simply clicking on a column with your mouse to place the respective piece.
You can take turns with a friend, and all of the win and draw states will be automatically taken care of by the game!

## **Files Included**
### requirements.txt 
States the necessary 3rd Party Libraries that one must import in order to use the program.
### README.md
File that gives a wealth of info about the project. You're reading it right now!
### project.py
The actual python file that the project is based in.

## **Design Considerations and Challenges**
I'm pretty proud of my work on this project, mainly because it presented a lot of unique challenges that I had to work my way through, both new and old.
### Old Challenges
I had to refresh myself on how pygame visuals worked, and the grid functionality used a system of multiplying lists to create a **matrix** of sorts that I'm pretty sure we had to do for one of the labs.
I also had to go back to the digital raindrops lab for a quick refresher on how classes worked, because they are probably the most complicated thing we learned in this class.
### New Challenges
While this project was mostly comprised of concepts I had learned before in this course, I was forced to dive deeper into these concepts to use them in new ways.
Similarly to our checkerboard lab, I used two lists in order to create a grid pattern that I used for the game functionality. This was difficult for a number of reasons.
First, I had to have the program place the piece at the bottom of its respective column, and then it had to check if that piece had made any 4-in-a-row matches.
That prospect was very daunting, but after searching around through some forums online I found a pretty neat solution. Just checking if a piece and the 3 pieces to the right of it are the same works wonders
if you do that check on nearly every piece. I was able to keep it constrained as much as possible, though, leaving out cases where it's impossible for that match to occur
(like a piece thats already on the far right wall.) This same concept could then be used for vertical matches and both the diagonals.
After the game functionality was created, I then had to make the visuals for it. This proved to be tricky since I was a little rusty on pygame and all of its ins and outs, but I eventually figured out
some solutions to give the game visuals and some basic animations.

## **Future Improvements**
If I were to improve on this project in the future, I think the first thing I would do is clean up the code. It uses a few too many global variables for my liking, but changing that would require me to rewrite a lot 
of the code which was just not an option given time constraints. My second priority would be to create an AI opponent. I wanted to implement this into the main project,
but I quickly realized that it was a little out of scope of my expertise. I think learning about that would be fun, though, so maybe I'll come back to this project someday. Finally, 
I would implement more animations to give the game more life. I initially wanted to have the pieces bounce a little when being dropped into the board and maybe even have the pieces have little designs on them, but 
I quickly realized that pygame is very limiting and also very confusing, and so I went with a simplistic style. I'm still happy with the animations I was able to add, though. Overall, even though I didn't get to add everything I wanted 
to for this project, I am still happy with the result, and it still makes me happy just how much I have learned from this course in a relatively short amount of time. 

## **VIDEO URL**
https://youtu.be/ZeQJBLeUiVg

## **GITHUB LINK**
https://github.com/PedroFrien/pfda_finalProject_BrittonTanner.git

