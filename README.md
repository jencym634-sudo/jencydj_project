 HEAD
### Jencydj_project

Jency DJ project

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app jencydj_project
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/jencydj_project
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
=======
# Tours-and-travels-in-php
Online Tours &amp; Travels management system: This is an online project developed using PHP and MySQL.  The purpose of this project is to provide the complete information about the vehicles available for a tour.  There are 2 different types of users. First the customer visits the site and enters the place from where to where he wishes to travel.  He also provides the date as when he would like to travel.  Then he sends these details to the travel and tourism agency. The employee of travel and tourism agency receives the mail and check which vehicle is available for that day and reverts back to the customer along with the quotation.  If the customer agrees for any one of the quotation, he can reply back along with agreed quotation.
Online Tours & Travels management system: This is an online project developed using PHP and MySQL.

The purpose of this project is to provide the complete information about the vehicles available for a tour.

There are 2 different types of users. First the customer visits the site and enters the place from where to where he wishes to travel.

He also provides the date as when he would like to travel.

Then he sends these details to the travel and tourism agency. The employee of travel and tourism agency receives the mail and check which vehicle is available for that day and reverts back to the customer along with the quotation.

If the customer agrees for any one of the quotation, he can reply back along with agreed quotation.

Objective Of the Project
Faster processing time and more accurate data for travel requests and reimbursements
Ability for travelers to track authorization and reimbursement request status through the system rather than via phone calls or campus mail
Major technological upgrades to the current travel system
Use of IU’s standardized, virtual J2EE environments
Many new features and enhancements
Software Requirements
WAMP Server
XAMPP Server
Installation/Configuration Steps
Download zip files and Unzip files.
Copy and Paste the unzip files inside “c:/wamp/www/” or “c:/xampp/htdocs/”.
Database Configuration:
Create a new database named “db name”.
Import database travel.sql file through phpmyadmin dashboard
Run/Execute PHP Projects
Open Your Web Browser
Put/type inside the web browser : “localhost/project folder”
Admin Login
Open Your Web Browser
Put/type inside the web browser : “localhost/project folder/Admin”
Admin User : admin
Admin Password : admin
 ef26300 (Initial commit1)
