## Matchmaking API minimal demo

## Intro
This demo showcases a simple flow to enqueue player to matchmaking, match suggestion
retrieval and match status updates. Submitting match results prints the updated
player stats including rating and ranking points.

For simplicity,this demo makes use of a python client generated from the OpenAPI
specs using the `openapi-python-client`. It relies on the REST API while we recommend
to use websockets for production settings. The following files are relevant:

- `config.py` contains the user credentials
- `main.py` contains an example flow for matchmaking

Remark: While the generated api client at `matchmaking_api_client` is production-ready,
however, the remaining scripts are for demonstration purposes only and are not
suitable for production use.

## Setup
Create and activate a virtual environment
```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Enter your credentials in `config.py`. You can retrieve them from https://console.idem.gg

## Running the demo

To run the demo, start `main.py` and follow the console output:
```shell
python main.py
```

## Contact
In case you have any questions, please let us know at match@idem.gg
