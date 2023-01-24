#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Boxes.py

#  Description: Calculates the maximum number of boxes that fit inside each other and the number of 
# nesting sets of boxes

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 03/09/2022

#  Date Last Modified: 03/11/2022

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes

# global variables
max_boxes = 0
num_sets = 0

def nesting_boxes (box_list):
  subsets = []
  nesting_boxes_helper(box_list, 0, subsets)
  return max_boxes, num_sets

def nesting_boxes_helper (box_list, index, subsets):
    global max_boxes
    global num_sets
    
    # base case 
    if index >= len(box_list):
        # when there is a larger box
        # sets max_boxes to length of subsets
        if len(subsets) > max_boxes:
            max_boxes = len(subsets)
            # num_sets resets to 1
            num_sets = 1
        elif len(subsets) == max_boxes:
            num_sets += 1
        return 
    else:
        # new subset
        if len(subsets) == 0:
            subsets.append(box_list[index])
            # recursive call
            nesting_boxes_helper(box_list, index + 1, subsets)
            # remove the box added
            subsets.remove(box_list[index])
        else:
            # sees if the current box fits in the last box in the subset
            if does_fit(subsets[-1], box_list[index]):
                subsets.append(box_list[index])
                # recursive call
                nesting_boxes_helper(box_list, index + 1, subsets)
                # removes the box added
                subsets.remove(box_list[index])
        # recursive call
        nesting_boxes_helper(box_list, index + 1, subsets)
                
        
            
        
        

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()
  
 

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()


