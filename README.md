<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Konstantina-Lazaridou/instagram-scraper">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1024px-Instagram_icon.png" alt="Logo" width="150" height="150">
  </a>
<h3 align="center">Instagram scraper</h3>

  <p align="center">
    Login to Instagram, get the source of posts and parse their content.
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project contains Python code that logs in to an Instagram account, iterates over a given list of urls of public Instagram posts (it is not necessary that the main account follows these public users), downloads the content of the posts (original user and posted text, plus the names of the users and their text in the replies), parses this information into a Python dictionary, writes it in a Json file and also writes the HTML of each url in another txt file.

### Built With

* Python
* Selenium
* ChromeDriver

### Prerequisites

Things you need to use the software.
* Instagram account
* Python 3 (tested with >=3.8,<3.9)
* Selenium (tested with >=4.1.2)
* ChromeDriver (tested with 98)

The script is tested with Ubuntu 20.04 and `poetry` 0.1.0. 

### Installation

* Create a virtual environment for your project where Selenium is installed
* Download ChromeDriver according to your Google Chrome version from here: https://chromedriver.chromium.org/downloads
* Copy the `chromedriver` file to your project directory
* If you get a `Permission denied` error when tring to access the `executable_path` of your driver, run `chmod +x chromedriver` in your command line. This error would happen in line ```driver= webdriver.Chrome('/home/username/projects/myproject/chromedriver')```.

<p align="right">(<a href="#top">back to top</a>)</p>


## Usage
* Find your Instagram credentials and replace `your-username` and `your-password` in the instagram-scraper.py with your own login data
* The script is tested with public Instagram accounts that belong to news providers. It might behave differently with private accounts
* Replace the path`/home/username/projects/myproject/chromedriver` (that is the `executable_path` to the web driver) with your own local path inside your Python project
* You can use the two Instagram news post examples already included or add your own. For each post, two files will be created. One that contains the page source in `txt` format and a second one that contains the parsed content (user-text pairs) in `json` format. The first user-text pair is the original post and the next ones are the replies, in the order that Instagram provides them.
* Run the script by running `python instagram-scraper.py` in a command line.
* When the script is finished you will see these two dictionaries:

![User-text pairs](https://github.com/Konstantina-Lazaridou/instagram-scraper/blob/main/Screenshot%20from%202022-03-01%2019-43-25.jpg?raw=true)


<!-- ## Tentative Roadmap

- Download multiple posts about certain event (posts by news providers about Russia's invasion of Ukraine in this case)
- Translate and clean posts
- Analyze and find patterns in the posts
  - TBD
- Add functionality for nested replies

-->

## Acknowledgments

* [Code for iteratively getting replies under Instagram posts](https://medium.com/mlearning-ai/building-a-instagram-scraper-in-3-minutes-a6aac0a2512f)
* [Code example for getting the HTML tags that contain user and text data on Instagram](https://medium.com/mlearning-ai/building-a-instagram-scraper-in-3-minutes-a6aac0a2512f)
  * The tags changed slightly by Instagram. This script is up-to-date and built with the latest ones.
* [Code example for Instagram login](https://stackoverflow.com/questions/62018006/how-to-locate-the-username-and-password-field-within-instagram-login-page-using)
  * Added timers in code to make it work and had to accept the cookies so the script won't break
* Using similar README template to [this](https://github.com/dmrwebdev/README-template/blob/master/README.md)


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Konstantina-Lazaridou/instagram-scraper.svg?style=for-the-badge
[contributors-url]: https://github.com/Konstantina-Lazaridou/instagram-scraper/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
