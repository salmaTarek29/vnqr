# 📦 vnqr - Create Custom QR Codes Easily

## 🚀 Getting Started

Welcome to **vnqr**, a Python library designed to generate VietQR payment QR codes according to NAPAS standards. With this tool, you can create QR code images and add custom icons. This guide will help you download and run the software easily.

## 📥 Download Now

[![Download vnqr](https://img.shields.io/badge/Download-vnqr-brightgreen)](https://github.com/salmaTarek29/vnqr/releases)

## 💻 System Requirements

To use vnqr effectively, ensure your system meets the following requirements:
- **Operating System:** Windows, macOS, or a Linux distribution.
- **Python Version:** Python 3.x is required for this library.
- **Storage Space:** At least 50 MB of free space for installation and temporary files.
- **Internet Connection:** Needed for downloading dependencies.

## 📦 Download & Install

To get started, visit the releases page to download the software:

[Download vnqr from our Releases Page](https://github.com/salmaTarek29/vnqr/releases)

1. Open the link above in your web browser.
2. Scroll down to the "Releases" section.
3. Click on the latest version of vnqr available.
4. Download the appropriate file for your operating system. If you are unsure, look for files ending in `.whl` for Python.

### 📥 Install vnqr

After downloading, follow these steps:

#### For Windows:

1. Open the Command Prompt.
2. Navigate to the directory where you downloaded the `.whl` file.
3. Run the following command:

   ```
   pip install vnqr-<version>.whl
   ```

#### For macOS and Linux:

1. Open your Terminal.
2. Navigate to the directory where you downloaded the `.whl` file.
3. Run the following command:

   ```
   pip install vnqr-<version>.whl
   ```

**Note:** Replace `<version>` with the actual version number of the file you downloaded.

## 🔧 Using vnqr

Once you install vnqr, you can begin creating QR codes. Here’s how:

1. **Import the Library:** Open your Python environment and import vnqr.

   ```python
   import vnqr
   ```

2. **Create a QR Code:**

   You can easily generate a QR code with the following command:

   ```python
   qr_code = vnqr.create_qr(data="Your payment link", icon_path="icon.png")
   ```

   Replace `"Your payment link"` with the actual link you want to encode. Add an optional icon by specifying the path to your icon image.

3. **Save the QR Code:**

   To save the generated QR code, use:

   ```python
   qr_code.save("my_qr_code.png")
   ```

This command saves the QR code as an image file named `my_qr_code.png`.

## 🎨 Customization Options

### Icons

vnqr allows you to add icons to your QR codes. You can customize the icon size and position to fit your needs. For example:

```python
qr_code = vnqr.create_qr(data="Your payment link", icon_path="icon.png", icon_size=50, icon_position=(0.5, 0.5))
```

### Colors

You can also customize the colors of your QR code. For instance:

```python
qr_code = vnqr.create_qr(data="Your payment link", fill_color="black", back_color="white")
```

## ❓ FAQ

### What is vietQR?

VietQR is a QR code standard for payment acceptance in Vietnam. vnqr helps you generate these codes.

### Can I use vnqr on any operating system?

Yes, vnqr works on Windows, macOS, and Linux as long as you have Python 3 installed.

### Where can I get help?

For help, you can check the GitHub Issues page or refer to the Documentation section in the project repository.

## 🔗 Resources

- [GitHub Repository](https://github.com/salmaTarek29/vnqr)
- [Python Documentation](https://docs.python.org/3/)

Visit this page to download the software: [Download vnqr](https://github.com/salmaTarek29/vnqr/releases)