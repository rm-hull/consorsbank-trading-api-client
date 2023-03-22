# consorsbank-trading-api-client

Example python client for connecting to [Consors Bank](https://www.consorsbank.de/) Trading API

## Setup

If necessary, upgrade your version of `pip`:

```console
$ python -m pip install --upgrade pip
```

Create a virtualenv and install dependencies with:

```console
$ python -m venv .venv
$ pip install -r requirements.txt
```

### Regenerating gRPC code

This command will generate python client stubs:

```console
$ python -m grpc_tools.protoc -I./proto --python_out=./generated --pyi_out=./generated --grpc_python_out=./generated ./proto/*.proto
```

The generated code is checked in to git, so would only need to be regenerated if the .proto files were updated.

## Running the client

There are some configuration settings that need to be updated. Check the `.env` file and update
the `LOGIN_SECRET` and `GRPC_DEFAULT_SSL_ROOTS_FILE_PATH` values - you should be able to get the
values from the ActiveTrader app (look in the Java Documentation: there is a pdf explaining how
to do this).

Activate the virtual env:

```console
$ source .venv/bin/activate
$ python trading_client.py
```

If it works you should see:

```
INFO:root:Trying to connect to hostname: localhost:40443
INFO:root:Using credentials: <grpc.ChannelCredentials object at 0x7fb7d56452d0>
INFO:root:Access token received: xxxxxxxxxxx
```