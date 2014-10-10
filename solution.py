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
	result = _solve(maze, 1, 0, set(), 39, 80)
	result.reverse()
	for x, y in result:
		print("({}, {})".format(x, y))

def _solve(maze, x_pos, y_pos, visited, x_dest, y_dest):
	if x_pos == x_dest and y_pos == y_dest:
		return [(x_pos, y_pos)]

	moves = [
		(0, 1),
		(1, 0),
		(0, -1),
		(-1, 0)]
	
	for dx, dy in moves:
		new_x = x_pos + dx
		new_y = y_pos + dy

		logging.info("current is (%d, %d), next is (%d, %d), path len is %d", x_pos, y_pos, new_x, new_y, len(visited))

		# not already visited?
		if (new_x, new_y) in visited:
			logging.info("(%d, %d) was already in the path", new_x, new_y)
			continue
		
		# dont recurse into this again
		visited.add((new_x, new_y))

		# new_x in bounds?
		if not (new_x >= 0 and new_x <= len(maze)):
			logging.info("(%d, %d) had a bad x", new_x, new_y)
			continue

		# new_y in bounds?
		if not (new_y >= 0 and new_y <= len(maze[0])):
			logging.info("(%d, %d) had a bad y", new_x, new_y)
			continue

		# no wall present?
		if maze[new_x, new_y]:
			logging.info("(%d, %d) was a wall", new_x, new_y)
			continue

		# all conditions checked, continue the recursion
		result = _solve(maze, new_x, new_y, visited, x_dest, y_dest)
		if result:
			return result + [(new_x, new_y)]

		else:
			logging.info("(%d, %d) wasnt part of the solution", new_x, new_y)

	logging.info("ending recursion from (%d, %d)", x_pos, y_pos)
	return None

def main():
	with open("maze.pickle", "rb") as f:
		maze_res = pickle.load(f)

	print len(maze_res)
	print len(maze_res[0])

	solver(maze_res)

	# pyplot.figure(figsize=(10, 5))
	# pyplot.imshow(maze_res, cmap=pyplot.cm.binary, interpolation='nearest')
	# pyplot.xticks([]), pyplot.yticks([])
	# pyplot.show()


if __name__ == "__main__":
	sys.exit(main())