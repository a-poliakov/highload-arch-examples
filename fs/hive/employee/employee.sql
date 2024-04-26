-- Создаём таблицы, загружаем данные
CREATE TABLE IF NOT EXISTS employee (
                                        name string,
                                        work_place ARRAY<string>,
                                        gender_age STRUCT<gender:string,age:int>,
                                        skills_score MAP<string,int>,
                                        depart_title MAP<STRING,ARRAY<STRING>>
)
--     PARTITIONED BY (year INT, month INT)
    ROW FORMAT DELIMITED
        FIELDS TERMINATED BY '|'
        COLLECTION ITEMS TERMINATED BY ','
        MAP KEYS TERMINATED BY ':'
    STORED AS TEXTFILE;

-- INSERT INTO employee_part PARTITION (year=2020, month=12) SELECT * from employee where name = 'Will';
LOAD DATA LOCAL INPATH '/employee/employee.txt' OVERWRITE INTO TABLE employee;
