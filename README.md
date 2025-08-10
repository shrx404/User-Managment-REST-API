# User Management REST API

This project is a simple User Management REST API built using Flask. It provides endpoints to create and retrieve user data, storing the information in a JSON file. The API is designed to handle basic user management operations such as creating a user and fetching user details by UID or email.

## Features

- **Create User**: Add a new user to the database with a unique UID and timestamp.
- **Get User**: Retrieve user details by UID or email.
- Data is stored persistently in a JSON file (`Data/users.json`).

## Project Structure

```
User Management API/
├── Data/
│   └── users.json          # JSON file to store user data
├── main.py                 # Main application file
├── pyproject.toml          # Python project configuration
├── README.md               # Project documentation
└── uv.lock                 # Dependency lock file
```

## Prerequisites

- Python 3.9 or higher
- Flask library

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/shrx404/User-Managment-REST-API.git
   cd User-Managment-REST-API
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install flask pandas
   ```

4. Run the application:

   ```bash
   python main.py
   ```

5. The API will be available at `http://{ip-out}:5000`.

## API Endpoints

### 1. Get User

**Endpoint**: `/get-user`

**Method**: `GET`

**Query Parameters**:

- `uid` (optional): Unique identifier of the user.
- `email` (optional): Email address of the user.

**Example**:

```bash
curl "http://{ip-out}:5000/get-user?uid=user_2025-08-10_12-00-00_1234abcd"
```

**Response**:

- `200 OK`: Returns the user details.
- `404 Not Found`: User not found.
- `400 Bad Request`: Missing query parameters.

### 2. Create User

**Endpoint**: `/create-user`

**Method**: `POST`

**Request Body** (JSON):

```json
{
  "userName": "John Doe",
  "password": "securepassword",
  "email": "johndoe@example.com"
}
```

**Example**:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"userName": "John Doe", "password": "securepassword", "email": "johndoe@example.com"}' http://{ip-out}:5000/create-user
```

**Response**:

- `201 Created`: Returns the updated list of users.

## Data Storage

User data is stored in a JSON file located at `Data/users.json`. The file is automatically created if it does not exist.

## Notes

- The application uses the `Asia/Kolkata` timezone for timestamps.
- Each user is assigned a unique UID based on the current timestamp and a random UUID.

## Future Enhancements

- Add user authentication and authorization.
- Implement additional endpoints for updating and deleting users.
- Use a database (e.g., SQLite, PostgreSQL) for better scalability.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Created using UV.
