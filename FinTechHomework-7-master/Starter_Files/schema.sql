DROP TABLE IF EXISTS Card_Holder CASCADE;
DROP TABLE IF EXISTS Credit_Card CASCADE;
DROP TABLE IF EXISTS Merchant_Category CASCADE;
DROP TABLE IF EXISTS Merchant CASCADE;
DROP TABLE IF EXISTS Transaction CASCADE;


CREATE TABLE Card_Holder (
    "id" SERIAL  PRIMARY KEY,
    "name" VARCHAR(30)   NOT NULL
);

CREATE TABLE Credit_Card (
    "card" BIGINT PRIMARY KEY,
    "cardholder_id" INT   NOT NULL,
	FOREIGN KEY (cardholder_id) REFERENCES Card_Holder(id)
);

CREATE TABLE Merchant_Category (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(30)   NOT NULL
);

CREATE TABLE Merchant (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(255)   NOT NULL,
    "id_merchant_category" INT   NOT NULL,
     FOREIGN KEY (id_merchant_category) REFERENCES Merchant_Category(id)
);

CREATE TABLE Transaction (
    "id" INT NOT NULL,
    "date" TIMESTAMP   NOT NULL,
    "amount" FLOAT   NOT NULL,
    "card" BIGINT   NOT NULL,
    "id_merchant" INT   NOT NULL,
	FOREIGN KEY (id_merchant) REFERENCES Merchant(id),
	FOREIGN KEY (card) REFERENCES Credit_Card(card)
);