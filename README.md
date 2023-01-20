<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


=====

# **RJW ARTSTUFF**

## **INTRODUCTION**
This **fifth and final Portfolio Project** is the product of combined knowledege and techniques from all modules of the ***Code Institute Full Stack Developer Course*** to date, culminating in the creation of this **E-Commerce Applications project**. This Application will ... and also allow the **site owner** to create, read, update and delete additional data records for the **RJW ARTSTUFF** website.

A live version of the site can be found [here](https://pp05-rjw-artstuff.herokuapp.com/)

![banner](static/readme/)

![amIresponsive](static/readme/)

### **PROJECT FUNCTIONALITY**
The application uses **Django 3** to encourage rapid development, by utilising a *model-template-view* approach.
In conjunction with **Django**, **sqlite** was used in the Project's inception phase as a database for local testing. **Sqlite** is self-contained highly reliable, SQL database engine that includes all the normal relational database management features. Later, development was switched to **ElephantSQL**, to ensure any data entered was visible in the deployed application. **ElephantSQL** is open source and boosts a fully technical and easy to use object-relational database management system.
The project is version controlled via **Git** & **Github** and is deployed via **Heroku**. All environment & secret variables are stored in an `env.py` file, which is then held in a `.git-ignored` file, ensuring project integrity is held to a high security standard, in relation to project and present day requirements.

Using **Django** and the above Database methods the site owner, as an administrator for the application, has complete access to a custom Admin dashboard where they can Create, Read, Update and Delete records for each of the application models as appropriate. In-built functionality also ensures the ability to maintain, add to, delete and curate the database from directly within the **RJW ARTSTUFF** website, via the ***Product Management*** link. 

To this end, please ensure when using the site and testing the **CRUD funcionality** of this application, **please log in as site owner, RJW:** 

| IS STAFF? | USER | EMAIL | PASSWORD | IS SUPERUSER? |
|-----|-----|-----|-----|-----|
| ***YES*** | ***rjw*** | **rjw.illustration@gmail.com** | **rian0592** | ***YES*** |

----

## PLEASE SEE [**CHALLENGES, BUGS and FIXES**](#challenges-bugs-and-fixes) SECTION BEFORE USE

----

# **UCD Phase 1: STRATEGY** 

## **PROJECT GOALS**

As... full-function e-comm portal.

Base styling and project setup relies mainly on Bootstrap and initially borrows from Code Institute's Boutique Ado project but with my own custom models. Full CRUD functionality is demonstrated in the ability for the site owner to create, update and delete **RJW ARTSTUFF** Product data directly through their browser or the Admin Panel. 

## **USER STORIES:**

A **GitHub** classic kanban project board was utilised throughout to log all ***User Stories***, track their progress and manage the project. This helped keep focus by moving them, in manageable batches, through *lanes*; from *"to do"* through *"in progress"* into ***"done"***, as they were completed.

![kanban image](static/readme/)

More **Kanban** screens [**here**](static/readme/).

***Unregistered User (Logged Out) Stories* include:**
- USER STORY #0: Title
  As a new or returning user I can easily register / login so that I can...

***Registered User (Logged In) Stories* include:**
- USER STORY #0: Title
  As a returning user I can... so that I can...

***Site Owner (Superuser) Stories* include:**
- USER STORY #0: Title
  As the site owner I can... so that I can...

***User Stories which fell outside of MVP solution*:**
- USER STORY #0: Title
  As a... user I can... so that I can...

Due to the inevitable development delays due to learning challenges, bug squashing and the like, time and skills unfortunately didn't allow for all ***User Stories*** to be met. However, all *'Must Have'* and *'Should Have'* stories were satisfied and **MVP functionality** was achieved. As site owner I am slightly disappointed that all features weren't included in this iteration but I'm happy overall to have a working proof of concept I can build on.  

## **GENERIC USER EXPECTATIONS:**

- Intuitive/conventional navigation elements
- Familiar and/or easily understandable site structure
- Responsive: access site easily on any device

---- 

# **UCD Phase 2: SCOPE**

### Analysis and ***MoSCoW grading*** of ***User Stories:***

| USER STORY                                 | MoSCoW | 
|--------------------------------------------|:------:|
| USER STORY #01: Title             |  M     |
| USER STORY #02: Title             |  M     |
| USER STORY #03: Title             |  M     |
| USER STORY #04: Title             |  M     |
| USER STORY #05: Title             |  S     |
| USER STORY #06: Title             |  M     |
| USER STORY #07: Title             |  S     |
| USER STORY #08: Title             |  S     |
| USER STORY #09: Title             |  S     |
| USER STORY #10: Title             |  C / W |
| USER STORY #11: Title             |  C / W |
| USER STORY #12: Title             |  C / W |

***Proposed Production:*** Delivery of **MVP as a fully functioning solution**, with the potential exception of:
- USER STORY #00: Title
  As a... user I can... so that I can...

As stated previously, due to general project coding challenges and bugtime, it was fairly apparent midway through development that implementation of all user stories was unlikely. It was at this point, after brief investigations into integrating the user stories above, that I decided to focus on the work in progress and on **completing the sprints required to achieve a base MVP**. 

----

# **UCD Phase 3: STRUCTURE**

## **ENTITY RELATIONSHIP DIAGRAM** 

An ***Entitiy Relationship diagram*** was produced in order to better visualise the data to be stored in the database. It demonstrates the basic design upon which the database will be built. It specifies what data entities and attributes will be stored and how they relate to eachother.

![ERD](static/readme/)

---- 

# **UCD Phase 4: SKELETON**

## **INITIAL WIREFRAMES**

Following current conventional practice, **RJW ARTSTUFF** was designed with a Mobile First approach.

----

![Example mobile wireframe](static/readme/)

----

![Example desktop wireframe](static/readme/)

All wireframes generated in **[Balsamiq](https://balsamiq.com)**. A full set of PDF & PNG wireframes for mobile and desktop can be found [**here**](static/wireframes/).

---- 

# **UCD Phase 5: SURFACE**

## **DESIGN CHOICES**

## Fonts

All fonts utilised in this project were sourced from and served by [**Google Fonts**](https://fonts.google.com):

- **Heading Font:** *NAME*
  
  *NAME* is a sans-serif typeface intended for display purposes, which stood out as an ideal choice for this project's header/logo when initially browsing Google Fonts. 

- **Body Font:** *NAME*

  *NAME* was chosen as a light, easy going body typeface; it's rounded bars and quirky typographic additions subtly contrast the weight and formality of **NAME**.

![Google Fonts Choices](static/readme/)

## Colours

Colours utilised were chosen with the **60:40:10 rule** in mind 

  • 60% Background/Primary - **#000000** *Guyabano* was chosen as a light, clean and calm alternative to white. Taken from *Original Xbox Green* list of Distantly Related Related colours.
  
  • 40% Body Text/Secondary: **#000000** *Original Xbox Green* chosen as it's a strong, brand-specific colour, which is familiar to Xbox users. Colour hex value referenced from: https://encycolorpedia.com/0e7a0d.
  
  • 10% Accent/Tertiary: **#000000** *Carmine* was chosen as a good contrasting accent colour to both Primary and Secondary colours. Taken from Original Xbox list of Intermediately Related colours, it is mainly utilised for link & button hover.

![Image](static/readme/)

## Imagery

• Main page banner image:

  - The image utilised for the site header is
  
    - Sourced from: https://

• Other images utilised sourced from: 
  
  - Details: https://

  - Details: https://


• All copy used for game descriptions have their relevant sources credited in-body where appropriate. 

----

# **TECHNOLOGIES**

During the course of this project I have utilised the following technologies:

## **LANGUAGES, VERSION CONTROL and FRAMEWORKS**

### HTML, CSS, JS & Python - core languages used to create this CRUD application:
- **JavaScript** (https://www.javascript.com/) was used to add interactivity and enrich the User eXperience.
- **HTML5** (https://html.com/html5/) (HyperText Markup Language) was used for structuring & presenting site content.
- **CSS** (https://www.css3.info/) (Cascading Style Sheets) was used to provide styling to the HTML.
- **Python** (https://www.python.org/) 'Python is a programming language that lets you work quickly
and integrate systems more effectively.'

### VERSION CONTROL and FRAMEWORKS:
- **Git** (https://git-scm.com) was used for version control (commit to **Git** and push to **GitHub**.)
- **Gitpod** (https://www.gitpod.io/) was used to write my code; an online IDE linked to the **GitHub** repository.
- **GitHub** (https://github.com/) was used to create the repository and store the project's code after being pushed from **Git**.
- **Bootstrap Framework** (https://getbootstrap.com/) was used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
- **Bootstrap's Imported Javascript** & **JQuery** (https://getbootstrap.com/docs/4.3/getting-started/introduction/#js) used for Responsive Navbar expand & collapse, **roundSlider** and alert messages timeout functionality.
- **Django** (https://www.djangoproject.com/) was used as the architectural engine following the *model-template-view* approach.
- **Heroku** (https://www.heroku.com/) A cloud platform as a service enabling deployment of this **CRUD application**.

## **TOOLS USED**
- **PostgreSQL** A free, open-source relational database management system emphasizing extensibility and technical standards compliance.
- **Balsamiq** (https://balsamiq.com) used to generate mobile and desktop wireframes.
- **favicon** (https://www.favicon.cc/) was used to create a **custom favicon** for the project: ![favicon](static/favicon.ico)
- **roundSlider** (https://roundsliderui.com/) is a **jQuery plugin** that allows the user to select a value. Used to input and update *User Ratings* on the site. 
- **Google Chrome Dev Tools** (https://www.google.com/intl/en_uk/chrome/) used to debug & test source code using HTML5 and to test site responsiveness, also assisted in identifying the correct style properties to override some **Bootstrap** styling.
- **Google Fonts** (https://fonts.google.com) used for all fonts utilised in the project.
- **amiresponsive** (http://ami.responsivedesign.is/) used to check how responsive the site is on different devices.
- **JSHint** (https://jshint.com/), [**W3C Markup**] (https://validator.w3.org/) and [**W3C Jigsaw**] (http://jigsaw.w3.org/css-validator/) used to validate all source **JavaScript**, **HTML** & **CSS** code.
- **CI Python Linter** (https://pep8ci.herokuapp.com/) ***Code Institute's*** very own linter, used to check **Python code** is consistent with *PEP8* requirements.
- **Font Awesome Icons** (https://fontawesome.com/icons?d=gallery) used for social icons in footer and site-wide iconography.
- **ToC** (https://) used to generate ReadMe **Table of Content**.

## Database

The main database used for this Project was **ElephantSQL**, as an installed add-on to the deployed Heroku Application. **Sqlite3** was used initially to test User Authentication, Registration & Login, and for testing the creation of Game data. However later in development I moved to local & deployed testing so **ElephantSQL** was utilised from that point on.

When the app and its models were created and implemented, `python manage.py makemigrations` was run in the terminal to create the initial model package and `python manage.py migrate` was then used to apply the model to the database and create the table.
Where possible, first-time-right methodology was approached when creating the models to avoid to many alterations to the models and the database table through multiple `makemigrations` and `migrate` commands.

----

# **FEATURES**

## **CURRENT FEATURES**

**Full E-Commerce Functionality**

As required...

  ![E-COMM](static/readme/)
  ![E-COMM](static/readme/)
  ![E-COMM](static/readme/)

**Full CRUD Functionality**

As required...

  ![CRUD Create](static/readme/)
  ![CRUD Create](static/readme/)
  ![CRUD Update](static/readme/)
  ![CRUD Update](static/readme/)
  ![CRUD Delete](static/readme/)
      
**Integrated Customer Feedback Functionality**

As required...

  ![FBACK](static/readme/)
  ![FBACK](static/readme/)
  ![FBACK](static/readme/)

**Contact & Newsletter Functionality**

As required...

  ![CONTACT](static/readme/)
  ![CONTACT](static/readme/)
  ![CONTACT](static/readme/)

**roundSlider jQuery Input**

I was looking for a cool and slick way for registered users to post their rating scores and found **roundSlider** (https://roundsliderui.com/), a fully customisable circular slider input - I was sold! Although not a strong Scripter, with a little tinkering and experimenting on their excellent jsfiddle playground, I'm pleased with the final implementation. There are some issues with alignment I couldn't spare the time to fathom but, despite this, overall my favourite feature! 

![Cold rating](static/readme/anticipator_screens/small_screen_pngs/site_small/rs_zero.png)
![Mid rating](static/readme/anticipator_screens/small_screen_pngs/site_small/rs_warm.png)
![Scorch rating](static/readme/anticipator_screens/small_screen_pngs/site_small/rs_scorch.png)

- Easily customisable **Tooltip labels**:

![rs temps](static/readme/anticipator_screens/small_screen_pngs/site_small/rs_js_temps.png)

- **Average Ratings** update on page refresh reflecting freshly calculated Average Rating!

![Rating averages](static/readme/anticipator_screens/small_screen_pngs/site_small/rs_avg_1.png)
![Rating averages](static/readme/anticipator_screens/small_screen_pngs/site_small/rs_avg_2.png)
  
## ***FEATURES TO IMPLEMENT***

- Identified at ***UXD Phase 2***, ... 

- In addition I would also like to consider implementing ***future features*** such as but not limited to:
  - ...
  - ...
  - ...

----

# **TESTING**

## CODE VALIDATION

## W3C Validator Testing 

- HTML
  - Aside from `{% CONTROL %}`, `{{ TEMPLATE VAR }}` and other template-related errors and warnings (for expected !DOCTYPE/title and adding language attributes, etc.), no further errors were returned when passing through the official [W3C validator](https://validator.w3.org)

| .html PAGE | RESULT |
|:-----:|:-----:|
| base | [VIEW](static/readme/) |
| other | [VIEW](static/readme/) |
| other | [VIEW](static/readme/) |
| other | [VIEW](static/readme/) |
| other | [VIEW](static/readme/) |
| other | [VIEW](static/readme/) |
| login | [VIEW](static/readme/) |
| logout | [VIEW](static/readme) |
| signup | [VIEW](static/readme) |

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org)

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

![W3C CSS](static/readme/)

## jshint Validator Testing 

- JavaScript
  - No errors were returned when passing through the [JSHint validator](https://jshint.com/)

![JSHint JS](static/readme/)

## PEP8 Validator Testing

- PEP8
  - All Project .py files passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) without issue

| APP | .py FILE | RESULT |
|:-----:|:-----:|:-----:|
| artstuff | urls | [VIEW](static/readme/) |
| app | admin | [VIEW](static/readme/anticipator_screens/code_validation/python/cipl_xbox_admin.png) |
| app | forms | [VIEW](static/readme/) |
| app | managers | [VIEW](static/readme/) |
| app | models | [VIEW](static/readme/) |
| app | urls | [VIEW](static/readme/) |
| app | views | [VIEW](static/readme/) |

**Google Developer Tools**

- I made use of the built-in **Chrome Dev Tools** to experiment and debug while coding, in addition to testing simulated responsive behaviour across a range of mobile and desktop devices, and finally checking all pages Performance using **Lighthouse**. 

![example lighthouse](static/readme/)

More **Lighthouse** test results in this folder [**here**](static/readme/).

**Response Testing**

In order to make sure that **RJW ARTSTUFF** was responsive to all device sizes, I used [amiresponsive](http://ami.responsivedesign.is/)

![amiresponsive](static/readme/)

## **MANUAL TESTING**

In addition to my own testing a link to the project was shared to family & friends for rigorous testing across varied devices and screen sizes.

- **Browsers** including: 
  - Chrome
  - Safari
  - Edge

- **Devices** including: 
  - iPhone 11
  - iPhone 12 Mini
  - Google Pixel 6
  - iPad Pro (2018)
  - iPad Air (2020)
  - MacBook Pro (2015)

## Manual Testing Results Summary

**TEST TABLE:**

| TEST | OUTCOME | PASS/FAIL |
|---|:---:|:---:|
| All users can... | example.html/example.html | PASS |
| All users can... | example.html/example.html | PASS |
| All users can easily register or login to access user features | signup.html/login.html | PASS |
| All users can... | example.html/example.html | PASS |
| *Unregistered* users can't leave comments | signup.html/login.html | PASS |
| *Unregistered* users can't leave/adjust ratings | signup.html/login.html | PASS |
| Registered users can log out easily | logout.html | PASS |
| Staff/admin users can easily create new data | example.html | PASS |
| Staff/admin users can easily update existing data | example.html | PASS |
| Staff/admin users can easily delete existing data | example.html | PASS |
| Admin users can disapprove/remove comments (via Admin panel) | /admin | PASS |
| Admin users can esily remove users & all associated data (via Admin panel) | /admin | PASS |

----

# **DEVELOPMENT CYCLE**

## **PROJECT CHECKLIST**

- Install **Django** and supporting libraries

  - Install **Django** and **Gunicorn**. Gunicorn is the server utilised to run Django on Heroku
  - Install support libraries including **psycopg2**, used to connect the **PostgreSQL database**
  - Install **Cloudinary** libraries, a host provider service for persistent image storage
  - Create `requirements.txt` file, which includes the dependencies to allow the project to run in Heroku

- Create a new, blank **Django Project**

  - Create new project: `rjw_artstuff`
  - Create new app: `product`
  - Add `product` to the installed apps in *settings.py*
  - Migrate all new changes to the database
  - Run the server to test

- Setup project to use **Amazon S3** and **ElephantSQL**
 
  - Create new **Heroku app**
    - Sign into **Heroku**
    - Select *New*
    - Select *Create new app*
    - Enter a relevant app name
    - Select appropriate region
    - Select the *Create app* button

  - Attach **ElephantSQL database**
    - In **Heroku/Resources**
      - Search add-ons for *Postgres*
      - Select: *Heroku Postgres*
      - Submit order form
 
  - Prepare ***environment*** and ***settings.py*** files
 
    - Create `env.py` file
    - In `env.py`:Add `DATABASE_URL` with the **Postgres** `URL` from **Heroku**
    - Get a randomly generated **SECRET_KEY** *e.g.* from [key generator](https://django-secret-key-generator.netlify.app/)
    - In **Heroku**: Add `SECRET_KEY` + generated key to the `Config Vars`
    - In ***settings.py***: Add `if` statement to prevent production server from erroring
    - Replace insecure key with the environment variable for the `SECRET_KEY`
    - Add **Heroku** database as the back end
    - Migrate changes to new database

  - Get static media files stored on **Cloudinary**
    - Create **Cloudinary** account
    - From the dashboard, copy the `API environment variable`
    - In the *settings.py* file create a new environment variable for `CLOUDINARY_URL`
    - Add the `CLOUDINARY_URL` variable to **Heroku**
    - Add a temporary `Config Var` for `DISABLE_COLLECTSTATIC`
    - In *settings.py* add **Cloudinary** as an installed app
    - Add `static` and `media` file variables
    - Add templates directory
    - Change `DIR's` key to point to `TEMPLATES_DIR`
    - Add **Heroku** hostname to `allowed hosts`
    - Create directories for `media`, `static` and `templates` in the project workspace
    - Create a `Procfile`

- Deploy *rjw_artstuff* to **Heroku**

----

## **DEPLOYMENT**

This full stack application was developed using in-browser IDE **Gitpod Code** v1.73.1 and version controlled via local **(git)** and online **(github)** repository technologies. All secret environment variables were stored in an `env.py` file, which was added to a `.gitignore` file and out of the public repo. Those variables detailed in the `env.py` file were re-enacted in **Heroku/Settings** for this application under the `Config Vars` section, allowing the deployed site to utilise these secret variables.

The terminal was used to deploy the project locally:
- Create a repository on **GitHub** from the ***Code Institute full template***
- Open repository in source code editor **(GitPod)**
- Enter `python3 manage.py runserver` into the terminal
- Open local host address on web browser
- All local saved changes appear here

Deploying this application was achieved by:
- Pushing code from the IDE to **Github** via **Git** and the built-in **bash terminal**
- Creating an app on **Heroku** & deploying it from same
- Adding secret environment variables to the app's `Config Vars` in **Heroku/Settings** and assigning to the respective secret values held in the `env.py` for Live Deployment
- In **Heroku/Deploy**, deployment method set to **Github**
Final deployment to **Heroku**:
- Set `debug = False` in *settings.py* file
- Commit & push all files to **GitHub**
- In **Heroku/Settings**: Remove `DISABLE_COLLECTSTATIC` from `Config Vars`
- In **Heroku/Deploy**: Check auto deploy if required; click ***Deploy branch*** to deploy app 

A live link to this project can be found **[here](https://pp05-rjw-artstuff.herokuapp.com/)**.

To clone the repository:
- Select the Repository from **Github Dashboard**
- Click on the green 'Clone or download' button
- Click on the clipboard icon to the right of the `Git URL` to copy the web URL of the Clone
- Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window
- Change the directory to where you want to clone the repository to
- Paste the `Git URL` copied from above and click 'Ok'
- Once open, create an `env.py` file and assign the *Database URL, Secret Key and other secret variables* - ensure the `env.py` is in the root project directory and add it to `.gitignore` to ensure any Secret details aren't exposed

----

## **CHALLENGES, BUGS and FIXES**

**IN-DEPLOYMENT BUG**

### **Ongoing Bug Report: Short Description...**
  
  • *Issue:* ...
  
  • *Fix:* ...

- **Example** Blurb..:

  ![image](static/readme/)

- **Example** Blurb..:

  ![image](static/readme/)

----

**SOLVED BUGS**

### **Bug: Short desc**
  
  • *Issue:* ...
  
  • *Fix:* ... 

  ![image](static/readme/)
  ![image](static/readme/)

----

### **Bug: Short desc**
  
  • *Issue:* ...
  
  • *Fix:* ... 

  ![image](static/readme/)
  ![image](static/readme/)

----

### **Bug: Short desc**
  
  • *Issue:* ...
  
  • *Fix:* ... 

  ![image](static/readme/)
  ![image](static/readme/)

----

### **Bug: Short desc**
  
  • *Issue:* ...
  
  • *Fix:* ... 

  ![image](static/readme/)
  ![image](static/readme/)

----

### **CONTRIBUTERS**

Other coders code that I've referenced, learnt from, been inspired by or just plain borrowed:

• **All document fonts** sourced from google fonts:

• **All game images & info** is credited either under the **UCD Phase 5** IMAGERY section or in-copy within the application.

• **Feature** Blurb from: https://

• **Feature** Blurb from: https://

• **Feature** Blurb from: https://

----

## **CREDITS**

Firstly, I'd like to thank my family and folks for putting up with me during my studies! I'd also like to thank Mike, Aoife and the Code Institute Student Care team for their help and, well, care. Finally thanks go to my Mentor, Marcel, for his continuing support and advice. 

----

![banner](static/readme/)