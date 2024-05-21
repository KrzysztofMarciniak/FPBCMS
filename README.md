# FPBCMS
```console
flask run --debug --debugger
```
![home](https://github.com/KrzysztofMarciniak/FPBCMS/assets/96542207/65804ceb-a4e0-48d7-ad74-9fdb6b6b9c8c)

## Flask Powered Basic Content Manager System

FPBCMS is a simple content management system built with Flask. It allows users to perform CRUD (Create, Read, Update, Delete) operations on articles. Additionally, users can be added and logged in to manage the articles. The system was designed to be straightforward and easy to use.

### Features
* Article Management: Create, read, update, and delete articles.
* User Management: Add and log in users to manage articles.
* Simple and Intuitive: Easy-to-use interface for managing content.
#### Installation
* Clone the repository:
 ```console
git clone https://github.com/KrzysztofMarciniak/FPBCMS.git
cd FPBCMS
```
* Create a virtual environment:
```console
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
* Setup the MySQL database.
 ```python
self.connection = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)
```
* Turn on the server:
 ```console
flask run --debug --debugger
```
* Access localhost:5000/checkdb to insert required tables.
* Access localhost:5000/register to register user. Secret password is (`pass`)
