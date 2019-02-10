from sys import maxsize


class contact:

    def __init__(self, name=None, middle_name=None, last_name=None, email=None, homephone=None, secondaryphone=None, mobilephone=None, workphone=None, id=None):
        self.name=name
        self.middle_name=middle_name
        self.last_name=last_name
        self.email = email
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id=id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.last_name == other.last_name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize