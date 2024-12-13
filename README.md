# CPSC-33511 Project 2
2024 California State University Fullerton CPSC 335-11 (Algorithm Engineering) Project 2 <p> <p> <br>

## Project Subject
Opponent Avoidance Problem <br>
Polynomial versus Exponential Time

<br>

## Requirements for dependencies 
Required modules: `matplotlib` `numpy` `time` `random`

<br>

## Instructions for running each algorithm
1. Clone Repository: `https://github.com/isliese/CPSC-33511-Project2.git` <br>
2. `cd CPSC-33511-Project2` <br>
3. Run programs
* To run Exhaustive Search Algorithm: `python exhaustivesearch.py` <br>
* To run Dynamic Programming: `python dynamicprogramming.py` <br>
* To measure the execution time of two algorithms for the problem: `python timingdata.py` <br>
* To draw scatter plots for two algorithms and compare with theoretical time complexity: `python scatterplot.py` <br>



<br><br><br>

## Hypothesis 
This project will test the following hypotheses:
1. Exhaustive search algorithms can be implemented, and produce correct outputs.
2. Algorithms with exponential or factorial running times are extremely slow, probably too
slow to be of practical use. <br> <br>

To test these hypotheses, you will implement two algorithms:
* a 𝑂(𝑛. $$2^𝑛$$) - time exhaustive search algorithm for the staged opponent avoidance
problem
* a O($$𝑛^2$$) − time dynamic programming algorithm for the same problem.

<br>

## Problem 
The Opponent Avoidance Problem
The staged opponent avoidance problem is a puzzle that comes from a modified real-life scenario,
where soccer players of a team maneuver through an opponent-filled field to find a safe
passage to reach the goalpost.

<br>

## Exhaustive Search
<br><br><br>
## Dynamic Programming 
<br><br><br>

## Results
<img src="https://github.com/user-attachments/assets/560d7e27-77bd-4a16-9c80-75818949ab81" width="40%">
<img src="https://github.com/user-attachments/assets/5872abdd-fae5-4bc5-9db6-dda1d50fa7f5" width="39%">

Using exhaustive search follows a time complexity of  O(𝑛. $$2^𝑛$$) , while dynamic programming (DP) follows a time complexity of  O($$n^2$$) , as confirmed through a scatter plot.
Although the exhaustive algorithm can obtain all possible paths, it takes too much time to be practical. On the other hand, using the DP algorithm significantly reduces the time required to find the solution.

<br>

## Collaborators 
- **Chanran Kim (shining04@csu.fullerton.edu)**: Dynamic Programming Algorithm and Scatter Plot Graph
- **Brian Alvarez (briandalvarez@csu.fullerton.edu)**: Exhaustive Search Algorithm
- **Christopher Contreras (CContreras71@csu.fullerton.edu)**: Timing Result and Scatter Plot Graph
- **Vinh Nguyen(vinhgod123@csu.fullerton.edu)**: Project Report
