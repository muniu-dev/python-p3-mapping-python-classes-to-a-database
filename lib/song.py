from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        # Create the 'songs' table
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        ''')

    def save(self, connection=CONN):
        # Save the song to the 'songs' table
        with connection:
            cursor = connection.cursor()
            cursor.execute(
            'INSERT INTO songs (name, album) VALUES (?, ?)',
            (self.name, self.album)
        )

        # Set the id using the last inserted row id
            self.id = cursor.lastrowid

    @classmethod
    def create(cls, name, album, connection=CONN):
        # Create and save a new song, then return the Song instance
        song = cls(name, album)
        song.save(connection)
        return song