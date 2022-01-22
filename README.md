<p align="center">
  <a href="https://getfalafel.github.io/docs/" target="_blank">
    <img src="https://raw.githubusercontent.com/getfalafel/art/main/logo/png/large-329%E2%80%8A%C3%97%E2%80%8A66.png" width="300">
  </a>
</p>

## About Fava CLI

Fava is the command-line interface (CLI) for Falafel, amd the CLI provides a number of helpful commands that can assist you while you build your application.  
Fava is a standalone Python package, but it is designed as a main dependency of Falafel. 
Its functionality depends on the Falafel base project and it isn't recommended to run just Fava without Falafel files.  

To view a list of all available Fava commands, you may use the list command:

```
fava -h
```

### Installation
You can install the Fava with PIP package manager.  
```
pip install fava
```

### Usage
Fava allows you to interact with your Falafel application in a development environment.   
With the CLI it is possible to create migrations, models, routes, controllers, run the development server and other features.

#### Check de commands: 
**Run the development server:**   
```
fava --server (port)
```

**Create a new migration file:**   
```
fava --make_migration create_user
```

**Create a new database model file:**
```
fava --make_model user
```

**Create a new controller file:**   
```
fava --make_controller user
```

**Create a new Route file:**
```
fava --make_route user
```

**Run all migrations or only one:**
```
fava --db_migrate (migration_name)
```

**Generate APP Key:**
```
fava --generate_key
```

You can find more documentation on the project website:   
[Falafel Docs](https://getfalafel.github.io/docs/en/)