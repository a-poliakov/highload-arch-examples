1 - Access the master container(you read right the user added to master will be replicated to slave)

docker-compose exec postgresql-master bash

2 - Access the psql client

psql -U postgres

3 - Run the SQL commands, creating the user 'reading_user' and giving him permissions

CREATE USER reading_user WITH PASSWORD 'reading_pass';
GRANT CONNECT ON DATABASE my_database TO reading_user;
\connect my_database
GRANT SELECT ON ALL TABLES IN SCHEMA public TO reading_user;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO reading_user;
GRANT USAGE ON SCHEMA public TO reading_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO reading_user;
