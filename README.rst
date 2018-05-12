Django-NextJS
~~~~~~~~~~~~~

Isomorphic UI Development with Decorator pattern for Django with:

- nextjs out of the box experience for frontend development,
- rendering of nextjs pages with context in Django with NextJS template engine.

For fun & profit

Run the example project
=======================

Run this commands as non root::

    git clone https://git.yourlabs.org/oss/djnext
    cd djnext
    pip install --user --editable .[dev]
    yarn install
    djnext watchstatic  # maintains nextjs pages/ directory for yarn dev
    yarn dev  # run localhost:3000
    djnext dev  # run localhost:8000

Choose NextJS page template in Django
=====================================

Example project lives in src/djnext_example, see ``src/djnext_example/artist/urls.py``::

    CreateView.as_view(
        model=Artist,
        fields=['name'],
        success_url=reverse_lazy('artist_list'),
        template_name='create.js',
    )

The template backend you added will make a request to the nextjs server you
have on port 3000 with yarn dev.

Watchstatic command
===================

Run your manage.py watchstatic or yourproject watchstatic if your project has an entrypoint.

This will watch static/ directories of all apps in INSTALLED_APPS, and build
static_root/ directory. Also, it creates a symlink from static_root/pages to
pages/, so that yarn dev will find it.

On port 8000 we don't yet have auto frontend code reload, but you have it on
port 3000 wit h watchstatic running at the same time.

Install in your project
=======================

Add to 'djnext' to INSTALLED_APPS, add ``dict(BACKEND='djnext.Backend')`` to TEMPLATES.

.. note:: To have the dev command, add crudlfap to INSTALLED_APPS.

With LOVE from POITOU CHARENTE

∞

About
=====

This project was made possible by Thomas Binetruy, frontend engineer.
