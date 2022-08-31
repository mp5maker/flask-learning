# Flask Learning

```bash
python3
from app import db
db.create_all()
```

### Query Params
<!-- example.com?language=value1&arg2=value2 -->

```python
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')
```


### Request Body


```python
request_data = request.get_json()
```



### Route Params

```python
@app.route("/data/<section>")
def data(section):
    assert section == request.view_args['section']
```