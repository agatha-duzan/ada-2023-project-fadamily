# Climate change on YouTube: evolution, trends and influences / ada-2023-project-fadamily

## Abstract

Climate change is a hot topic that needs to draw people's attention more than ever. Using the YouNiverse dataset, we observe the influence of the topic in YouTube’s videos. The ladder being a social media, its data reflects the interest of its users and with the analysis of climate change, we are able to examine the emergence of people awareness' on environment. In our analysis, we compare view peaks of climate change -related videos and particular events such as a natural disaster or political decision at that moment to make a connection between the two. We also look at the viral videos on climate change et analyse what subject related to the environment people are the most sensitive to.


## Research questions
We would like to answer several research questions from basic trend analysis to more specific:
- Did climate change become a more important topic on YouTube as it became a very important matter in our societies?
    - Evolution of the number of videos about climate change (and proportion)
    - Evolution of the number of views of these videos
    - Also look at these only in relevant categories (News, politics, education)
    - Category wise: are now all categories affected?
    - Channel wise: are many channels taking over this topic ?
- YouTube as a reflect of society: can we relate spikes in the interest in climate change on YouTube with real word events? (Cop 21, climate related natural disaster…)
- How popular are videos/channels about climate change compared to overall videos/channels?
- Did some channels experience growth thanks to videos about climate change?
- What is a popular video about climate change:
    - Should it follow (or precede) some event?
    - Are popular videos about climate change from a channel that is already popular (and not about climate change)?
    - Sentiment analysis: do pessimistic videos get more views than optimistic/neutral videos? What about likes/dislikes? 
- Activism: How many videos on climate change are also political videos, does that number increase at every election period? Has ecology become a political topic?
- Evolution in audience responses (particularly in the like/dislike ratio) as the subject matter transitioned from niche to more widely discussed


## Methods


### Dataset


#### Storage
Since the dataset is very large (97GB), we extracted it on a drive and performed a first filtering using pyspark.
The resulting, more reasonable sized, filtered dataset can be found on this google drive : https://drive.google.com/drive/folders/1RSguLUcUIk9Rt2Bf6IchXuTbhEWtkC6u . There are also other datasets with useful features we extracted from the original dataset (video and view counts). You can download it all locally to run the notebooks without having to deal with the original large dataset.

#### Pre-processing


### Analysis



## Proposed Timeline & Task Delivery Dates
17/11/2023 - Deliver milestone 2

01/12/2023 - Create visualizations, finish analysis

08/12/2023 - Focus on the data story 

15/12/2023 - Create the website and upload the data story

22/12/2023 - Deliver milestone 3

## Team Organisation
Sébastien: data story and influence graph

Agatha: data story and time series analysis

Maxime: data story and advanced filtering

Paul: data story and sentiment analysis

Nastasia: data story and event correlation