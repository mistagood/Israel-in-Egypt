# Install reportlab Python package



---



---

arygreen@Garys-MBP-2 training % python3 cli_export.py
Traceback (most recent call last):
  File "/Users/garygreen/Creative Cloud Files/websites/training/cli_export.py", line 4, in <module>
    from reportlab.pdfgen import canvas
ModuleNotFoundError: No module named 'reportlab'
garygreen@Garys-MBP-2 training % 

---



---

The error message you're encountering, `ModuleNotFoundError: No module named 'reportlab'`, indicates that the Python package `reportlab` is not installed in your Python environment. The `reportlab` library is used to create PDF files in Python.

To resolve this issue, you need to install the `reportlab` package. You can do this using pip, Python's package manager. Here's how you can do it:

Open your terminal (on Mac or Linux) or command prompt/powershell (on Windows).

Ensure that you have pip installed and that it is updated to the latest version. You can update pip by running:

```sh
python3 -m pip install --upgrade pip
```

Install the `reportlab` package by running:

```sh
python3 -m pip install reportlab
```

After the installation is complete, you should be able to run your `cli_export.py` script without encountering the `ModuleNotFoundError`.

If you're using a virtual environment (which is a good practice for Python projects to manage dependencies), make sure you've activated the virtual environment before installing the package. If you haven't created a virtual environment for your project yet, you can do so by running `python3 -m venv venv` in your project directory and then activate it with `source venv/bin/activate` on Mac/Linux or `.\venv\Scripts\activate` on Windows.

---

garygreen@Garys-MBP-2 training % /usr/local/bin/python3 "/Users/garygreen/Creative Cloud Files/websites/training/exportplus.py"
Traceback (most recent call last):
  File "/Users/garygreen/Creative Cloud Files/websites/training/exportplus.py", line 8, in <module>
    from reportlab.pdf import canvas
ModuleNotFoundError: No module named 'reportlab.pdf'
garygreen@Garys-MBP-2 training % 

---

The error message `ModuleNotFoundError: No module named 'reportlab.pdf'` indicates a mistake in the import statement within your `exportplus.py` script. The correct module for creating PDF canvases in the `reportlab` library is `reportlab.pdfgen.canvas`, not `reportlab.pdf.canvas`.

To fix this issue, you should modify the import statement in your `exportplus.py` file. Replace:

```python
from reportlab.pdf import canvas
```

with:

```python
from reportlab.pdfgen import canvas
```

This should resolve the `ModuleNotFoundError` and allow your script to run correctly, assuming `reportlab` is already installed in your environment. If `reportlab` is not installed, you can install it using pip as described in the previous response.