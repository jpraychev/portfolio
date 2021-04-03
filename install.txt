# Python virtual environment
apt-get install python3-venv

# pip install -r requirements.txt
# you may get error with psycopg2 driver.
# in order to avoid building from source install psycopg2-binary
pip install psycopg2-binary
pip install wheel
sudo apt-get install python-dev
sudo apt install python3-dev
sudo apt-get install libpq-dev
sudo apt-get install gcc libpq-dev -y

pip install -r requirements.txt

# install postgres
sudo apt install postgresql postgresql-contrib

# change pwd of postgres
passwd postgres

# log in with postgres to database
su postgres
psql

# Create DB
createdb portfolio

# Create user with password
CREATE DATABASE yourdbname;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;