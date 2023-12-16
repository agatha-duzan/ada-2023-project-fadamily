from typing import Iterable

import numpy as np
from fuzzywuzzy import fuzz


class TagGrouper:
    tags: set[str]
    threshold: int

    def __init__(self, threshold: int = 50):
        self.tags = set()
        self.threshold = threshold

    def get(self, tag: str):
        tag = tag.lower()

        if len(self.tags) == 0:
            self.tags.add(tag)
            return tag

        if tag.lower() in self.tags:
            return tag

        fuzz_scores = {t: fuzz.ratio(tag, t) for t in self.tags}
        closest_tag = max(fuzz_scores, key=fuzz_scores.get)
        max_score = fuzz_scores[closest_tag]
        if max_score <= self.threshold:
            self.tags.add(tag)
            return tag
        else:
            return closest_tag


if __name__ == '__main__':
    tags = ["cop21", "Cop 21", "gello", "hello", "goodbye"]
    tg = TagGrouper()
    for tag in tags:
        print(tg.get(tag))

    print(tg.tags)
