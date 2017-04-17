# Document-Classifier-using-Python

# Problem Statement : 
Customers will provide a bunch of documents to us and we will always have to sort the documents and figure out if they have provided everything they need to provide, is it legible, , password protected, bad scan, rotated doc, partial document etc. So we should be able to analyse the documents uploaded by the user and classify it. Customers provide us a variety of documents e.g Identity Related like SSN, Drivers Licence, Passport; Income Related like W2, 1099 DIV/MISC; Tuition Related like 1098T, University Transaction Statements

# Things to consider:
  Files may be password protected / be partial / not be legible etc
  They can be multiple formats e.g pdf, picture formats
  Output of analysis should be persisted and contain
    Predicted Category (enum for Doc Categories)
    Bank Interest
    W2
  Validation Failures (json field)
  Corrupted File
  Password Protection
  Ability to Re-Trigger Analyzer for previously processed file or skip
  Be in a position to provide a Report that will identify 
  #of Files per customer
  #of Files per category
  #of Files that have validation errors per customer



# Installation (with pip): 
pip install tika


# Running the code: 
python app.py

# Solution Specification Document : 
[Solution Spec](https://docs.google.com/document/d/1REU5DE7MIecbjsOeEqsufoooQIOBIenZxYSAJSykdsc/edit?usp=sharing)

