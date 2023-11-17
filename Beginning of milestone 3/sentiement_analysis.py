# Use a pipeline as a high-level helper
from typing import Literal
from time import perf_counter
from transformers import pipeline


class SentimentAnalysis:
    def __init__(self):
        self.pipe = pipeline(
            task="text-classification",
            model="lxyuan/distilbert-base-multilingual-cased-sentiments-student"
        )

    def get_sentiment(self, text: str) -> Literal['positive', 'negative', 'neutral']:
        return self.pipe(text)[0]['label']

    def get_sentiment_batch(self, texts: list[str]) -> list[Literal['positive', 'negative', 'neutral']]:
        return [r['label'] for r in self.pipe(texts)]

    def get_sentiment_and_score(self, text: str) -> tuple[str, float]:
        return self.pipe(text)[0]['label'], self.pipe(text)[0]['score']

    def get_sentiment_and_score_batch(self, texts: list[str]) -> list[tuple[str, float]]:
        return [(r['label'], r['score']) for r in self.pipe(texts)]


if __name__ == '__main__':
    sa = SentimentAnalysis()
    text = """This week the MelVee Sabbath School Panelists of Elder Melusi Ndhlalambi (anchor), Shaun Ryan and Nixon Kadiramwando discuss the second lesson of the new series on Rebellion and Redemption.\n\nThe..."""
    texts = [text] * 100

    t0 = perf_counter()
    print(sa.get_sentiment(text))
    t1 = perf_counter()
    print(sa.get_sentiment_batch(texts))
    t2 = perf_counter()

    print(f"Single compute time: {t1 - t0}")
    print(f"Batch compute time: {t2 - t1}")
    print(f"Batch per iter compute time: {(t2 - t1) / len(texts)}")
