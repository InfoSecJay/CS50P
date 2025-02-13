#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // If name is a match for the name of a valid candidate, then you should update the global preferences array to indicate that the voter voter has that candidate as their rank preference
    for (int i = 0; i < candidate_count; i++)  // Loop over the candidates
    {
        if (strcmp(name, candidates[i].name) == 0) // Compare the name to see if it exists, if it does, update the preference
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO
    for (int i = 0; i < voter_count; i++)  // Loop over the voters
    {
        for (int j = 0; j < candidate_count; j++) // Loop over the candidates
        {
            if(!candidates[preferences[i][j]].eliminated) // If the candidate is not eliminated, then add a vote
            {
                candidates[preferences[i][j]].votes++;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // If any candidate has more than half of the vote, their name should be printed and the function should return true
    int majority = round(voter_count / 2);
    for (int i = 0; i < candidate_count; i++)  // Loop over the candidates
    {
        if (candidates[i].votes > majority)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // The function should return the minimum vote total for any candidate who is still in the election.
    //Set min_votes to the first candidate and loop through candidates to find the new min until finished
    int min_votes = candidates[0].votes;
    for (int i = 0; i < candidate_count; i++)  // Loop over the candidates
    {
        if(!candidates[i].eliminated && candidates[i].votes < min_votes) // If the candidate is not eliminated and candidate has
        {
            min_votes = candidates[i].votes;
        }
    }
    return min_votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // take in min which is min number of votes anyone in election has and returns turn if eery candidate remainig has same number of votes or false otherwise

    for (int i = 0; i < candidate_count; i++)  // Loop over the candidates
    {
       if (!candidates[i].eliminated && candidates[i].votes != min)
       {
            return false;
       }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // Takes in min which is min number of votes anyone has and eliminiate the candiadte who has the min votes
    for (int i = 0; i < candidate_count; i++)  // Loop over the candidates
        if (candidates[i].eliminated == false && candidates[i].votes == min)
        {
            candidates[i].eliminated=true;
        }
    return;
}
