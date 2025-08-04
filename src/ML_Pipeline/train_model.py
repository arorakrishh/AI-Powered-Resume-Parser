import spacy
import random
from spacy.util import minibatch, compounding

# Function to train the spaCy NER model
def build_spacy_model(train, model):
    if model is not None:
        nlp = spacy.load(model)  # Load an existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # Create a blank Language class
        print("Created a blank 'en' model")

    TRAIN_DATA = train  # Training data in spaCy format

    # nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy


    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')  # Create a Named Entity Recognition (NER) pipe
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe("ner")
       

     # Add custom labels to the NER model
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])


      # Get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    
    """
    with nlp.disable_pipes(*other_pipes):  # only train NER
        if model is None:
            optimizer = nlp.begin_training()
        for itn in range(2):
            print("Starting iteration " + str(itn))
            # random.shuffle(TRAIN_DATA)
            # losses = {}
            # batches = minibatch(TRAIN_DATA, size=compounding(8., 32., 1.001))
            # for batch in batches:
            #     texts, annotations = zip(*batch)
            #     nlp.update(texts, annotations, sgd=optimizer, 
            #                losses=losses)
            # print('Losses', losses)
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                    try:
                        nlp.update(
                            [text],  # batch of texts
                            [annotations],  # batch of annotations
                            drop=0.2,  # dropout - make it harder to memorise data
                            sgd=optimizer,  # callable to update weights
                            losses=losses)
                    except Exception as e:
                        pass
            print(losses)
    
    nlp.to_disk("model")
    return nlp

"""

    # Disable all other pipeline components, only train Named Entity Recognition (NER)
    with nlp.disable_pipes(*other_pipes):
        # If the model doesn't exist, initialize the optimizer
        if model is None:
            optimizer = nlp.begin_training()

        # Iterate over training for two iterations
        for itn in range(2):
            print("Starting iteration " + str(itn))

            # Shuffle the training data to introduce randomness
            random.shuffle(TRAIN_DATA)

            # Initialize an empty dictionary to store losses
            losses = {}

            # Iterate over the training data
            for text, annotations in TRAIN_DATA:
                try:
                    # Update the model with a batch of text and annotations
                    nlp.update(
                        [text],         # Batch of texts
                        [annotations],  # Batch of corresponding annotations
                        drop=0.2,        # Dropout rate to prevent overfitting
                        sgd=optimizer,  # Stochastic Gradient Descent optimizer
                        losses=losses   # Store the losses for this iteration
                    )
                except Exception as e:
                    pass  # Handle exceptions gracefully, e.g., if there are annotation format issues

            # Print the losses for this iteration
            print(losses)

    # Save the trained model to disk
    nlp.to_disk("model")

    # Return the trained NLP model
    return nlp
