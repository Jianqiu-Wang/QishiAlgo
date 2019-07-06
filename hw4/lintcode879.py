"""
Description
During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're given n teams, and you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is the strongest team and Rank n is the weakest team.) We'll use parentheses () and commas , to represent the contest team pairing - parentheses () for pairing and commas , for partition. During the pairing process in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.
The n is in range [2, 2^12].
We ensure that the input n can be converted into the form 2^k, where k is a positive integer.
"""
class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: a string
    """
    def findContestMatch(self, n):
        round1 = ["("+str(i+1)+","+str(n-i)+")" for i in list(range(0, int(n/2)))]
        
        def generate_next_round(crt_teams):
            """ crt_teams is a list of strings
            """
            numb_teams = len(crt_teams)
            if len(crt_teams) == 1:
                return crt_teams[0]
            else:
                next_num_teams = int(num_teams/2)
                next_round = ["("+crt_teams[i]+","+crt_teams[number_teams-i-1]+")" for i in list(range(0, next_num_teams))]
                return generate_next_round(next_round)
        
        return generate_next_round(round1)