# DocCollect

## Instructions

### Conda Environment

All the project's dependencies are listed in the `environment.yml` file.
The easiest way to replicate the environment is using conda:

    conda env create --file environment.yml

This will create a conda environment called `dc` (for DocCollect).
To activate the environment:

    conda activate dc

And to deactivate it when we're done:

    conda deactivate

### Create Database

    python manage.py makemigrations
    python manage.py migrate

### Create Superuser

    python manage.py createsuperuser

### Launch Server

    python manage.py runserver
