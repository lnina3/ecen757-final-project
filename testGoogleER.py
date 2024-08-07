# sample code based on https://cloud.google.com/natural-language/docs/reference/libraries#use

# Imports the Google Cloud client library
from google.cloud import language_v1
from time import time
import argparse

# No argument checking implemented - make sure passed argument is valid file path
parser = argparse.ArgumentParser(description='Call Google Cloud Natural Language API methods on an input file')
parser.add_argument('filename', help='name of file to be processed')

args = parser.parse_args()

file = args.filename

t0 = time()

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
f = open(file, "r")
text_list = f.readlines()
text = ""
for line in text_list:
    text += line
#print(text)
document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the entities in the text
entities = client.analyze_entities(
    request={"document": document}
).entities

tt = time() - t0

print(f"Text: {text}")
print(f"Entities: {entities}")
print("Job completed in {} seconds".format(round(tt,3)))
