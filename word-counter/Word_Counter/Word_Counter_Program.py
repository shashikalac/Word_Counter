# Word Counter Program
# This program counts the number of words in a given sentence or paragraph.

def count_words(text):
    """
    Counts the number of words in the given text.
    
    Parameters:
    text (str): The input text to be analyzed.

    Returns:
    int: The word count.
    """
    # Split the text by whitespace and count the resulting words
    words = text.split()
    return len(words)

def main():
    # Prompt the user for input
    text = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not text:
        print("Error: No input provided. Please enter some text.")
        return
    
    # Calculate word count
    word_count = count_words(text)
    
    # Display the result
    print(f"Word Count: {word_count}")

# User friendly interface as per user's convince
while(True):
    a=int(input("Enter: 1 or 2 \n 1 : To continue word counting \n 2 : To exit\n"))
    if(a==1):
        {
            main()
        }
    elif(a==2) :
        break
    else:
        print("Enter valid input")
