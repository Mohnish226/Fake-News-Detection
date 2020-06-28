# MSA Project
![Website](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=UP&url=https%3A%2F%2Fdatascience.app)

### Fake News Detection

### Datasets from:
1. [Fake and real news dataset: Classifying the news](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset/)
2. [Getting Real about Fake News: Text & metadata from fake & biased news sources around the web](https://www.kaggle.com/mrisdal/fake-news)
3. ~~[Fake-News-Dataset: Two fake news datasets covering seven different news domains](https://www.kaggle.com/sumanthvrao/fakenewsdataset)~~
4. [BBC News Summary: Extractive Summarization of BBC News Articles ](https://www.kaggle.com/pariza/bbc-news-summary)
5. [All the news: 143,000 articles from 15 American publications](https://www.kaggle.com/snapcrack/all-the-news)

### Requirements:
| Package | Version |
| ------ | ------ |
| numpy | 1.18.1 |
| pandas | 1.0.3 |
| tqdm | 4.46.0 |
| scikit-learn | 0.22.1 |
| keras | 2.3.1 |
| nltk | 3.4.5 |
| spacy | 2.2.3 |
| h5py | 2.10.0 |


To install requirements:
```sh
cd MSA_Proj
pip install -r requirements.txt
```

To run app locally:
```sh
cd MSA_Proj/app/
python app.py
```

### Machine Learning Approach tried:
 - Analysis [view](https://github.com/Mohnish226/MSA_Proj/blob/master/Analysis.ipynb)
 - Logistic Regression [view](https://github.com/Mohnish226/MSA_Proj/blob/master/Basic%20Machine%20Learning.ipynb)
 - Linear Support Vector Classification [view](https://github.com/Mohnish226/MSA_Proj/blob/master/Basic%20Machine%20Learning.ipynb)
 - XG Boost [view](https://github.com/Mohnish226/MSA_Proj/blob/master/Basic%20Machine%20Learning.ipynb) [Optimized](https://github.com/Mohnish226/MSA_Proj/blob/master/XGBoost.ipynb)
 - LightGBM [view](https://github.com/Mohnish226/MSA_Proj/blob/master/Basic%20Machine%20Learning.ipynb)
 - Sequential [view](https://github.com/Mohnish226/MSA_Proj/blob/master/Sequential.ipynb)
 - RNN + GloVe [view](https://github.com/Mohnish226/MSA_Proj/blob/master/GloVe.ipynb)
 - Final Sequential and RNN+GloVe trial [view](https://github.com/Mohnish226/MSA_Proj/blob/master/final-Sequential.ipynb)

### Website:

###### View Working on : [msa.datascience.app](http://msa.datascience.app)
Note: The server might be slow to respond depending on the load on the system
The model has not been trained on test data (available on website)
For more data use data from [here](https://github.com/Mohnish226/MSA_Proj/tree/master/test_data) they are also not trained on

### Screens

![Website](https://github.com/Mohnish226/MSA_Proj/blob/master/screens/output.gif)


### Limitation:
 - The dataset is mostly based on data from USA
 - News from the years 2004 to 2005 and 2011 to 2018 Due to the dataset
 - Output of `tqdm` progressbar is not visible on githubs notebook viewer it might show some error or `HBox(children=(FloatProgress(value=0.0, max=83.0), HTML(value='')))`