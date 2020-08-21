# Introduction to Python for Geo Information Minor

Dear student,

Welcome to the python part of the [Geo Information Minor](www.nationalegiminor.nl) organized by the Vrije Universiteit Amsterdam together with Utrecht University. In this course we'll take a small dive into the Python programming language. We'll cover some **basic programming concepts** and briefly delve into **data acquisition** by using API's.

By the way: Did you know that the python programming language was developed in Amsterdam? Guido van Rossum, a researcher from the **Centrum voor Wiskunde en Informatica**, developed it in the 1990s. [https://en.wikipedia.org/wiki/Python_(programming_language)](https://en.wikipedia.org/wiki/Python_(programming_language))

From previous iterations we've distilled that learning the basics isn't the challenge (anymore) due to the abundance of open online courses and interactive online tutorials. **Rather, the question is: how do I craft useful scripts that solve real-world problems?**

Hence, we'll show you how to **apply your knowledge** to the challenges you'd like to **address day-to-day activities**. Along the way, we'll show you how to solve common Python-related problems, give you tips-and-tricks about finding help and expanding Python's capabilities with external modules. We expect you use this knowledge at a later stage of our course when you will have to work on the case-study. 

This course is hands-on: **we don't have slides or extensive lecture notes;**. We will help you to make two assignments, however before that you will have to do some homework in order to get the basics of python. We expect you to have finished these tutorials before the 14th of September. 

## Course overview

-   Introduction to Python
-   Introduction to API access using the requests module
-   Accessing air quality data and include in your GIS
-   Downloading information about traffic preprocess data for an analysis on the impact of traffic on air quality

## Methodology and programme

This course consists of a self-learning part and two hands-on workshops. Each workshop lasts a full day. During these days (i.e. 14/09 and 15/09) we will be available from 11:00 - 12:45 and from 13:30 - 17:00 via zoom. Please leave your question in the chat. A link to our Zoom session can be found at Canvas. 

The program is as follows:

-   self-study (to be finished before th 14th of September)

-   [practical assignment py1](https://github.com/SPINLab/GI_Minor_2020/tree/master/py1_LuchtmeetnetAPI) 14/09/2020 - using the Luchtmeetnet API, with the requests module
-   [practical assignment py2](https://github.com/SPINLab/GI_Minor_2020/tree/master/py2_Traffic) 15/09/2020 - Combining air quality data with traffic data

Each practical assignment is accompanied by a short manual and some Python scripts.

## Self-study: 

To maximize the time available for the hands-on lectures and exercises we kindly ask you to complete a number Python lessons in advance **(BEFORE the 14th of September)**.

There are multiple online tutorial to learn the basics of python. We give you a couple of options of which you can decide what works best for you. 

**Option 1**
[https://www.w3schools.com/python/default.asp](https://www.w3schools.com/python/default.asp) is an online learning platform that offers programming courses in a wide range of languages. You learn to program by typing and executing Python commands directly in your browser.

Complete all exercises listed under **Python Tutorial** and **File Handling** before coming to class on the 14th of September.

**Option 2**
A more text book like format with a more in depth explanation can be accessed here:
[https://greenteapress.com/wp/think-python-2e/](https://greenteapress.com/wp/think-python-2e/)

## Practical assignment

This python course has two mandatory practical assignments. Each assignment contains a short manual and one or more Python scripts.

-   [practical assignment luchtmeetnet](https://github.com/SPINLab/GI_Minor_2020/tree/master/py1_LuchtmeetnetAPI)

-   [practical assignment traffic](https://github.com/SPINLab/GI_Minor_2020/tree/master/py2_Traffic)

For these practical assignments you can download the accompanying files as follows:

1. scroll to the top of this page
2. click on the green button labelled `Clone or download`
3. click on `Download ZIP`
4. Unzip the file you downloaded and load the `.py` scripts contained in one of the folders in your favourite editor.

## Installing Python (Windows)

You'll need to install Python and a number of external modules on your machine to run the example scripts and perform the exercises. To make it easier we will use a Python distribution that already comes with a large number of modules that are useful for scientific computing, called Anaconda. Anaconda also comes with a module manager called Conda, which we will use to install a few modules.

For this course we will be working with **Python 3** which is used in both ArcGIS Pro and QGIS 3.

You can install Anaconda and the needed modules as follows:

-   Download and install Anaconda -> [Download Anaconda](https://www.anaconda.com/download/) and double click it. You can accept the default choices. You can skip the installation of Visual Studio Code. This is a text editor made for coding, and while it is a really good application, we will not use it in this course. (For a short introduction to Anaconda please watch either [this](https://www.youtube.com/watch?v=zYNRqVimU3Q) or [this](https://www.youtube.com/watch?v=ou65T_mC8Z8) video. )

-   Install the `pandas` module open a Anaconda prompt (`Start Menu` -> `Anaconda` -> `Anaconda Prompt`) in administrator mode (right click -> More -> Run as administrator) and enter the following command:

    `conda install pandas`

    press `Enter` to execute it.

However, since pandas is very commonly used it is very likely you already installed it or that is was automatically installed when you installed Anaconda.

-   Install the `geopandas` module: open a Anaconda prompt (`Start Menu` -> `Anaconda` -> `Anaconda Prompt`) in administrator mode (right click -> More -> Run as administrator) and enter the following command:

    `conda install geopandas`

    press `Enter` to execute it.

-   If you ever want to install other modules just Google `conda *module name*` and look for the result (with `Anaconda Cloud` in the title) with the latest version available for your platform. Copy the text under `To install this package with conda run one of the following:` and enter this command in the Anaconda prompt.

Test if everything works:

-   start the Python editor `Spyder` (`Start Menu` -> `Anaconda` -> `Spyder`) NOTE: If spyder does not start, reinstall anaconda and skip the step to install geopandas. In the exercises skip the steps which involve geopandas.
-   copy/paste the following code into the newly opened editor

Python 3:

```python
import geopandas
import pandas

print('Everything works!')
```

-   save the file: `File` -> `Save`
-   run the code: `Run` -> `Run`
-   do you see `Everything works!` in the output screen? Great, you're all set!
-   do you see something else? Too bad, something's wrong. Please copy/paste the output in the issue tracker (see below for instructions) and we'll try to assist you.

## BONUS Practical Assignment
We have one bonus practical assignment which we used in previous years about how to extract location information of tweets from twitter. If you want you are interested you can make it
-   [practical assignment twitter](https://github.com/SPINLab/GI_Minor_2020/tree/master/py3_TwitterAPI)


## The team
-   Maurice de Kleijn
-	Devi Brands
-	Dewi Westra

## Previous contributors
-   Simeon Nedkov
-   Chris Lucas
