# Data-Science

The data was gathered from the good reads website located here: https://www.goodreads.com/list/show/1.Best_Books_Ever

## Natural Language Processing (NLP)

The NLP library used for this project is located here: https://spacy.io/

The central data structures in spaCy are the Doc and the Vocab. The Doc object owns the sequence of tokens and all their annotations. The Vocab object owns a set of look-up tables that make common information available across documents. By centralizing strings, word vectors and lexical attributes, we avoid storing multiple copies of this data. This saves memory, and ensures there’s a single source of truth.

Text annotations are also designed to allow a single source of truth: the Doc object owns the data, and Span and Token are views that point into it. The Doc object is constructed by the Tokenizer, and then modified in place by the components of the pipeline. The Language object coordinates these components. It takes raw text and sends it through the pipeline, returning an annotated document. It also orchestrates training and serialization.

## Goal

Create a NLP model to analyze book descriptions and recommend the user books based on their search.


# Product Canvas

Proposal

- What problem does your app solve?

The search function on Goodreads is terrible. We want to make it better.

- Be as specific as possible; how does your app solve the problem?

	We’re going to use natural language processing to allow users to type a review of a book they’d like to read, then return the most similar results.

- What is the mission statement?
	Make it easier to find better reads
Features

- What features are required for your minimum viable product?
	- Database of top 10,000 (30,000; 50,000) books on Goodreads
	- Robust management of stored data across relevant tables (UPC, product reviews, etc.)
	- Natural language processing/sentiment analysis/LDA on gathered reviews
	- Front-end/back-end web features 

- What features may you wish to put in a future release?
	- Filtering by genre, release date, country of origin, language, popularity, highest rating, number of ratings, length.
	- Larger database
	-

- What do the top 3 similar apps do for their users?
	- Goodreads has a (poor) search functionality
	- Amazon has recommendations based on recent purchase history
	- Audible also has recommendations

Frameworks - Libraries

- What 3rd party frameworks/libraries are you considering using?
	- Express, Node, React, pandas, numpy, scikit-learn, spacy, Keras, Goodreads API (possibly), BeautifulSoup, Google Books API (possibly) , OpenLibrary API
- Do APIs require you to contact its maintainer to gain access?
- Are you required to pay to use the API?
	- No
- Have you considered using Apple Frameworks? (MapKit, Healthkit, ARKit?)
For Data Scientists


- Describe the Established data source with at least rough data able to be provided on day 1. 
- Use Goodreads/Google Books API along with scraped data
	
- You can gather information about the data set you’ll be working with from the project description. Be sure to collaborate with your PM, and your Backend Architect to chat about the resources you have.
- Write a description for what the DS problem is (what uncertainty/prediction are we trying to do here? Sentiment analysis? Why is this a useful solution to a problem?)
	- We are going
- A target (e.g. JSON format or such) for output that DS students can deliver to web/other students for them to ingest and use in the app

Target Audience

- Who is your target audience? Be specific.
	Readers who are looking for book recs but who don’t have enough time to look through all the books out there.
- What feedback have you gotten from potential users?
“Seems pretty dope” -anonymous user

- Have you validated the problem and your solution with your target audience? How?

Users have run into the problem we described and they are excited with our solution.

Research

- Research thoroughly before writing a single line of code. Solidify the features of your app conceptually before implementation. Spend the weekend researching so you can hit the ground running on Monday.
Prototype Key Feature(s)

- This is the “bread and butter” of the app, this is what makes your app yours. Calculate how long it takes to implement these features and triple the time estimated. That way you’ll have plenty of time to finish. It is preferred to drop features and spend more time working on your MVP features if needed.
MVP: 
User provides a short description of a book the user would like to read, then the site provides a list of the top ten most similar books based on NLP sentiment analysis.

