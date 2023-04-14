# Plant Disease Detection - Final Year Project

## Final Webapp Preview

- Initial landing page
  ![Landing page](https://github.com/Subhadeep0506/plant-disease-detection/blob/main/screenshots/0001.png?raw=true)

- Prediction
  ![Prediction](https://github.com/Subhadeep0506/plant-disease-detection/blob/main/screenshots/0002.png?raw=true)

- Loading image (Notice the file name)
  ![Loading image](https://github.com/Subhadeep0506/plant-disease-detection/blob/main/screenshots/0003.png?raw=true)

- Predicting the right label
  ![Predicting the right label](https://github.com/Subhadeep0506/plant-disease-detection/blob/main/screenshots/0004.png?raw=true)

## 01. Setting up Python environment

Create a virtual environment with Python 3.8

> ### **Note**
>
> Make sure you have Python 3.8 installed in your system and know where it is located.

**Linux or macos**

```bash
python -m virtualenv --python=/path/to/python3.8 .venv
```

**Windows Powershell or Command Prompt**

```powershell
python -m virtualenv --python="\path\to\python3.8" .venv
```

> ### **Note**
>
> If you don't have `virtualenv` installed, here's the command to do it right away:
>
> **Linux and macos**
>
> ```bash
> pip install --upgrade virtualenv
> ```
>
> **Windows**
>
> ```powershell
> python -m pip install  --upgrade virtualenv
> ```
>
> If `pip` doesn't work in Windows, try with `pip3`.

## 02. Activate the environment

If you have followed the steps properly without error, you will be able to start the python virtual environment with the following command

**Linux or macos**

```bash
source .venv/bin/activate
```

**Windows Powershell or Command Prompt**

```powershell
.venv\Scripts\activate
```

## 03. Install the necessary packages

```bash
pip install -r requirements.txt
```

> ### **Warning!**
>
> Tensorflow will be installed in this step and it's huge (around 600mb). So make sure you are connected to a WiFi network.

## 04. Run the app

Run the application with the following command

```bash
python app.py
```
