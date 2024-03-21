# Ticketify

Ticketify is a web application that provides a platform for booking tickets to various events. Users can register, login, browse featured and upcoming events, and purchase tickets for their desired events.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Registration and Authentication**: Users can register for a new account and authenticate themselves to access the application.
- **Browse Events**: Users can browse through featured and upcoming events to find the ones they are interested in.
- **Purchase Tickets**: Users can purchase tickets for their chosen events securely through the application.
- **Advertise Events**: Event organizers can advertise their events on Ticketify to reach a wider audience.
- **Responsive Design**: The application is designed to be responsive, ensuring a seamless user experience across different devices.

## Installation

1. Clone the repository:
    
bash
    git clone <repository_url>
    cd ticketify
    
2. Install the dependencies:
    
bash
    pip install -r requirements.txt
    
3. Set up the database:
    
bash
    flask db init
    flask db migrate
    flask db upgrade
    
## Usage

### Running the Application

1. Run the application:
    
bash
    flask run
    
2. Open a web browser and go to [http://localhost:5000](http://localhost:5000) to view the Ticketify application.

### Registering a User

To register a new user, send a POST request to `/register` with the following JSON payload:
json
{
  "username": "your_username",
  "password": "your_password"
}
### Logging In

To log in, send a POST request to `/login` with the following JSON payload:
json
{
  "username": "your_username",
  "password": "your_password"
}
After successful login, you will receive a JWT token that can be used to access protected routes.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.