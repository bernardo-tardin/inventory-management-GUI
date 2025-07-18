# Product and Invoice Management GUI
A simple desktop application built with Python and PySimpleGUI to manage a product catalog and generate professionally formatted Excel invoices.

## Features
This application provides a user-friendly graphical interface (GUI) for the following operations:

* **Product Management (CRUD)** 📦

    * Add: Add new products with a name, price, and an image.

    * View: Browse the list of all products. Selecting a product displays its details and an image thumbnail.

    * Update: Edit the information of any existing product.

    * Delete: Remove products from the catalog.

* **Invoice Generation** 📝

    * Create a new invoice by selecting products from the catalog and specifying quantities.

    * Review a draft of the invoice before finalizing.

    * Automatically generate a formatted .xlsx (Excel) file for the invoice, with custom styles, colors, and column widths for a professional look.

* **Data Persistence** 💾

    * The entire product catalog is saved to a local produtos.csv file, so your data is preserved between sessions.

* **Automatic Translation** 🌐

    * Includes a special feature to automatically translate certain product names from Brazilian Portuguese to European Portuguese variants (e.g., `Calcola` to `Cueca`).
