import psycopg

DEFAULT_DB_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

class PgClient:

    def __init__(self, url: str = DEFAULT_DB_URL):
        # dsn=f"postgresql://{user}:{password}@{host}:{port}/{database}
        self.conn = psycopg.connect(conninfo=url)

    def exec_query(self, query: str):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def read_query(self, query: str):
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def insert_tx_hash(self, tx_hash: str):
        """Inserts (`tx_hash`) into event_tx_hashes table"""
        # ! this function assumes existence of table `event_tx_hashes` with a column `tx_hash`
        self.exec_query(f"INSERT INTO event_tx_hashes (tx_hash) values ('{tx_hash}')")
        print(f"insert success: ({tx_hash})!")


    def select_given_string(self, given_str: str):
        """Does not require any existing schema on DB."""
        return self.read_query(f"SELECT '{given_str}'")
        