# FastAPI CRUD Application with MongoDB and Kubernetes

This project consists of a FastAPI application that serves basic CRUD (Create, Read, Update, Delete) operations via HTTP requests. It uses MongoDB, a popular NoSQL database, to persist data. Additionally, it includes Dockerization of the FastAPI application and Kubernetes deployment manifests for both the MongoDB database and the FastAPI application.

## Getting Started

### Prerequisites

Before you can run and deploy this project, you need to have the following prerequisites installed:

- [Docker](https://www.docker.com/get-started)
- [Kubernetes](https://kubernetes.io/docs/setup/)
- [Kind](https://kind.sigs.k8s.io/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/)
- [MongoDB](https://www.mongodb.com/try/download/community)


### Installation
1. Clone this repository to your local machine, create cluster with Kind (Kind needs to be installed) and load images:

    ```bash
    kind create cluster
    kind load docker-image fast-api-backend:v1
    ```
2. When images are loaded, apply the manifest files in order below:

    ```bash
    kubectl apply -f <FILENAME>
    kubectl apply -f persistent-volume.yaml
    kubectl apply -f mongo.yaml
    kubectl apply -f fastapi.yaml
    ```
3. To interact with deployed services, you can use port-forwarding:

    ```bash
    kubectl port-forward service/fast-api-service 5000:5000
    kubectl port-forward service/mongo 31048:27017
    ```

4. You can run the following commands on your machine to persist the data on MongoDB, get information about the pods and delete cluster:

    ```bash
    docker run -d -p 27017:27017 -v ~/data:/data/db mongo
    kubectl get all
    kind delete cluster
    ```
    
## Usage

### FastAPI Application
The FastAPI application listens for HTTP requests and provides CRUD operations for two main entities: Course and Student. Here are the available routes:

Course:
- Create a new course:
    - Request: POST /courses
    - Request Body: CourseData
    - Response Body: { "message": "Course successfully created", "id": course_id }
    - Response Status Code: 201

- Read all courses (with optional query parameters for filtering):
    - Request: GET /courses
    - Response Body: Multiple database objects [Course]
    - Response Status Code: 200

- Read a single course by ID:
    - Request: GET /courses/{course_id}
    - Response Body: Single database object Course
    - Response Status Code: 200

- Update an existing course:
    - Request: PUT /courses/{course_id}
    - Request Body: CourseData
    - Response Body: { "message": "Course successfully updated" }
    - Response Status Code: 200

- Delete a course by ID:
    - Request: DELETE /courses/{course_id}
    - Response Body: { "message": "Course successfully deleted" }
    - Response Status Code: 200
      

Student:
- Create a new student:
    - Request: POST /students
    - Request Body: StudentData
    - Response Body: { "message": "Student successfully created", "id": student_id }
    - Response Status Code: 201

- Read a single student by ID:
    - Request: GET /students/{student_id}
    - Response Body: Single database object Student
    - Response Status Code: 200

- Update an existing student:
    - Request: PUT /students/{student_id}
    - Request Body: StudentData
    - Response Body: { "message": "Student successfully updated" }
    - Response Status Code: 200

- Delete a student by ID:
    - Request: DELETE /students/{student_id}
    - Response Body: { "message": "Student successfully deleted" }
    - Response Status Code: 200

### MongoDB

The FastAPI application uses MongoDB to store and retrieve data for courses and students. Ensure that you have a running MongoDB instance available as specified in the Kubernetes manifest.
