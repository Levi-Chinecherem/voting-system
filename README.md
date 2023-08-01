
# Automated/Web-Based Voting System

The Voting System is a web-based application built with Django that allows users to vote for their preferred candidates based on different positions. The system provides a user-friendly interface for voting, displaying candidate details, and presenting the voting results.

![sample image](https://github.com/Levi-Chinecherem/voting-system/blob/master/sample.PNG)

## Features

- User Registration and Authentication: Users can sign up and log in to access the voting system.
- Candidate Management: Administrators can add, edit, and remove candidates for different positions.
- Position Management: Administrators can add and manage different voting positions with specific start and end dates for voting.
- Voting Timer: Users can only vote during the specified voting period for each position.
- One Vote Per User: Users can vote for candidates in each position only once.
- Voting Results: The system displays real-time voting results and percentage of votes for each candidate.

## Installation

Follow these steps to set up the Voting System on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/voting-system.git
   cd voting-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin) to manage the system:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the Voting System in your web browser at `http://localhost:8000/`.

## Usage

1. **Administrator**

   - Log in with the admin credentials created during setup (`http://localhost:8000/admin/`).
   - Add voting positions by navigating to the "Positions" section and specifying the start and end dates for voting.
   - Manage candidates by navigating to the "Candidates" section and adding/editing/removing candidate details.

2. **Users**

   - Users can access the home page (`http://localhost:8000/`) to view general information about the voting system.
   - During the voting period for each position, users can access the "Vote" page (`http://localhost:8000/vote/`) to cast their votes.
   - Users can only vote for each position once. If they attempt to vote again, they will be informed that they have already voted for that position.
   - After voting, users can view the "Results" page (`http://localhost:8000/results/`) to see real-time voting results and percentage of votes for each candidate.

## Dependencies

The Voting System relies on the following key technologies:

- Django: A high-level Python web framework for rapid development.
- Django Allauth: Provides user authentication and social media login functionalities.
- Bootstrap 5: A popular front-end CSS framework for building responsive web applications.


## Directory Structure

The project follows this directory structure:

```
├── manage.py
├── project
│   ├── settings.py
│   └── urls.py
└── voting
    ├── migrations
    ├── templates
    │   ├── account
    │   │   ├── account.html
    │   │   ├── login.html
    │   │   ├── logout.html
    │   │   ├── password_change.html
    │   │   └── password_change_done.html
    │   ├── base.html
    │   ├── candidate_list.html
    │   ├── home.html
    │   ├── result.html
    │   ├── voting_closed.html
    │   ├── already_voted.html
    │   ├── voting_success.html
    │   └── vote.html
    ├── models.py
    ├── urls.py
    └── views.py
```

## Contributions

Contributions to the Voting System project are welcome! If you have any ideas, bug reports, or feature requests, please feel free to open an issue or submit a pull request.

## License

The Voting System is open-source and licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

Special thanks to all contributors and the Django community for their excellent work and support.

Enjoy using the Voting System! If you have any questions or need assistance, please don't hesitate to reach out. Happy voting!

