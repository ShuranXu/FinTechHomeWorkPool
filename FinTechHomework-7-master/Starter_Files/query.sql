-- How can you isolate (or group) the transactions of each cardholder?
Since each value in 'card' column corresponds to one unique cardholder, we can perform a select statement that is 
grouped by card. 

--Consider the time period 7:00 a.m. to 9:00 a.m. 
--What are the top 100 highest transactions during this time period?

SELECT * 
FROM transaction 
WHERE EXTRACT(HOUR FROM date) > 7 AND EXTRACT(HOUR FROM date) < 9
ORDER BY amount DESC
LIMIT 100;

-- Do you see any fraudulent or anomalous transactions?

There are  some evidence that prone fradulent transactions exist:

Reason 1: 

Some transaction amount using one credit card is less than $10, but later in future the transaction amount using the 
same card is close or above $1000.

e.g.

For card_id 5570600642865857 and  merchant_id 4:
2018-02-14 18:59:49: 8.45
2018-03-05 08:26:08 1617.0000000000002


Some transactions have the transaction amount close or exceed $1000 while in the last payment the amount
consumed using the same credit are all less than $10 :

For card_id 5570600642865857 and  merchant_id 4:
2018-02-14 18:59:49: 8.45
2018-03-05 08:26:08 1617.0000000000002

For card_id 5570600642865857 and metchant_id 144:
2018-07-04 19:25:28 11.42
2018-01-22 08:07:03 1131

Reason 2:

One credit card is used by multiple merchants, for example the credit card with id 5570600642865857 is used by many merchants: 
Mccarty-Thomas, Fisher-Bolton and Walker, Deleon and Wolf.


--Some fraudsters hack a credit card by making several small payments (generally less than $2.00), 
--which are typically ignored by cardholders. Count the transactions that are less than $2.00 per cardholder. 
--Is there any evidence to suggest that a credit card has been hacked? Explain your rationale.

SELECT id_merchant, COUNT(amount)
FROM transaction
WHERE amount < 2
GROUP BY id_merchant;


