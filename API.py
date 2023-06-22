import requests
import shutil

class API_remove():

    def remove_background(image_path, api_key):
        # Create a temporary file path for the result image
        result_path = "result.png"

        # Send a POST request to the remove.bg API
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(image_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': api_key}
        )
        # Save the result image
        with open(result_path, 'wb') as f:
            f.write(response.content)

        return result_path

# Example usage
image_path = "static/person.jpeg"
api_key = "Vs5BJEfznmo4cdZ9cJP9EZ2M"
# result_image_path = API_remove.remove_background(image_path, api_key)

# Move or use the result image as needed
# shutil.move(result_image_path, "3.webp")