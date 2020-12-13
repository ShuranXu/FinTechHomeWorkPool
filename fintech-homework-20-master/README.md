# FinTech Assignment 20


## AssociateProfitSplitter on local ether test net

AssociateProfitSplitter contract accepts ether into the contract, and divide it evenly among associate-level employees. This will allow the human resources department to pay employees quickly and efficiently.

Addresses `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`, `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`  and `0xdcBb8E08e93fD1442039eD65C381666D495d75Be` are used to register the AssociateProfitSplitter contract:

![task1_reg](./Images/task1_deposit_pre.png)

The original balances for these addresses prior to the transaction are shown as follows:

![task1_old_balance](./Images/task1_old_balance.png)

We sent `10 ether` to the contract and deposit it to these three addresses:

![task1_deposit_mid](./Images/task1_deposit_mid.png)

Upon the transaction, each account will have `3 ether` evenly:

![task1_new_balance](./Images/task1_new_balance.png)

The transaction is verified by the `balance` field:

![task1_transact_balance](./Images/task1_transact_balance.png)


---


## TieredProfitSplitter on local ether test net

TieredProfitSplitter contract is used to distribute different percentages of incoming ether to employees at different tiers/levels. For example, the CEO gets paid 60%, CTO 25%, and Bob gets 15%. This contract ensures 
each employee earns fair amount of compensation based on their contribution to the company.

Addresses `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`, `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`  and `0xdcBb8E08e93fD1442039eD65C381666D495d75Be` are used to register the TieredProfitSplitter contract:

![task2_reg](./Images/task2_reg.png)

The original balances for these addresses prior to the transaction are shown as follows:

![task2_old_balance](./Images/task2_old_balance.png)

We sent `10 ether` to the contract and deposit it to these three addresses:

![task2_deposit](./Images/task2_deposit.png)

Upon the transaction, each account will have different amounts of ether, with `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2` getting `6 ether`, `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D` getting `2.5 ether` and
`0xdcBb8E08e93fD1442039eD65C381666D495d75Be` getting `1.5 ether`:

![task2_new_balance](./Images/task2_new_balance.png)

The transaction is verified by the `balance` field:

![task2_deposit_balance](./Images/task2_deposit_balance.png)


---


## DeferredEquityPlan on local ether test net

DeferredEquityPlan contract models traditional company stock plans, it automatically manages 1000 shares, with an annual distribution of 250 shares over four years for a single employee. The intention is to motivate
employees to stay and contribute to the company.

address `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D` is used to deploy the contract:

![task3_reg](./Images/task3_reg.png)

Since the time lock is 365 days, distributing shares at the beginning of the employment or less than a year will not exceed:

![task3_transact_too_early](./Images/task3_transact_too_early.png)

Provided that `fast_forward( )` is implemented and applied, we can click `fastforward` button to simulate time-passing. Fast forwarding is initiated as a transaction of `0 ether`:

![task3_ff](./Images/task3_ff.png)

Upon 4 times of fast forwarding, we are able to distribute the first 250 shares, and this sets the `distributed shares` to `250`:

![task3_distributed_balance_1](./Images/task3_distributed_balance_1.png)

Suppose we continue doing fast forward for the next 3 years, we will accumulate the distributed shares annually with 250 shares:

![task3_distributed_balance_2](./Images/task3_distributed_balance_2.png)

![task3_distributed_balance_3](./Images/task3_distributed_balance_3.png)

![task3_distributed_balance_4](./Images/task3_distributed_balance_4.png)


---


## AssociateProfitSplitter on the Kovan net

Now we deploy a `AssociateProfitSplitter` contract at the Kovan net and continue using addresses `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`, `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`  and `0xdcBb8E08e93fD1442039eD65C381666D495d75Be` to register the AssociateProfitSplitter contract. The original balances for these addresses prior to the transaction are shown as follows:

The original balance for account `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`:
![task4_addr1_old_balance](./Images/task4_addr1_old_balance.png)

The original balance for account `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`:
![task4_addr1_old_balance](./Images/task4_addr2_old_balance.png)

The original balance for account `0xdcBb8E08e93fD1442039eD65C381666D495d75Be`:
![task4_addr1_old_balance](./Images/task4_addr3_old_balance.png)


We sent `0.3 ether` to the contract and deposit it to these three addresses:

![task4_transact](./Images/task4_transact.png)

Upon the transaction, each account will have `3 ether` evenly:

The new balance for account `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`:
![task4_addr1_old_balance](./Images/task4_addr1_new_balance.png)

The new balance for account `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`:
![task4_addr1_old_balance](./Images/task4_addr2_new_balance.png)

The new balance for account `0xdcBb8E08e93fD1442039eD65C381666D495d75Be`:
![task4_addr1_old_balance](./Images/task4_addr3_new_balance.png)


The transaction is verified by the `balance` field:

![task4_balance](./Images/task4_balance.png)


---


## TieredProfitSplitter on the Kovan net

Now we deploy a `TieredProfitSplitter` contract at the Kovan net and continue using addresses `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`, `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`  and `0xdcBb8E08e93fD1442039eD65C381666D495d75Be` to register the AssociateProfitSplitter contract. Note that the original balances for these addresses prior to the transaction all start with `0.2 ether`.

![task5_reg](./Images/task5_reg.png)

We sent `0.2 ether` to the contract and deposit it to these three addresses:

![task5_transact](./Images/task5_transact.png)

Upon the transaction, each account will have `3 ether` evenly:

The new balance for account `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2`:
![task5_addr1_old_balance](./Images/task5_addr1_new_balance.png)

The new balance for account `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D`:
![task5_addr2_old_balance](./Images/task5_addr2_new_balance.png)

The new balance for account `0xdcBb8E08e93fD1442039eD65C381666D495d75Be`:
![task5_addr3_old_balance](./Images/task5_addr3_new_balance.png)


---


## DeferredEquityPlan on the Kovan net

Now we deploy a `DeferredEquityPlan` contract at the Kovan net and continue using address `0xeEC895DfbC492cf34eDacF58696d7B7e931e2a1D` is used to deploy the contract. Since we need to wait for `365 days` 
to see the changes, I continue using `fakenow` to test on the Kovan net. Upon clicking `fastforward` button 4 times 250 shares was able to be distributed to the participated account and the distributed shares
was able to reflect the distribution.

Fast Forwarding is achieved by initiating the transaction via `MetaMask` with `0 ether`:

![task6_ff](./Images/task6_ff.png)

After the first year, which is simulated by pressing `fastforward` button four times, `distributed shares` increased to `250`:

![task6_distributed_balance](./Images/task6_distributed_balance.png)


__Note__: 

1. Due to limit of available `ether` amount, I was not able to fast forwarding the next three years as I couldn't afford the gas. However, 
I believe one should understand both the concept and the evidence of the working contract by now. </br>
2. To send ether, please send to `0x31DF33B2031198e05E4Dd6BA47C70913Be053ca2` and verify from `etherscan`.


