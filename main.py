from database.database import create_db_and_tables

def bootstrap():
    print("Starting up system...")
    create_db_and_tables()
    print("Db is up!")

if __name__ == "__main__":
    bootstrap()