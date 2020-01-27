CREATE TABLE "User" (
  "id" integer,
  "name" varchar,
  "f_name" varchar,
  "email" varchar,
  "hashd_password" varchar,
  "date_created" datetime,
  "national_num" integer,
  "last_login" datetime,
  PRIMARY KEY ("id", "national_num")
);

CREATE TABLE "Wallet" (
  "id" integer PRIMARY KEY,
  "amount" integer,
  "last_updated" datetime,
  "user_id" integer
);

CREATE TABLE "Transaction" (
  "id" integer PRIMARY KEY,
  "amount" integer,
  "wallet_id" integer,
  "date_created" datetime
);

CREATE TABLE "OS" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "base_RAM" integer,
  "base_CPU" integer,
  "base_CORE" integer,
  "base_disk" float,
  "base_cost" float,
  "base_band_width" float
);

CREATE TABLE "SSH" (
  "id" integer,
  "name" varchar,
  "key" varchar,
  "user_id" integer,
  PRIMARY KEY ("id", "key")
);

CREATE TABLE "Cloud" (
  "id" integer PRIMARY KEY,
  "ssh_id" integer,
  "os_id" integer,
  "cpu_amount" integer,
  "core_amount" integer,
  "disk_amount" integer,
  "ram_amount" float,
  "band_width" float,
  "cost_per_day" float
);

CREATE TABLE "Snapshot" (
  "id" integer PRIMARY KEY,
  "cloud" integer,
  "date_created" datetime
);

ALTER TABLE "Wallet" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Transaction" ADD FOREIGN KEY ("wallet_id") REFERENCES "Wallet" ("id");

ALTER TABLE "SSH" ADD FOREIGN KEY ("user_id") REFERENCES "User" ("id");

ALTER TABLE "Cloud" ADD FOREIGN KEY ("ssh_id") REFERENCES "SSH" ("id");

ALTER TABLE "Cloud" ADD FOREIGN KEY ("os_id") REFERENCES "OS" ("id");

ALTER TABLE "Snapshot" ADD FOREIGN KEY ("cloud") REFERENCES "Cloud" ("id");
