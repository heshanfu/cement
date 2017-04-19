---
weight: 1
title: Cement Framework
---

# Cement Framework v2.99.1

> Installation via PyPi (Stable)

```
$ pip install cement
```

> Hello World Example

```python
from cement import App

with App('myapp') as app:
    app.run()
    app.log.info('Hello World!')
```

> Usage

```
$ python helloworld.py --help
usage: helloworld [-h] [--debug] [--quiet]

optional arguments:
  -h, --help  show this help message and exit
  --debug     toggle debug output
  --quiet     suppress all output

$ python helloworld.py
INFO: Hello World!
```


<aside class="warning">
This is the Portland branch of Cement, intended for future-looking and
non-backward-compatible development.  It is a complete fork of Cement 2, and
will eventually become Cement 3.  It is guaranteed to be broken!  Please use
Cement 2 in production until stable/3.0.0 is released.
</aside>

Cement is an advanced CLI Application Framework for Python.  Its goal is to
introduce a standard, and feature-full platform for both simple and complex
command line applications as well as support rapid development needs without
sacrificing quality.  Cement is flexible, and it's use cases span from the
simplicity of a micro-framework to the complexity of a mega-framework.
Whether it's a single file script, or a multi-tier application, Cement is the
foundation you've been looking for.

The first commit to Git was on Dec 4, 2009.  Since then, the framework has
seen several iterations in design, and has continued to grow and improve
since it's inception.  Cement is the most stable, and complete framework for
command line and backend application development.

[![Continuous Integration Status](https://travis-ci.org/datafolklabs/cement.svg)](https://travis-ci.org/datafolklabs/cement) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/datafolklabs/cement?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Cement core features include (but are not limited to):

 * Core pieces of the framework are customizable via handlers/interfaces
 * Extension handler interface to easily extend framework functionality
 * Config handler supports parsing multiple config files into one config
 * Argument handler parses command line arguments and merges with config
 * Log handler supports console and file logging
 * Plugin handler provides an interface to easily extend your application
 * Hook support adds a bit of magic to apps and also ties into framework
 * Handler system connects implementation classes with Interfaces
 * Output handler interface renders return dictionaries to console
 * Cache handler interface adds caching support for improved performance
 * Controller handler supports sub-commands, and nested controllers
 * Zero external dependencies* (not including optional extensions)
 * 100% test coverage using `nose` and `coverage`
 * 100% PEP8 and style compliant using `flake8`
 * Extensive Sphinx documentation
 * Tested on Python 3.5+

<aside class="notice">
Some optional extensions that are shipped with the mainline Cement sources do
require external dependencies.  It is the responsibility of the application
developer to include these dependencies along with their application, as
Cement explicitly does not include them.
</aside>

**More Information**

 * DOCS: http://builtoncement.com/2.99/
 * CODE: http://github.com/datafolklabs/cement/
 * PYPI: http://pypi.python.org/pypi/cement/
 * SITE: http://builtoncement.com/
 * T-CI: https://travis-ci.org/datafolklabs/cement
 * HELP: cement@librelist.org - #cement - gitter.im/datafolklabs/cement


**License**

The Cement CLI Application Framework is Open Source and is distributed under
the BSD License (three clause).  Please see the LICENSE file included with
this software.
