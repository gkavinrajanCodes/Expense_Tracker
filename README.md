# Expense Tracker CLI

A simple command-line interface (CLI) application to manage your expenses. The Expense Tracker allows you to add, update, delete, and view your expenses. You can also view a summary of expenses and filter them by month.

## Features

- **Add Expense**: Add an expense with a description and amount.
- **Update Expense**: Modify the description or amount of an existing expense.
- **Delete Expense**: Remove an expense by its ID.
- **View All Expenses**: List all recorded expenses.
- **View Expense Summary**: Display the total amount spent.
- **Filter Expenses by Month**: Display the total expenses for a specific month.
- **Expense Categories** (Optional): Add categories to expenses and filter by category.
- **Budget Management** (Optional): Set a monthly budget and receive a warning when it is exceeded.
- **Export to CSV** (Optional): Export the list of expenses to a CSV file.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of using the terminal or command prompt.

### Project URL
    
    https://roadmap.sh/projects/expense-tracker
    

### Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/expense-tracker-cli.git
    cd expense-tracker-cli
    ```

2. **Run the Script:**
    ```bash
    python expense_tracker.py
    ```

### Usage

Run the application using the terminal or command prompt with the following commands:

- **Add an Expense:**
    ```bash
    python expense_tracker.py add --description "Lunch" --amount 20
    ```
    Output: `Expense added successfully (ID: 1)`

- **List All Expenses:**
    ```bash
    python expense_tracker.py list
    ```
    Output:
    ```
    ID  Date       Description  Amount
    1   2024-08-06 Lunch        $20
    2   2024-08-06 Dinner       $10
    ```

- **Delete an Expense:**
    ```bash
    python expense_tracker.py delete --id 1
    ```
    Output: `Expense deleted successfully`

- **View Expense Summary:**
    ```bash
    python expense_tracker.py summary
    ```
    Output: `Total expenses: $20`

- **View Expense Summary for a Specific Month:**
    ```bash
    python expense_tracker.py summary --month 8
    ```
    Output: `Total expenses for August: $20`

### Optional Features

1. **Add Expense Categories:**
   Use the `--category` flag while adding expenses to assign a category.

2. **Set a Monthly Budget:**
   You can set a budget and receive a warning when the budget is exceeded.

3. **Export Expenses to CSV:**
   Use the `export` command to save expenses to a CSV file.

### Error Handling

- Handles invalid inputs (e.g., negative amounts).
- Manages non-existent expense IDs.
- Displays helpful error messages for incorrect commands or arguments.

## Future Enhancements

- Add a graphical user interface (GUI) for a more user-friendly experience.
- Implement user authentication to store expenses for different users.
- Integrate with online services to sync expenses across multiple devices.

## Contributing

Feel free to contribute to the project by submitting pull requests or opening issues.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

Inspired by various personal finance management tools and CLI applications.
