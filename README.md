# Specification

You should build a new API endpoint that allows an end user to:

- **Create** a new Dog model by making a `POST` to `/api/dogs`.
- **View** current dogs that have been saved to the server by making a `GET` to `/api/dogs`.
- **Get**, **modify**, or **delete** an existing Dog record by making a `GET`, `PUT`, or `DELETE` request (respectively) to `/api/dogs/<id>`, where `<id>` is the ID of the Dog record to be retrieved, modified, or deleted.

Since a Dog includes a foreign key to the breed, you also need to make the same type of endpoints for dog breeds at `/api/breeds/` and `/api/breeds/<id>`.

## Dog Model

A dog should contain the following fields:

- `name` (a character string)
- `age` (an integer)
- `breed` (a foreign key to the Breed Model)
- `gender` (a character string)
- `color` (a character string)
- `favorite_food` (a character string)
- `favorite_toy` (a character string)

## Breed Model

A breed should contain the following fields:

- `name` (a character string)
- `size` (a character string)  
  _Should accept: **Tiny**, **Small**, **Medium**, **Large**_
- `friendliness` (an integer field)  
  _Should accept values from **1** to **5**_
- `trainability` (an integer field)  
  _Should accept values from **1** to **5**_
- `shedding_amount` (an integer field)  
  _Should accept values from **1** to **5**_
- `exercise_needs` (an integer field)  
  _Should accept values from **1** to **5**_

# Todo List

To complete this task, do the following:

1. **Track all of your changes using GitHub.**  
   You can use the GitHub repository you used for the webservice lab.

2. **Add Dog and Breed models to `models.py`.**

3. **Migrate your database** to include tables for Dog and Breed.

4. **Add two class-based API view controllers for handling Dog REST endpoints** to `controllers.py`:

   - **DogDetail**  
     Should have three methods named `get`, `put`, `delete`.
   - **DogList**  
     Should have two methods named `get` and `post`.

   Refer to the [Django REST Framework Tutorial - Class-Based Views](http://www.django-rest-framework.org/tutorial/3-class-based-views/) for examples.

5. **Add two class-based API viewset controllers for handling Breed REST endpoints** to `controllers.py`:

   - **BreedDetail**  
     Should have three methods named `get`, `put`, `delete`.
   - **BreedList**  
     Should have two methods named `get` and `post`.

   Refer to the [Django REST Framework API Guide - Viewsets](https://www.django-rest-framework.org/api-guide/viewsets/) for examples.

6. **Add the appropriate URL patterns** to the `urls.py` file to accept all of the patterns and map them to the correct controller.

7. **Test your endpoints with Postman**, taking screenshots of each type of request. There should be **5 requests total for each type of model**, for a total of **10 tests and screenshots**:

   - `GET` (list) and `POST` to `/api/dogs/`
   - `GET`, `PUT`, `DELETE` to `/api/dogs/<id>`
   - `GET` (list) and `POST` to `/api/breeds/`
   - `GET`, `PUT`, `DELETE` to `/api/breeds/<id>`
