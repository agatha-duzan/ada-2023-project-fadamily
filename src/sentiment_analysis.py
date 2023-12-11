# Use a pipeline as a high-level helper
from typing import Literal
from time import perf_counter

import pandas as pd
from tqdm import tqdm
from transformers import pipeline


class SentimentAnalysis:

    label_to_sentiment = {
        'LABEL_0': 'negative',
        'LABEL_1': 'neutral',
        'LABEL_2': 'positive'
    }

    sentiment_to_label = {v: k for k, v in label_to_sentiment.items()}

    sentiment_names = ['positive', 'neutral', 'negative']

    def __init__(self):
        self.pipe = pipeline(
            task="text-classification",
            model="cardiffnlp/twitter-roberta-base-sentiment"
        )

    def get_sentiment(self, text: str) -> Literal['positive', 'negative', 'neutral']:
        return self.pipe(text)[0]['label']

    def get_sentiment_batch(self, texts: list[str]) -> list[Literal['positive', 'negative', 'neutral']]:
        return [r['label'] for r in self.pipe(texts)]

    def get_sentiment_and_score(self, text: str) -> tuple[str, float]:
        res = self.pipe(text, top_k=3)
        print(res)
        return self.pipe(text)[0]['label'], self.pipe(text)[0]['score']

    def get_sentiment_and_score_batch(self, texts: list[str]) -> list[tuple[str, float]]:
        return [(r['label'], r['score']) for r in self.pipe(texts)]

    def get_scores(self, text: str) -> list[float]:
        res = self.pipe(text, top_k=3)
        res = {r['label']: r['score'] for r in res}
        return [res[self.sentiment_to_label[s]] for s in self.sentiment_names]

    def get_scores_batch(self, texts: list[str]) -> list[dict[str, float]]:
        res = self.pipe(texts, top_k=3)
        res = [{r['label']: r['score'] for r in rs} for rs in res]
        return res


if __name__ == '__main__':
    sa = SentimentAnalysis()
    # text = """This week the MelVee Sabbath School Panelists of Elder Melusi Ndhlalambi (anchor), Shaun Ryan and Nixon Kadiramwando discuss the second lesson of the new series on Rebellion and Redemption.\n\nThe..."""
    # texts = [text] * 100

    text = "Global warming is the bg"
    for i in tqdm(range(1000)):
        res = sa.get_scores(text)
    print(res)
