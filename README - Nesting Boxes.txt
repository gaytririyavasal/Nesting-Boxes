
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Imagine a room full of boxes. Each box has a length, width, and height. Since the boxes can be rotated those terms are interchangeable. The dimensions are integral values in a consistent system of units. The boxes have rectangular surfaces and can be nested inside each other. A box can nest inside another box if all its dimensions are strictly less than the corresponding dimensions of the other. You may only nest a box such that the corresponding surfaces are parallel to each other. A box may not be nested along the diagonal. You cannot also put two or more boxes side by side inside another box.

You will read your input from standard input. The list of boxes will be in a file called boxes.in. The first line gives the number of boxes n. The next n lines give a set of three integers separated by one or more spaces. These integers represent the 3 dimensions of a box. Since you can rotate the boxes, the order of the dimensions does not matter. It may be to your advantage to sort the dimensions in ascending order.

There will be just two lines in your output. The first line will be an integer giving the largest number of boxes that can fit inside each other. The second line will give the number of such sets of boxes that do fit. For the input values given above, here is the solution set:

Largest Subset of Nesting Boxes
[14, 27, 62]
[16, 40, 90]
[53, 56, 91]
[57, 82, 94]

[14, 27, 62]
[27, 50, 89]
[53, 56, 91]
[57, 82, 94]

[14, 27, 62]
[37, 43, 66]
[53, 56, 91]
[57, 82, 94]

[22, 39, 56]
[27, 50, 89]
[53, 56, 91]
[57, 82, 94]

[22, 39, 56]
[37, 43, 66]
[53, 56, 91]
[57, 82, 94]

[32, 38, 50]
[37, 43, 66]
[53, 56, 91]
[57, 82, 94]

For this solution set, your output will be:

4
6

Where 4 represents the largest number of boxes that fit inside each other, and 6 represents the number of sets of such nesting boxes.

What if there are no nesting boxes? That is, you cannot find a pair of boxes that fit. Then, for the above input file (if this case was true), your output will be:

1
20

The 1 represents that there are no boxes that fit, and the 20 is the total number of boxes.

What if all the boxes fit inside one another? Then, for the above input file, your output will be:

20
1

You must use memoization for this problem. For the boxes in the above input file, the sample memo is included in the repository. You will re-create this memo as a 2-D list in your program.

To run this code on the command line on Mac, you will do:

python3 Boxes.py 

To run the code on the command line on a Windows machine, you will do:

python Boxes.py

