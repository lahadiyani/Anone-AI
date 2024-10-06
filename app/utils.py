import requests
import time

def query(api_url, headers, data, retries=3, delay=5):
    for attempt in range(retries):
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.content
        if response.status_code == 200 and "error" in response.json():
            error_message = response.json()["error"]
            if "is currently loading" in error_message:
                estimated_time = response.json().get("estimated_time", delay)
                print(f"Model is currently loading, retrying in {estimated_time:.2f} seconds...")
                time.sleep(estimated_time)
            else:
                break
        else:
            return None
            
    print("Model is still loading after retries.")
    return None
