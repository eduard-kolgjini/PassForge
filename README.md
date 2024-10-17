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
```

### Clone the Repository

To clone the repository, run:

```bash
git clone https://github.com/yourusername/PassForge.git
cd PassForge
```

### Usage

Run the Password Manager:

```bash
python main.py
```
### Example

```bash
Generate a new password (G), Retrieve saved passwords (R), or Quit (Q)? G
Enter desired password length (default is 12): 16
Generated Password: kW5$9!xzP@3sL&Qm
Password saved successfully!
```

## Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request. All contributions should adhere to best practices and security standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Let's make secure password management accessible and easy for everyone!
