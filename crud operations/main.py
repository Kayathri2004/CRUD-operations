from fastapi import FastAPI,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,JSONResponse
from database import SessionLocal
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
# from models import base
import models

app=FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/templates",StaticFiles(directory="templates"), name="templates")

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/login")
def login_page(request: Request):   
    return templates.TemplateResponse('login.html', context={'request': request}) 
    
@app.post("/signup")
def signup(request:Request,db:Session=Depends(get_db),signup_username:str=Form(...),signup_email:str=Form(...),signup_password:str=Form(...)):
    find=db.query(models.Signup).filter(models.Signup.Username ==signup_username,models.Signup.Email==signup_email).first()
    if find is not None:
        error= "This user name and email is already exist"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        data=models.Signup(Username=signup_username,Email=signup_email,Password=signup_password)
        db.add(data)
        db.commit()
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    

@app.post("/logcheck")
def logcheck(request:Request,db:Session=Depends(get_db),login_email:str=Form(...),login_password:str=Form(...)):
    find=db.query(models.Signup).filter(models.Signup.Email==login_email,models.Signup.Password==login_password).first()
    if find is None:
        error= "Invalid Creditional"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)

        
@app.get('/get_hotel_profit') 
def get_form(request:Request,db:Session = Depends(get_db)):
    new_user=db.query(models.Profit).filter(models.Profit.status=="ACTIVE").all()
    return templates.TemplateResponse("2hotel_profit.html",context={"request":request,"new_id":new_user})

@app.get('/get_res_profit') 
def get_form(request:Request,db:Session = Depends(get_db)):
    new_user=db.query(models.ResProfit).filter(models.ResProfit.status=="ACTIVE").all()
    return templates.TemplateResponse("2restaurant_profit.html",context={"request":request,"new_id":new_user})

@app.get('/get_bar_profit') 
def get_form(request:Request,db:Session = Depends(get_db)):
    new_user=db.query(models.BarProfit).filter(models.BarProfit.status=="ACTIVE").all()
    return templates.TemplateResponse("2bar_profit.html",context={"request":request,"new_id":new_user})

    
@app.post("/create_hotel_profit")
def create_data(request:Request,db:Session=Depends(get_db),Room_No:str=Form(...),Booking_Count:str=Form(...),Reservation_Type:str=Form(...),Price_Amount:str=Form(...),Tax_Percentage:str=Form(...),Total_Amount:str=Form(...)):
    statuss="ACTIVE"
    find=db.query(models.Profit).filter(models.Profit.Room_No==Room_No,models.Profit.status =="ACTIVE").first()
    if find is None:
        body=models.Profit(Room_No=Room_No,Booking_Count=Booking_Count,Reservation_Type=Reservation_Type,Price_Amount=Price_Amount,Tax_Percentage=Tax_Percentage,Total_Amount=Total_Amount,status=statuss)
        db.add(body)
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    
@app.post("/create_res_profit")
def create_data(request:Request,db:Session=Depends(get_db),Table_No:str=Form(...),Booking_Count:str=Form(...),Price_Amount:str=Form(...),Tax_Percentage:str=Form(...),Total_Amount:str=Form(...)):
    statuss="ACTIVE"
    find=db.query(models.ResProfit).filter(models.ResProfit.Table_No==Table_No,models.ResProfit.status =="ACTIVE").first()
    if find is None:
        body=models.ResProfit(Table_No=Table_No,Booking_Count=Booking_Count,Price_Amount=Price_Amount,Tax_Percentage=Tax_Percentage,Total_Amount=Total_Amount,status=statuss)
        db.add(body)
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    
@app.post("/create_bar_profit")
def create_data(request:Request,db:Session=Depends(get_db),Table_No:str=Form(...),Booking_Count:str=Form(...),Price_Amount:str=Form(...),Tax_Percentage:str=Form(...),Total_Amount:str=Form(...)):
    statuss="ACTIVE"
    find=db.query(models.BarProfit).filter(models.BarProfit.Table_No==Table_No,models.BarProfit.status =="ACTIVE").first()
    if find is None:
        body=models.BarProfit(Table_No=Table_No,Booking_Count=Booking_Count,Price_Amount=Price_Amount,Tax_Percentage=Tax_Percentage,Total_Amount=Total_Amount,status=statuss)
        db.add(body)
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
   
@app.put('/put_hotel_profit/{id}')
def get_form(id:int,request:Request,db:Session = Depends(get_db)):
    result1 = db.query(models.Profit).filter(models.Profit.id == id,models.Profit.status=="ACTIVE").first()
    json_compatible_item_data = jsonable_encoder(result1)
    return JSONResponse(content=json_compatible_item_data)

