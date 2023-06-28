#!/usr/bin/python3
from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

from api.v1.routes.MainBank import *
from api.v1.routes.Login import *
from api.v1.routes.index import *
from api.v1.routes.Account import *
from api.v1.routes.Customer import *
from api.v1.routes.Transaction import *
from api.v1.routes.Loan import *
