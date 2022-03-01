<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]

<!-- Buttons
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
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

Downloading and parsing Instagram posts with Python.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* Python
* Selenium
* ChromeDriver

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ## Getting Started
GETTING STARTED -->

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
* If you get a `Permission denied` error when tring to access the `executable_path` of your driver, run `chmod +x chromedriver` in your command line. This error would happen in line `driver= webdriver.Chrome('/home/username/projects/myproject/chromedriver')`.
* Copy the `chromedriver` file to your project directory

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
* Find your Instagram credentials and replace `your-username` and `your-password` in the instagram-scraper.py with your own login data


<p align="right">(<a href="#top">back to top</a>)</p>



ROADMAP
## Tentative roadmap

- Download multiple posts about certain event (posts by news providers about Russia's invasion of Ukraine in this case)
- Translate and clean posts
- Analyze and find patterns in the posts
  - TBD
- Add functionality for nested replies

## Acknowledgments

* [Code for iteratively getting Intagram posts](https://medium.com/mlearning-ai/building-a-instagram-scraper-in-3-minutes-a6aac0a2512f)
* [Code for getting the HTML tags that contain user and text data on Instagram](https://medium.com/mlearning-ai/building-a-instagram-scraper-in-3-minutes-a6aac0a2512f)
* []()




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
