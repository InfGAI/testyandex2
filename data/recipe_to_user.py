import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class RecipeToUser(SqlAlchemyBase):
    __tablename__ = 'recipetouser'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    id_recipe = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("recipes.id"))
    recipe_id = orm.relation("Recipe", back_populates='recipe')
    user_id = orm.relation("User", back_populates='recipe')
