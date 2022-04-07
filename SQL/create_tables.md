# Create a table

The standard syntax for creating a table in SQL is using the `CREATE TABLE` command. The below example creates a `person` table with various datatypes and a `PRIMARY KEY` of `pk_person`, set to the column `person_id`.

The table is normalized (which is the process of ensuring there is no duplicate (other than foreign keys) or compounded columns in the database design) and compound columns have been account for. For example, `name` consists of a `fname` and `lname`. The `name` column alone is referred to as a `compound` column. 

## Using a database engine, such as MySQL

```sql
CREATE TABLE person
    (person_id SMALLINT UNSIGNED,
    fname VARCHAR(20),
    lname VARCHAR(20),
    eye_color ENUM('BR', 'BL', 'GR'),
    birth_date DATE,
    street VARCHAR(30),
    city VARCHAR(20),
    state VARCAR(20),
    country VARCHAR(20),
    postal_code VAR(20),
    CONSTRAINT pk_person PRIMARY KEY (person_id)
    );
```

### Creating another table with a foreign key to the person table

The table above has a primary key called `person_id` to guarantee uniqueness. 

```sql
CREATE TABLE favourite_food
(person_id SMALLINT UNSIGNED,
food VARCHAR(20),
CONSTRAINT pk_favourite_food PRIMARY KEY (person_id, food),
CONSTRAINT fk_fv_food_person_id FOREIGN KEY (person_id)
REFERENCES person (person_id)
);
```

This table has two primary keys to guarantee uniqueness, since a person can have more than one favourite food - `person_id` and `food`. The `favourite_food` table contains another type of constraint which is called a `foreign key` constraint. This constrains the value of the `person_id` column in the `favourite_food` table to include only values found in the `person` table.

## In SQLite

`sqlite3 my_db.db`
