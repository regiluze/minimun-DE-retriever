# minimun-DE-retriever
A simple REST API to calculate the minumun devops engineer needed to to call in in addition to the devops manager in order to maintain all servers in all currently active datacenters.

## Dev environment set up

### create virtual environment

```shellscript
mkvirtualenv -p /usr/local/bin/python3.5 minumum-DE-retriever
```

### setup virtual environment

```shellscript
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Run tests

### Run all tests

```shellscript
./dev/all_tests.sh
```
### Run unit tests

```shellscript
./dev/unit_tests.sh
```
### Run acceptance tests

```shellscript
./dev/acceptance_tests.sh
```

## Example
```shellscript
curl -X PUT \                                                                                                            ◼
  'http://localhost:5000/de-minumum-retriever' \
  -H 'Content-Type: application/json' \
  -d '{"DE_capacity":7, "DM_capacity": 5, "data_centers": [{"name": "Paris", "servers": 23}]}'
```
