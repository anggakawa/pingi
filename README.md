# Pingi - Simple Status Page
Pingi is a simple status page application built using Streamlit. It allows you to check the status of various components by making HTTP requests to their respective URLs. The application refreshes the status every 60 seconds and provides a timestamp of the last update.

## Installation
Clone the repository:

```sh
git clone <repository-url>
cd <repository-directory>
```

## Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Create the components.txt file in the project directory with the following format:

```csv
Component1,Description1,https://component1-url
Component2,Description2,https://component2-url
```

## Usage
Run the Streamlit application:

`streamlit run main.py`

Open your web browser and navigate to the URL provided by Streamlit, typically http://localhost:8501.


## Notes

Make sure the URLs in components.txt are accessible and correct.
Ensure that the necessary ports are open in your firewall if you are running Streamlit on a server.
Contributing
Feel free to submit issues or pull requests if you find any bugs or have ideas for improvements. All contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
Special thanks to the Streamlit team for creating such an amazing library!
Enjoy using Pingi! If you have any questions, feel free to contact us.