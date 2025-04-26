from prefect import flow

@flow(log_prints=True)
def my_flow():
    raise Exception("test")
    print("Goodbye, world!")

if __name__ == "__main__":
    my_flow()
