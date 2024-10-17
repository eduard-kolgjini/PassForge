# PassForge

PassForge is a powerful yet simple password manager designed for generating and managing secure passwords. It supports password encryption, retrieval, and seamless user interaction through a command-line interface (CLI). This project showcases practical skills in development, cybersecurity, and software testing, providing a secure and user-friendly password management solution.

## Features

- **Password Generation**: Generates secure passwords with customizable lengths.
- **Password Encryption**: Uses the Fernet symmetric encryption method to protect passwords.
- **Password Storage**: Saves encrypted passwords in a local file.
- **Password Retrieval**: Decrypts and retrieves previously saved passwords.
- **Boundary Value Analysis**: Ensures password length validation and security.
- **Extensive Testing**: Implements unit tests for critical operations, ensuring functionality across edge cases.

## Technologies Used

- Python 3
- `cryptography` package for encryption
- Unit testing with `unittest`

## Getting Started

### Prerequisites

- Python 3 installed on your machine.
- Install the required Python packages by running the following command:

```bash
pip install cryptography

### Clone the Repository

To clone the repository, run:

```bash
git clone https://github.com/yourusername/PassForge.git
cd PassForge
