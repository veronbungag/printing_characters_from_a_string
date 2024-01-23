#define a function to get characters from even index
def even_index_characters(input_string):
    even_index_characters = []
#for loop
    for i in range(len(input_string)):
        if i % 2 == 0:
            even_index_characters.append(input_string[i])
    
    return even_index_characters
#accepting user input for a string
input_string = input("Please enter a string: ")
#getting the characters from even index
even_index_characters = even_index_characters(input_string)
#printing the chracters from even index
#for adding newline character after each character