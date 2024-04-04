from datetime import datetime

import db, uuid
from utils import Utils
from peewee import *

base_dir = Utils.get_base_dir()
db = SqliteDatabase(f"{base_dir}/db/dcm.sqlite3")

# define a classe do modelo
class Conext(Model):

    id          = IntegerField(primary_key=True)
    name        = TextField()
    host        = TextField()
    description = TextField(default="")
    created_on  = DateTimeField(default=datetime.now())

    class Meta:
        database = db

    def get_all(self):
        return Context.select()

    def create(self, host, description=""):
        
        if db.table_exists():

            if host:
                name = uuid.uuid4().__str__()
                context = Context(name=name, host=host, description=description)

                if not context:
                    return False, None

                context.save()
                return True, name
        else:
            db.create_tables([Context])
            self.create(host, description)

        return False, None

    #def delete(self, host):
