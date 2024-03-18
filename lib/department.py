from __init__ import CURSOR, CONN  

class Department:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.id = None  # Initialize ID as None

    @classmethod
    def create_table(cls):
        """Creates the departments table if it doesn't exist."""
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drops the departments table if it exists."""
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Saves the Department instance to the database and assigns it an ID."""
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid  # Retrieve the newly assigned ID

    @classmethod
    def create(cls, name, location):
        """Creates a new department row in the database and returns a Department instance."""
        department = Department(name, location)
        department.save()
        return department

    def update(self):
        """Updates the department's corresponding database row with new attribute values."""
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Deletes the department's corresponding database row."""
        sql = "DELETE FROM departments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()