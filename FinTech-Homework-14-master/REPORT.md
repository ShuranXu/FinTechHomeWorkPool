# Assignnent 14: LSTM Stock Predictor in Deep Learning 

<img src="Images/bg.jpg" width="800" height="400" /> </br>


## Report Summary

This assignment covers the following tasks:

1. [RNN prediction on Closing Price with FNG values](#1---RNN-Prediction-on-Closing-Price-with-FNG-values)
2. [RNN Prediction on Closing Price with Closing values](#2---RNN-Prediction-on-Closing-Price-with-Closing-values)
3. [Answers on Performance Evaluation Questions](#3---Answers-on-Performance-Evaluation-Questions)

---

## Files

[Task 1 Starter Notebook](Instructions/Starter_Code/lstm_stock_predictor_fng.ipynb) </br>
[Task 2 Starter Notebook](Instructions/Starter_Code/lstm_stock_predictor_closing.ipynb) </br>

---

## Breakdown

---

### 1 - RNN Prediction on Closing Price with FNG values

In this section, a custom LSTM RNN was designed and built. The LSTM RNN model uses a 10 day window of Bitcoin fear and greed index values to predict the 11th day closing price.

The steps invovled during the process are the following: </br>

(1). Read both btc_sentiment.csv and btc_historic.csv as two dataframes and combine them into one using `join()` </br>
(2). Use the `window_data(df, window, feature_col_number, target_col_number)` to generate the X and y values for the model. </br>
(3). Split the data into 70% training and 30% testing </br>
(4). Apply the MinMaxScaler to the X and y values to standardize input data for RNN processing </br>
(5). Reshape the X_train and X_test data for the model using `reshape((X_train.shape[0], X_train.shape[1], 1))` </br>
(6). Build and train a custom LSTM RNN </br>
    
&nbsp;&nbsp;&nbsp;&nbsp;- The RNN model has 3 LSTM layers followed by dropout layers </br>
&nbsp;&nbsp;&nbsp;&nbsp;- The number of neurons in the hidden layers = 9, window size = 3 </br>
&nbsp;&nbsp;&nbsp;&nbsp;- The dropout fraction is 0.2 </br>
&nbsp;&nbsp;&nbsp;&nbsp;- Model Summary: </br>
<img src="Images/rnn_summary.png" width="600" height="400" /> </br>
(7). Evaluate the model using the X_test and y_test data. </br>
(8). Use the X_test data to make predictions </br>
(9). Plot the Real vs predicted values as a line chart: </br>
<img src="Images/model1_perf.png" width="600" height="400" /> </br>

</br>

---

### 2 - RNN Prediction on Closing Price with Closing values

In this section, a custom LSTM RNN was designed and built. The LSTM RNN model uses a 10 day window of Bitcoin closing prices to predict the 11th day closing price.

The steps invovled during the process are the following: </br>

(1). Read both btc_sentiment.csv and btc_historic.csv as two dataframes and combine them into one using `join()` </br>
(2). Use the `window_data(df, window, feature_col_number, target_col_number)` to generate the X and y values for the model. </br>
(3). Split the data into 70% training and 30% testing </br>
(4). Apply the MinMaxScaler to the X and y values to standardize input data for RNN processing </br>
(5). Reshape the X_train and X_test data for the model using `reshape((X_train.shape[0], X_train.shape[1], 1))` </br>
(6). Build and train a custom LSTM RNN </br>
&nbsp;&nbsp;&nbsp;&nbsp;- The RNN model has 3 LSTM layers followed by dropout layers </br>
&nbsp;&nbsp;&nbsp;&nbsp;- The number of neurons in the hidden layers = 9, window size = 3 </br>
&nbsp;&nbsp;&nbsp;&nbsp;- The dropout fraction is 0.2 </br>
&nbsp;&nbsp;&nbsp;&nbsp;- Model Summary: </br>
<img src="Images/rnn_summary.png" width="600" height="400" /> </br>
(7). Evaluate the model using the X_test and y_test data. </br>
(8). Use the X_test data to make predictions </br>
(9). Plot the Real vs predicted values as a line chart: </br>
<img src="Images/model2_perf.png" width="600" height="400" /> </br>

---

### 3 - Answers on Performance Evaluation Questions

This section answers questions listed in README.md </br>

>__Q__: Which model has a lower loss? </br>
>__A__: LSTM model with closing price feature has a lower loss, which is 0.0245, whereas the loss of LSTM model with fng feature is 0.1063. </br>
>__Q__: Which model tracks the actual values better over time? </br>
>__A__: LSTM model with closing price feature performs better than the one with fng value in terms of value tracking. 
This can be seen from the line charts provided for both models. </br>
>__Q__: Which window size works best for the model? </br>
>__A__: window size = 3 and unit size = 9 tends to work best. Experiementation shown that the bigger the window size, the poorer the model performance. 
For instance, if window size = 20 and unit size = 40, the predicted closing prices tend to be consistent (i.e. flat line). 