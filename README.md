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
**The Opponent Avoidance Problem**
The staged opponent avoidance problem is a puzzle that comes from a modified real-life scenario,
where soccer players of a team maneuver through an opponent-filled field to find a safe
passage to reach the goalpost.

For example, we could consider the Red Team trying to overcome the Blue Team.
The field is represented by a square 𝒓 × 𝒄 grid with r rows and c columns.
In this modified game, unlike in real-life, players of the opposing team are stationary, and are located in some cells. 
The Red Team starts from the top-left corner of the field, at (row, column) location (0,0), dribbles past the opponents,
and aims to reach the goal post in the bottomright corner at location (r−𝟏, 𝒄 − 𝟏). 
The occupied cells are impenetrable and movements towards the goal post can only be done by moving right,
from location (𝒊,𝒋) to (𝒊,𝒋 + 𝟏); or down, from (𝒊,𝒋) to (𝒊 + 𝟏,𝒋). 
A path may not go through an occupied cell, so the Red Team can only
move to a new location, if there is no opponent at that location.

**The problem objective is to compute the number of different paths to cross the field.**
Two paths are different if they differ by at least one location.

<br>

## Exhaustive Search
The exhaustive search algorithm is designed to find all possible paths from the top-left corner (0,0) to the bottom-right corner (r−1,c−1) of a grid G.
It counts the number of valid paths that do not cross any "X" cells (obstacles) and remain within the bounds of the grid.
The algorithm generates all potential paths by treating moves as binary sequences, where "0" represents a downward move (↓) and "1" represents a rightward move (→). The total number of moves required to reach the target is $$n=r+c−2$$, with exactly $$r−1$$ downward moves and $$c−1$$ rightward moves. Using binary numbers from 0 to $$2^n−1$$, each bit sequence is interpreted as a candidate path.

For each candidate:
1. The algorithm constructs the sequence of moves based on the binary representation.
2. It verifies whether the path stays within the grid, avoids "X" cells, and ends at $$(r−1,c−1)$$.
3. If valid, the path counter is incremented.

<br><br><br>

## Dynamic Programming 
This problem can also be solved using a dynamic programming approach. The dynamic
programming 𝑚𝑎𝑡𝑟𝑖𝑥 𝐴 stores partial solutions to the problem. In particular,
𝐴[𝑖][𝑗] = the number of different valid paths that start at (0,0) and end at (𝑖,𝑗); or 0 if (𝑖,𝑗) is
unreachable.
Recall that in this problem, some cells are filled with Blue Team players and are therefore
unreachable by a valid path. The base case is the value for 𝐴[0][0], which is the trivial path that
starts at (0,0) and takes no subsequent steps: A[0][0] = 1. A solution for a general case can be
built based on pre-existing shorter paths. The Red Team player can only move right and down. So,
there are two ways a player can reach location (𝑖,𝑗).
1. A path reaches the location above (𝑖,𝑗), then moves down.
2. A path reaches the location left of (𝑖,𝑗), then moves right.
The algorithm should count both alternatives.


**Therefore, the general solution is:**
𝐴[𝑖][𝑗] = 0
if 𝐹[𝑖][𝑗] = 𝑋
  𝐴[𝑖][𝑗] = 𝑎𝑏𝑜𝑣𝑒 + 𝑙𝑒𝑓t
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
