# Project 3: Natural Language Processing

---

# Folder structure
- /Data contains scraped as well as processed data
- /Notebooks contains jupyter notebooks, as well as some other code/pictures used in the notebooks.

---

# Executive  Summary

We would like to identify what it is that makes a sentence or text interesting, and to make a computer do it for us instead of manually classifying text. However, it is difficult to get labelled data that states whether something is interesting or not, so we have turned to scraping Reddit. For this project, we scraped r/shittysuperpowers and r/godtiersuperpowers.

---

*For people who are not familiar with these 2 sub-forums of Reddit (referred to as 'subreddits'), here is a quick explanation. Reddit is essentially an online messaging board where people can submit posts and other users can view/comment on these posts. These 2 subreddits in particular both have people proposing an idea for a super power.

---

These subreddits were chosen because they have very similar content but with one key difference: posts in r/godtiersuperpowers need to be either sufficiently funny or creative per the subreddit rules. If a title is funny or creative we can say that it is more interesting. On the other hand, posts in r/shittysuperpowers just have to be not-useful superpowers so they aren't as interesting.

The data was scraped using Reddit's API, then some cleaning and data exploration was performed. It was found that posts in r/godtiersuperpowers tend to use longer sentences as well as emojis/non-standard characters, e.g. something like "ゴゴゴゴゴゴゴ". Some feature engineered columns were added and the text data standardized into lowercase English characters.

Throughout the analysis, other interested parties (stakeholders) such as writers or comedians were also considered.

---

Next, I used various NLP methods along with classification models in order to try and predict which subreddit a post was from. These include:
- Stemming/lemmatization to reduce words to their base form
- Count and TFIDF vectorizers to convert words into numeric data
- Naive Bayes, Logistic, and KNN classifiers to predict subreddit category from the numeric data

I found that the best combination was stemming, TFIDF vectorizing, then using Naive Bayes. This resulted in a 67% accuracy rate, which is better than getting a human (me) to categorize (64% accuracy).

From this model, I extracted out the most important words that the model used when classifying. It turns out that r/godtiersuperpowers has a lot of unique words which are not present in the other subreddit. From this, we can conclude that using rare or specific words can contribute to the interesting-ness of a sentence. Comedians and writers should also take note of this point in order to attract audiences.

---

We can conclude that good ways to increase the interesting-ness of text are to adhere to these 3 points:
- Be more detailed when describing something. Use more words, clarify points that may be ambigious.
- Use less common words, for example ("he ate the food" vs "he devoured the food")
- Use emojis or non-standard characters. The data shows it works! ¯\\_(ツ)_/¯.

Also, the model is somewhat successful at determining how interesting a piece of text is (at least with regards to Reddit post titles). However, as this model was trained in a very specific context, it may not necessarily generalize to other areas.

---


# Problem Statement:
We would like to develop a machine learning algorithm that can tell whether a sentence is interesting or not. However, it's troublesome to find data which is labelled as 'interesting' and 'not interesting'. Reddit however is a good place to scrape data, so we scraped posts from 2 similar subreddits.

After some discussion, our group has chosen r/shittysuperpowers and r/godtiersuperpowers as two distinct categories.

### Why these subreddits? What will it tell us about interesting sentences?

First, let's see what the differences between the subreddits are. The 2 subreddits have somewhat similar formats, in which a user proposes a novel type of super power. The differences can be seen from their guidelines/rules

r/shittysuperpowers
- "Something sort of useful, but **not really useful**"
- "No Curses: If you wouldn't want that super power, or your life would be worse with that power, it's probably a curse."

r/godtiersuperpowers
- "Things that aren't actually overpowered, but are **funny** so we pretend they are [...], let's keep that here"
- "Additionally, **creative powers**, like finding a way the above not-very-good power could actually be god tier, are at the heart of the sub"

Based on these rules, we can see that posts in r/godtiersuperpowers need to be more interesting, since the rule states that it must be more creative, or funny (which also counts as being interesting). Posts in shittysuperpowers don't have to be interesting, it just has to be not-really-useful.

#### The main benefits of developing a model that can differentiate between these 2 subreddits are:
- We can determine how interesting a post title is
- We can get a computer to test if something is interesting instead of asking another person (convenient for comedians, for example).

The scope of this is limited to reddit post titles but there may be some good information/findings from it.

### Types of Models
The data will first be cleaned and investigated. After this, there will be 3 stages to the modelling

1) Words converted into their base form using either Porter stemming, or lemmatizing

2) Words converted into a matrix using either count vectorizing, or TFIDF

3) Classification models such as logistic regression, KNN, or Naive Bayes are tested.

The best one is decided using the metrics below

### Determining Success
To determine how successful each model is, we would like to compare it to several metrics:
- Accuracy (we will be scraping approximately equal numbers of posts so the baseline is ~50%)
    - Accuracy is chosen because neither category is more 'important' and there are equal class sizes
    - Accuracy vs human (I will manually try to sort through some posts to see how accurate I am, and hopefully the computer should be able to do better)
- AUC ROC is another useful metric as it tells us how well the model can distinguish the 2 subreddits.
- I didn't use sensitivity or specificity since I didn't consider either subreddit to be more important. We want to know what is an interesting sentence, but also what is *not* an interesting sentence.

To evaluate success I will set a goal of being more accurate than a human (me). If the model can be even more accurate than that, of course it will be nice.

