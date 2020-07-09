from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from . import Base

association_table = Table('charities_tags', Base.metadata,
                          Column('charities_id', Integer, ForeignKey('charities.id')),
                          Column('tags_id', Integer, ForeignKey('tags.id'))
                          )


class Charity(Base):
    __tablename__ = "charities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    tags = relationship(
        "Tag",
        secondary=association_table,
        back_populates="charities")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    charities = relationship(
        "Charity",
        secondary=association_table,
        back_populates="tags")
