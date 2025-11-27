from prefect import flow, task

@task
def create_message():
    msg = "Hello world!"
    return msg

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

if __name__ == "_main":
    hello_world()