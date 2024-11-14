## Star Wars Characters

### Project Overview
The Star Wars Characters project required me to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. I used Node.js and the `request` module to fetch data from the Star Wars API and display character names.

### Requirements

- All files will be interpreted on Ubuntu 20.04 LTS using node (version 10.14.x)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- The code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All files must be executable
- The length of files will be tested using `wc`
- Not allowed to use `var`

#### Concepts Needed

1. **HTTP Requests in JavaScript**: 
   - Making HTTP requests using the `request` module (or alternatives like `fetch`).
   
2. **Working with APIs**:
   - Understanding RESTful APIs and parsing JSON data returned from APIs.
   
3. **Asynchronous Programming**:
   - Using callbacks, promises, and async/await to manage asynchronous operations.
   
4. **Command Line Arguments in Node.js**:
   - Using `process.argv` to handle command-line arguments.
   
5. **Array Manipulation and Iteration**:
   - Iterating over arrays and manipulating data structures.
#### Installation

1. Install Node.js 10.x:

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

2. Install semistandard for code formatting:

```bash
$ sudo npm install semistandard --global
```
3. Install request module to make HTTP requests:

```
$ sudo npm install request --global

$ export NODE_PATH=/usr/lib/node_modules
```

## Task: 0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID. Example: 3 = "Return of the Jedi"
Display one character name per line in the same order as the "characters" list in the /films/ endpoint
You must use the Star Wars API (https://swapi.dev/)
You must use the request module to fetch data


####  Example
```
./0-starwars_characters.js 3
```

Output:
```
Luke Skywalker

Han Solo

Leia Organa

...
```

Solution

1: Get the movie ID from the command-line argument (process.argv[2]).

2: Use ID to send a request to the Star Wars API and get data about the movie.

3: With the movie data, grab the list of characters (which are URLs).

4: For each character URL, send another request to get information about the character and print their name to the console
