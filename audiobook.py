import pyttsx3
import fitz

# Flag to track whether the speech is paused
paused = False

# Function to toggle the paused state
def toggle_pause():
    global paused
    paused = not paused

try:
    # Open the PDF file
    with fitz.open('OS_Module-3.pdf') as pdf_document:#replace "OS_Module-3.pdf" with the name of your PDF file

        # Get the number of pages
        pages = pdf_document.page_count
        print("Number of pages:", pages)

        # Initialize text-to-speech engine
        speak = pyttsx3.init()

        # Read text from each page and concatenate
        for page_num in range(pages):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            print(text)  # Print text for debugging

            # Check for Enter button press to toggle pause
            input("Press Enter to pause or resume...")  # Wait for Enter key press
            toggle_pause()

            # Speak the text if not paused
            if not paused:
                speak.say(text)
                speak.runAndWait()

        speak.say('The number of pages in the PDF is ' + str(pages))
        speak.runAndWait()

except FileNotFoundError:
    print("File not found. Please ensure the PDF file exists.")
except Exception as e:
    print("An error occurred:", e)