@app.put('/put_res_profit/{id}')
def get_form(id:int,request:Request,db:Session = Depends(get_db)):
    result1 = db.query(models.ResProfit).filter(models.ResProfit.id == id,models.ResProfit.status=="ACTIVE").first()
    json_compatible_item_data = jsonable_encoder(result1)
    return JSONResponse(content=json_compatible_item_data)

@app.put('/put_bar_profit/{id}')
def get_form(id:int,request:Request,db:Session = Depends(get_db)):
    result1 = db.query(models.BarProfit).filter(models.BarProfit.id == id,models.BarProfit.status=="ACTIVE").first()
    json_compatible_item_data = jsonable_encoder(result1)
    return JSONResponse(content=json_compatible_item_data)
    
@app.post("/update_hotel_profit")
def create_data(request:Request,db:Session=Depends(get_db),edit_id:int=Form(...),edit_Room_No:str=Form(...),edit_Booking_Count:str=Form(...),edit_Reservation_Type:str=Form(...),edit_Price_Amount:str=Form(...),edit_Tax_Percentage:str=Form(...),edit_Total_Amount:str=Form(...)):
    find=db.query(models.Profit).filter(models.Profit.id!=edit_id,models.Profit.Room_No==edit_Room_No,models.Profit.status =="ACTIVE").first()
    if find is None:
        db.query(models.Profit).filter(models.Profit.id==edit_id).update({"Room_No":edit_Room_No,"Booking_Count":edit_Booking_Count,"Reservation_Type":edit_Reservation_Type,"Price_Amount":edit_Price_Amount,"Tax_Percentage":edit_Tax_Percentage,"Total_Amount":edit_Total_Amount})
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)

@app.post("/update_res_profit")
def create_data(request:Request,db:Session=Depends(get_db),edit_id:int=Form(...),edit_Table_No:str=Form(...),edit_Booking_Count:str=Form(...),edit_Price_Amount:str=Form(...),edit_Tax_Percentage:str=Form(...),edit_Total_Amount:str=Form(...)):
    find=db.query(models.ResProfit).filter(models.ResProfit.id!=edit_id,models.ResProfit.Table_No==edit_Table_No,models.ResProfit.status =="ACTIVE").first()
    if find is None:
        db.query(models.ResProfit).filter(models.ResProfit.id==edit_id).update({"Table_No":edit_Table_No,"Booking_Count":edit_Booking_Count,"Price_Amount":edit_Price_Amount,"Tax_Percentage":edit_Tax_Percentage,"Total_Amount":edit_Total_Amount})
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    
@app.post("/update_bar_profit")
def create_data(request:Request,db:Session=Depends(get_db),edit_id:int=Form(...),edit_Table_No:str=Form(...),edit_Booking_Count:str=Form(...),edit_Price_Amount:str=Form(...),edit_Tax_Percentage:str=Form(...),edit_Total_Amount:str=Form(...)):
    find=db.query(models.BarProfit).filter(models.BarProfit.id!=edit_id,models.BarProfit.Table_No==edit_Table_No,models.BarProfit.status =="ACTIVE").first()
    if find is None:
        db.query(models.BarProfit).filter(models.BarProfit.id==edit_id).update({"Table_No":edit_Table_No,"Booking_Count":edit_Booking_Count,"Price_Amount":edit_Price_Amount,"Tax_Percentage":edit_Tax_Percentage,"Total_Amount":edit_Total_Amount})
        db.commit()
        error = "Done"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "Already this name Exist"
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)

@app.get("/del_hotel_profit/{id}")
def create_data(id:int,request:Request,db:Session=Depends(get_db)):
    db.query(models.Profit).filter(models.Profit.id==id,models.Profit.status=="ACTIVE").update({"status":"INACTIVE"})
    db.commit()
    return RedirectResponse("/get_hotel_profit",status_code=302)

@app.get("/del_res_profit/{id}")
def create_data(id:int,request:Request,db:Session=Depends(get_db)):
    db.query(models.ResProfit).filter(models.ResProfit.id==id,models.ResProfit.status=="ACTIVE").update({"status":"INACTIVE"})
    db.commit()
    return RedirectResponse("/get_res_profit",status_code=302)

@app.get("/del_bar_profit/{id}")
def create_data(id:int,request:Request,db:Session=Depends(get_db)):
    db.query(models.BarProfit).filter(models.BarProfit.id==id,models.BarProfit.status=="ACTIVE").update({"status":"INACTIVE"})
    db.commit()
    return RedirectResponse("/get_bar_profit",status_code=302)
