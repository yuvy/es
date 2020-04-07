# es

cd to directory

```python
python3 es.py num_of_data True(To create es_data.json file)
eg: python3 es.py 100 True
```

use as lib

```python
from es import generate_es_data
d = generate_es_data(doc_len=100, add_to_file=True)
```
