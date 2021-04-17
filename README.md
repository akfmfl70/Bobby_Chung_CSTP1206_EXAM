## Requirements

 - MVC
 - Match functionality from design
 - Works on 1080p screens

## Functionality
Please note that the functionality is what you will be graded on. This includes the UI and so it will be tested using 1080p screens. I am not expecting an exact match but it must look similar or better (this is subjective so check with me first).

For specifics the code has TODO comments throughout as a way to guide you to get to the solution. Follow these and you will be able to work through the exam without much difficulty.

You may use window alerts for all the popups to save time.

### Home Page
Pull data from the models and display a list of Alpacas.

#### Age <= 25 Button
When clicked the page displays all the alpacas that are younger than or equal to 25 and switches the text to Age > 25. On first launch it displays all the alpacas regardless of age.

#### Age > 25 Button
When clicked the page displays all the alpacas that are older than 25 and switches the text to Age <= 25. On first launch it displays all the alpacas regardless of age.

Hint: Use URL parameters!!

#### Search Button
When clicked execute JS that communicates with a back-end API endpoint that gets all Alpaca's that start with a certain word. You **must** provide the data from the front-end (it can come in any form) but the API must conform to the CRUD principles as explained in class. This does **not** mean that you get user from the input but you can do that if you like. Instead you are allowed to save time by hard-coding the data and sending that data when you click the button.

For example, you may send data such as Ph and this will return a list of alpacas whose names begin with Ph,
so Phil, Phineas, etc.

To verify this works, you may simply log the output in JS and as long as the output is present (from backend -> frontend), this will be marked as completed.

#### Images
Look at the data given in the Alpaca model and look at the images, see if you can find a pattern and use that to generate the file name dynamically. Once you have done that use that image to display the images on the page

#### Profile Button
The profile button opens the profile page for the specific user

### Profile Page
Pull data from the models and display the profile for the specific Alpaca that the user requested. If you did the home page correctly, you will be able to reuse most of that code to create this page (visually with data) with ease.

#### Home Button
Links back to the home page

#### Delete Button
When clicked executes JS that sends a request to the backend to an API endpoint that you created following
CRUD principles. The data may **not** be hardcoded for this button and requires you to send information for the relevant profile that is being viewed. You are **not** required to perform the delete operation completely as in remove the object from the data provided but rather simulate it.

This means that there should exist logs in the backend that show which profile is being deleted, and a log indicating the success of the deletion. The logic for the endpoint will be viewed to verify the completion of this.

Hint: Make sure you use the approriate CRUD request method and **only** send what is required (will make it easier to code + understand the flow)

#### Hello Button
When clicked opens a popup (window alert is sufficient to save time) that displays the contact information about the Alpaca.
You may create a back-end API endpoint that gives you the contact information for the specific Alpaca. This approach shares code with the create endpoint but obviously should use a different HTTP Method (CRUD). Another approach to perhaps save time and for simplicity may be to hide the data and ..... (That's all I will say for that ;))

In the end, make sure when I click Hello, it shows the users contact information in a popup manner.

#### Create Button
When clicked execute JS that communicates with a back-end API endpoint that creates an Alpaca. You **must** provide the data from the front-end (it can come in any form) but the API must conform to the CRUD principles as explained in class. This does **not** mean that you get user from the input but you can do that if you like. Instead you are allowed to save time by hard-coding the data and sending that data when you click the button.

Different from the Mock Exam, you must provide one detail from the current profile into the request. This means that when hardcoding the data leave a gap for data from the open profile. You may choose any field to make it easier for you. For example, if you choose the name field, you would send the current user profile's name in addition to your hardcoded data to create the alpaca.

Rough example JSON:
```
{
    [CHOSEN PROPERTY]: [INSERT THE VALUE HERE FROM THE PROFILE],
    bio: '',
    age: 21,
    ...
}
```

You would replace [CHOSEN PROPERTY] with name in my instance and on the right would replace [INSERT THE VALUE HERE FROM THE PROFILE] with the value from the opened profile.

To make sure the creation happens on the back-end make sure to print text to the console that displays some of the information sent (there is a comment in the code to show you where you may put this). Following the success of creation on the back-end through the API, make sure to display a message on the front-end saying

```
[NAME] was created successfully
```

Replace [NAME] accordingly using the data that you sent.

Hint: If you know how to do contact information, you can do this one!! ;)

Second option: You also have the option of getting user input and using that to get data to input into the JSON object, so if you feel that is better, you are allowed to do that.

## Base Grading (Rough)
As an estimate, getting all the UI done is 50% and the functionality is the other 50%.
Both pages are equal in value so getting one page done completely is worth around 50% too.

## Bonus (Side Quests)
### Home Page
#### Search Button
Adding an input to the search button will result in 1 bonus mark
Displaying the results of the search button using the API visually will result in 3 bonus marks (dynamic page search)

## Design
[Design](https://www.figma.com/file/U5cVLOdXkd3hrJ2PfUh9H0/Exam?node-id=0%3A1)

## Running

    python3 main.py

## Before You Start
1. Clone this project
2. Create a new project with the name FIRSTNAME_LASTNAME_CSTP1206_EXAM (Make sure it is empty)
3. Copy the git URL of the project but do **not** clone and make sure it is completely empty
4. In the terminal, change directory into the project folder.
5. Execute the following commands

```
rm -rf .git
git init
git add .
git commit -m "starting exam"
git branch -M main
git remote add origin [INSERT GIT URL FROM STEP 3]
git push -u origin main
```

Failure to name the git project correctly according to step 2 will result in a 10% penalty.