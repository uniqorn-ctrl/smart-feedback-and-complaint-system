# Smart Complaint App

## Overview
The Smart Complaint App is a web application built using Python's Flask framework. It allows users to submit complaints, view existing complaints, and resolve them. The application features a simple and intuitive interface, making it easy for users to interact with.

## Project Structure
```
smart-complaint-app
├── app.py                # Main entry point of the Flask application
├── templates             # Contains HTML templates
│   ├── index.html       # Homepage with complaint submission form
│   ├── base.html        # Base template for common structure
│   └── complaint.html    # Template for displaying individual complaint details
├── static               # Contains static files
│   ├── css
│   │   └── style.css    # CSS styles for the application
│   └── js
│       └── script.js     # JavaScript for client-side functionality
├── requirements.txt      # Python dependencies for the project
└── README.md             # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd smart-complaint-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
- Users can submit their complaints through the form on the homepage.
- Submitted complaints will be displayed on the same page.
- Users can resolve complaints by clicking on the appropriate link next to each complaint.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.