# FastAPI and MongoDB Cookiecutter Template

A Cookiecutter template for FastAPI + MongoDB + Jinja2

# Quick Start

`create_env.sh` - create the venv
`start.sh` - start the server

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
Make sure to double check your `.env` file.

```
<project_name>/
├── LICENSE
├── .env
├── README.md
├── app.py
├── apprunner.yaml
├── cookiecutter.json
├── core
│   ├── __pycache__
│   ├── config.py
│   ├── emails.py
│   ├── files.py
│   ├── log.py
│   ├── models.py
│   ├── responses.py
│   ├── storage.py
│   └── utils.py
├── create_env.sh
├── requirements.txt
├── routers
│   ├── __init__.py
│   ├── __pycache__
│   ├── blog.py
│   ├── devops.py
│   ├── health.py
│   └── ui.py
├── scripts
│   └── seed_db.py
├── start.sh
├── static
│   ├── logo.png
│   └── style.css
├── templates
│   ├── blog.html
│   └── home.html
└── vercel.json
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
  - For customizations see `vercel.json`
- AWS AppRunner
  - For customizations see `apprunner.yaml`and this resource for more information: ()

# Roadmap

- Handling all lingering TOODs
- Fixing logging config
- Update `seed_db.py` to have Pydantic support
- Move collection names to config.py (and .env)
- Add Aggregation Pipeline endpoints