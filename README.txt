1. How to use this program.
With the photo you want to manipulate saved in the same folder as the program 
file, run the file "ppm_changer.py" in the Python Shell. Then follow the 
printed directions in the program. (For convenience I have saved the 'cake.ppm' 
image saved in this folder.)

2. Design decisions.
I decided to split my program into the following functions/tasks:
- Phase 2 functions
- taking the user's input for file names
- reading the input file and storing its information as variables and lists
- menu
- managing the user's decision to implement an operation
- creating and writing the manipulated ppm file.
- the main function that utilizes all the previous functions

I stored my input file contents into separate lists: one for the first three
"header" lines and one for the pixels. I did this because it would be more
efficient to edit the list of pixels for every manipulation instead of writing,
closing, and reopening the output file for every manipulation. This method
allowed me to only write the output file once: at the very end when the program
is done with its ppm manipulations.

For horizontal flip, I used a temporary list to extract a complete row of
pixels, and implemented the flip by first reversing each set of three pixels,
then reversing the whole row. I did it this way because it was the simplest
method of horizontal flip I could think of. Then I would append the flipped
temporary list into a new list, and repeated until each row had been flipped.
