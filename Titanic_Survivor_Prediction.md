# Final Project - Titanic Survivor Prediction

    Contributors: ROULET Maria Paula & ROUX Dorian  
    Web App Link: https://titanicsurvivorprediction-zpclogepwq-ew.a.run.app

---

## Introduction, Datasets and Model

As part of our final project of Cloud Computing we were asked to realise a web app containing a machine learning algorithm with a graphical interface.  
We decided to look at some online available and open-source datasets. 

### Around the Data

#### Source

While working on finding an interesting dataset, we found a Kaggle competition called _"Titanic - Machine Learning from Disaster"_ with as purpose to predict the survival on the Titanic. This Kaggle competition have a data split into two groups:
- training set
- test set  

The datasets have information about the passenger such as his name, name title, ticket class, gender, age, cabin, port of embarkation and some other that are less relevant.

#### Cleaning

The datasets were not perfect and had some missing values, thus, we had to clean unknow information. To do so, we decided to fill the missing values using the known information for each passenger, which helped us to clean the datasets without affecting it nor creating outliers.

#### Feature Engineering

Once the datasets were cleaned, we had to prepare it to our model and thus construct the features. 

### Model 

We decided to use a Sequential model with Tensorflow and Keras. After different model and appliance for different parameters, we took as features:
- The ticket class of the passenger
- Knowing if the passenger was in a cabin 
- The age of the passenger
- The gender of the passenger
- The port of embarkation of the passenger
- The Name title of the passenger
- Knowing if the passenger was traveling alone or not
- If not how many person were traveling with the passenger.

Among those features some were more relevant concerning the survival rate such as the Name Title (Mr. Master., ect.), the Ticket Class (First, Second, Third) or the Gender (Male, Female) but some other were less important but were still useful to have a better accuracy in our model but also a better relevance in our graphical interface.

With the sequential model, we reached an accuracy of 0.802.

## Web App Cost

### Deployment Cost
### Deployment Use

## Problems

In the creation of the application, we do not face much issues excepted during the deployement where some python libraries were not at the good version.

## Web App Functionment

Let us explain the functionment of our web application. 

When launching the web app, the main page will give mutliples options. First, either do a personalized prediction or a random prediction. Second, either do a first class, a second class or a third class prediction. Chosing one of the last four choices will lead to the result page which we will describe after.

If you choose the personalized prediction, then, you will appear in a page including a form where you have to fill all the information as if you were a passenger who embarks in the titanic. This form is interactive, meaning that taking some options might remove some others (to not create outliers such as an age of 200) to keep a certain coherence. From this page you can fill everything by yourself or select a random filling as well. Then when clicking on the "prediction" button you will be send to the result page.

In the result page, you can have a recall of your information and you will know either you survived from the sinking or not with a certain percentage. This recall is interesting when you took a random selection in the previous state to know what characteristics were defined.

---
