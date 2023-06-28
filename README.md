# This Basic Mysql API 

### Aim of the rep

to apply the databases concept which is able to use 3NF databases

### Technology used

- Flask
- Mysql

### How to run the project

- clone the project
- create virtual environment
- install the requirements
- run the project

```bash
git clone https://github.com/robelandro/SimpleBankApi
cd SimpleBankApi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m api.v1.app
```

### api endpoints tables

| Endpoints | Methods | Description |
| --- | --- | --- |
| /customer | GET | get all users |
| /customers | POST | create new user |
| /customer/<string:cust_id> | GET | get user by id |

### Author of The Project

- [Nftalem Arega](https://github.com/robelandro) 
and other my fellow collage contributors
