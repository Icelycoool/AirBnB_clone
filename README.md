# AirBnB clone

![alt text](header.png)

## The Console

The Console is a command-line tool designed to manage instances of various classes representing entities in an Airbnb-like system. This project is part of a AirBnB Clone and is a foundational exercise
in creating and managing objects, implementing command-line interfaces, and handling basic storage operations.

### Features

- Command-Line Interface: Interact with the system via a command-line interface.
- CRUD Operations: Create, read, update, and delete instances of various classes.
- Dynamic Class Management: Manage instances of BaseModel, User, State, City, Amenity, Place, and Review.
- Persistent Storage: Save and retrieve instances using an in-memory storage system.
- Error Handling: Handle error and guide user in proper usage.

### Usage

To start the command-line interface, run the following command:

`./console.py`

You should see the prompt (hbnb). You can now enter commands to interact with the system.

### Commands

1. Create `create <class_name>`

   Creates a new instance of the specified class and prints its ID.

   Example: `create User`

2. Show `show <class_name> <id> `

   Displays the string representation of the instance with the given class name and ID.

   Example: `show User 2dbfbb0c-41c6-4555-8924-07682fef7e33`

3. Destroy `destroy <class_name> <id>`

   Deletes the instance with the specified class name and ID.

   Example: `destroy User 2dbfbb0c-41c6-4555-8924-07682fef7e33`

4. All `all [<class_name>]`

   Displays string representations of all instances or all instances of a specific class if a class name is provided.

   Example: `all` or `all User`

5. Update `update <class_name> <id> <attribute_name> <attribute_value>`

   Updates the specified attribute of an instance with the given class name and ID.

   Example: `update User 2dbfbb0c-41c6-4555-8924-07682fef7e33 first_name "John"`

6. Help help `[<commands]`

   Displays a list of available commands or detailed help for a specific command.

   Example: `help` or `help update`

7. Quit `quit`

   Exits the command interpreter.

   Example: `quit`

### Feedback and Suggestions

if there is something that can be improved or be done better. Be Sure to let me know. All your suggestions are welcome. Email: mohammedcali350@gmail.com
