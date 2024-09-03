# There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. 
# You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the
# block at row r and column c.

# A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. 
# The skyline from each cardinal direction north, east, south, and west may be different.

# We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). 
# The height of a 0-height building can also be increased. 
# However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

# Return the maximum total sum that the height of the buildings can be increased by 
# without changing the city's skyline from any cardinal direction.

grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]
n = len(grid)
rows = n * [0] # we are intiating an array of lenth of grid
cols = n * [0]
print(grid[1][1])
for x in range(n):
    for y in range(n):
        rows[x] = max(rows[x], grid[x][y]) # here we get the skyline seeing from east and west.. first one element in row is fixed and we find 
                                           # maximum by comparing with corresponding row values i.e., 3 with 0,8,4 next 2 with 4,5,7
        cols[y] = max(cols[y], grid[x][y]) # here we get the skyline seeing from north and south.. first we store the first coloumn in cols[y]
                                           # i.e., cols[y]=[3,0,8,4] next it is compared with next coloumn each element like 3 with 2, 0 with 4 etc

print(rows)
print(cols)

total = 0
for x in range(n):
    for y in range(n):
        total += max(min(rows[x], cols[y]) - grid[x][y], 0)

print(total)