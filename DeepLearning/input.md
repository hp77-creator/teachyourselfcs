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
- Refinements of Beam Search
- Bleu Score
- Attention Model



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
 $$
 arg max \prod_{t=1}^{Ty} P{y^<t> |x, y^<1>, …, y^<t-1>}
 $$

 This is converted into log and the product is converted into summation like 


 $$
 arg max \sum_{t=1}^{Ty} \log_P{y^<t> | x, y^<1>, . . . , y^<t-1>}
 $$


#### Beam search discussion

 Beam width B?
 How to select B:
  large B: you tend to consider lot of possibilities but it will be slower
  small B: worse result but is faster
  
  Unlike exact search algorithms like BFS(breadth first search) or DFS(Depth first search), Beam search is a lot faster but does not guarantees exact arg max P.

### Error Analysis on Beam Search

Example of machine translation from french to English:
  Sentence: *Jane visite l'Afrique en septembre*. 
  Human: Jane visits Africa in September. ($y^(^)$)
  Algorithm: Jane visited Africa last September. (y*)
  
  There is error in sentence translation so we should be able to provide this feedback to the algorithm either in RNN or Beam Search because both of these components combine to find the translation.

  RNN computes P(y | x). In our example there are two possibilities which will provide what part of our architecture is at fault.

  Case 1: P( y* | x ) >= P ( $y^(^)$ | x) 
    Here Beam Search is at fault

  Case 2: P($y^(^)$ | x) >= P(y* | x) 
    Here RNN is responsible for error


### Bleu Score

How to evaluate when there are multiple correct score:

Here Bleu score comes into picture. 

Ex:
  French: Le chat est sur le tapis

  Ref 1: The cat is on the mat.

  Ref 2: There is a cat on the mat.


BLEU: BiLingual Evaluation Understudy.

Intuition: we will look at different machine generated words and will look these words with human interpretation(or reference) and will check them in the references if they occur in the References and give it a precision

  MT output: the the the the the the
  here 'the' appears 7 and 
  Precision: $fract_{7}^{7}$

  This is not such a good measure so we use modified precision where in numerator we see how many times the detected word(here 'the') and in denominator we have the length of the Machine Translation output.


Another way is Bleu score on bigrams(we can also do tri-gram or n-gram):

In this way we check two words at a time, and noting their count in 'clipCount' columns and our modified precision score will be the sum of the clipCount divided by total number of clipCount that we obtained.


This definition is generalized way of finding modified precision.

#### Bleu details:
$$
\p_n = Bleu Score on n-grams only

Combined Bleu score: BP * e^(1/4 \sum_{n=1}^{4} P_n)

BP = Brevy penalty
$$

BP = 1 if MT_output_length > reference_output_length
BP = exp(1 - reference_output_length/MT_output_length) otherwise

for more details about Bleu read the reference [paper](#Research Papers):

Not used in speech recognition. Bleu score is used in image captioning or machine translation type of applications.


### Attention Model Intuition

Alternative to encoder-decoder architecture

Encoder-Decoder architecture works well(bleu score is good) for short sentences because it is difficult for a NN to memorize the sentences.

But with the use of attention model we can change this. In Attention model, what we do is define weights which is assigned to the neighbors of the word which is currently in focus and the currently focus is translated by keeping the assigned weights in mind.

This leads to a better accuracy in the machine translation task






## Research Papers

- [Man is to computer programmer as woman is to homemaker? Debiasing word embeddings](https://arxiv.org/abs/1607.06520)
- [Sequence to sequence learning with neural networks](https://arxiv.org/abs/1409.3215)
- [Learning phrase representation using RNN encoder-decoder for statistical machine translation](https://arxiv.org/abs/1406.1078)
- [Deep Captioning with multimodal recurrent neural networks](https://arxiv.org/abs/1412.6632)
- [Show and Tell: Neural Image caption generator](https://arxiv.org/abs/1411.4555)
- [A method for automatic evaluation of machine translation: Bleu Score](https://www.aclweb.org/anthology/P02-1040.pdf)
- [Neural Machine Translation by jointly learning to align and translate](https://arxiv.org/abs/1409.0473)
- [Show, attend and Tell: Neural Image caption generation with visual attention](https://arxiv.org/abs/1502.03044)
