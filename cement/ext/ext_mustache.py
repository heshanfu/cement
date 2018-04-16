"""
The Mustache Extension provides output and file templating based on the
`Mustache Templating Language <http://mustache.github.com>`_.

Requirements
------------

 * pystache (``pip install pystache``)


Configuration
-------------

To **prepend** a directory to the ``template_dirs`` list defined by the
application/developer, an end-user can add the configuration option
``template_dir`` to their application configuration file under the main
config section:

.. code-block:: text

    [myapp]
    template_dir = /path/to/my/templates


Example
-------

**Output Handler**

.. code-block:: python

    from cement import App

    class MyApp(App):
        class Meta:
            label = 'myapp'
            extensions = ['mustache']
            output_handler = 'mustache'
            template_module = 'myapp.templates'
            template_dirs = [
                '~/.myapp/templates',
                '/usr/lib/myapp/templates',
                ]
    # ...

Note that the above ``template_module`` and ``template_dirs`` are the
auto-defined defaults but are added here for clarity.  From here, you
would then put a Mustache template file in
``myapp/templates/my_template.mustache`` or
``/usr/lib/myapp/templates/my_template.mustache`` and then render a data
dictionary with it:

.. code-block:: python

    app.render(some_data_dict, 'my_template.mustache')


**Template Handler**

.. code-block:: python

    from cement import App

    class MyApp(App):
        class Meta:
            label = 'myapp'
            extensions = ['mustache']
            template_handler = 'mustache'

    with MyApp() as app:
        app.run()

        # create some data
        data = dict(foo='bar')

        # copy a source template directory to destination
        app.template.copy('/path/to/source/', '/path/to/destination/', data)

        # render any content as a template
        app.template.render('foo -> {{ foo }}', data)


Loading Partials
----------------

Mustache supports ``partials``, or in other words template ``includes``.
These are also loaded by the output handler, but require a full file name.
The partials will be loaded in the same way as the base templates

For example:

**templates/base.mustache**

.. code-block:: console

    Inside base.mustache
    {{> partial.mustache}}


**template/partial.mustache**

.. code-block:: console

    Inside partial.mustache


Would output:

.. code-block:: console

    Inside base.mustache
    Inside partial.mustache

"""

from pystache.renderer import Renderer
from ..core.output import OutputHandler
from ..core.template import TemplateHandler
from ..utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class PartialsLoader(object):

    def __init__(self, handler):
        self.handler = handler

    def get(self, template):
        content, _type, _path = self.handler.load(template)
        return content


class MustacheOutputHandler(OutputHandler):

    """
    This class implements the :ref:`Output <cement.core.output>` Handler
    interface.  It provides text output from template and uses the
    `Mustache Templating Language <http://mustache.github.com>`_.  Please
    see the developer documentation on
    :cement:`Output Handling <dev/output>`.

    **Note** This extension has an external dependency on ``pystache``.  You
    must include ``pystache`` in your applications dependencies as Cement
    explicitly does **not** include external dependencies for optional
    extensions.
    """

    class Meta:

        """Handler meta-data."""

        label = 'mustache'

        #: Whether or not to include ``mustache`` as an available to choice
        #: to override the ``output_handler`` via command line options.
        overridable = False

    def __init__(self, *args, **kw):
        super(MustacheOutputHandler, self).__init__(*args, **kw)
        # self._partials_loader = PartialsLoader(self)
        self.templater = None

    def _setup(self, app):
        super(MustacheOutputHandler, self)._setup(app)
        self.templater = self.app.handler.resolve('template', 'mustache',
                                                  setup=True)

    def render(self, data, template=None, **kw):
        """
        Take a data dictionary and render it using the given template file.
        Additional keyword arguments passed to ``stache.render()``.

        Args:
            data (dict): The data dictionary to render.

        Keyword Args:
            template (str): The path to the template, after the
                ``template_module`` or ``template_dirs`` prefix as defined in
                the application.

        Returns:
            str: The rendered template text

        """

        LOG.debug("rendering output using '%s' as a template." % template)
        content, _type, _path = self.templater.load(template)
        return self.templater.render(content, data)


class MustacheTemplateHandler(TemplateHandler):

    """
    This class implements the :ref:`Template <cement.core.template>` Handler
    interface.  It renderd content as template, and supports copying entire
    source template directories using the
    `Mustache Templating Language <http://mustache.github.com>`_.  Please
    see the developer documentation on
    :cement:`Template Handling <dev/template>`.

    **Note** This extension has an external dependency on ``pystache``.  You
    must include ``pystache`` in your applications dependencies as Cement
    explicitly does **not** include external dependencies for optional
    extensions.
    """

    class Meta:

        """Handler meta-data."""

        label = 'mustache'

    def __init__(self, *args, **kw):
        super(MustacheTemplateHandler, self).__init__(*args, **kw)
        self._partials_loader = PartialsLoader(self)

    def render(self, content, data):
        """
        Render the given ``content`` as template with the ``data`` dictionary.

        Args:
            content (str): The template content to render.
            data (dict): The data dictionary to render.

        Returns:
            str: The rendered template text

        """

        stache = Renderer(partials=self._partials_loader)
        return stache.render(content, data)


def load(app):
    app.handler.register(MustacheOutputHandler)
    app.handler.register(MustacheTemplateHandler)
