from googletrans import Translator

def translate_text(text, src_language='en', dest_language='ru'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_language, dest=dest_language)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Enter text to translate:")
    text = input()
    
    print("Enter source language (e.g., 'en' for English):")
    src_language = input()
    
    print("Enter target language (e.g., 'ru' for Russian):")
    dest_language = input()
    
    translated_text = translate_text(text, src_language, dest_language)
    print(f"Translated text: {translated_text}")


main()