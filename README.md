# kintone for Python

## Notice

This project is still under development. The APIs may change without notice.

## Overview

`kintone` is a Python package that provides a client to access [kintone](https://kintone.cybozu.co.jp/). It is inspired
by
the [kintone ruby gem](https://github.com/jue58/kintone).

## Requirements

- Python 3.7 or higher

## Installation

You can install the `kintone` package using pip:

```bash
pip install kintone
```

## Usage

```python
from kintone import Kintone

# Use password authentication
kintone = Kintone(
    domain='example.cybozu.com',
    user='username',
    password='password',
)

# Use token authentication
kintone = Kintone(
    domain='example.cybozu.com',
    token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
)

# or multiple tokens
kintone = Kintone(
    domain='example.cybozu.com',
    token=[
        'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',
    ],
)
```

### Supported APIs

- [Record retrieval](#record_retrieval)
- [Space management](#space_management)
- [Application information](#application_information)
- [Form structure](#form_structure)

### <a name="record_retrieval">Record retrieval</a>

```python
# Record retrieval(Assign by Record Number)
app_id = 1
record_id = 1
kintone.record.get(app=app_id, record_id=record_id)

# Records retrieval(Assign by Conditions by Query Strings)
app_id = 1
fields = ['record_id', 'title']
query = 'created_time > "2020-01-01T00:00:00+09:00"'
kintone.records.get(app=app_id, query=query, fields=fields)
```

### <a name="space_management">Space Management</a>

```python
# Get space information
space_id = 1
kintone.space.get(space_id=space_id)
```

### <a name="application_information">Application Information</a>

```python
# Get application information
app_id = 1
kintone.app.get(app_id=app_id)
```

### <a name="form_structure">Form Structure</a>

```python
# Get form structure
app_id = 1
kintone.form.get(app_id=app_id)
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request, or open an issue for discussion. Make
sure to follow the general coding standards and guidelines.

## Contact

For any questions, feedback, or support, please contact:

- **Masahiro Nishimi(@mah_lab)**: [Twitter Profile](https://twitter.com/mah_lab)
