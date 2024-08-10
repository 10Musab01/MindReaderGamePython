Hello there!
This was one of my first Python projects where i created a simple "Heads and Tails: Mind Guessing" game using whilst implementing the famous Claude Shannon's Algorithm...
The Claude Shannon's Algorithm consists of analysing the user's last/ last 2 inputs and then predicting their next move.
For example in this game:
There are 8 possible situations and, for each situation, a player can do two things. These 8 situations are:

    The player wins, plays the same and wins again. The player then plays the same or plays differently.

    The player wins, plays the same and loses. The player then plays the same or plays differently.

    The player wins, plays differently and wins again. The player then plays the same or plays differently.

    The player wins, plays differently and loses. The player then plays the same or plays differently.

    The player loses, plays the same and wins. The player then plays the same or plays differently.

    The player loses, plays the same and loses again. The player then plays the same or plays differently.

    The player loses, plays differently and wins. The player then plays the same or plays differently.

    The player loses, plays differently and loses again. The player then plays the same or plays differently.

Each situation corresponds to a different cell in the memory of a machine. Within a cell, two events are registered:

    Whether the last time this situation arose, the player played the same or different.

    Whether or not the behaviour indicated in the first point, was a repeat of the same behaviour in the preceding situation.

The sole of the game (for the user) is to make sure that the computer does not guess your number...

