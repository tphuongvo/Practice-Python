# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

def minion_game(string):
    kevin_counts, stuart_counts = 0,0

    for i in range(len(string)):
        if string[i] in 'UEOAI':
            kevin_counts += len(string)-i
        else:
            stuart_counts += len(string)-i 

    if stuart_counts > kevin_counts:
        return print(f'Stuart {stuart_counts}')
    elif kevin_counts > stuart_counts:
        return print(f'Kevin {kevin_counts}')
    else:
        return print(f'Draw')
    
s = input()
print(minion_game(s))