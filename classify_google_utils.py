import os
import pandas as pd
import asyncio
import nest_asyncio
from google.cloud import language_v2
import time
import numpy as np
from tqdm import tqdm

async def classify(text,  client):
    """Classify the input text into categories."""


    document = language_v2.Document(
        content=text, type_=language_v2.Document.Type.PLAIN_TEXT
    )
    response = await client.classify_text(request={"document": document})
    categories = response.categories
    result = {}
    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    return result

async def classify_videos(text, max_retries=1):
    retries = 0
    while retries < max_retries:
        try:
            result = await asyncio.wait_for(classify(text), timeout=1000)  # Set the timeout value as per your requirement
            return result
        except asyncio.TimeoutError:
            retries += 1
            print(f"TimeoutError occurred. Retrying... ({retries}/{max_retries})")
        except Exception as e:
            retries += 1
            print(f"Exception occurred: {str(e)}. Retrying... ({retries}/{max_retries})")
    return {'error': f"Max retries ({max_retries}) exceeded"}

async def dispatch_requests(text_list):
    nb_done = 0
    
    async def one_call(text: str):
        ''' One async call to ask_chat. '''
        nonlocal nb_done
        res = await classify_videos(text = text)
        nb_done += 1
        if nb_done % 50 == 0: #informative outputs
            print(nb_done)
        else: 
            print('.', end = '')
        return res    
    async_responses = [one_call(x) for x in text_list] #multiple calls
    new_responses = await asyncio.gather(*async_responses)

    return new_responses

def classify_chunk(text_list):

    loop = asyncio.get_event_loop()
    nest_asyncio.apply()
    answers = loop.run_until_complete(
        dispatch_requests(text_list=text_list))

    return(answers)

def classify_all(video_dataframe, credentials_path, chunk_size=599):
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=credentials_path
    language_client = language_v2.LanguageServiceAsyncClient()

    chunks = np.array_split(video_dataframe, len(video_dataframe) // chunk_size)
    dfs = []  # List to store the dataframes
    
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        text_list = [f"{row['title']}\n\n{row['description']}" for _, row in tqdm(chunk.iterrows(), total=len(chunk))] 
        start_time = time.time()
        chunk['classification_categories'] = classify_chunk(text_list=text_list)
        chunk.to_json(f'safety_saves/output_{i}.jsonl', orient='records', lines=True)
        dfs.append(chunk)  # Append the chunk dataframe to the list
        time_spent = time.time() - start_time
        time_to_wait = max(62 - time_spent, 2)
        print(f"Waiting {time_to_wait} seconds")
        time.sleep(time_to_wait)
        print("Done")
        
    # Concatenate the dataframes in the list
    rebuilt_dataframe = pd.concat(dfs, ignore_index=True)
    
    return rebuilt_dataframe