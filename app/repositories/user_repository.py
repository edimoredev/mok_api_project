from app.adapters.database import db
from app.models.user import User


class UserRepository:
    def create_user(self, name, email):
        user = User(name, email)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_all_users(self):
        return User.query.all()

    def update_user(self, user_id, name, email):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
