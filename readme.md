# Resume Parsing with Spacy NER

## Introduction
Resumes come in various formats, making it challenging to extract crucial information. NK.com is a platform that hosts resumes and connects them with hiring managers from Fortune 500 companies. Currently, their process relies heavily on manual labor. When a resume is uploaded, a human reviewer goes through it to extract essential details such as the Name, Designation, and Place of Work.

This manual process is labor-intensive and problematic, especially when dealing with thousands of uploaded resumes and a limited workforce. To address this issue, NK.com has commissioned us to develop a resume parser that can automatically extract key elements from resumes using Machine Learning (ML) and present the results.

---

## Dataset Description

To aid in the development of the resume parser, NK.com has provided us with a dataset sourced from Dataturks. This dataset includes JSON files with labeled information for each resume. The labeled fields include:

- Location
- Designation
- Name
- Years of Experience
- College
- Degree
- Graduation Year
- Companies worked at
- Email address

---

## Objective

To build resume parser model to automatically identify and extract the key elements from resumes, streamlining the hiring process for NK.com.

---

## Execution Instructions
- Please create the directory structure in the following way to execute.
    - '/Resume_Parser'

- Install requirements with "pip install -r requirements.txt"

- Run `engine.py`

---
