# 🌍 TravelGuide CLI

A simple and intuitive Command-Line Interface (CLI) tool designed to help you organize your travel plans by specifying your destination, travel dates, and budget. Get quick summaries of your trip details right from your terminal!

## ✨ Features

* **Quick Trip Planning:** Easily input your origin, destination, start date, end date, and budget.

* **Clear Output:** Get a concise summary of your travel details.

* **User-Friendly:** Designed for simple and efficient command-line interaction.

## 🚀 Installation

Follow these steps to get TravelGuide up and running on your local machine.

### Prerequisites

* Python 3.6 or higher

* `pip` (Python package installer)

### Steps

1. **Clone the Repository (or download the source code):**

git clone https://github.com/yourusername/travelguide.git
Or if you downloaded a zip: unzip travelguide-main.zip


2. **Navigate to the Project Directory:**

cd travelguide


3. **Create a Virtual Environment (Recommended):**
It's best practice to use a virtual environment to avoid conflicts with other Python projects.

python3 -m venv venv


4. **Activate the Virtual Environment:**

* **macOS / Linux:**

  ```
  source venv/bin/activate
  
  ```

* **Windows (Command Prompt)::**

  ```
  venv\Scripts\activate.bat
  
  ```

* **Windows (PowerShell):**

  ```
  .\venv\Scripts\Activate.ps1
  
  ```

5. **Install the Project:**
With your virtual environment active, install TravelGuide using pip. The `.` indicates installing from the current directory.

pip install .


*If you make changes to the code, you can reinstall with `pip install . --force-reinstall`.*

## 💡 Usage

Once installed, you can use the `travelguide` command directly from your terminal, no matter which directory you are in (as long as your virtual environment is active).

### Basic Command Structure:

travelguide -o &lt;origin> -d &lt;destination> -sd &lt;start_date> -ed &lt;end_date> -b &lt;budget>


### Arguments:

| Short Flag | Long Flag | Description | Type | Example | 
 | ----- | ----- | ----- | ----- | ----- | 
| `-d` | `--destination` | The city or place you plan to visit. | String | `'Paris'` | 
| `-sd` | `--start-date` | Your trip's start date (DDMMYY). | String | `'201020'` | 
| `-ed` | `--end-date` | Your trip's end date (DDMMYY). | String | `'221020'` | 
| `-b` | `--budget` | Your estimated budget for the trip. | Float | `3020.40` | 

### Example:

travelguide -o 'rio de janeiro' -d 'london' -sd '01/01/25' -ed '07/01/25' -b 1500.00


*(Note: Output might vary slightly based on your exact `cli.py` implementation, especially for "Not specified" cases.)*

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, feel free to:

1. Fork the repository.

2. Create a new branch (`git checkout -b feature/your-feature-name`).

3. Make your changes.

4. Commit your changes (`git commit -m 'Add new feature'`).

5. Push to the branch (`git push origin feature/your-feature-name`).

6. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
*(Remember to create a `LICENSE` file if you haven't already!)*

## 📧 Contact

For questions or feedback, feel free to reach out:

* **Carlos Vinícius Teixeira de Souza** - carlosvtsdev@gmail.com

* Project Link: <https://github.com/carlosvts/travel-guide> *(Update this link to your actual GitHub repository)*