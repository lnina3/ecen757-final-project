# sample code from https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#entities

import json
from time import time
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions

t0 = time()

authenticator = IAMAuthenticator('{apikey}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    url='www.cnn.com',
    features=Features(entities=EntitiesOptions(sentiment=True,limit=1))).get_result()

tt = time() - t0

print(json.dumps(response, indent=2))
print("Job completed in {} seconds".format(round(tt,3)))
