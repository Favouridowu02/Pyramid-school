# Pyramid SWE Main API Documentation

## Overview
The Pyramid SWE Main API powers the Pyramid School Web Application, enabling user authentication, student management, and resource handling. This documentation provides a detailed description of the API's endpoints and their usage.

---

## Base URL
`https://loaclhost/api/v1/`

---

## Authentication Endpoints

### Status
**Endpoint:** `GET /status`

**Description:** Confirm if the api endpoint is set up.

**Request Body:**
```json
{

}
```
**Response:**
- `200`: OK.

### 1. Register
**Endpoint:** `POST /auth/register`

**Description:** Registers a new user.

**Request Body:**
```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "username": "string",
  "password": "string"
}
```
**Response:**
- `201 OK`: Registration successful.

**Example Request:**
```bash
curl -X POST https://api.pyramidswe.com/v1/auth/register \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "username": "johndoe",
  "password": "securepassword"
}'
```

---

### 2. Login
**Endpoint:** `POST /auth/login`

**Description:** Authenticates a user and provides tokens.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```
**Response:**
```json
{
  "access_token": "string",
  "refresh_token": "string"
}
```
- `200 OK`: Authentication successful.

**Example Request:**
```bash
curl -X POST https://api.pyramidswe.com/v1/auth/login \
-H "Content-Type: application/json" \
-d '{
  "username": "johndoe",
  "password": "securepassword"
}'
```

---

### 3. Logout
**Endpoint:** `POST /auth/logout`

**Description:** Logs out a user by blacklisting their token.

**Response:**
- `200 OK`: Logout successful.

**Example Request:**
```bash
curl -X POST https://api.pyramidswe.com/v1/auth/logout \
-H "Authorization: Bearer access_token"
```

---

### 4. Forgot Password
**Endpoint:** `POST /auth/forgot_password`

**Description:** Resets a user's password.

**Request Body:**
```json
{
  "reset_token": "string",
  "new_password": "string"
}
```
**Response:**
- `200 OK`: Password reset successful.
- `401 Unauthorized`: Invalid token.
- `400 Bad Request`: Missing required fields.

**Example Request:**
```bash
curl -X POST https://api.pyramidswe.com/v1/auth/forgot_password \
-H "Content-Type: application/json" \
-d '{
  "reset_token": "valid_reset_token",
  "new_password": "newsecurepassword"
}'
```

---

## Student Endpoints

### 1. Get All Students
**Endpoint:** `GET /students`

**Description:** Retrieves a list of all registered students.

**Response:**
```json
[
  {
    "id": "string",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "username": "string",
    "xp": "string"
  }
]
```
- `200 OK`: Students retrieved successfully.

**Example Request:**
```bash
curl -X GET https://api.pyramidswe.com/v1/students \
-H "Authorization: Bearer access_token"
```

---

### 2. Get Student by ID
**Endpoint:** `GET /student/{id}`

**Description:** Retrieves details of a specific student.

**Path Parameter:**
- `id` (string): Student ID.

**Response:**
```json
{
  "id": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "username": "string",
  "xp": "string"
}
```
- `200 OK`: Student retrieved successfully.

**Example Request:**
```bash
curl -X GET https://api.pyramidswe.com/v1/student/{id} \
-H "Authorization: Bearer access_token"
```

---

### 3. Delete Student
**Endpoint:** `DELETE /student/{id}`

**Description:** Deletes a student record.

**Path Parameter:**
- `id` (string): Student ID.

**Response:**
- `200 OK`: Student deleted successfully.
- `401 Unauthorized`: Action not permitted.

**Example Request:**
```bash
curl -X DELETE https://api.pyramidswe.com/v1/student/{id} \
-H "Authorization: Bearer access_token"
```

---

### 4. Update Student
**Endpoint:** `PATCH /student/{id}`

**Description:** Updates a student's information.

**Path Parameter:**
- `id` (string): Student ID.

**Request Body:**
Only send fields that require updates.
```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "username": "string",
  "xp": "string"
}
```
**Response:**
- `200 OK`: Student updated successfully.

**Example Request:**
```bash
curl -X PATCH https://api.pyramidswe.com/v1/student/{id} \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token" \
-d '{
  "first_name": "Jane",
  "last_name": "Doe"
}'
```

---

## Mentor Endpoints

### 1. Get All Mentors
**Endpoint:** `GET /mentors`

**Description:** Retrieves a list of all registered mentors.

**Response:**
```json
[
  {
    "id": "string",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "username": "string",
    "xp": "string"
  }
]
```
- `200 OK`: Mentors retrieved successfully.

**Example Request:**
```bash
curl -X GET https://api.pyramidswe.com/v1/mentors \
-H "Authorization: Bearer access_token"
```

---

### 2. Get Mentor by ID
**Endpoint:** `GET /mentor/{id}`

**Description:** Retrieves details of a specific mentor.

**Path Parameter:**
- `id` (string): Mentor ID.

**Response:**
```json
{
  "id": "string",
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "username": "string",
  "xp": "string"
}
```
- `200 OK`: Mentor retrieved successfully.

**Example Request:**
```bash
curl -X GET https://api.pyramidswe.com/v1/mentor/{id} \
-H "Authorization: Bearer access_token"
```

---

### 3. Delete Mentor
**Endpoint:** `DELETE /mentor/{id}`

**Description:** Deletes a mentor record.

**Path Parameter:**
- `id` (string): Mentor ID.

**Response:**
- `200 OK`: Mentor deleted successfully.
- `401 Unauthorized`: Action not permitted.

**Example Request:**
```bash
curl -X DELETE https://api.pyramidswe.com/v1/mentor/{id} \
-H "Authorization: Bearer access_token"
```

---

### 4. Update Mentor
**Endpoint:** `PATCH /mentor/{id}`

**Description:** Updates a mentor's information.

**Path Parameter:**
- `id` (string): Mentor ID.

**Request Body:**
Only send fields that require updates.
```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "username": "string",
  "xp": "string"
}
```
**Response:**
- `200 OK`: Mentor updated successfully.

**Example Request:**
```bash
curl -X PATCH https://api.pyramidswe.com/v1/mentor/{id} \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token" \
-d '{
  "first_name": "Jane",
  "last_name": "Doe"
}'
```

---

## Resource Endpoints

### Program, Course, Project, and Task
Each resource follows a similar structure with endpoints for CRUD operations:

**Endpoints:**
- `GET /{resource}`: Retrieves a specific resource by ID.
- `POST /{resource}`: Creates a new resource.
- `DELETE /{resource}`: Deletes a resource by ID.
- `PATCH /{resource}`: Updates a resource by ID.

**Example Resources:**
- **Program** (`/program`)
- **Course** (`/course`)
- **Project** (`/project`)
- **Task** (`/task`)

**Example Request:**
```bash
curl -X GET https://api.pyramidswe.com/v1/project/{id} \
-H "Authorization: Bearer access_token"
```

---

## Rate Limiting
The API supports up to 100 requests per minute per user. Exceeding this limit will result in a `429 Too Many Requests` response.

---

## Additional Endpoints

### Add Project to Student Collection
**Endpoint:** `POST /student/project/add`

**Description:** Adds a project to a student's collection as "pending."

**Request Body:**
```json
{
  "user_id": "string",
  "project_id": "string"
}
```
**Response:**
- `200 OK`: Project added successfully.

**Example Request:**
```bash
curl -X POST https://api.pyramidswe.com/v1/student/project/add \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token" \
-d '{
  "user_id": "123",
  "project_id": "456"
}'
```

---

### Submit Project
**Endpoint:** `POST /student/project/submit`

**Description:** Marks a project as "done."

**Request Body:**
```json
{
  "user_id": "string",
  "project_id": "string"
}
```
**Response:**
- `200 OK`: Project submitted successfully.

**Example Request:**
```bash
curl -X POST https://api.pyramidswe.com/v1/student/project/submit \
-H "Content-Type: application/json" \
-H "Authorization: Bearer access_token" \
-d '{
  "user_id": "123",
  "project_id": "456"
}'
```

---

## Error Codes
- `200 OK`: Successful operation.
- `201 Created`: Resource created successfully.
- `400 Bad Request`: Invalid request format.
- `401 Unauthorized`: Access denied.
- `404 Not Found`: Resource not found.
- `429 Too Many Requests`: Rate limit exceeded.

---

## How to Use
1. Base URL for all endpoints: `https://localhost.com/api/v1/`
2. Authenticate using `/auth/login` to obtain access and refresh tokens.
3. Use the provided tokens for secure access to other endpoints.
4. Adhere to the rate limit of 100 requests per minute.
5. Refer to specific endpoint descriptions for request and response formats.

---

## Notes
- Ensure proper authentication headers are included where required.
- Refer to error codes for troubleshooting issues.
- For additional details, contact the API support team.

---

## License
This API is licensed under [Your License Here].

