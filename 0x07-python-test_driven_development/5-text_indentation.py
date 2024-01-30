def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_of_sentence_chars = ['.', '?', ':']
    
    current_line = ""
    for char in text:
        current_line += char
        if char in end_of_sentence_chars:
            print(current_line.strip())
            print()  # Print two new lines
            current_line = ""

    if current_line.strip():
        print(current_line.strip())

# Example usage:
text = "This is a sample text. It has multiple sentences. How does it handle question marks? Let's see!"
text_indentation(text)

