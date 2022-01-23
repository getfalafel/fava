<p align="center">
  <a href="https://getfalafel.github.io/docs/" target="_blank">
    <img src="https://raw.githubusercontent.com/getfalafel/art/main/logo/png/large-329%E2%80%8A%C3%97%E2%80%8A66.png" width="300">
  </a>
</p>

## What kind of food is Falafel?
Falafel is a web development framework that bundles libraries and tools, providing an elegant and satisfying web development experience. We believe that there is no need to feel pain when developing software, whether it's a "warp engine" or a web page.
Falafel isn't a new independent or "alien" web Framework. It's just a web framework that provides a standard project with MVC concepts, and a collection of facilities for your web Python project.    
More here: [Falafel](https://getfalafel.github.io/docs/en/welcome-to-falafel/about-the-falafel/)

## About Fava CLI

Fava is the command-line interface (CLI) for Falafel, and the CLI provides several useful commands that can help you as you build your app.    
Fava is a standalone Python package, but it was designed as a main dependency of Falafel. Its functionality depends on the base Falafel project and it isn't recommended to run just Fava without Falafel files.    

Fava, our CLI provides tools to facilitate your application development. With Fava you can interact with your favorite database engine, generating migrations, models, and seeds. It is also possible to create routes, controllers and other functionality.    

Fava is a good friend! :)     

To view a list of all available Fava commands, you may use the list command:

```
fava -h
```

### Installation
You can install the Fava with PIP package manager.  
```
pip install falafel-fava
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