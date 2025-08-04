# Import necessary modules from the ML_Pipeline package
from ML_Pipeline import json_spacy
from ML_Pipeline import train_model
from ML_Pipeline import predict_model
from ML_Pipeline import text_extractor
from ML_Pipeline import utils

# Convert tagged data into a format compatible with spaCy
train = json_spacy.convert_data_to_spacy("../input/training/Entity Recognition in Resumes.json")

# Display the first element of the training data (for debugging)
#print(train[0])

# Inform that the data has been successfully converted into spaCy format
print("Done. Converted into spaCy format")

# Check if a pre-built spaCy model exists, if not, train a new one
print("Checking if previously built spaCy model exists. If not, we will train a new one")
model = utils.check_existing_model("nlp_model")
model = train_model.build_spacy_model(train, model)

# Convert PDFs to text for processing
test_text = text_extractor.convert_pdf_to_text("../output/")

# Perform predictions on the extracted text
predict_model.predict("../output/")

# Additional commented-out code (not active)
#mine = text_extractor.convert_pdf_to_text('../input/resumes')
#print(test.head())
