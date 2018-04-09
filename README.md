# Universal Analytics for Python


This library provides a Python interface to Google Analytics, supporting the Universal Analytics Measurement Protocol, with an interface modeled (loosely) after Google's `analytics.js`.

| Service | Status |
| --- | --- |
| CircleCI | [![CircleCI](https://circleci.com/gh/lyndsysimon/universal-analytics-python.svg?style=svg)](https://circleci.com/gh/lyndsysimon/universal-analytics-python) |

# Usage

A simple example:

```python
from UniversalAnalytics import Tracker

tracker = Tracker.create('UA-XXXXX-Y', client_id = CUSTOMER_UNIQUE_ID)
tracker.send('event', 'Subscription', 'billing')
```

Please see the [test/test_everything.py](./test/test_everything.py) script for additional examples.

This library support the following tracking types, with corresponding (optional) arguments:

* pageview: [ page path ]
* event: category, action, [ label [, value ] ]
* social: network, action [, target ]
* timing: category, variable, time [, label ]

Additional tracking types supported with property dictionaries:

* transaction
* item
* screenview
* exception

Property dictionaries permit the same naming conventions given in the [analytics.js Field Reference](https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference), with the addition of common spelling variations, abbreviations, and hyphenated names (rather than camel-case).  These are also demonstrated in the [tests/main.py](./tests/main.py) file.

Further, the property dictionaries support names as per the [Measurement Protocol Parameter Reference](https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters), and properties/parameters can be passed as named arguments.

Example:

```python
  # as python named-arguments
  tracker.send('pageview', path = "/test", title = "Test page")

  # as property dictionary
  tracker.send('pageview', {
    'path': "/test",
    'title': "Test page"
  })
```

# Attribution

This package is a fork of a package by the same name by [Analytics Pros](https://github.com/analytics-pros/universal-analytics-python).

# License

universal-analytics-python is licensed under the [BSD license](./LICENSE)
