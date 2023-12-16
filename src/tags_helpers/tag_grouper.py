from typing import Iterable
import json
import numpy as np
from fuzzywuzzy import fuzz


class TagGrouper:
    threshold: int
    cache_name: str
    unique_tags: set[str]
    tags_mapping: dict[str, str]

    def __init__(self, threshold: int = 50, tag_cache_name: str = "src/tags_helpers/tag_cache.json"):
        self.threshold = threshold
        self.cache_name = tag_cache_name

        # Load cache
        tags_cache = json.load(open(tag_cache_name, "r"))
        self.unique_tags = set(tags_cache["unique_tags"])
        self.tags_mapping = tags_cache["tags_mapping"]

    def get(self, tag: str):
        tag = tag.lower()

        if len(self.unique_tags) == 0:  # If no tags, add it
            self.unique_tags.add(tag)
            return tag

        if tag in self.unique_tags:  # If tag is already in unique tags, return it
            return tag

        tag_hit = self.tags_mapping.get(tag)
        if tag_hit is not None:  # If tag is in mapping, return it
            return tag_hit

        # If tag is not in mapping, find the closest tag and check if it's difference score is below threshold
        fuzz_scores = {t: fuzz.ratio(tag, t) for t in self.unique_tags}
        closest_tag = max(fuzz_scores, key=fuzz_scores.get)
        max_score = fuzz_scores[closest_tag]
        if max_score <= self.threshold:
            self.unique_tags.add(tag)
            return tag
        else:
            self.tags_mapping[tag] = closest_tag
            return closest_tag

    def save(self):
        json.dump({
            "unique_tags": list(self.unique_tags),
            "tags_mapping": self.tags_mapping
        }, open(self.cache_name, "w"))

    def reset_cache(self):
        self.unique_tags = set()
        self.tags_mapping = {}
        self.save()


if __name__ == '__main__':
    unique_tags = ["cop21", "Cop 21", "gello", "hello", "goodbye", "climate", "climate change", "breaking news", "news"]
    tg = TagGrouper(threshold=50, tag_cache_name="../../src/tags_helpers/tag_cache.json")
    tg.reset_cache()
    for tag in unique_tags:
        print(tg.get(tag))
    print(tg.unique_tags)
    print(tg.tags_mapping)

    score = fuzz.ratio("new", "breaking news")
    print(score)
    print(fuzz.ratio("climate", "climate change"))
    tg.reset_cache()
    tg.save()
