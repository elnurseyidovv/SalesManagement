CREATE DATABASE salesDB;
use salesDB;


CREATE TABLE CLIENT (
  Id int NOT NULL,
  Name varchar(255) NOT NULL,
  Phone varchar(255) NOT NULL,
  PRIMARY KEY (Id)
);

CREATE TABLE CATEGORY (
  Id int NOT NULL,
  Name varchar(255) NOT NULL,
  PRIMARY KEY (Id)
);

CREATE TABLE PRODUCT (
  Id int NOT NULL,
  CategoryId int NOT NULL,
  Name varchar(255) NOT NULL,
  Description varchar(255) NOT NULL,
  Quantity int NOT NULL,
  Price float NOT NULL,
  PRIMARY KEY (Id),
  FOREIGN KEY (CategoryId) REFERENCES CATEGORY(Id)
);

CREATE TABLE INTEREST (
  Id int NOT NULL,
  ClientId int NOT NULL,
  ProductId int NOT NULL,
  Active boolean NOT NULL,
  InterestDate date NOT NULL,
  PRIMARY KEY (Id),
  FOREIGN KEY (ClientId) REFERENCES CLIENT(Id),
  FOREIGN KEY (ProductId) REFERENCES PRODUCT(Id)
);

CREATE TABLE PURCHASE (
  Id int NOT NULL,
  ClientId int NOT NULL,
  ProductId int NOT NULL,
  Price float NOT NULL,
  PurchaseDate date NOT NULL,
  PRIMARY KEY (Id),
  FOREIGN KEY (ClientId) REFERENCES CLIENT(Id),
  FOREIGN KEY (ProductId) REFERENCES PRODUCT(Id)
);
