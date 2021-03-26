import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Recipe(SqlAlchemyBase):
    __tablename__ = 'recipes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    recipe = orm.relation('RecipeToUser')
