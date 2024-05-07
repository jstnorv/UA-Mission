import pandas as pd
from deep_translator import GoogleTranslator

# Load the CSV file
df = pd.read_csv('AFUStratComTest.csv')

# Create a GoogleTranslator instance
translator = GoogleTranslator(source='uk', target='en')

# Define a function to translate text
def translate_text(text):
    try:
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"Error translating text: {e}")
        return text

# Apply the translation function to the 'Text' column and create a new 'English_Text' column
df['English_Text'] = df['Text'].apply(translate_text)

# Save the updated DataFrame to a new CSV file
df.to_csv('AFUStratComTest_Translated.csv', index=False)
