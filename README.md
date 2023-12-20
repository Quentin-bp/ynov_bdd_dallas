For this project, you mainly need to have python fastapi and uvicorn installed  

```sh
pip install fastapi
pip install uvicorn
```

## || First step ||
Before to make everything, you have to install all packages.  
Once done, you have to load the api, then this steps : 

## || Run API ||
Under the root folder :  
You have to make the command :  ``` uvicorn api.main:app --reload```   
Once done, you can use Postman (or other app you want) and load the following routes :    
create_roles
- GET ( Create database structure  ) : http://127.0.0.1:8000/create_database
- GET ( Insert data into the database (not required) ) : http://127.0.0.1:8000/insert_data
- GET ( Insert roles : required if you want test one fonction ) : http://127.0.0.1:8000/create_roles

![Home Page](data/images/bye_readme.gif)
