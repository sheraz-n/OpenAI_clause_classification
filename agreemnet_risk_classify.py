# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12   19:12:37 2023

@author: SNaseer
"""

import openai
import cv2
import pytesseract

# Load the image
img = cv2.imread("imageAgreemnet.png")

# OCR the image
text = pytesseract.image_to_string(img)

# identify the clauses
clauses = text.split("\n\n")
list1=[]
for i in range(len(clauses)):
    if(len(clauses[i])>100):
        list1.append(clauses[i])
        
for i in range(len(list1)):
    print(list1[i])
    print()
    print()
    
# Send to open Ai Instruct GPT for classification
import openai
import os

def gpt3(stext):
    #openai.api_key='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'
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response=openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
        max_tokens=1000,
        top_p=1,    
        frequency_penalty=0,
        presence_penalty=0
        )
    
    content=response.choices[0].text.split('.')
    #print(content)
    return response.choices[0].text

print("Output from gpt3 ------------")
print()
print()
Finaltext=['is this agreement risky? Just provide me answer in Yes or NO Agreement :']
Finaltext.append(list1[0])

text2=' '.join(Finaltext)
print(gpt3(text2))

Check_Recommendation='What is the risk in the above agreement?'
print(gpt3(Check_Recommendation))





