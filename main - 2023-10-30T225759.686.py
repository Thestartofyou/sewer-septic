import requests

# Define your GIS API endpoint and parameters
gis_api_url = "https://your-gis-api-url.com/properties"
api_key = "your_api_key"  # Replace with your API key if required
location = "Your Location"  # Replace with the location you want to query

# Define the parameters for your query (if applicable)
params = {
    "location": location,
    # Add any other necessary parameters here
}

# Set up headers (if an API key is required)
headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    # Make the API request
    response = requests.get(gis_api_url, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Process the data to identify properties that need sewer and septic
        sewer_properties = []
        septic_properties = []

        for property in data['properties']:
            if property['requires_sewer']:
                sewer_properties.append(property)
            elif property['requires_septic']:
                septic_properties.append(property)

        # Print the results
        print("Properties that require sewer:")
        for property in sewer_properties:
            print(property)

        print("\nProperties that require septic:")
        for property in septic_properties:
            print(property)

    else:
        print(f"API request failed with status code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {str(e)}")
