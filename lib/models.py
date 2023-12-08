from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def give_freebie(self, session, dev, item_name, value):
        freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(freebie)
        session.commit()

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()


    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'

    @property
    def freebies(self):
        return self.freebies

    @property
    def companies(self):
        return [freebie.company for freebie in self.freebies]

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer())
    dev_id = Column(Integer, ForeignKey('devs.id'))  # Corrected foreign key reference
    company_id = Column(Integer, ForeignKey('companies.id'))  # Corrected foreign key reference

    dev = relationship('Dev', backref=backref('freebies', cascade='all,delete-orphan'))
    company = relationship('Company', backref=backref('freebies', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<Freebie {self.id}, {self.item_name}, {self.value}, {self.dev_id}, {self.company_id}>'

    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'