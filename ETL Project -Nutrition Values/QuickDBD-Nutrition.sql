-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/KD4b84
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Simple Conceptual ERD
CREATE TABLE "food_groups" (
    "id" Integer   NOT NULL,
    "foodgroup" varchar(30)   NOT NULL,
    "shortdescrip" varchar(90)   NOT NULL,
    CONSTRAINT "pk_food_groups" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "basic_nutrient" (
    "id" Integer   NOT NULL,
    "energ_Kcal" float8   NOT NULL,
    "protein" float8   NOT NULL,
    "fat" float8   NOT NULL,
    "water" float8   NOT NULL
);

CREATE TABLE "vitamins" (
    "id" Integer   NOT NULL,
    "vit_a_iu" float8   NOT NULL,
    "vit_b6" float8   NOT NULL,
    "vit_b12" float8   NOT NULL,
    "vit_c" float8   NOT NULL,
    "vit_d" float8   NOT NULL,
    "vit_e" float8   NOT NULL
);

CREATE TABLE "minerals" (
    "id" Integer   NOT NULL,
    "calcium" float8   NOT NULL,
    "phosphorus" float8   NOT NULL,
    "potassium" float8   NOT NULL,
    "sodium" float8   NOT NULL,
    "magnesium" float8   NOT NULL
);

ALTER TABLE "basic_nutrient" ADD CONSTRAINT "fk_basic_nutrient_id" FOREIGN KEY("id")
REFERENCES "food_groups" ("id");

ALTER TABLE "vitamins" ADD CONSTRAINT "fk_vitamins_id" FOREIGN KEY("id")
REFERENCES "food_groups" ("id");

ALTER TABLE "minerals" ADD CONSTRAINT "fk_minerals_id" FOREIGN KEY("id")
REFERENCES "food_groups" ("id");

