from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer 
from database import base,db_engine
    
class Signup(base):
    __tablename__ ="signup"

    id = Column(Integer, primary_key=True, index=True)
    Username = Column(String(30),nullable=False)
    Email = Column(String(255), nullable=False, unique=True)
    Password = Column(String(128), nullable=False)

class Profit(base):
    __tablename__ = "Profit"

    id = Column(Integer, primary_key=True, index=True)
    Room_No = Column(String(30))
    Booking_Count = Column(String(30))
    Reservation_Type = Column(String(30))
    Price_Amount = Column(String(30))
    Tax_Percentage = Column(String(30))
    Total_Amount = Column(String(30))
    status = Column(String(30))

class ResProfit(base):
    __tablename__ = "ResProfit"

    id = Column(Integer, primary_key=True, index=True)
    Table_No = Column(String(30))
    Booking_Count = Column(String(30))
    Price_Amount = Column(String(30))
    Tax_Percentage = Column(String(30))
    Total_Amount = Column(String(30))
    status = Column(String(30))

class BarProfit(base):
    __tablename__ = "BarProfit"

    id = Column(Integer, primary_key=True, index=True)
    Table_No = Column(String(30))
    Booking_Count = Column(String(30))
    Price_Amount = Column(String(30))
    Tax_Percentage = Column(String(30))
    Total_Amount = Column(String(30))
    status = Column(String(30))
    
base.metadata.create_all(bind=db_engine)