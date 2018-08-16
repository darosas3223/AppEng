from google.appengine.ext import ndb



class Note(ndb.Model):
    usr_img = ndb.BlobProperty()
    describe = ndb.StringProperty()


class CheckListItem(ndb.Model):
    title = ndb.StringProperty()
    checked = ndb.BooleanProperty(default=False)
