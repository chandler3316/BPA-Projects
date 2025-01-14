import random
# Step 1 prompts user for # of dials for lock combos, makes sure input is at least 3, converts input into integer, chekcs if its less than 3, executes when passes validation, prevents program from crashing
def get_number_in_dials():
    while True:
        try:
            num_dials = int(input("Each lock has how many dials? "))
            if num_dials < 3:
                print("Error: Each lock must have at least 3 dials.")
            else:
                return num_dials
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Step  2 -  define function: Make it reusable, prompts user for num of lock combinations to display and returns it to combinations, infinite loop so user has to put valid input, prompts user for lock combinations
# Error handling if user puts less than 1, once it passes check it ends the function and input returns back to user, and finally makes sure user puts a number not a word or letter
def get_how_many_to_list():
    while True:
        try:
            num_combinations = int(input(" How many combinations should I generate? "))
            if num_combinations < 1:
                print("Error: You have to generate more than 1 combination. ")
            else:
                return num_combinations
        except ValueError:
            print("Invalid input: Please enter a number not a word.")

# Step 3 - defines the function iwth a min and max range of values, calls random.randrange to generate a random # and returns it to the caller, generates numbeer whithin range, uses +1 to make it inclusive 
def get_number(min_value, max_value):
    return random.randrange(min_value, max_value + 1)

# Step 4 - defines function to generate lock combos and has setp parameters for number of dials in lock combo, generates lock combos as list of random numbers then converts them to strings
# Uses _ as a placeholder since we dont know what the value is yet and calls get_number and generates random digit between 0 and 9 and converts each number into a string, 
# combines list of strings into string with spaces between digits like "3 7 8" not ["3", "7", "8"]
def next_combo_number(num_dials):
    combo = [str(get_number(0, 9)) for _ in range(num_dials)]
    return" ".join(combo)

# Step 5 - defines main function and is the programs workflow, calls variable for each lock and stores the number, calls variable and stores the number, formatting with \n, 
# Starts loop from 1 to num_combinations + 1 and generates the lock combo, prints seperator line indicating end of list, uses f string to insert the value amd produces the ourput of the program
def main():
    num_dials = get_number_in_dials()
    num_combinations = get_how_many_to_list()

    print("\n----------")
    for i in range(1, num_combinations + 1):
        combo = next_combo_number(num_dials)
        print(f"Number {i}: {combo}")
    print("----------")
    print(f"{num_combinations} random combinations were generated.")

# Step 6 - special variable and determines if script is being imported to module and makes sure main() is executed directly, calls main function to start the program and its entry point
if __name__ == "__main__":
    main()
    