import pypyodbc
import azurecred
from datetime import datetime


class AzureDB:
    dsn = 'DRIVER=' + azurecred.AZDBDRIVER + ';SERVER=' + azurecred.AZDBSERVER + ';PORT=1433;DATABASE=' + azurecred.AZDBNAME + ';UID=' + azurecred.AZDBUSER + ';PWD=' + azurecred.AZDBPW

    def __init__(self):
        self.conn = pypyodbc.connect(self.dsn)
        self.cursor = self.conn.cursor()

    def finalize(self):
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def azureGetData(self):
        try:
            self.cursor.execute("SELECT id, name, text, created_at FROM data")
            data = self.cursor.fetchall()
            return data
        except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            return None

    def azureAddData(self, name, text):
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            self.cursor.execute("INSERT INTO data (name, text, created_at) VALUES (?, ?, ?)", (name, text, created_at))
            self.conn.commit()
            return True
        except pypyodbc.DatabaseError as exception:
            print('Failed to insert data')
            print(exception)
            return False

    def azureDeleteData(self, id):
        try:
            self.cursor.execute("DELETE FROM data WHERE id=?", (id,))
            self.conn.commit()
            return True
        except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            return False
