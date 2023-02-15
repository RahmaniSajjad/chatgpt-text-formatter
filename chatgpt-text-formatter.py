"""
The program waits for the user to input some text and press enter.
The entered text is then formatted to have a newline character after each period (".") using the replace method.
The formatted text is then copied to the clipboard using the pyperclip.copy() method.
Finally, a message is printed to the console to indicate that the text has been copied to the clipboard.

The program will continue to run in an infinite loop,
 prompting the user to enter text and copy it to the clipboard until the program is interrupted or closed.

This program can be useful for quickly formatting paragraphs of text to be used in other applications or documents.
By copying the formatted text to the clipboard,
 the user can easily paste it into another program without having to manually add newlines after each period.
"""


# Import the pyperclip module
import pyperclip

# Run an infinite loop to keep the program running until it is interrupted
while True:
    # Prompt the user to enter text
    text = input("Enter Text: ")

    # Replace all occurrences of ". " with ".\n" to create new lines after each period
    text = text.replace(". ", ".\n")

    # Copy the modified text to the clipboard
    pyperclip.copy(text)

    # Notify the user that the text has been copied to the clipboard
    print("Done!")

    # Print an empty line for readability
    print()
