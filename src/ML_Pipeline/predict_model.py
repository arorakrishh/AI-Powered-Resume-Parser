import spacy
from ML_Pipeline import text_extractor

# Function for making predictions using a spaCy NER model
def predict(path):
    # Create an empty dictionary for the output (if needed)
    #output = {}
    
    # Load the spaCy NER model
    nlp = spacy.load("model")  # Replace "model" with the actual path to your model
    
    # Convert PDF files to text using the text_extractor module
    test_text = text_extractor.convert_pdf_to_text(path)
    
    # Process each extracted text
    for text in test_text:
        text = text.replace('\n', ' ')  # Replace newline characters with spaces
        doc = nlp(text)  # Process the text with the spaCy model
        
        # Extract and print named entities
        for ent in doc.ents:
            print(f'{ent.label_.upper():{30}} - {ent.text}')
            # You can also store the entities in the output dictionary
            #output[ent.label_.upper()] = ent.text
    
    # Return the output dictionary if needed
    #return output
