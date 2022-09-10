# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String, Text
from db import Base
from db import ENGINE


class TargetsTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(50), nullable=False)
    statut = Column(Integer)
    report = Column(Text)


def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
