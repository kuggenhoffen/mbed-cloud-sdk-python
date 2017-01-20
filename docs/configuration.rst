Configuration
-------------

When instantiating a new API object it will look for configuration files on
your file system and environment variables.

In particular, it will look for the following files - listed in order:

- `/etc/mbed_cloud_config.json`
- `$HOME/.mbed_cloud_config.json`
- `$PWD/.mbed_cloud_config.json`
- `$MBED_CLOUD_SDK_CONFIG`
- Passed in as `dict` to API constructor

With priority given to last file/property. I.e. you can override the config
file in `/etc` by placing a local config file in the project directory or
passing it directly to the API object constructor.

Configuration parameters
========================

The following configuration parameters can/needs to be set:

- `api_key`: The API key created in https://portal.mbedcloud.com (Required)
- `host`: Override the default API host to use. Needs to be HTTPS. (Optional)

Example configuration file
==========================

This file can be placed in any of the locations listed above.

.. code-block:: text

  $ cat .mbed_cloud_config.json
  {
    "api_key": "ak_*********",
    "host": "https://custom-api.example.org"
  }

Passing in configuration parameters in constructor
==================================================

You can also override the configuration on a per-API basis.

.. code-block:: python

  >>> config = { "api_key": "ak_******", "host": "https://custom-api.example.org" }
  >>> api = AccessAPI(config)
