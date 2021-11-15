# Final Project - Titanic Survivor Prediction

    Contributors: ROULET Maria Paula & ROUX Dorian  
    Web App Link: https://titanicsurvivorprediction-zpclogepwq-ew.a.run.app

This final project allows an user using our web interface to predict his survival chances if he was a passenger of the titanic, given some personal parameters.

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

We started by doing an EDA to understand the data we had at our disposal. From the previous analysis, we noticed the datasets were not perfect and had some missing values, thus, we had to clean unknow information. To do so, we decided to fill the missing values using imputation techniques, which helped us to clean the datasets without affecting it nor creating outliers.

#### Feature Engineering

Once the datasets were clean, we had to prepare it to our model and thus construct the features. 

### Model 

After different models and appliances for different parameters, we decided to use a Sequential model with Tensorflow and Keras.
We took as features:
- Passenger Class: The ticket class of the passenger
- Cabin: Knowing if the passenger was in a cabin 
- Age: The age of the passenger
- Gender: The gender of the passenger
- Embarkation Port: The port of embarkation of the passenger
- Title: The Name title of the passenger
- Travel Alone: Knowing if the passenger was traveling alone or not
- Relatives Travelling: If not how many persons were traveling with the passenger.

Among those features some were more relevant concerning the survival rate such as the Title (Mr. Master., ect.), the Passenger Class (First, Second, Third) or the Gender (Male, Female). The remaining were still useful to have a better accuracy in our model. These last parameters contributed also with a better relevance in our graphical interface.

With the sequential model, we reached an accuracy of 0.802.

Using this type of model allows us to have as output a probability of surviving given the entries. From that, we decided to state that whenever the predicted probability is higher then 0.5 the passenger survives.

## Web App Cost

### Deployment Cost
### Deployment Use

## Problems

In the creation of the application, we do not face much issues excepted during the deployement where some python libraries were not at the good version.

## Web App Operation

Let us explain the running of our web application. 

When launching the web app, the main page will give mutliple options for the user to select. First, either do a personalized prediction or a random prediction. Second, either do a first class, a second class or a third class prediction. Chosing one of the last four choices will lead to the result page which we will describe after.

In the case the user choses the personalized prediction, then, he/she will see appear a page with a form for him/her to fill with all the information as if he/she was a passenger who embarks in the titanic. This form is interactive, meaning that taking some options might remove some others (to not create outliers such as an age of 200) to keep a certain coherence for prediction our model gives. From this page he/she can fill everything by her/himself or select a random filling as well. Then when clicking on the "prediction" button he/she will be send to the result page with the prediction result.

In that last page, you can have a recall of your information and you will know either you survived from sinking or not with a certain percentage. This recall is interesting when the user took a random selection in the previous state to know what characteristics were defined.


---
