import sqlite3

DB_NAME = "scratchpay.db"


# Create table automatically
def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scratch_cards(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        reward_amount INTEGER,
        used INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def create_scratch_link(code):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scratch_cards (code, used) VALUES (?, ?)",
        (code, 0)
    )

    conn.commit()
    conn.close()


def get_scratch_card(code):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM scratch_cards WHERE code=?",
        (code,)
    )

    result = cursor.fetchone()

    conn.close()

    if result is None:
        return None

    return {
        "id": result[0],
        "code": result[1],
        "reward": result[2],
        "used": result[3]
    }


def update_scratch(code, reward):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE scratch_cards SET used=?, reward_amount=? WHERE code=?",
        (1, reward, code)
    )

    conn.commit()
    conn.close()


def get_all_links():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scratch_cards")

    rows = cursor.fetchall()

    conn.close()

    return rows