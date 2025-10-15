
<div>
<h3>Local Installation</h3>
<br>
<span style="color:yellowgreen;font-size: 15px">Prerequisites:</span><br>

Python 3.9+ ; PostgreSQL16+

<br>
<span style="color:yellowgreen;font-size: 15px">Project deployment:</span>
<br><br>
Open a terminal and run the following commands:

```bash
git clone https://github.com/735Andrew/WB_API_Tester
cd WB_API_Tester 
python -m venv venv 
venv\Scripts\activate
(venv) pip install -r requirements.txt
```

Create a <b>.env</b> file in the root directory with the following variables:

```commandline 
TOKEN = <WB_TOKEN>
POSTGRESQL_DATABASE_URL = postgresql+psycopg2://<USER_VARIABLE>:<PASSWORD_VARIABLE>@localhost:5432/<DB_VARIABLE>
```
<br>
Open a terminal in the root directory and execute these commands:

```
# Testing of WB API work
(venv) python
>>> from app.task_1 import report_creator
>>> report_creator()
{'2025-..-..': {'nmId_...': {'price': ...}}, '2025-..-..': {..} }
    
    
# Testing of server work    
(venv) uvicorn project:app --port 8000 

# Open another terminal
(venv) python
>>> import requests as r
>>>
>>> URL1 = "http://localhost:8000/sales/all"            # URL to take all sales for 2 weeks period
>>> URL2 = "http://localhost:8000/sales/2025-10-05"     # URL to take sales for certain day in 2 weeks period
>>> URL3 = "http://localhost:8000/sales/2050-05-10"     # Incorrect URL 
>>> 
>>> r.get(URL1).json()    # {'2025-..-..': {'nmId_...': {'price': ...}}, '2025-..-..': {..} }
>>> r.get(URL2).json()    # {'2025-10-05': {'nmId_...': {'price': ...}}}
>>> r.get(URL3).json()    # {'detail': "There is no sale with date '2050-05-10'"}
```
</div>
<hr>