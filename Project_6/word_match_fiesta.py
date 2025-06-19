# Step 1: Import the random module to use for shuffling lists
import random

# Step 2: Create a function to generate randomised matrices from English and Spanish word lists.
def generate_random_matrix(rows, cols, words1, words2):

    # Calculate the total number of words needed for the matrices
    total_words = rows * cols
    if total_words > len(words1) or total_words > len(words2):
        raise ValueError("Matrix size exceeds the number of available words.")
    
    paired_words = list(zip(words1, words2))
    random.shuffle(paired_words)

    english_words, spanish_words = zip(*paired_words)

    #shuffle Spanish words to ensure they don't line up
    spanish_words = list(spanish_words)
    random.shuffle(spanish_words)

    matrix1 = []
    matrix2 = []

    for i in range(rows):
        row1 = english_words[i * cols: (i + 1) * cols]
        row2 = spanish_words[i * cols: (i + 1) * cols]
        matrix1.append(list(row1))
        matrix2.append(list(row2))

    return matrix1, matrix2

# Step 3: Display the English and Spanish word matrices side by side
def display_matrices(matrix1, matrix2):
    for row in range(len(matrix1)):
        for column in range(len(matrix1[row])):

            # Print English word from both matrices in the same row
            word1 = matrix1[row][column] if column < len(matrix1[row]) else ""
            word2 = matrix2[row][column] if column < len(matrix2[row]) else ""

            # Align English words to the left with 15 spaces for readability
            print(f"{word1.ljust(15)} {word2}")
        print() # Print a new line after each row

# Step 4: Define the match_words function to handle user input 
# Also checks if the entered word pair is correct
def match_words(matrix1, matrix2, word_pairs):
    
    user_input = input("Enter a pair (English Spanish) or type 'quit' to exit or 'restart' to restart the game: ").strip()

    if user_input.lower() == 'quit':
        print("Game Ended.")
        return None, None

    if user_input.lower() == 'restart':
        main()
        return None, None

    user_input = user_input.split()

    if len(user_input) != 2:
        print("Error: Please enter exactly two words.")
        return matrix1, matrix2

    english_word, spanish_word = user_input

    # Check if the pair matches any in the list of correct pairs
    if (english_word, spanish_word) in word_pairs:
        print("Correct match!")

        # Remove the matched words from the matrices
        matrix1, matrix2 = clear_matched_words(matrix1, matrix2, english_word, spanish_word)

        # Remove the matched pair from the word_pairs list
        word_pairs.remove((english_word, spanish_word))
    else:
        print("Incorrect match. Try again.")
    
    return matrix1, matrix2

# Step 5: Define the clear_matched_words function to remove matched words from the matrices
def clear_matched_words(matrix1, matrix2, english_word, spanish_word):

    for row in range(len(matrix1)):
        for column in range(len(matrix1[row])):
            if matrix1[row][column] == english_word:
                matrix1[row][column] = "" # Clear the matched English word
            if matrix2[row][column] == spanish_word:
                matrix2[row][column] = "" # Clear the matched Spanish word
    
    return matrix1, matrix2

# Step 6: Define the main function to start and manage the word matching game
def main():
    
    # Define lists of English and Spanish words
    english_words = ['apple', 'strawberry', 'orange', 'grape', 'pear', 'peach']
    spanish_words = ['manzana', 'fresa', 'naranja', 'uva', 'pera', 'durazno']

    # Set the number of rows and columns for the matrices
    rows, cols = 3, 2

    # Generate randomised matrices from the word lists
    matrix1, matrix2 = generate_random_matrix(rows, cols, english_words, spanish_words)

    # Display the matrices side by side
    display_matrices(matrix1, matrix2)

    # Create a list of correct word pairs for checking matches
    word_pairs = list(zip(english_words, spanish_words))

    # Start the game loop
    while word_pairs:

        # Handle user input and update the matrices
        matrix1, matrix2 = match_words(matrix1, matrix2, word_pairs)

        if matrix1 is None: # This happens if the user quits or restarts the game
            break

        # Display updated matrices
        display_matrices(matrix1, matrix2)

    if matrix1 is not None: 
        print("Congratulations! You've matched all the words!")

# Start the game when launched
main()
