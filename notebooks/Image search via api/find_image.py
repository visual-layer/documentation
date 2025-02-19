import requests
import sys

# Define the URL
url = "https://app.visual-layer.com/api/v1/dataset/2348e2ec-860c-11ef-968d-76f1445e4fca/search-image-similarity"

# Define parameters
params = {
    'entity_type': 'IMAGES',
    'bounding_box': '0,0,2048,1536',
}

# Define the image file path
image_path = "image_file.jpg"  # Update with your actual image path

# Open the image file in binary mode
with open(image_path, 'rb') as image_file:
    files = {'file': ('image_file.jpg', image_file, 'image/jpeg')}
    
    # Send the POST request
    response = requests.post(url, files=files, params=params)

# Print the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
    sys.exit(1)

create_embedding_res = response.json()
anchor_media_id = create_embedding_res["anchor_media_id"]
anchor_type = create_embedding_res["anchor_type"]

url2 = "https://app.visual-layer.com/api/v1/explore/2348e2ec-860c-11ef-968d-76f1445e4fca"

params2 = {
   'anchor_media_id': anchor_media_id,
   "entity_type": "IMAGES",
   "anchor_type": anchor_type,
   "threshold": '0'
}

# Send the GET request
response2 = requests.get(url2, params=params2)

# Print the response
if response2.status_code == 200:
    print("Response:", response2.json())
else:
    print(f"Error: {response2.status_code} - {response2.text}")
    sys.exit(1)
explore_res = response2.json()
clusters = explore_res["clusters"]
