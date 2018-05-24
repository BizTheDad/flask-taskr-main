# import models
# from datetime import date
from views import db

db.create_all()

# db.session.add(models.Task("Finish this tutorial", date(2018, 5, 25), 10, 1))
# db.session.add(models.Task("Finish Real Python", date(2018, 10, 3), 10, 1))

db.session.commit()
