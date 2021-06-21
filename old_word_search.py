 
 
Grid = [
    ['D','U','S','T'],
 	['M', 'R', 'D','A'],
	['V','N','A','B'],
	['R','G','O','D']
]
Grid2 = [
    ['D','U','S','T'],
 	['M', 'T', 'E','G'],
	['V','E','A','B'],
	['R','G','B','D']
]
 
 
 
 
# def check_surrounding_letters(a, cur_x, cur_y):
#
 
 
 
 
def word_search(search_space, search):
 
    # iterate over the entire array
    for i in range(0, len(search_space[0])):
        for j in range(0, len(search_space[i])):
            # check if the array contains the first letter of the search
            if search_space[i][j] == search[0]:
 
                # store current position in array as temporary variables to manipulate for search
                curr_x = i
                curr_y = j
                direction = "reset"
                # iterate over length of search word
 
                if j != len(search_space[i])-1:
                    if search_space[i][j+1] == search[1]:
                        direction = "right"
                if j != 0:
                    if search_space[i][j-1] == search[1]:
                        direction = "left"
                if i != 0:
                    if search_space[i-1][j] == search[1]:
                        direction = "up"
                if i != len(search_space[i])-1:
                    if search_space[i+1][j] == search[1]:
                        direction = "down"
 
 
                if direction == "right":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_y = curr_y + 1
                            if curr_y == len(search_space[i]):
                                break
                if direction == "left":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
 
                            curr_y = curr_y - 1
                            if curr_y == 0:
                                break
                if direction == "down":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_x = curr_x + 1
                if direction == "up":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_x = curr_x - 1
                if direction == "up_right":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_x = curr_x - 1
                            curr_y = curr_y + 1
                if direction == "up_left":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_x = curr_x - 1
                            curr_y = curr_y - 1
                if direction == "down_left":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_x = curr_x + 1
                            curr_y = curr_y - 1
                if direction == "down_right":
                    for k in range(0, len(search)):
                        if search_space[curr_x][curr_y] == search[k]:
                            print(search[k], k)
                            if k == len(search) - 1:
                                return "YES"
                            curr_x = curr_x + 1
                            curr_y = curr_y + 1
 
 
 
                # for k in range(0, len(search)):
                #
                #
                #     # check to the right
                #     if j != len(search_space[i])-1:
                #         if search_space[curr_x][curr_y] == search[k]:
                #             print(search[k], k)
                #             if k == len(search)-1:
                #                     return "YES"
                #             curr_y = curr_y + 1
                #
                #     # check to the left
                #     elif search_space[curr_x][curr_y] == search[k]:
                #         direction = "left"
                #         print(search[k], k)
                #         if k == len(search)-1:
                #                 return "YES"
                #         curr_y = curr_y - 1
                #
                #     # check downward
                #     elif search_space[curr_x][curr_y] == search[k]:
                #
                #         direction = "down"
                #         print(search[k], k)
                #         if k == len(search)-1:
                #                 return "YES"
                #         curr_x = curr_x + 1
                #
                #
                #     # elif search_space[i][j - 1] == search[k]:
                #     #     if k == len(search):
                #     #             return "YES"
                #     else:
                #         break
    return "NO"
 
 
 
 
 
print("test")
print(word_search(Grid, "DUST"))
print(word_search(Grid2, "GET"))
print(word_search(Grid, "DAB"))
print(word_search(Grid, "TAB"))
print(word_search(Grid, "NO"))
