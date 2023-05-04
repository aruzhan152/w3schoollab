import psycopg2 as ps

conn = ps.connect(host = 'localhost',
                  dbname = 'players',
                  user = 'postgres',
                  password = '1234',
                  port = '5432'
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE snake (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL DEFAULT 0
);
""")


conn.commit()

cur.close()
conn.close()