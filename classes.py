import datetime
class TelegramUser:
    def __init__(self, user_id):
        self.id = user_id
        self.status = None
        self.username = self.first_name = self.second_name = None
        self.pic = None
        self.time()
    def time(self):
        self.last_ivent = datetime.datetime.now().replace(microsecond=0)

class SessionStore:
    def __init__(self):
        self.users = {}

    def short_init(self, user_id: int) -> TelegramUser:
        if user_id not in self.users:
            self.users[user_id] = TelegramUser(user_id)
        return self.users[user_id]

session = SessionStore()