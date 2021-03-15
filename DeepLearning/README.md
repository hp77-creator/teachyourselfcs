# Deep Learning Specialisation

This is a very good set of courses on deep learning by Andrew ng. 


## Course 1 

## Course 2

## Course 3

## Course 4

## Course 5 - Sequence Models

- RNN(Recurrent Neural Networks)
- GRU(Gated Recurrent Units)
- LSTM(Long Short Term Memory)
- BRNN(Bidirectional Recurrent Neural Networks)
- One hot encoder
- Word Embeddings
- Cosine similarity
- SkipGram
- WordVec
- GloVe word vectors(global vectors for word representation)
- Sentiment Classification(using word embeddings)
- Debiasing(gender or racial that kind of bias, not our ML terminology) Word embeddings
- Sequence Models
- Beam Search
- 



### Sentiment Classification

Problem Statement is basically extracting number of stars from the reviews that they write i.e understanding how positive or negative are the sentiments from the word.

Problem faced during this task is one doesn't have lot of data for this task so word embeddings come to rescue in this situations.

We can use RNN for sentiment Classification. And one should also keep track that one can use "good" in a negative review as well so we need to also define 

It is an example of many-to-one architecture or we can use this approach to keep track of if there is some negative word in the paragraph and mapping/using it to generalise the sentiment of the paragraph. 


### Debiasing word embeddings

Word embeddings can reflect gender, ethnicity, age, sexual orientation, and other biases of the text used to train the model.

#### Addressing bias in word embeddings

1. Identify bias direction
    a. Take difference of gender bias directions
    b. Sum them
2. Neutralize: For every word that is not definitional, project to get rid of bias(Like we need gender for grandmother or grandfather but there need not be gender bias for doctor or babysitter).
3. Equalize pairs.

### Sequence models and attention mechanism

Sequence to sequence models | Basic Models

Examples are Machine Translation, Language recognition

### Beam Search

Why not a greedy search?

It looks for all the possible meaning/related words with current word in focus in word embedding and takes them out

It has something called Beam width which determines the number of words to predict out.
When B=1, it becomes greedy search.

#### Refinements of Beam Search

Length normalization: 
arg max






## Research Papers

- [Man is to computer programmer as woman is to homemaker? Debiasing word embeddings](https://arxiv.org/abs/1607.06520)
- [Sequence to sequence learning with neural networks](https://arxiv.org/abs/1409.3215)
- [Learning phrase representation using RNN encoder-decoder for statistical machine translation](https://arxiv.org/abs/1406.1078)
- [Deep Captioning with multimodal recurrent neural networks](https://arxiv.org/abs/1412.6632)
- [Show and Tell: Neural Image caption generator](https://arxiv.org/abs/1411.4555)
- 
