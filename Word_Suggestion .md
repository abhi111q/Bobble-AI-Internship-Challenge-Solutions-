# Bobble-AI-Internship-Challenge-Solutions-

Word Suggestion  
Goal: Given a list of words (say dictionary) in a csv file along with its frequency. Take a word as input and suggest five closest words from the dictionary sorted in order of relevance. 
Assume that the user is trying to type a dictionary word which they misspelled, and you have to suggest the correct word. `
Language: Any
Example Input file: 
Content of dictionary.csv 
Hello, 300
World, 50
Hi, 600
How, 500
Are, 900
You, 200
Expected CLI Input:
> ./executable dictionary.csv hellp 
Hello, word2, word3, word4, word5
 
 
Language: C++

Data Structure : BK Tree (BK Tree or Burkhard Keller Tree is a data structure that is used to perform spell check based on
                Edit Distance (Levenshtein distance) concept. 
                BK trees are also used for approximate string matching.)
                
