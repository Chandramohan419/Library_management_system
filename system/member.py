'''class Member:
    def __init__(self, first_name, last_name, email, member_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.member_id = member_id
        self.borrowed_books = []
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.member_id}"'''

class Member:
    def __init__(self, member_id, first_name):
        self.first_name = first_name
        self.member_id = member_id
        self.borrowed_books = []
    def __str__(self):
        return f"{self.member_id} {self.first_name}"

