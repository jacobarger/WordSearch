# function to take in a two-dimensional search space (2D array of characters)
# and a search string, then attempt to find that search string in the search
# 2D array. It will check if the word is  forwards, backwards, going upwards or downwards,
# or on a diagonal in the grid. If the word is present, it will return "YES", otherwise it
# will return "NO"
def word_search(search_space, search):

    # iterate over the entire array
    for i in range(0, len(search_space[0])):
        for j in range(0, len(search_space[i])):
            # check if the array contains the first letter of the search
            if search_space[i][j] == search[0]:

                # store current position in array as temporary variables to manipulate for search
                # reset between each direction check
                curr_x = i
                curr_y = j


                # iterate over length of search word

                # check the direction right of the found letter
                if j != len(search_space[i])-1:
                    if search_space[i][j+1] == search[1]:
                        # iterate over each word in the letter
                        for k in range(0, len(search)):
                            # check if our current letter matches the next of the input search
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)

                                # if you have found the last letter, return yes
                                if k == len(search) - 1:
                                    return "YES"

                                # change to the index of the letter to the right
                                curr_y = curr_y + 1

                                # if at right edge, exit to avoid array index error
                                if curr_y == len(search_space[i]):
                                    break

                # check the direction left of the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if j != 0:
                    if search_space[i][j-1] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_y = curr_y - 1
                                if curr_y == -1:
                                    break

                # check the direction above the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if i != 0:
                    if search_space[i-1][j] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_x = curr_x - 1
                                if curr_x == -1:
                                    break
                # check the direction below the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if i != len(search_space[i])-1:
                    if search_space[i+1][j] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_x = curr_x + 1

                                if curr_x == len(search_space[i]):
                                    break

                # check the direction to the upper right of the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if i != 0 and j != len(search_space[i])-1:
                    if search_space[i-1][j+1] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_x = curr_x - 1
                                curr_y = curr_y + 1
                                if curr_x == -1 or curr_y == len(search_space[i]):
                                    break

                # check the direction to the lower right of the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if i != len(search_space[i])-1 and j != len(search_space[i])-1:
                    if search_space[i+1][j+1] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_x = curr_x + 1
                                curr_y = curr_y + 1
                                if curr_x == len(search_space[i]) or curr_y == len(search_space[i]):
                                    break

                # check the direction to the upper left of the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if i != 0 and j != 0:
                    if search_space[i-1][j-1] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_x = curr_x - 1
                                curr_y = curr_y - 1
                                if curr_x == -1 or curr_y == -1:
                                    break

                # check the direction to the lower left of the found letter
                # reset  temporary coordinates to current letter index
                curr_x = i
                curr_y = j
                if i != len(search_space[i])-1 and j != 0:
                    if search_space[i+1][j-1] == search[1]:
                        for k in range(0, len(search)):
                            if search_space[curr_x][curr_y] == search[k]:
                                # print(search[k], k)
                                if k == len(search) - 1:
                                    return "YES"
                                curr_x = curr_x + 1
                                curr_y = curr_y - 1
                                if curr_x == len(search_space[i]) or curr_y == -1:
                                    break

    return "NO"





# Set up test cases
Grid = [
    ['D','U','S','T'],
 	['M', 'R', 'L','A'],
	['V','N','A','B'],
	['O','G','B','D']
]


# run tests on function

print("Is the word: LAB present in the grid? ", word_search(Grid, "LAB"))
print("Is the word: TAB present in the grid? ", word_search(Grid, "TAB"))
print("Is the word: YES present in the grid? ", word_search(Grid, "YES"))
print("Is the word: DUST present in the grid? ", word_search(Grid, "DUST"))
print("Is the word: FERN present in the grid? ", word_search(Grid, "FERN"))
print("Is the word: URN present in the grid? ", word_search(Grid, "URN"))
print("Is the word: NO present in the grid? ", word_search(Grid, "NO"))
