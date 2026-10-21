----------------------------------------------
PLANT identification using Web Service that 
invokes an images classification AI model 
trained on Flora
author: Hakim Mitiche, 
update: February 2026
----------------------------------------------

In this lab, we will call PL@NTNET API to 
identify some plants based on images 
we have in 'images/' folder

# Step 1: get an API token
open your Web browser and go to this website: 
https://my.plantnet.org/

sign up, then create a free token

# Step 2: store the API secret
open .env file and put your key like this:
PLANTNET_API_KEY="..."


You may want to read the API documentation here : 
https://my.plantnet.org/doc/api/openapi

Here the API url we use (in identify_plant.py):
url = "https://my-api.plantnet.org/v2/identify/all"

# Step 3: install required packages

open terminal and type:

python -m pip install -r requirements.txt

Notice that pip module should be installed first if it is missing, 
it is python packages manager.
Also, make sure all the required Python libraries are 
installed successfully! You may want to use a 
virtual environment to avoid installing packages 
that conflict with system Python

# Step 4: run the script 

python indentify_plant.py 

# Step 5: result interpretation

The screenshot image: plant_identify_screenshot.jpeg illustrates 
an identification done on image number 20: IMG_0791.jpeg, 
notice the low confidance, 

Answer the following questions: (as much as you can)

1- Can you tell why so? 
2- What can you conclude? 
 Is it epistemic or aleatoric uncertainty?
 What can you conclude?
3- Can you identify the plant knowing it's endemic to your region 
(the Algerian Steppe)?
4- Where is the ML classification model run?
5- Why do you need a secret key?
6- What is the type of the Web/cloud service?
7- Argue why calling the API is on-demand computing?
8- Modify the code to recuperate the 3 top predictions with confidance rate?
9- Use: 'inaturalist.org' and 'bioclip2-demo (on HF)', 
to reduce uncertainty with regard to identifying plant in image: IMG_0791.jpeg? 


# About the API

Pl@ntNet API provides a computational access to the visual identification engine used in Pl@ntNet apps in the form of a RESTful Web service. The service allows you to submit simultaneously from 1 to 5 images of the same plant and to have in return the list of the most likely species as well as a confidence score for each of them. The identification engine is based on most advanced deep learning technologies and is regularly updated thanks to the contributions of the community and the integration of new expert databases

Since we will identify local plants, it may be worth to know that 
the Northern Africa flora can identify 4,461 native species from 
this region.