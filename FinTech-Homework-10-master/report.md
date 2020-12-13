# Data Modeling Report in Analysis of CAD-JPY Exchange Rate

![bg_image](./bg_image.jpg)



## Report Summary

This report focuses on the forecasting of CAD-JPY exchange rate. Specifically, time series analysis of the historical exchange rate data and time series forecasting are provided in this report. Additionally, linear regression technique is also applied to predict CAD/JPY returns.



## Report Breakdown

* ### Section 1: Time Series Analysis

        The following steps are taken to analysis the historical exchange rate data:

        1. Decomposition using a Hodrick-Prescott filter: 

            The filter identified that trend is generally stationary.

        2. Forecasting returns using an ARMA model with AR parameter = 2 and MA parameter = 1:

            Based on the summary report, I think the model is not a good fit because the P-value for both const coefficient and ar.L2.Price coefficient are above 0.05, and this means that these P-values are statistically insignificant to reject the null-hypothesis, meaning that these two coefficients have no relationship with the evaulation of the prediction results.

            In addition, both AIC and BIC values are really high, which indicates that it is more likely that the model is overfitting.
        
        3. Forecasting the exchange rate price using an ARIMA model with AR = 5, differenceing = 1 and MA = 1:

            Based on the summary report, I think the model outperforms the above ARMA model since both AIC and BIC are lower than those from the ARMA model. And most of P-values are statistically significant to reject the null-hypothesis.

            Additionally, from the 5-day future price forecasting step, the Japanese Yen will continue weakening in the near term.

        4. Forecasting volatility with GARCH:

            Based on the forecasting model, the forecast for CAD/JPY volatility is expected to rise over the next 5 days.

* ### Section 2: Regression Analysis

        This section builds a SKLearn linear regression model to predict CAD/JPY exchange rate returns with lagged CAD/JPY exchange rate returns.

        From the actual result vs predicted result comparison from the top 20 values, we can get the sense that the model is not quite accurate, when the prediction is taken place using the test data.

        The In-Sample Performance outweights the Out-of-Sample Performance according the the RMSE metric:

        * In-Sample Root Mean Squared Error (RMSE): 0.841994632894117
        * Out-of-Sample Root Mean Squared Error (RMSE): 0.6445805658569028

        In summary, the model can be further improved partially by more training data. 