#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""
perevease = 1
hold = 0
corent = 1
print("1 1", end=' ')

while corent < 100:
    hold = corent
    corent = corent + perevease
    perevease = hold
    print(corent, end=' ')