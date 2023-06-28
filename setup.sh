#!/bin/bash

cat setup_mysql_dev.sql | sudo mysql -hlocalhost -uroot -p

# cat bank_setup.sql | sudo mysql -hlocalhost -ubanks -p
