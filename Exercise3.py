import requests
import json
import os

def task_1_append_logger():
    print("--- Task 1: Append Logger ---")
    note = input("Enter a note for the log: ")

    with open("session_log.txt", "a") as file:
        file.write(note + "\n")

    with open("session_log.txt", "r") as file:
        content = file.read()

    print("\nLog History:")
    print(content)

def task_2_word_count_utility():
    print("\n--- Task 2: Word Count Utility ---")
    text = "Knowledge is Power. Go Lightning! Python makes data easy."

    with open("lehman_motto.txt", "w") as file:
        file.write(text)

    with open("lehman_motto.txt", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

    print(content)

    print("\nWord Count:")
    print(word_count)

def task_3_api_status_checker():
    print("\n--- Task 3: API Status Checker ---")
    url = "https://jsonplaceholder.typicode.com/posts/101"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(response.json())
        elif response.status_code == 404:
            print("Error: Post not found.")

    except requests.exceptions.Timeout:
        print("Error: Timeout.")

def task_4_data_filtering():
    print("\n--- Task 4: Data Filtering ---")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    print("Users who live in a suite:\n")
    for user in users:
        if "Suite" in user["address"]["suite"]:
            print(user["name"])

def task_5_integration_report():
    print("\n--- Task 5: Integration Report ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()

    title = data["title"]
    body = data["body"]

    with open ("api_report.txt", "w") as file:
        file.write("Title: \n")
        file.write(title + "\n")
        file.write("Body:\n")
        file.write(body)

    print("Report Generated")


if __name__ == "__main__":
    # You can uncomment these as you complete them to test your code
     task_1_append_logger()
     task_2_word_count_utility()
     task_3_api_status_checker()
     task_4_data_filtering()
     task_5_integration_report()

