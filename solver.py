import sys
import pickle
import logging
logging.basicConfig(level=logging.INFO)

import matplotlib.pyplot as pyplot

def solver(maze):
	"""
	Finds and prints a path from the starting cell (1, 0)
	to the ending cell (-2, -1). Returns None if no such
	path exists.

	maze: 2d array of size (41, 81). True => wall, False => no wall
	"""


def main():
	with open("maze.pickle", "rb") as f:
		maze_res = pickle.load(f)

	# uncomment to print the maze
	# pyplot.figure(figsize=(10, 5))
	# pyplot.imshow(maze_res, cmap=pyplot.cm.binary, interpolation='nearest')
	# pyplot.xticks([]), pyplot.yticks([])
	# pyplot.show()

	# invoke the solver
	solver(maze_res)


if __name__ == "__main__":
	sys.exit(main())