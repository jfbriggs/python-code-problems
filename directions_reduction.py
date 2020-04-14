"""
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort.
Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountain desert the smart way.
The directions given to the man are, for example, the following:

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]

Other examples:

In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [].

TASK:

Write a function dir_reduc() which will take a list of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

*Note: Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible.
"NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such.
Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
"""

def dir_reduc(arr):
    pass

## TEST CODE ##
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) # ["WEST"]
print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])) # ["NORTH", "WEST", "SOUTH", "EAST"]