### Other Stakeholders
These 2 subreddits are about super powers. This is probably not that useful to everyday life, but there are a few parties who may be interested.
- Writers/TV or Film producers: per the rules, super powers in r/godtiersuperpowers should be considered funny or unexpectedly useful, both of which are good for putting in a book/film. Also these parties might want to know what people consider interesting in general.
- Social scientists investigating relationships between related communities: godtiersuperpowers seems to be an alternate version of shittysuperpowers but is there actually a difference between them?
- Comedians: They might seek inspiration about what is considered funny.
- People who want to make popular Reddit posts

---


# Conclusions

### Best model
After cleaning the data, and testing a bunch of different models, we found that Naive Bayes with a TFIDF vectorizer was the best model for predicting if a post was interesting (as we are considering r/godtiersuperpowers posts to be more interesting than r/shittysuperpowers)

### How successful was it?
The model was more successful than a human when tested on all-time top posts (68% for model, 64% for human). The stated goal was achieved. However, there is still room for improvement since about 30% of the time, the model predicts wrongly. Part of this is because the 2 subreddits are very similar so the random error causes a lot of problems.

In addition, the model doesn't work as well on 'hot' posts instead of top posts, this is probably because the top posts have some interesting quality to them that made them top. However, the model still does better than guessing at a ~60% accuracy.

### Findings
Some factors that make a title more interesting, and more likely to be in r/godtiersuperpowers
- Longer title
- Rarer words
- More unique characters (e.g. emojis)

To summarize, should a writer wish to engage more with their audience, they would be well-advised to use a broader spectrum of vocabulary, provide more extensive descriptions, and👏use👏more👏emojis, like in this sentence.

A computer can also determine whether a reddit post is considered 'interesting' or not by looking for words that occur less, and how long the post title is. Depending on what exactly you consider to be 'interesting' vs 'not interesting' this may come with a lot of random error so it depends on the categories that you use.

### Info For Stakeholders
- For writers of books/films, try to avoid using superpowers that are of the form 'If you do X, Y will happen instantly'. Everyone's super-power idea involves something like that so it isn't unique at all.
- For comedians try to use rare words (emojis too) as that might be funnier
- For social scientists studying differences between 2 communities with very similar backgrounds: there seems to be some difference as both a human and a computer were able to classify posts better than random chance, however there are still a lot of similarities (in this case) because neither humans or computers could get a very high accuracy.


### Future Steps
By collecting more data, a more accurate prediction can be made.

Also, there are other subreddits which are good for determining how interesting text is. For example r/pointlessstories vs r/writingprompts has stories which are interesting vs uninteresting. These subreddits may also have a clearer distinction between the two of them as well as more text to collect.

Finally, using more advanced models (e.g. neural nets) it might be be possible to extract more nuance from the sentences. Right now the model just uses a bag-of-words which doesn't take into account the relationships between the words in a sentence.

---

# Data Dictionary

### Top posts:

project_3/data/cleaned/top_posts_both.csv

|Column|Mean|Standard Deviation|Other Info
|---|---|---|---|
|title|-|-|The title of the Reddit post. Non-letter characters are removed and turned into spaces, except apostrophes which were just removed. All text is lowercase. Is used for modelling|
|id|-|-|The unique ID of the reddit post used to identify duplicates. Not used for modelling.
|timestamp|1,573,905,725|14,633,038|Unix timestamp of post date. See 'days ago' column below for more context. Not used for modelling.|
|is_sub1|0.487|0.5|1 for shittysuperpowers, 0 for godtiersuperpowers. The target variable|
|days_ago|313.7|169.4|How many days ago the post was created, as of Unix time 1601013341. Not used for modelling. Shittysuperpowers has posts that go back significantly longer than godtiersuperpowers but the majority are within about 2-3 years|
|has_weird_chars|0.022|0.146|Whether the post title had non-standard characters before cleaning. Is used for modelling. The characters are defined as anything not a letter, digit, space, or these punctuations: ,.!?"'%“”’)(\/: These are a lot more common in godtiersuperpowers|
|sentence_len|14.86|8.24|Number of words in the sentence. For shittysuperpowers the mean is 13.99 and for godtiersuperpowers the mean is 15.68. Is used for modelling as there was a statistically significant difference. Some posts have very long titles (50+ words) and the shortest just one (e.g. "This") but most are within 8-20|

---

### Hot posts:

project_3/data/cleaned/hot_posts_both.csv

|Column|Mean|Standard Deviation|Other Info
|---|---|---|---|
|title|-|-|The title of the Reddit post. Non-letter characters are removed and turned into spaces, except apostrophes which were just removed. All text is lowercase. Is used for modelling|
|id|-|-|The unique ID of the reddit post used to identify duplicates. Not used for modelling.
|timestamp|1,600,403,302|747,264|Unix timestamp of post date. Not used for modelling.|
|is_sub1|0.477|0.5|1 for shittysuperpowers, 0 for godtiersuperpowers. The target variable|
|has_weird_chars|0.018|0.134|Whether the post title had non-standard characters before cleaning. Is used for modelling. The characters are defined as anything not a letter, digit, space, or these punctuations: ,.!?"'%“”’)(\/:|
|sentence_len|14.03|8.33|Number of words in the sentence. Is used for modelling.|

---

# Data Sources
Reddit:

reddit.com/r/shittysuperpowers (sub1)

reddit.com/r/godtiersuperpowers (sub2)

Word cloud generator:

https://www.wordclouds.com/

---

# Other notes
The file project_3/Notebooks/mytransformer.py contains code that will preprocess the text column by removing non-letter characters and adding 2 extra columns denoting the number of non-standard characters as well as the number of words in the title. Just instantiate the object and use the transform method on a Pandas DF which has a "title" column.

You can use this to process newly scraped data easily.