SetUp Instructions:
1. Activate the virtual environment:
source homework2_env/bin/activate

2. Navigate to the project directory:
cd cs4300/homework2/movie_theater_booking

3. Start the server:
python3 manage.py runserver 0.0.0.0:3000

4. Open the app:
Click the APP button in DevEdu or open the URL in your browser:
https://editor-cs5300-21.devedu.io

Logging In:
You will be prompted with a login screen. Use the following credentials:
Username: THastings
Password: password1

Using the App:
Once logged in you will see the movie listing page with all previously added movies.
Book Now — Click on any movie to view available seats and book one
My Booking History — View all seats you have booked
Movie Theater (top left) — Always takes you back to the movie listing page
Add Movies — Takes you to the Django admin panel where you can manage:
Movies, Seats, and Bookings
Users and Groups with specefic admin permissions for specific users
To return from admin — Simply delete /admin/ from the browser URL
Logout — Click the Logout button in the top right corner when done

Adding New Users:
To create a new user from the terminal:
python3 manage.py createsuperuser
You will be prompted for a Username, Email, and Password. 
You can also create and manage users directly through the admin panel and hand out login credentials as needed.



AI Usage Citation
Tool Used: Claude.ai (Anthropic)

(tests.py)- Claude helped come up with some ideas for what 
specefic things I should test for since last homework I did 
not write enough tests I wanted to make sure I was bringing 
everything into account.

(features/steps/steps.py)- Claude helped clarify and clean 
up step definitions to properly match the feature file scenarios.

Claude helped implement Django's built-in login system and 
the @login_required decorator on the confirm_booking view.

Claude assisted with debugging various errors throughout 
development including import errors, URL configuration 
issues, and test failures.

(settings.py): Claude helped fix settings required for 
deployment including STATIC_ROOT, ALLOWED_HOSTS, and
CSRF_TRUSTED_ORIGINS

Claude walked through the full Render deployment process 
including setting up build.sh, requirements.txt, and 
configuring the web service settings since I found the
render doc quite confusing.