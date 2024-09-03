# Biomass Energy Sizer

## Overview

The Bioproduct Flowrate Evaluator is a Django-based web application designed to calculate and evaluate the flow rate of bioproducts in various industrial processes. This tool allows users to input specific parameters related to bioproducts, perform complex calculations using predefined formulas, and visualize the results through dynamically generated graphs.

## Prerequisites

- Python 3.8+
- Django 5.0.6
- Virtual environment setup

## Setup Instructions

### 1. Clone the Repository

```bash
    git clone https://github.com/your-repo/bioproduct-flowrate-calculator.git
    cd bioproduct-flowrate-calculator
```

### 2. Create and Activate Virtual Environment

Create a virtual environment and activate it:

Windows:

```bash
    python -m venv .venv
    .venv\Scripts\activate
```

Mac/Linux:

```bash
    python3 -m venv .venv
    source .venv/bin/activate
```

### 3. Install Dependencies

```bash
    pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
    python manage.py migrate
```

### 5. Run the Development Server

```bash
    python manage.py runserver
```

### 6. Access the application

Open your browser and go to `http://127.0.0.1:3000/api/bioproducts_flowrate_calculator/`.

## Methodologies and Validation

1. Mathematical Calculations
   Validation: Ensure that the mathematical formulas are correctly implemented in views.py.

   Test: Provide test cases with known outputs to confirm that the logic is correct.

2. Form Validation
   Validation: Forms are validated using Django’s built-in form validation framework.

   Test: Include edge cases in your form validation, such as negative values, non-numeric inputs, and out-of-bound values.

3. Data Visualization
   Validation: Graphs are generated using matplotlib and encoded in Base64 for embedding in HTML.

   Test: Verify that graphs are correctly generated and displayed for various datasets.

4. Error Handling
   Validation: Ensure that all potential errors are handled gracefully, with appropriate messages displayed to the user.

   Test: Simulate errors such as invalid inputs, missing data, and unexpected data types to ensure that the application handles these scenarios correctly.

5. Security and Authentication
   Validation: Ensure that all user inputs are sanitized and that sensitive data is handled securely.

   Test: Test for common security vulnerabilities such as SQL injection, XSS, and CSRF.

6. Code Quality
   Validation: Follow PEP 8 guidelines for Python code and ensure that the codebase is clean and maintainable.

   Test: Use tools like flake8 or pylint to check for style issues and potential bugs.

## Testing

### Unit Tests

Location: tests/ directory

Run Tests:

```bash
    python manage.py test
```

Manual Testing

- Form Inputs: Test with various valid and invalid inputs to ensure correct functionality.
- Graphs: Confirm that the graphs are generated correctly for different input values.

## Deployment

- Production Server: Set up a production server with necessary configurations (e.g., gunicorn, nginx).
- Environment Variables: Ensure that environment variables such as SECRET_KEY, DEBUG, and database credentials are correctly set in the production environment.

## Troubleshooting

Common Issues

- Django ImportError: Ensure the virtual environment is activated and Django is installed.
- Graph Display Errors: Ensure that matplotlib is correctly installed and that the Base64 encoding is handled properly.
- Logs
- Check logs/ directory for detailed logs if the application encounters any issues.

## Contribution

- Contributions are welcome! Please fork the repository and create a pull request with detailed information about your changes.

## License

This project is licensed under the MIT License.

## Project Structure

```plaintext
bioproduct-flowrate-calculator/
│
├── biocalculator/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│
├── calculator/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ ├── views.py
│ ├── services.py # For business logic and API integrations
│ ├── tasks.py # For background tasks if needed
│ ├── templates/
│ ├── static/
│ ├── tests.py
│
├── requirements.txt
├── manage.py
└── README.md
```
