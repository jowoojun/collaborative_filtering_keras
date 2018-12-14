# collaborative_filtering_keras

Collaborative filtering (CF) recommender approaches are extensively investigated in research community and widely used in industry. They are based on the simple intuition that ∗Xin-Yu Dai is the corresponding author. This work was supported by the 863 program(2015AA015406) and the NSFC (61472183,61672277). 
if users rate items similarly in the past, they are likely to rate other items similarly in the future [Sarwar et al., 2001; Linden et al., 2003]. As the most popular approach among various collaborative filtering techniques, matrix factorization (MF) which learns a latent space to represent a user or an item becomes a standard model for recommendation due to its scalability, simplicity, and flexibility [Billsus and Pazzani, 1998;
Koren et al., 2009]. In the latent space, the recommender system predicts a personalized ranking over a set of items for each individual user with the similarities among the users and items.

We propose a new neural matrix factorizationmodel for top-N recommendation. We firstly construct a user-item matrix with both explicit ratings and nonpreference implicit feedback, which is different from other related methods using either only explicit ratings or only implicit ratings. With this full matrix (explicit ratings and zero of implicit feedback) as input, a neural network architecture is proposed to learn a common latent low dimensional space to represent the users and items. This architecture is inspired by the deep structured semantic models which have been proved to be useful for web search [Huang et al., 2013], where it can map the query and document in a latent space through multiple layers of non-linear projections. In addition, we design a new loss function based on cross entropy, which includes the considerations of both explicit ratings and implicit feedback.

From https://www.ijcai.org/proceedings/2017/0447.pdf

How to use
==============================
1. Download python package
  ```
  pip install -r requirements.txt
  ```
2. Download dataset & models

  https://drive.google.com/open?id=1qhSfwugNhDiesYsB62GKGGsUC-B-TYf3
  
  https://drive.google.com/open?id=1KSwUnZ3jgtPeu9IdKH3rqR_cFLgNfxYL
  
3. move dataset & models to its directory
  
  ```
  tar xvzf input.tar.gz
  tar xvzf models.tar.gz
  ```
  
4. Execute jupyter
  ```
  jupyter notebook
  ```
  
5. run
  
  
Reference
===========================
 - https://github.com/bradleypallen/keras-movielens-cf
 - https://www.ijcai.org/proceedings/2017/0447.pdf
 - https://arxiv.org/pdf/1606.07659.pdf
 - https://static.googleusercontent.com/media/research.google.com/ko//pubs/archive/45530.pdf
 - https://beta.vu.nl/nl/Images/werkstuk-postmus_tcm235-877824.pdf
