CREATE DATABASE swiggy;

USE swiggy;

CREATE TABLE `Customer` (
  `cid` integer,
  `name` varchar(255),
  `email` varchar(255),
  `phone` varchar(10),
  PRIMARY KEY (`cid`)
);

CREATE TABLE `Restaurants` (
  `rid` integer,
  `name` varchar(255),
  `rating` decimal,
  `address` text,
  PRIMARY KEY (`rid`)
);

CREATE TABLE `Food` (
  `fid` integer,
  `name` varchar(255),
  `price` integer,
  `type` boolean,
  PRIMARY KEY (`fid`)
);

CREATE TABLE `Orders` (
  `oid` integer,
  `cid` integer,
  `rid` integer,
  `time` datetime,
  PRIMARY KEY (`oid`),
  FOREIGN KEY (`cid`)
      REFERENCES `Customer`(`cid`)
);

