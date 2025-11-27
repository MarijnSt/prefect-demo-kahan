# Prefect demo

This repository follows this [demo](https://www.youtube.com/watch?v=D5DhwVNHWeU)

## 1. Create venv

```bash
python -m venv venv
source venv/bin/activate
```

## 2. Install prefect

```bash
pip install -U prefect
```
`-U` is the same as using `--ugrade` to install the newest version available.

Test installation is successful:
```bash
prefect version
```

Start local prefect server
```bash
prefect server start
```

## 3. Create a flow and task

```python
from prefect import flow, task

@task
def create_message():
    msg = "Hello world!"
    return msg

@flow
def hello_world():
    msg = create_message()
    print(msg)

hello_world()
```
* Flows: bigger concepts to string together
* Tasks: smaller unit of work within a flow

## 4. Create subflow
```python
# ...

@flow
def something_else():
    result = 10
    return result

@flow
def hello_world():
    sub = something_else()
    msg = create_message()
    new_msg = msg + str(sub)
    print(new_msg)

# ...
```

## 5. Create a deployment

```bash
prefect deploy
```

This will start an interactive process in the terminal to create a deployment. For the demo I used:
* `hello_word()` as flow entrypoint
* Set `demo-deployment` as the name
* Created `pool-demo`as work pool
* Picked the `process` infrastructure
* No remote storage location
* No schedule
* Saved configuration in a [prefect.yaml](./prefect.yaml) file

```bash
prefect deploy -n demo-deployment # deploy using this config
```

## 6. Worker

To run a deployment we need to start a worker
```bash
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api # set api url
prefect worker start --pool "pool-demo"
```

We're now ready to run the deployment!
```bash
prefect deployment run 'hello-world/demo-deployment' # schedule a run for this deployment
```