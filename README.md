# Web Applicatoin for [MentorPhilly](www.mentorphilly.com)


## Getting Started
The project currently uses the python-base Django web framework. 
We recommended installing the latest version of [anaconda](https://www.anaconda.com/download/)
and using conda environments for package management.

Create a fresh environment for the project

```
conda create -n mentorphilly
source activate mentorphilly
```

Next, clone the repository and use the provided requirements.txt file to install the necessary
dependencies.

```
git clone https://github.com/zduey/mentorphl.git
pip install -r requirements.txt
```

The first time you run the website locally, you will need to prepare the database tables:

```
python manage.py migrate
```

Now (and all subsequent timess), you can run the webserver locally:

```
python manage.py runserver
```

By default, the website will start serving on port 8000. Navigate to localhost:8000 in your
favorite browser and play around.

