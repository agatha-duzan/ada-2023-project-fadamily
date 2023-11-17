# Climate change on YouTube: evolution, trends and influences / ada-2023-project-fadamily

## Abstract

Climate change is a hot topic that needs to draw people's attention more than ever. Using the YouNiverse dataset, we observe the influence of the topic in YouTube’s videos. As any social media, YouTube's data reflects the interest of its users and with the analysis of climate change, we are able to examine the emergence of people awareness' on environment. In our analysis, we compare view peaks of climate change related videos and particular events such as a natural disaster or political decision at that moment to make a connection between the two. We also look at the viral videos on climate change and analyse what subject related to the environment people are the most sensitive to.


## Research questions

- Did climate change become a more important topic on YouTube as it became a very important matter in our societies?
    - Evolution of the views & number of videos about climate change (and proportion)
    - Look also at these only in relevant categories (News, politics, education)
    - Category wise: are now all categories affected?
    - Channel wise: are many channels taking over this topic ?
- YouTube as a reflect of society: can we relate spikes in the interest in climate change on YouTube with real word events?
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

The primary objective is to analyze YouTube videos associated with climate change, and the initial step involved filtering the extensive dataset to focus solely on pertinent content.
To achieve this, we curated a meticulous list of 41 keywords that exhibited the closest relevance to climate change. Deliberately, we opted for two-word keywords, aiming to optimize the correlation between a keyword's presence and the video's subject matter. Subsequently, we conducted scans within the dataset, examining whether these selected keywords were present in the video titles, tags, or descriptions. It was essential to ensure a singular count for each keyword, regardless of its multiple occurrences across different sections. We then selected the videos that contained the keywords in their metadata.

Leveraging Spark due to the dataset's magnitude, we executed this filtering process efficiently. Upon completion, we stored the refined dataset containing videos pertinent to climate change locally for further analysis and study.

#### Filtering refinement

During our analysis, we encountered a significant issue related to video selection based on keywords. We noticed that merely selecting videos with specific keywords occasionally led us to include content not directly addressing climate change. For instance, a video might mention a keyword in its title, description, or tags, but discuss an unrelated topic—such as gaming scenarios involving a post-apocalyptic world or discussions about dandruff exacerbated by weather conditions like winter.
We found certain keywords to be more indicative of relevant content. Videos containing the phrase 'climate change' were more likely to genuinely address the topic compared to instances of 'pollution,' which might be tangentially related. Additionally, the category of the video influenced its accuracy; videos categorized under 'Science & Technology' were more likely to be on-topic than those under 'gaming,' 'sport,' or 'music.'
Moreover, we observed that the placement of keywords within the title, tags, or description affected their relevance differently. Notably, descriptions often contain varied subject matter, potentially diverging from the video's main theme.
To address these challenges, we devised a new filtering method specifically aimed at identifying videos focusing primarily on climate change. This involved assigning a weight from 1 to 5 to each keyword. A weight of 1 signifies a low probability of the video covering climate change upon mentioning the keyword, while a weight of 5 indicates high odds of climate change being the discussed topic. 
Furthermore, we attributed weights to titles, tags, and descriptions. We ensured that each keyword was counted only once, regardless of its multiple occurrences. Additionally, we prioritized the location of the keyword (title, tag, or description) by arranging them in descending order of weight. If a keyword appeared in both the title and the description, we only considered it from the title for accuracy assessment.
Finally, we established a category-weight dictionary. A video must attain a higher score than its category's requirement to be retained in the selection process.
By manipulating these parameters and conducting numerous random sampling experiments, we iteratively refined our filter. We are currently undergoing further analysis using p-value assessments to identify the most effective parameters. The numerical values present in the code may evolve as part of our ongoing effort to enhance our filtering methodology.

### Analysis

After acquiring our filtered dataset, our focus shifted towards investigating potential correlations between news or global events and public interest in the climate change topic on YouTube. We based our study on the ratio of uploaded videos specifically addressing climate change from 2010 to 2019.
Our analyses were conducted across various timeframes: daily, weekly, and monthly rates of video uploads. These analyses were instrumental in identifying trends. Notably, we observed substantial volatility in these plots, highlighting distinct periods where the rate of videos addressing climate change surged, sometimes reaching tenfold increases.
To establish connections between these peaks and significant events, we identified the 62 most pivotal climate events between 2010 and 2019, as identified by ChatGPT, ensuring their authenticity. We then assessed to the highest peak its event: the Paris Agreement Adopted at COP21 on the 2015-12-12.

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