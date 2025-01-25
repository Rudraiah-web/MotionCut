def count_words(text):

    words = text.split()
    return len(words)


def get_user_input():
    
    user_input = input("Enter a text to count the number of words: ")
    return user_input


def main():
    
    text = get_user_input()
    

    if text.strip() == "":
        print("No text entered. Please enter some text.")
    else:
    
        word_count = count_words(text)
    
        print(f"The number of words in the provided text is: {word_count}")


if __name__ == "__main__":
    main()
