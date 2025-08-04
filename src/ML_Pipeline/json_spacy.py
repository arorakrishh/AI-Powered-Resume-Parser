import json
import os
import random
import logging
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
from spacy.gold import GoldParse
from spacy.scorer import Scorer

# Function to convert data from a JSON file to spaCy format
def convert_data_to_spacy(JSON_FilePath):
    try:
        training_data = []  # Create an empty list to store training data
        lines = []

        with open(JSON_FilePath, 'r', encoding='utf-8') as f:
            lines = f.readlines()  # Read the lines from the JSON file

        for line in lines:
            data = json.loads(line)
            text = data['content']  # Extract the text from the JSON data
            entities = []

            for annotation in data['annotation']:
                # Extract the annotation points and labels
                point = annotation['points'][0]
                labels = annotation['label']

                # Ensure labels are in a list format
                if not isinstance(labels, list):
                    labels = [labels]

                for label in labels:
                    # Append the start, end, and label information to entities list
                    entities.append((point['start'], point['end'] + 1, label))

            training_data.append((text, {"entities": entities}))

        return training_data  # Return the training data in spaCy format
    except Exception as e:
        # Handle exceptions and log errors
        logging.exception("Unable to process " + JSON_FilePath + "\n" + "error = " + str(e))
        return None
