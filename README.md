# Data-Science

The data was gathered from the good reads website located here: https://www.goodreads.com/list/show/1.Best_Books_Ever

# Natural Language Processing (NLP)

- https://spacy.io/

The central data structures in spaCy are the Doc and the Vocab. The Doc object owns the sequence of tokens and all their annotations. The Vocab object owns a set of look-up tables that make common information available across documents. By centralizing strings, word vectors and lexical attributes, we avoid storing multiple copies of this data. This saves memory, and ensures there’s a single source of truth.

Text annotations are also designed to allow a single source of truth: the Doc object owns the data, and Span and Token are views that point into it. The Doc object is constructed by the Tokenizer, and then modified in place by the components of the pipeline. The Language object coordinates these components. It takes raw text and sends it through the pipeline, returning an annotated document. It also orchestrates training and serialization.
