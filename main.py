from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import datetime
import calendar

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users=[
    {"username": "admin", "password":"admin"},
    {"username": "harish", "password":"harish"},
]

listBookings =[
    {
        "Empid":101,
        "Bookdate":"8/8/2022",
        "Dept":"5G",
        "Activity":"Cloud",
        "Reason":"Urgent booking required",
        "Members":"A, B, C"
    },

    {
        "Empid":102,
        "Bookdate":"8/8/2022",
        "Dept":"5G",
        "Activity":"Cloud Native",
        "Reason":"Urgent booking required",
        "Members":" B, C"
    }

    ]


@app.get('/list/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("list.html", context)

@app.get('/', response_class=HTMLResponse)
def index(request: Request):

    context = {'request': request}
    return templates.TemplateResponse("login.html", context)                      

@app.post('/', response_class=HTMLResponse)
async def index(request: Request):
    form = await request.form()
    username = form["txtusername"]
    password = form["txtpassword"]
    context = {'request': request}
    validuser = False
    for user in users:
        if user["username"] == username and user["password"]==password:
            validuser = True
            break

    if validuser:
        return templates.TemplateResponse("bookSlot.html", context)
    else:       
        context = {'request': request, "error":"Invalid user"} 
        return templates.TemplateResponse("login.html", context)

@app.get('/SignUp', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("SignUp.html", context)

@app.post('/SignUp/', response_class=HTMLResponse)
async def index(request: Request):
    form = await request.form()
    Fullname= form["txtusername"]
    phone= form["txtnumber"]
    username= form["txtusername"]
    password= form["txtpassword"]
    Repeatpassword= form["txtpassword"]
    context = {'request': request}
    validuser = False
    for user in users:
        if user["username"] == username and user["password"]==password and user["password"]==Repeatpassword:
            validuser = True
            break

    if validuser:
        return templates.TemplateResponse("login.html", context)
    else:       
        context = {'request': request, "error":"Invalid user"} 
        return templates.TemplateResponse("SignUp.html", context)

@app.get('/Loginwithadm&RD', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("Loginwithadm&RD.html", context)

@app.post('/Loginwithadm&RD', response_class=HTMLResponse)
async def index(request: Request):
    form = await request.form()
    username = form["txtusername"]
    password = form["txtpassword"]
    context = {'request': request}
    validuser = False
    for user in users:
        if user["username"] == username and user["password"]==password:
            validuser = True
            break

    if validuser:
        return templates.TemplateResponse("Go.html", context)
    else:       
        context = {'request': request, "error":"Invalid user"} 
        return templates.TemplateResponse("Loginwithadm&RD.html", context)

@app.get('/bookSlot/', response_class=HTMLResponse)
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("bookSlot.html", context)

@app.post('/bookSlot/', response_class=HTMLResponse)
async def index(request: Request):
    form = await request.form()
    print(form)
    listBookings.append({
         "Empid":form["txtempid"],
        "Bookdate":"8/8/2022",
        "Dept":"5G",
        "Activity":"Cloud Native",
        "Reason":"Urgent booking required",
        "Members":" B, C"
    })
    context = {'request': request}
    #return RedirectResponse(url="/list/")
    return templates.TemplateResponse("list.html", context)


@app.post('/SignUp/', response_class=HTMLResponse)
async def index(request: Request):
    form = await request.form()
    print(form)
    context = {'request': request}
    #return RedirectResponse(url="/list/")
    return templates.TemplateResponse("list.html", context)



@app.post('/Go/', response_class=HTMLResponse)
async def index(request: Request):
    form = await request.form()
    print(form)
    context = {'request': request}
    #return RedirectResponse(url="/Loginwithadm&RD/")
    return templates.TemplateResponse("Loginwithadm&RD.html", context)

@app.get('/calendar/', response_class=HTMLResponse)
async def index(request: Request, selCalendar:str|None=None):
    form = await request.form()
    print(form)
    if selCalendar:
        selCalendar = int(selCalendar)
    else:
        selCalendar = 1
    dateList = []
    cols = 7
    rows = 6
    currentYear = datetime.date.today()

    print(currentYear)  
    startDateMonth = datetime.date(currentYear.year,selCalendar,1)
    startNextMonth = datetime.date(currentYear.year if selCalendar < 12 else currentYear.year+1 ,selCalendar+1 if selCalendar < 12 else 1 ,1)
    startDayNum = startDateMonth.weekday() 
    #totDaysInMonth = calendar.monthrange(2022, 9)
   # monthrangecalendar.monthrange(year, month))
    #print(currentYear.year)
    #print(currentYear.month)
    totDaysInMnth = (startNextMonth - startDateMonth).days
    #print((startNextMonth - startDateMonth).days)
    bookingSaved = [
        {'day':3, 'isBook':'yes', 'time':'10:20 - 12:00', 'bookName':'Stephen from 5g team'},
        {'day':13, 'isBook':'yes','time':'10:20 - 12:00',  'bookName':'Raghu from 5g team'},
        {'day':15, 'isBook':'yes', 'time':'10:20 - 12:00', 'bookName':'Raj from 5g team'},
        {'day':16, 'isBook':'yes', 'time':'11:00 - 12:00', 'bookName':'Lab1 from 5g team'}
    ]

    for i in range(0,totDaysInMnth):
        dateList.append({'day':i+1, 'time':'', 'isBook':'no', 'bookName':''})
    
    for bkng in bookingSaved:
       # print(bkng['day'])
        dateList[bkng['day'] - 1]['isBook']= bkng['isBook']
        dateList[bkng['day'] - 1]['time']= bkng['time']
        dateList[bkng['day'] - 1]['bookName']= bkng['bookName']
        #'bookName': bkng['bookName']},
    
    print(dateList)
    context = {'request': request, 'rows': rows, 'cols':cols    , 'startDayNum': startDayNum, 'dateList': dateList, 'selCalendarVal': selCalendar}
    return templates.TemplateResponse("calendar.html", context) 

