import wikipedia
import os
import sys
from testing import db_add

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'application_default_credentials.json'

def detect_logos2(path):
    url = "http://8.213.25.141/"+path
    db_add(url)
    from azure.cognitiveservices.vision.computervision import ComputerVisionClient
    from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
    from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
    from msrest.authentication import CognitiveServicesCredentials

    import os

    subscription_key = "f3f302f9162243f095d626b2b3abe506"
    endpoint = "https://logologo.cognitiveservices.azure.com/"

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")

    remote_image_features = [VisualFeatureTypes.categories,VisualFeatureTypes.brands,VisualFeatureTypes.adult,VisualFeatureTypes.color,VisualFeatureTypes.description,VisualFeatureTypes.faces,VisualFeatureTypes.image_type,VisualFeatureTypes.objects,VisualFeatureTypes.tags]

    tags_result_remote = computervision_client.analyze_image(url, remote_image_features)

    if (len(tags_result_remote.brands) == 0):
        return "No tags detected."
    else:
        for tag in tags_result_remote.brands:
            return tag.name

def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        return logo

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


path = "uploads/"+str(sys.argv[1])

from Size_Fixer import Fix_Image

Fix_Image(path)

#try:
#data = detect_logos(path)
#logo = data.description
logo = detect_logos2(path)
#except:
#    print("Error")
#    exit(0)

print(logo)

company = logo

print(company)

try:
    x = wikipedia.summary(company + " (company)", auto_suggest=True)
    print(x)
except:
    try:
        x = wikipedia.summary(company + " (company)", auto_suggest=False)
        print(x)
    except:
        try: 
            x = wikipedia.summary(company, auto_suggest=True)
            print(x)
        except:
            try:
                x = wikipedia.summary(company, auto_suggest=False)
                print(x)
            except:
                print("No page found")

exit(0)

from Make_Box import draw_rectangle

mnx = 0
mny = 0
mxx = 0
mxy = 0

if hasattr(data.bounding_poly.vertices[0],"x"):
    mnx = data.bounding_poly.vertices[0].x
    
if hasattr(data.bounding_poly.vertices[0],"y"):
    mny = data.bounding_poly.vertices[0].y
    
if hasattr(data.bounding_poly.vertices[2],"x"):
    mxx = data.bounding_poly.vertices[2].x
    
if hasattr(data.bounding_poly.vertices[2],"y"):
    mxy = data.bounding_poly.vertices[2].y

draw_rectangle(path, [mnx, mny], [mxx, mxy])

