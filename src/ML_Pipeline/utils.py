import json
import random
import spacy

# Function to check if an existing model with the given name exists
def check_existing_model(model_name):
    try:
        # Try to load the model with the provided name
        nlp = spacy.load(model_name)
        print("Model Exists. Updating the model")
        return model_name  # Return the existing model name
    except Exception as e:
        # If an exception occurs, it means the model doesn't exist
        print("Model by this name does not exist. Building a new one")
        return None  # Return None to indicate the need to create a new model
