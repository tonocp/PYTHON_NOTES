import users.db_conection as connection
import datetime
import hashlib

connect = connection.connect()
database = connect[0]
cursor = connect[1]


class User:

    def __init__(self, name, surnames, email, password):
        self.name = name
        self.surnames = surnames
        self.email = email
        self.password = password

    def register(self):
        securePass = hashlib.sha256()
        securePass.update(self.password.encode('utf8'))
        sql = "INSERT INTO users VALUES(null,%s,%s,%s,%s,%s)"
        user = (self.name, self.surnames, self.email,
                securePass.hexdigest(), datetime.datetime.now())
        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identify(self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        securePass = hashlib.sha256()
        securePass.update(self.password.encode('utf8'))
        user = (self.email, securePass.hexdigest())
        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result
