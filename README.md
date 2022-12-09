This repository is for [Advent of Code 2022](https://adventofcode.com/) 🎄

### Contents
1. [Day 1](#day1)
2. [Day 2](#day-2-rock-paper-scissors) 🎸📰✂
3. [Day 3](#day-3-)
4. [Day 4](#day-4-)
5. [Day 5](#day-5-)
6. [Day 6](#day-6-)
7. [Day 7](#day-7-)
8. [Day 8](#day-8-treetop-tree-house) 🌲🏠
9. [Day 9](#day-9-)
10. ...

Day 1: [Calorie Counting](/day1#day-1-calorie-counting)

## Day 2: Rock Paper Scissors

### Part 1: Rock Paper Scissors

The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant [Rock Paper Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an __encrypted strategy guide__ (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: `A` for Rock, `B` for Paper, and `C` for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: `X` for Rock, `Y` for Paper, and `Z` for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your __total score__ is the sum of your scores for each round. The score for a single round is the score for the __shape you selected__ (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the __outcome of the round__ (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

```
A Y
B X
C Z
```

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (`A`), and you should choose Paper (`Y`). This ends in a win for you with a score of __8__ (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of __1__ (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = __6__.
In this example, if you were to follow the strategy guide, you would get a total score of `15` (8 + 1 + 6).

__What would your total score be if everything goes exactly according to your strategy guide?__


### Part Two

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (`A`), and you need the round to end in a draw (`Y`), so you also choose Rock. This gives you a score of 1 + 3 = __4__.
In the second round, your opponent will choose Paper (`B`), and you choose Rock so you lose (`X`) with a score of 1 + 0 = __1__.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = __7__.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of `12`.

Following the Elf's instructions for the second column, __what would your total score be if everything goes exactly according to your strategy guide?__

...

## Day 8: Treetop Tree House

Assumptions within our code: 
- input is and `n` x `n` grid

In this challenge we started with the usual approach of taking our input and splitting it into separate rows, from here we iterate through each element, in each row. Since all exterior trees in the `n` x `n` grid are visible we don't need to perform any calculations on them and we'll revisit this later. 

As mentioned in our approach we perform no calculations on the first and final rows in the grid, this logic is [here](https://github.com/mitchdawson1982/aoc22/blob/2178441dd9ee8fdae687b192c4aaaa66e3d570db/day8/main.py#L16):

```
...
if number_index == 0 or number_index == last_number_index:
    continue
...
``` 

Following this we iterate through each element in each row and check if it is visible. In order, we examine elements to the [left](https://github.com/mitchdawson1982/aoc22/blob/2178441dd9ee8fdae687b192c4aaaa66e3d570db/day8/main.py#L21), [right](https://github.com/mitchdawson1982/aoc22/blob/2178441dd9ee8fdae687b192c4aaaa66e3d570db/day8/main.py#L26), [above](https://github.com/mitchdawson1982/aoc22/blob/2178441dd9ee8fdae687b192c4aaaa66e3d570db/day8/main.py#L34) and [below](https://github.com/mitchdawson1982/aoc22/blob/2178441dd9ee8fdae687b192c4aaaa66e3d570db/day8/main.py#L42). As demonstrated below for the element in the centre of the grid - `3`, elements which are to be compared are highlighted in bold.

Left:
<pre>
30373
25512
<b>65</b>332
33549
35390
</pre>

Right:
<pre>
30373
25512
653<b>32</b>
33549
35390
</pre>

Above:
<pre>
30<b>3</b>73
25<b>5</b>12
65332
33549
35390
</pre>

Below:
<pre>
30373
25512
65332
33<b>5</b>49
35<b>3</b>90
</pre>

In each comparison we compare the element in question to the maximum element in whichever direction is being examined. We could compare to each element indicudiau

