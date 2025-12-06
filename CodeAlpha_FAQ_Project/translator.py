# --- START OF translator.py CODE ---
from googletrans import Translator, LANGUAGES

def translate_text():
    """
    Translates user input text into Tamil and Hindi.
    """
    
    # 1. Create a Translator object
    try:
        translator = Translator()
    except Exception as e:
        print(f"Error initializing translator: {e}")
        print("Please check your internet connection or the library installation.")
        return

    print("--- 🌍 Language Translation Tool (Task 1) ---")
    print("Enter the text you want to translate (Type 'exit' to quit):")

    while True:
        try:
            # Get input from the user
            user_input = input("\n Enter English Text: ")
            
            if user_input.lower() == 'exit':
                print("Translator closing. Goodbye!")
                break
                
            if not user_input.strip():
                continue
            
            # Define source and target languages
            source_lang = 'en' # We assume input is English (can be auto-detected)
            target_tamil = 'ta'
            target_hindi = 'hi'
            
            print("\n🤖 Translation Results:")

            # Translate to Tamil
            translation_ta = translator.translate(user_input, src=source_lang, dest=target_tamil)
            print(f"Tamil :{translation_ta.text}")

            # Translate to Hindi
            translation_hi = translator.translate(user_input, src=source_lang, dest=target_hindi)
            print(f"Hindi : {translation_hi.text}")
            
            # Optional: Add a copy-to-clipboard feature simulation
            # (Note: Direct clipboard access is complex in standard terminal scripts, so we'll just print a hint)
            print("\n💡 Note: You can manually copy the translated text now.")


        except Exception as e:
            # Handle potential translation API or connection errors
            print(f"\n❌ An error occurred during translation: {e}")
            print("Trying again...")


# Run the main function
if __name__ == "__main__":
    translate_text()

# --- END OF translator.py CODE ---