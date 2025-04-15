# Phone Book App

This is a basic Phone Book application built using the FastAPI framework. It allows users to manage their contacts by performing CRUD (Create, Read, Update, Delete) operations.

## Features

- **Retrieve Contacts**: Get a list of all contacts.
- **Add Contact**: Add a new contact to the phone book.
- **Update Contact**: Update an existing contact's details.
- **Delete Contact**: Remove a contact from the phone book.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ak-mustafa/test-repo-1.git
   cd test-repo-1
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## Usage

1. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Open your browser and navigate to:
   - API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Interactive API: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### 1. Get All Contacts
- **Endpoint**: `/contacts`
- **Method**: `GET`
- **Description**: Retrieve all contacts in the phone book.

### 2. Add a Contact
- **Endpoint**: `/contacts`
- **Method**: `POST`
- **Description**: Add a new contact.
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "phone": "123-456-7890"
  }
  ```

### 3. Update a Contact
- **Endpoint**: `/contacts/{name}`
- **Method**: `PUT`
- **Description**: Update an existing contact's details.
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "phone": "987-654-3210"
  }
  ```

### 4. Delete a Contact
- **Endpoint**: `/contacts/{name}`
- **Method**: `DELETE`
- **Description**: Delete a contact by name.

## License

This project is licensed under the MIT License.