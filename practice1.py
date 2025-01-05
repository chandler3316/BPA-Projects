# Contestant number: 

# Step 1 - Making main function, prompting user, and initializing list
def main():
    num_words = int(input("How many words would you like to enter? "))
    words = []

    # Step 2 - created the for loop, prompts the user while updating "Enter word 1" to "Enter word 2", and stores the word to a list
    for i in range(num_words):
        word = input(f"Enter word {i + 1}: ")
        words.append(word)

    # Step 3 Write words to file, file handling, iterating over words list, and confirmation message 
    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

    print("Words have been saved to 'words.txt'.")

    # Step 4 opens file in read mode and assigns it to variable file, reads all lines seperately, and strips each word of white spaces or \n
    with open("words.txt" , "r") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        
    # Step 5 finds length of the list, finds the max or highest numbered word, finds the total length of all words, and gets the evrage of all of the error handling
    num_words = len(words)
    longest_word = max(words, key=len)
    total_length = sum(len(word) for word in words)
    average_length = total_length / num_words if num_words > 0 else 0


   # Step 6: Display the results,
    print("\nAnalysis of 'words.txt':")
    print(f"Total number of words: {num_words}")
    print(f"Longest word: {longest_word}")
    print(f"Average word length: {average_length:.2f}")

if __name__ == "__main__":
    main()











