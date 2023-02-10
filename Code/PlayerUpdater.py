import csv
import requests
import requests_mock
import random
import uuid
import argparse

fake_response_200 = {
    "statusCode": 200,
    "x-client-id": "required",
    "x-authentication-token": "required",
    "profile": {
        "applications": [
            {
                "applicationId": "music_app",
                "version": "v1.4.10"
            },
            {
                "applicationId": "diagnostic_app",
                "version": "v1.2.6"
            },
            {
                "applicationId": "settings_app",
                "version": "v1.1.5"
            }
        ]
    }
}
fake_response_401 = {
    "statusCode": 401,
    "error": "Unauthorized",
    "message": "invalid clientId or token supplied"
}
fake_response_404 = {
    "statusCode": 404,
    "error": "Not Found",
    "message": "profile of client 823f3161ae4f4495bf0a90c00a7dfbff does not exist"
}
fake_response_409 = {
    "statusCode": 409,
    "error": "Conflict",
    "message": "child \"profile\" fails because [child \"applications\" fails because [\"applications\" is required]]"
}
fake_response_500 = {
    "statusCode": 500,
    "error": "Internal Server Error",
    "message": "An internal server error occurred"
}
fake_responses = [fake_response_200, fake_response_401, fake_response_404, fake_response_409, fake_response_500]
fake_response = fake_response_200;
def generate_fake_id():
    return str(uuid.uuid4())
def update_music_player(mac_address, client_id, auth_token):
    # If that was a real tool and not a test
    # Your code to update the music player using the API would be here
    # For now we just send a fake response

    # Use the requests-mock library to simulate the API call
    with requests_mock.Mocker() as m:
        fake_response = random.choice(fake_responses)
        # Specify the API endpoint
        url = "https://api.example.com/profiles/"+client_id+":"+mac_address
        #add client_id and auth_token if needed
        if "x-client-id" in fake_response:
            fake_response["x-client-id"] = client_id;
        if "x-authentication-token" in fake_response:
            fake_response["x-authentication-token"] = auth_token;
        print(url)
        print(fake_response);
        # Specify the fake response to return
        m.put(url, json=fake_response, status_code=fake_response["statusCode"])

        # Make the fake API call
        response = requests.put(url, json=fake_response)

        # Verify the response
        assert response.status_code == fake_response["statusCode"]
        assert response.json() == fake_response

    return response

def main():
    # Use argparse to parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The name of the .csv file containing the music players")
    args = parser.parse_args()
    # Read the .csv file
    with open(args.filename) as file:
        reader = csv.reader(file)
        next(reader) # skip the header row
        for row in reader:
            mac_address = row[0]
            # Use the function to generate a fake client_id and auth_token
            client_id = generate_fake_id()
            auth_token = generate_fake_id()
            response = update_music_player(mac_address, client_id, auth_token)
            print(response)

if __name__ == "__main__":
    main()
