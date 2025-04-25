# jam-quest

## Description

Solve a puzzle or a riddle to gain mutually exclusive access to a shared spotify queue inspired by mobile game spaceteam

## Installation

In order for your application to interface with the spotify api, you will need to log into your spotify account through the [spotify developer site](https://developer.spotify.com/). From there, you will need to create a new app by clicking on your profile in the top right-hand corner and then dashboard->create app. Fill out the information, setting the callback uri to \[BACKEND URL\]/callback and selecting the "Web API" option at the bottom. 

After creating the app, copy the client id from the basic information page into `jam-quest-api/.env` as `CLIENT_ID=[CLIENT ID]`. Additionally, click "View client secret" and copy that into the same .env file as `CLIENT_SC=[CLIENT SECRET]`.

Then run the following command: `pip install -r jam-quest-api/requirements.txt`

## Usage

``` Bash
# Start backend
python jam-quest-api/main.py

# Start frontend
cd jam-quest-ui && npm run dev && cd ..
```

## To-Do
- [ ] Backend code cleanup
- [x] Integrate MongoDB
- [ ] Frontend code cleanup
- [ ] Dockerize
- [x] Confirm sessions work as intended