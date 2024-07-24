# Question Answering on MEDMCQA Dataset

This repository provides a streamlined approach to answer multiple-choice medical questions using the MEDMCQA dataset. We employ a simple Retrieval-Augmented Generation (RAG) method.


## The order of the notebooks:

1. **`mlm_finetune_bert.ipynb`**:
    - Fine-tunes the BioClinical BERT model on the MEDMCQA dataset.
    - Pushes the resulting model to your Hugging Face repository.

2. **`preprocess_medmcqa.ipynb`**:
    - Creates the database which is going to be used for retrieving similar questions. The CLS embeddings of the questions are added to this database to use them for finding the most relevant questions to the user's query.
    - Pushes the processed dataset to your Hugging Face repository.

3. **`t5_finetune.ipynb`**:
    - Fine-tunes the T5 model on a subset of the MEDMCQA dataset to align T5 with the task of multiple-choice question answering.
    - Pushes the resulting model to your Hugging Face repository.

4. **`retrieval_medmcqa.ipynb`**:
    - Demonstrates the complete system in action.
    - Evaluates the performance of the entire pipeline.