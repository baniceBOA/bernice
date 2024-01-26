from .server import admin
from .model import db, User, Post, Category
# from flask import redirect, url_for, request
# from flask_login import current_user
from flask_admin.contrib.sqla import ModelView

class CustomView(ModelView):
    '''
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))
    '''
    
admin.add_view(CustomView(Category, db.session))
admin.add_view(CustomView(User, db.session))
admin.add_view(CustomView(Post, db.session))

