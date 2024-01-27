# FastAPI and MongoDB Cookiecutter Template
 A Cookiecutter template for FastAPI + MongoDB + Jinja2

# How It Works

This Cookiecutter template allows you to quickly set up a FastAPI project with MongoDB as the database. Follow these steps to create a new project using this template.

## Prerequisites

Make sure you have the following prerequisites installed on your system:

- Cookiecutter - A command-line utility that creates projects from templates.

   ```
   pip3 install cookiecutter
   ```
   
- Git - Version control system.

   ```
   https://git-scm.com/
   ```

## Usage

1. Open your terminal or command prompt.

2. Use Cookiecutter to generate a new project from this template. Replace `[REPO]` with the actual GitHub repository link where this Cookiecutter template is hosted.

   ```
   cookiecutter [REPO]
   ```

   For example, if your template is hosted at `https://github.com/yourusername/your-fastapi-mongodb-template.git`, you would run:

   ```
   cookiecutter https://github.com/yourusername/your-fastapi-mongodb-template.git
   ```

3. Cookiecutter will prompt you for various project details, such as project name, author name, and other customizable variables. Provide the required information.

4. Once you've provided all the information, Cookiecutter will generate your FastAPI project using the template.

5. Change into the newly created project directory:

   ```
   cd <project_name>
   ```

6. You can now set up your virtual environment, install the project dependencies, and start developing your FastAPI application with MongoDB as the database. We've added helper scripts for this. 
   `create_env.sh` - to create the virtual environment
   `start.sh` - to start the Uvicorn server

## Project Structure

The generated project will typically have a structure similar to the following:

```
<project_name>/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   └── v2/
│   │       ├── __init__.py
│   │       └── main.py
│   ├── core/
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── main.py
│   └── settings.py
│
├── tests/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

This structure is designed to help you get started quickly with your FastAPI and MongoDB project.

## Customization

You can customize your FastAPI and MongoDB project further by modifying the generated code and configuration files as needed. Refer to the FastAPI documentation and MongoDB documentation for more information on how to work with these technologies.

## Contributors

Nelson Roque, PhD: `nelsonroquejr@gmail.com`

## License

This project is licensed under the MIT Licene - see the `LICENSE` file for details.

## Deployment Options

- Vercel
  - For customizations  see `vercel.json`
- AWS AppRunner 
  - For customizations  see `apprunner.yaml`and this resource for more information: ()

# Roadmap

   - Adding logguru