# minEditDistance
This is Python program that calculates the minimum edit distance between a source word (correctly spelled word) and target word (incorrectly spelleed word).

It uses simple dynamic programming to calculate the most efficient way to change the target word into the source word.
There are three edit operations used to reach this target word: deletion, insertion, and substitution, each edit operation having an equal cost of 1.

The program then uses this minimum edit distance function to calculate the minimum edit distance of the word pairs in a file such as spelling_error.pairs. 

This project was originally created for my Introduction to Natural Language Processing class at San Jose State University.

Created by:
Scott Ruddell
sruddell09@gmail.com
