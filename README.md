# Mahsoub
## Mohammad Mostafa Elkhiat
27.10.2024
Alx SWE (Backend Specializations)


### Overview
* Mahsoub is your Gym Pal, the one doing all the calculations for you to know 	where you left last time and where to start this time.
* Using Mahsoub guarantees for you to always break your record successfully 	with more loads or more counts all together.
* The secret behind the name which isn’t a secret if you are Arabic is the 	meaning of Mahsoub in English is Calculated, and that’s the whole idea, to 	calculate everything for you.


### Goals
1. To give the user the ability to modify everything himself, from puttin
in 	the exercise name, the counts he did, the time he take doing, an
the weight 	he used
2. Also mainly he should have access to all his exercising history to kee
up 	with his record


### Specifications
1. Database Design
	* User Profiles: Track users' information and preferences.
	* Exercises: Store exercise names, descriptions, and any preset or user-customized categories.
	* Workout Sessions: Include data like exercise name, repetitions, sets, 	weight, and duration.
	* Progress Tracking: Track each user's exercise history to allow for 	comparisons and trend analysis over time.

2. API Endpoints
	You’ll likely be creating RESTful APIs (or maybe GraphQL if that's 	preferred) to manage user actions. Some potential endpoints:
	* POST /exercise: To add or edit exercise details.
	* POST /workout-session: To log a workout session with data on reps, weight, 	etc.
	* GET /history: To fetch the user's workout history and progress records.
	* PUT /settings: To allow users to modify exercise names or any personal 	settings.

3. Calculations and Progress Analysis
	* Since "Mahsoub" means calculated, adding features to measure progress, 	suggest improvements, or track personal bests would be great.
	* Consider implementing logic to calculate improvements from past workouts (e.	g., increase in weight lifted, or time reduced).

4. User Authentication and Authorization
	* Enable secure login and sign-up, perhaps with JWT (JSON Web Tokens) for 	session management.
	* Implement role-based access control if needed (e.g., admin to manage 	exercises or users).

5. Data Validation & Error Handling
	* Validate inputs (like numbers for weights and repetitions) to ensure data 	integrity.
	* Set up comprehensive error handling to manage potential issues with invalid 	entries or system errors.

6. Data Security and Privacy
	* Since this involves personal health information, security is a must. 	Implement HTTPS, encrypt sensitive data, and apply best practices for API 	security.
	* Ensure user privacy by carefully managing how data is stored and accessed.


### Stack & Tools
* Database: A relational database like PostgreSQL or MySQL is a good choice 	since you’ll have structured data.

* Backend Framework: Express (Node.js), Django (Python), or Flask could work 	well, depending on your familiarity.

* Auth & Security: Use libraries like JWT for tokens, bcrypt for password 	hashing, and libraries like Passport (for Node.js) to handle authentication 	flows.


### Planning Development Workflow
1. Set Milestones https://trello.com/c/K7edNsW9
	* Start with setting up the user profile and basic CRUD operations for 	workouts.
	* Gradually add more complexity, such as calculations for progress tracking.
2. Version Control
	* Make use of Git for version control to ensure smooth collaboration and easy 	rollback in case of errors.
3. Testing
	* Write tests for each endpoint and major function to make sure your code 	works as expected.
