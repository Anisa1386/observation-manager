import sqlite3


def save_to_db(observations):
    connection = sqlite3.connect("observation.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            target TEXT,
            observer TEXT,
            filter_name TEXT,
            exposure REAL
        )
    """)

    cursor.execute("DELETE FROM observations")

    for obs in observations:
        cursor.execute(
            "INSERT INTO observations VALUES (?, ?, ?, ?)",
            (obs.target, obs.observer, obs.filter, obs.exposure)
        )

    connection.commit()
    connection.close()