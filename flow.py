from prefect import flow

@flow(log_prints=True)
def my_flow():
    print("Hello again and again, world!")

if __name__ == "__main__":
    my_flow()
