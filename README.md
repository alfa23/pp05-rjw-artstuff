<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

=====

# **RJW ARTSTUFF**

![banner](static/readme/site/pp05_readme_banner.jpg)

## **INTRODUCTION**
This **fifth and final Portfolio Project** is the product of combined knowledege and techniques from all modules of the ***Code Institute Full Stack Developer Course*** to date, culminating in the creation of this **E-Commerce Applications project**. 

**RJW ARTSTUFF** allows users to shop original artwork and illustration products from **UK tradigital artist**, ***RJW***. The e-commerce portal offers a range of *quality printed original artworks and garments* at affordable prices, in addition to *artist commissions and custom original art* at competitive rates.

![amIresponsive](static/readme/am_i_responsive/pp05_am_i_responsive.jpg)

A live version of the site can be found [here](https://pp05-rjw-artstuff.herokuapp.com/)

### **PROJECT FUNCTIONALITY**
The application uses **Django 3** to encourage rapid development, by utilising a *model-template-view* approach.
In conjunction with **Django**, **sqlite** was used in the Project's inception phase as a database for local testing. **Sqlite** is self-contained highly reliable, SQL database engine that includes all the normal relational database management features. Later, development was switched to **ElephantSQL**, to ensure any data entered was visible in the deployed application. **ElephantSQL** provides an open-source, fully technical and easy-to-use object-relational database management system.

The project is version controlled via **Git** & **Github** and is deployed via **Heroku**. All environment & secret variables are stored in an `env.py` file, which is then held in a `.git-ignored` file, ensuring project integrity is held to a high security standard, in relation to project and present day requirements. The online payment system utilised in this project is provided by **Stripe**.

Using **Django** and the above Database methods the **site owner**, as an administrator for the application, has complete access to a custom Admin dashboard where they can ***Create***, ***Read***, ***Update*** and ***Delete*** records for each of the application models as appropriate. In-built functionality also ensures the ability to maintain, add to, delete and curate the database from directly within the **RJW ARTSTUFF** website, via the ***Product Management*** link. Client-facing ***CRUD functionality*** is provided to **registed site users** through the ability to ***create***, ***read***, ***update*** and ***delete*** feedback on any product on the site. Finally, a **Connect** page provides users with the opportunity to initiate their own *custom art project* by completeing a ***contact form***, in addition to a ***newsletter subscription*** link, where they can choose to subscribe to the **RJW ARTSTUFF** newsletter. 

To this end, please ensure when using the site to test the full **CRUD funcionality** of this application, **please log in as site owner, RJW:** 

| IS STAFF? | USER | EMAIL | PASSWORD | IS SUPERUSER? |
|-----|-----|-----|-----|-----|
| ***YES*** | ***rjw*** | **rjw.illustration@gmail.com** | **rian0592** | ***YES*** |

----

# **UCD Phase 1: STRATEGY** 

## **PROJECT GOALS**

This project will aim to provide **users** with a *smooth and stylish e-commerce portal*, where they are able to search and purchase ***original custom artworks*** and ***garments*** by **tradigital UK artist *RJW***. A secondary service proposition is also to be offered, where **users** - registered or unregistered - have the ability to *commission their own custom artworks*. The site will also allow the **site owner** to *create, read, update and delete product data records* for the **RJW ARTSTUFF** website directly through the browser.

Base styling and project setup relies mainly on **Django**, **Bootstrap** and borrows from **Code Institute's** *Boutique Ado* project, with the addition of three custom models; ***Feedback***, ***Contact*** and ***Newsletter***. Full *non-superuser CRUD functionality* is demonstrated in the ability for **registered site users** to create, update and delete ***feedback*** on any product, and *manage their posted feedbacks* through a dedicated ***My Feedback*** page. The **site owner** has full *CRUD functionality* to create, update and delete Product data directly through their browser, without a need to access the Admin Panel. 

## **USER STORIES:**

A **GitHub** classic kanban project board was utilised throughout to log all ***User Stories*** necessary to meet MVP requirements, track their progress and manage the project. This helped keep focus by moving them, in manageable batches, through *lanes*; from *"to do"* through *"in progress"* into ***"done"***, as they were completed.

![kanban image](static/readme/kanban/pp05_sprint_kanban_s02.jpg)

![user stories image](static/readme/kanban/pp05_user_stories_s1-s2.jpg)

![stage complete image](static/readme/kanban/pp05_sprint_functionality_s02.jpg)

All other **Kanban** screens [**here**](static/readme/kanban/).

***Milestone/Sprint One User Stories***

- USER STORY #05: Account Registration
As an unregistered user I can easily register for an account so that I can shop more conveniently on future visits.

- USER STORY #04: View Purchase Total
  As an unregistered user I can easily view my purchase total at any time so that I can see my current total & avoid overspending.

- USER STORY #06: Account Login / Logout
  As a registered user I can login or logout easily so that I can securely access my personal account info.

- USER STORY #07: Account Password Recovery
  As a registered user I can recover my password if I forget it so that I can easily regain access to my account.

***Milestone/Sprint Two User Stories***

- USER STORY #01: View List of Items
  As an unregistered user I can view a list of items available to purchase so that I can select items to purchase.

- USER STORY #02: View Item Details
  As an unregistered user I can view specific item details so that I can see the price, description, image, rating & available options of certain items I'm interested in.

- USER STORY #03: View Deal and Offer Items
  As an unregistered user I can easily identify new items, current deals & special offers so that I can shop the latest items or benefit from special savings on items.

***Milestone/Sprint Three User Stories***

- USER STORY #13: Search for Specific Items
  As a registered or unregistered user I can search items by name or description so that I can find specific items to purchase.

- USER STORY #14: View Searches & Results
  As a registered or unregistered user I can easily view searched items & the results so that I can easily check if items are available.

***Milestone/Sprint Four User Stories***

- USER STORY #10: Sort List of Available Items
  As a registered or unregistered user I can sort a list of the available items so that I can view categorically-sorted list to easily identify best-rated or best-priced items.

- USER STORY #11: Sort Items By Specific Category
  As a registered or unregistered user I can sort items by specific category so that I can view category-specific best-rated or best-priced items.

- USER STORY #12: Sort Multiple Categories Simultaneously
  As a registered or unregistered user I can sort multiple categories simultaneously so that I can find best-rated or best-priced items across broad categories of items, e.g. 'artwork' or 'artwear'.

***Milestone/Sprint Five User Stories***

- USER STORY #15: Checkout - Item Options & Quantity
  As a registered or unregistered user I can easily select options & quantity of items when buying so that I can ensure the correct product/quantity/options are selected.

- USER STORY #16: Checkout - View Bag Items
  As a registered or unregistered user I can view items in bag to be purchased so that I can see the total cost of purchases & all items to be received.

- USER STORY #17: Checkout - Adjust Bag Quantities
  As a registered or unregistered user I can easily adjust quantities of items in bag so that I can easily make changes to basket items before checkout.

***Milestone/Sprint Six User Stories***

- USER STORY #18: Easy Purchase Process
  As a registered or unregistered user I can easily complete the purchase process so that I can checkout quickly and hassle-free.

- USER STORY #19: Checkout - View Order Confirmation
  As a registered user I can view an order confirmation after checkout so that I can check there are no mistakes.

- USER STORY #20: Checkout - Receive Email Confirmation
  As a role I can receive email confirmation after checkout so that I can keep a confirmation of order details for my own records.

***Milestone/Sprint Seven User Stories***

- USER STORY #08: Account Registration Verification Email
  
As a registered user I can receive an email confirming account registration so that I can verify account registration was successful.

- USER STORY #09: Account User Profiles
  As a registered user I can access a personalised user profile so that I can save personal & payment info, view personal order history/order confirmations.

***Milestone/Sprint Eight User Stories***

- USER STORY #21: Admin - Add New Items
  As the site owner I can create/add new items so that I can add new products to the site.

- USER STORY #22: Admin - Update Items
  As the site owner I can update/edit existing items so that I can easily change an item's price, description, image & other criteria.

- USER STORY #23: Admin - Delete Items
  As the site owner I can delete items so that I can easily remove items no longer for sale.

***Milestone/Sprint Nine User Stories***

- USER STORY #24: Feedback - Create Comment / Review
  As a registered user I can create a comment/review on items I purchase so that I can leave feedback for other users on purchased items.

- USER STORY #25: Feedback - Update Comment / Review
  As a registered user I can update/edit comments/reviews I have previously created so that I can easily amend comments/reviews for purchased items.

- USER STORY #26: Feedback - Delete Comment / Review
  As a registered user I can delete comments/reviews I have previously created so that I can easily remove comments/reviews for purchased items.

- USER STORY #27: Feedback - Manage All Comments / Reviews
  As a registered user I can easily view a summary of my comments/reviews so that I can easily view & manage comments/reviews for purchased items.

***Milestone/Sprint Ten User Stories***

- USER STORY #28: Contact - Submit Contact Form
  As a registered or unregistered user I can submit a contact form so that I can easily get in touch with the site owner for enquiries and information.

- USER STORY #29: Contact - Message Received Confirmation
  As a registered or unregistered user I can receive a 'thank you for your message!' confirmation email so that I can be confident my enquiry has been received.

- USER STORY #30: Contact - Newsletter Sign Up
  As a registered or unregistered user I can sign up for the RJW Illustration newsletter so that I can keep updated & informed with RJWs creative & commercial activity.

## **GENERIC USER EXPECTATIONS:**

- Intuitive/conventional navigation elements

- Familiar and/or easily understandable site structure

- Responsive: access site easily on any device

- Users are offered the opportunity to register an account

- Easy shopping process to provide a good customer experience

---- 

# **UCD Phase 2: SCOPE**

## **Analysis of *User Stories:***

| OPPORTUNITY/PROBLEM  | IMPORTANCE | VIABILITY/FEASIBILITY |
|------|:------:|:------:|
| US #01 View List of Items |  5  |  5  |
| US #02 View Item Details |  5  |  5  |
| US #03 View Deal and Offer Items |  5  |  5  |
| US #04 View Purchase Total |  5  |  5  |
| US #05 Account Registration |  5  |  5  |
| US #06 Account Login / Logout |  5  |  5  |
| US #07 Account Password Recovery |  5  |  5  |
| US #08 Account Registration Verification Email |  5  |  5  |
| US #09 Account User Profiles |  5  |  5  |
| US #10 Sort List of Available Items |  5  |  5  |
| US #11: Sort Items By Specific Category |  5  |  5  |
| US #12: Sort Multiple Categories Simultaneously |  5  |  5  |
| US #13: Search for Specific Items |  5  |  5  |
| US #14: View Searches & Results |  5  |  5  |
| US #15: Checkout - Item Options & Quantity |  5  |  5  |
| US #16: Checkout - View Bag Items |  5  |  5  |
| US #17: Checkout - Adjust Bag Quantities |  5  |  4  |
| US #18: Easy Purchase Process |  5  |  5  |
| US #19: Checkout - View Order Confirmation |  5  |  5  |
| US #20: Checkout - Receive Email Confirmation |  5  |  5  |
| US #21: Admin - Add New Items |  5  |  5  |
| US #22: Admin - Update Items |  5  |  5  |
| US #23: Admin - Delete Items |  5  |  5  |
| US #24: Feedback - Create Comment / Review |  5  |  5  |
| US #25: Feedback - Update Comment / Review |  5  |  4  |
| US #26: Feedback - Delete Comment / Review |  5  |  4  |
| US #27: Feedback - Manage All Comments / Reviews |  5  |  4  |
| US #28: Contact - Submit Contact Form |  5  |  4  |
| US #29: Contact - Message Received Confirmation |  5  |  5  |
| US #30: Contact - Newsletter Sign Up |  5  |  4  |
| TOTAL: |: 150 :| 144 |

***Proposed Production:*** The project will include all the features, as identified above, in order to build the *minimum viable product* (**MVP**). Completing the work in manageable ***sprints***, organised with the help of **GitHub's** baked-in ***issues*** and ***milestones** project features*, to produce the *robust viable solution* required.  

----

# **UCD Phase 3: STRUCTURE**

## **SITE MAP**

**RJW ARTSTUFF** is organised in a Hierarchical Tree Structure to assist the site user in navigating through the site effortlessly and intuitively.

![ARTSTUFF sitemap](static/readme/pp05_wf_desktop/pp05_wf_desk_site_map.jpg)

- Header and navigation consistent site-wide

- Smooth and consistent site performance & styling across all devices

- Links and forms provide clear feedback to users

- Additional features available to users after they register and sign in

- A 404-error page is available.

## **ENTITY RELATIONSHIP DIAGRAM** 

An ***Entitiy Relationship diagram*** was created with [drawsql](https://drawsql.app/) in order to better visualise the data to be stored in the database. It demonstrates the basic design upon which the database will be built. It specifies what data entities and attributes will be stored and how they relate to eachother. The type of database being used is relational, being managed using SQLite3 during development and deployed using [ElephantSQL](https://elephantsql.com/).

![ERD](static/readme/ERD/pp05_erd.jpg)

---- 

# **UCD Phase 4: SKELETON**

## **INITIAL WIREFRAMES**

Following current conventional practice, **RJW ARTSTUFF** was designed with a Mobile First approach.

----

![Example mobile wireframe](static/readme/pp05_wf_mobile/pp05_wf_mob_sign_up.jpg) ![Example mobile wireframe](static/readme/pp05_wf_mobile/pp05_wf_mob_sign_in.jpg) ![Example mobile wireframe](static/readme/pp05_wf_mobile/pp05_wf_mob_sign_out.jpg)

----

![Example desktop wireframe](static/readme/pp05_wf_desktop/pp05_wf_desk_connect.jpg)

All wireframes generated in **[Balsamiq](https://balsamiq.com)**. A full set of wireframes can be found [**here for mobile**](static/readme/pp05_wf_mobile/) and [**here for desktop**](static/readme/pp05_wf_desktop/).


---- 

# **UCD Phase 5: SURFACE**

## **DESIGN CHOICES**

## Fonts

All fonts utilised in this project were sourced from and served by [**Google Fonts**](https://fonts.google.com):

- **Heading Font:** *Amatic SC*
  
  *Amatic SC* is a sans-serif typeface intended for display purposes, which stood out as an ideal choice for this project's header/logo when initially browsing Google Fonts for my very first Portfolio Project, [**RJW Illustration**](https://alfa23.github.io/portfolio-project-one/index.html). It works well with his brand and was an obvious choice for this project. 

- **Body Font:** *Ubuntu*

  *Ubuntu* was chosen for it's quirky typography and clean lines

![Google Fonts Choices](static/readme/colour_fonts/pp05_google_fonts.jpg)

- Several fonts were under consideration for the body font and [**Pair and Compare**](https://www.pairandcompare.net) was found to be an invaluable tool for helping with the final choice

![PairAndCompare](static/readme/colour_fonts/pp05_google_fonts_compare.jpg)

## Colours

Colours utilised were chosen with the **60:40:10 rule** in mind 

- 60% Background/Primary - **#000032** was chosen as as-dark-a-blue-to-black as possible! Wanted to avoid a completely flat black or grey site, aiming for something deep-space-ish

- 40% Body Text/Secondary: **#f8f8ff** *Ghost White* chosen as a fresh, slightly-cool-white contrast to primary

- 10% Accent/Tertiary: **#d** *Crimson* was chosen as a strong contrasting accent colour to both primary and secondary
  
  - Initially utilised as border and text secondary, text has been returned to Ghost White for client-facing copy and crimson is now primarily used for input borders and buttons. This decision was taken after testing colour contrast:

![Colours 1](static/readme/colour_fonts/pp05_color_contrast_ghost.jpg)

![Colours 2](static/readme/colour_fonts/pp05_color_contrast_accent.jpg)

## Imagery

All artwork used in this site is ***original RJW tradigital artwork***. Product mocks were generated using original ***RJW artworks*** and *royalty-free product mockup files*, sources as detailed under ***Resources Used***.

All icons provided and hosted by [**FontAwesome**](https://www.fontawesome.com/).

----

# **MARKETING**

## **Search Engine Optimisation**

***Keywords***

To improve **Google** search ratings, [**keyword research**](static/readme/seo_web_marketing_kwords/pp05_seo_keywords.pdf) was carried out using a number of tools, for example [**rankingCoach**](https://www.rankingcoach.com/), to search for relevant *short-* and *long-tail keywords* for use as **RJW ARTSTUFF** *meta tag content* in the project `head` element.

Search terms *original art prints*, *custom art garments* and *illustrator for hire* were initially used to return popular keywords. After further searching and refining, a number of *short-* and *long-tail keywords* were chosen for use in the *head element* of ***base.html***. Initial selected keywords include but aren't limited to:

- Tradigital art

- Printed t-shirt 

- Graphic hoodies 

- Commission illustration

- Cool custom canvas art

- Original artist prints 

These keywords will, however, remain a work in progress. As is normal practice, in production these keywords will be monitored (via, for example, **Google Analytics**) to determine which terms are driving traffic to the site. These terms will then be updated and tweaked, with a view to continual improvement and refinement over time. This should utlimately assist in the site ranking higher on **Google**.

As the chosen market is saturated with several large players and a plethora of small independent offerings, it was decided with the store owner to lean towards more niche and specific keywording. To this end, several extremely niche and low-scoring keywords have also been purposefully included, with the aim of hopefully seeing an increase in the popularity of some of these keywords and phrases!

![rankingCoach](static/readme/seo_web_marketing_kwords/pp05_seo_keywords-01.jpg)

## **E-Commerce Business Model**

***Company Mission & Audience***

*Who are **RJW ARTSTUFF** users?*

  **Product:** Comprising items from initial ***ARTWORK*** (limited edition prints & canvas art) and ***ARTWEAR*** (custom art printed garments - tees, hoodies & caps) categories. Potential **RJW ARTSTUFF** ***B2C users*** could be anyone - male, female, young or old - looking for *quality, original art products* as a gift or to own. 

  - Primarily **Business to Consumer**, focusing on supplying cool art to the general public

  - Prints & canvas have wide-range appeal across all age groups

  - Hoodies, tees and caps likely to appeal more to younger and millenial audiences

  - Commercial **B2B** projects *not* being ruled out, although *not currently actively targeting* this market

  **Service:** *Hire, commission a custom artwork by*, or *discuss a collaboration with* ***RJW;*** easily initiate a *custom project enquiry* by completing an online form on the site's ***Contact*** page 

  - Primarily **B2C**: Focusing on small *custom projects (portraits, original illustrations)* for interested individuals

  - Again, commercial **B2B** projects not being ruled out, although not currently actively targeting this market

*Which online platfoms would we find many **RJW ARTSTUFF** users?*

  The online market for *custom artwork products* and *artist/illustrator services* is vast and competitive: 

  - **Product:** Sites such as [**Etsy**](https://www.etsy.com/uk), [**Everpress**](https://www.everpress.com), [**Threadless**](https://www.threadless.com), [**Amazon**](https://www.amazon.co.uk), [**eBay**](https://www.ebay.co.uk) 

  - **Service:** Sites such as [**Fiverr**](https://www.fiverr.com), [**Upwork**](https://www.upwork.com), [**Creativepool**](https://www.creativepool.com)

  **RJW ARTSTUFF** will create/maintain profiles at the above sites and others - *if you can’t beat ‘em, join ‘em!* 

***Core Business Intents***

*What are the **RJW ARTSTUFF** business goals?*

  To organically develop an *online business community* that support, share and hopefully invest in ***RJW’s*** artistic endeavours, ultimately to be capable of sustaining his career as a **full-time tradigital artist**. **RJW** understands that creating, nurturing and maintaining such a community will require patience, hard work and perseverance, and is unlikely to appear overnight - *however, one always hopes for that unexpected viral success..!*  

  - **Global Brand Goals:** Fast, friendly, efficient and reliable service. Easy to use, secure and trustworthy.

  - **Product:** Good quality, great looking, well produced and finished art products. Affordability. Value for money.

  - **Service:** Reliable, quality custom art, hand produced to user specification, in a timely manner. Competitively priced.

*Which marketing strategies would offer the best way(s) to meet these goals?*

Due to reasons detailed further below, **RJW ARTSTUFF** will primarily focus on ***SEO***, ***email marketing*** and ***organic social media marketing*** through **RJW ARTSTUFF** social media channels.

***Core Marketing Strategies***

*Does **RJW ARTSTUFF** currently have an effective advertising budget?*

  No. Initially **RJW ARTSTUFF** plans to utilise as many *free* and *low-cost web marketing options* as resources & time allow for. As a one-man studio, generally with several projects underway at any given time, **RJW** rarely has the extra time required for extensive additional content creation at present. 

  **Outcome:** Both **Product** and **Service** propositions will rely initially on ***free and low-cost web marketing techniques:*** 

  - **Good SEO:** A robust initial set of short- and long-tailed keywords, which will be monitored and updated using feedback from **rankingCoach**

  - *Semi-regular, non-spammy email marketing:*

    **Product and Service:** *Email/newsletter* communications sent semi-regularly to subscribers, detailing *current offers*, *promotions* and *discounts* from across the site.

      - Perpetual ***new subscriber/first order discounts*** for both propositions

      - Regular ***new arrival*** and ***stock-clear offers*** to keep users engaged and product offerings fresh

      - ***Seasonal/event-related promotions*** for **service** proposition

  - Organic social media marketing:

      - **Product and Service:** *Email/newsletter marketing content*, refactored and posted via **RJW ARTSTUFF** social media channels, in order to target and inform *non-subscribed users*

      - Creation of a **Facebook Business Page** to leverage the exposure offered by the social media channel's huge *user base*, *sharing services* and *free marketplace features*

  - Development of *really effective content marketing strategies* for **RJW ARTSTUFF** is currently restricted by a lack of the neccessary time and budgetary resources.
  
      - Therefore the *web marketing techniques* as detailed above will be utilised *as much as possible* to *develop, support and enhance* ***customer engagement and loyalty***.

Course-related web marketing materials; [Content Considerations - Connect Page](static/readme/seo_web_marketing_kwords/pp05_connect_content.pdf) and [source support doc for ***E-Commerce Business Model***](static/readme/seo_web_marketing_kwords/pp05_web_marketing.pdf).

*Facebook Business Page Mock for **RJW ARTSTUFF***

![FaceBook Business Page](static/readme/site/pp05_facebook_business_page_mock.png)

----

# **FEATURES**

## **CURRENT FEATURES**

**Site-wide Functionality**

Perisistent header on *index/home page* appears across the site. Comprises of; a left-aligned ***home-BrandLink***; centre-aligned ***search box*** and ***main nav bar***, with links to categories and related listings; and a right-aligned set of 3 links: The leftmost links to the ***Connect*** page (no login required), rightmost links to to the ***ArtCart*** page and the centre provides a dropdown with initial options to ***Sign Up*** or ***Sign In***.

  ![Index](static/readme/site/pp05_site_index.jpg) 

***User sign up, sign in and sign out***

Consistently styled AllAuth-driven account pages.

  ![OTHER](static/readme/site/pp05_site_sign_up.jpg) 

  ![OTHER](static/readme/site/pp05_site_sign_in.jpg) 

  ![OTHER](static/readme/site/pp05_site_sign_out.jpg) 

**Full E-Commerce Functionality**

Complete User Experience to view all **RJW ARTSTUFF** products, sort by various means, add to basket, adjust bag contents and securely check out, if they so wish. User-dismissable contextual toast messaging exists site-wide for all user interactions.

  ![View all products](static/readme/site/pp05_site_products_all.jpg) View all products with integrated search & sort functionality.

  ![View detailed product info](static/readme/site/pp05_site_products_detail.jpg) View detailed info and any user feedback for a product, with options to change quantities, choose sizes where appropriate, add to bag or return to products.

  ![View ArtCart](static/readme/site/pp05_site_artcart.jpg) View ArtCart to see current items for purchase, add or remove items, checkout or return to products.

  ![Secure checkout page](static/readme/site/pp05_site_checkout.jpg) Secure checkout page powered by Stripe; requires entry of user details and valid (test: 4242 4242 4242 4242, any future date, CVC & Zip Code) card details to proceed. Final time user has the option to adjust Cart contents before purchasing.

  ![Checkout success page](static/readme/site/pp05_site_checkout_success.jpg) Checkout success page providing customers with an on-screen order summary and message that an email record will also be issued. 

**Full CRUD Functionality**

***Integrated Site Owner CRUD Functionality***

Site owner has in-browser functionality to add new products, edit existing and delete out of stock/sold out/unrequired products from the store

  ![Add a product](static/readme/site/pp05_site_products_add.jpg) Add a product page allows superusers to add Products through the browser.

  ![Edit a product](static/readme/site/pp05_site_products_edit.jpg) Edit a product page loads pre-filled with existing product data.

The ***delete functionality*** for products currently doesn't use a template page or validation method - consequently **RJW** currently needs to be sure before hitting ***delete*** on any products! This will be a primary focus for the next iteration of this project. 
      
***Client-facing User Feedback CRUD Functionality***

Full ***client-facing CRUD functionality*** is offered to users through a *product feedback system*. Once registered and logged in a ***Leave Feedback*** button is made available directly underneath the Customer Feedback section on the product detail page. A dedicated My Feedback link is also enabled in the user's My Stuff tab, where users can go to manage their posted feedbacks. In an effort to populate all products with some comments, users currently enjoy the ability to leave feedback on any product, whether they have purchased it or not. Functionality to only allow users to feedback on products they own may be introduced at a later time. 

  ![If no feedback](static/readme/site/pp05_site_feedback_none.jpg) If a user is logged in the ***Leave Feedback*** button is enabled below the comments in the ***Customer Feedback*** section. If no feedback currently exists for a product a simple *no feedback* message is displayed instead.
  ![Add feedback](static/readme/site/pp05_site_feedback_add.jpg) Clicking the link takes the user to the ***add feedback*** page, where the user is presented with the image and title of the product they are giving their feedback on.  The user can choose to post or cancel, both result in a redirect back to the product page; any just-posted feedback appears in the *Customer Feedback* section immediately.
  ![Already fed](static/readme/site/pp05_site_feedback_already_sub.jpg) Although they have the ability to feedback on any product, users are limited to one feedback per product. If they try to feedback again on a product they are refused and notified through the site's toast messaging.
  ![View feedback](static/readme/site/pp05_site_feedback_all.jpg) Users are able to view and manage their feedbacks from their My Feedback page. Clicking on the title of an existing feedback in their list, should they have any, will allow users to open and manage any specific feedbacks they have posted. 
  ![Edit feedback](static/readme/site/pp05_site_feedback_edit.jpg) When users choose to edit feedback they are taken to a pre-populated update page, where they can choose to edit & update, cancel their editing and return to My Feedback, or delete the post. 
  ![Delete feedback](static/readme/site/pp05_site_feedback_deleted.jpg) As with product deletion, feddback deletion doesn't currently employ a separate template or validation the user really wants to delete. Again, this would be a prime goal of future iterations.

**Contact & Newsletter Functionality**

Any user, registered or unregistered, has the ability to access RJW ARTSTUFF's ***Connect*** page. 

  ![Connect](static/readme/site/pp05_site_connect.jpg) The page comprises of a simple contact form and related messaging regarding initiating custom projects, a section containg a form to capture the email details of anyone wishing to subscribe to the RJW ARTSTUFF newsletter and a section of external links; Social Medias, Other Platforms RJW appears on and also to websites of some of the businesses RJW ARTSTUFF are proud to work alongside. 

  ![Connect success](static/readme/site/pp05_site_connect_success.jpg) When a user has successfully submitted a custom project message they are taken to a success page, confirming that their message has been received and informing them of what to expect next. 

  ![Newsletter](static/readme/site/pp05_site_news_sub_success.jpg) Upon successful subscription to the RJW ARTSTUFF newsletter users are notified via the site toast messaging.
  
**Other Functionality**

Users also have the ability to save their details to speed up future checkouts, if they so wish. This data is available for them to view and update on their My Profile page, available when they have logged in. This page also displays any previous order details for the customer. Clicking the order number takes the user to a copy of that original order.

  ![User profile page](static/readme/site/pp05_site_profile.jpg) User profile page.
  ![User order history view](static/readme/site/pp05_site_order_history.jpg) User order history view.
  
## ***FEATURES TO IMPLEMENT*** 

- In addition I would also like to consider implementing ***future features*** such as but not limited to:

- USER STORY #00: View FAQs
  As a registered or unregistered user I can view a FAQs page so that I can search a list of common questions about the business

- USER STORY #00: Newsletter Unsubscribe
  As the site owner I can offer newsletter subscribers the option to unsubscribe through the website so that I can improve my GDPR compliance by simplifying the users unsubscribe process further

  A link at the bottom of all email marketing will allow users to unsubscribe from the newsletter. However, a feature to allow on-site unsubscriptions, which would also help with GDPR compliance, would be desirable. 

- USER STORY #00: Live User Ratings
  As the site owner I can collect and process individual user ratings with existing product ratings so that I can update the product rating with real-time data

  At present the user feedback feature captures and stores individual user ratings; ideally these user ratings will be averaged and added to the existing product ratings 

Real-time product ratings, FAQs, TOS, T&Cs and on-site newsletter unsubs were/are all desirable additions to the site. Unfortunately these, and a few others still, fell outside the scope of this current project.

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

### DATABASE MANAGEMENT

- [**SQLite**](https://www.sqlite.com/) was used as a single-file database during development.

- [**ElephantSQL**](https://www.elehantsql.com/) A free, open-source relational database management system emphasizing extensibility and technical standards compliance: "The most advanced open-source database, hosted in the cloud." 

  Initially **Sqlite3** was used to test User Authentication, Registration & Login, and for testing the creation of product and category data. Later in development the project used both local & deployed databases and **ElephantSQL** was also utilised from that point forward.

  When the app and its models were created and implemented, `python manage.py makemigrations` was run in the terminal to create the initial model package and `python manage.py migrate` was then used to apply the model to the database and create the table. Where possible, first-time-right methodology was approached when creating the models to avoid to many alterations to the models and the database table through multiple `makemigrations` and `migrate` commands.

### VERSION CONTROL, FRAMEWORKS & LIBRARIES:

- **Git** (https://git-scm.com) was used for version control (commit to **Git** and push to **GitHub**.)

- **Gitpod** (https://www.gitpod.io/) was used to write my code; an online IDE linked to the **GitHub** repository.

- **GitHub** (https://github.com/) was used to create the repository and store the project's code after being pushed from **Git**.

- **Bootstrap Framework** (https://getbootstrap.com/) was used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.

- **Bootstrap's Imported Javascript** & **JQuery** (https://getbootstrap.com/docs/4.3/getting-started/introduction/#js) used for Responsive Navbar expand & collapse, **roundSlider** and alert messages timeout functionality.

- **Django** (https://www.djangoproject.com/) was used as the architectural engine following the *model-template-view* approach.

- **Google Fonts** (https://fonts.google.com) used for all fonts utilised in the project.

- **Font Awesome Icons** (https://fontawesome.com/icons?d=gallery) used site-wide to add icons for aesthetic and UX purposes.

### PACKAGES & DEPENDENCIES:

- **Django AllAuth** (https://django-allauth.readthedocs.io/en/latest/) used for user authentication, registration, and account management.

- **Django Crispy Forms** (https://django-crispy-forms.readthedocs.io/en/latest/) used to control the rendering of forms. 

- **Django Countries** (https://pypi.org/project/django-countries/) used to provide country choices for use with forms and a country field for models.

- **Pillow** (https://pypi.org/project/Pillow/) used to add image processing capabilities.  
 
- **Gunicorn** (https://gunicorn.org/) used as Python WSGI HTTP Server for UNIX to support the deployment of Django applications.

### PAYMENT SERVICE:

- **Stripe** (https://stripe.com/) used to process all online transactions.

### CLOUD STORAGE:

- **Amazon Web Service S3** (https://aws.amazon.com/s3/) used to store all static and media files in production.

### OTHER TOOLS AND PROGRAMS:

- **Heroku** (https://www.heroku.com/) A cloud platform as a service enabling deployment of this **CRUD application**.

- **Balsamiq** (https://balsamiq.com) used to generate mobile and desktop wireframes.

- **favicon** (https://www.favicon.cc/) was used to create a **custom favicon** for the project: ![favicon](static/favicon.ico)

- **Google Chrome Dev Tools** (https://www.google.com/intl/en_uk/chrome/) used to debug & test source code using HTML5 and to test site responsiveness, also assisted in identifying the correct style properties to override some **Bootstrap** styling.

- **amiresponsive** (http://ami.responsivedesign.is/) used to check how responsive the site is on different devices.

- **JSHint** (https://jshint.com/), [**W3C Markup**] (https://validator.w3.org/) and [**W3C Jigsaw**] (http://jigsaw.w3.org/css-validator/) used to validate all source **JavaScript**, **HTML** & **CSS** code.

- **CI Python Linter** (https://pep8ci.herokuapp.com/) ***Code Institute's*** very own linter, used to check **Python code** is consistent with *PEP8* requirements.

- **WebAIM** (https://webaim.org/resources/contrastchecker/) used to verify the contrast radio for the color on the website.

- **json formatter** (https://jsonformatter.org/) used to generate initial categories.json & products.json fixtures. 

- **Bulk Resize Photos** (https://bulkresizephotos.com/en) used to resize & optimise site & readme media.

- **ToC** (https://) used to generate ReadMe **Table of Content**.

----

# **TESTING**

## CODE VALIDATION

## W3C Validator Testing 

- HTML
  - Aside from `{% CONTROL %}`, `{{ TEMPLATE VAR }}` and other template-related errors and warnings (for expected !DOCTYPE/title and adding language attributes, etc.), no further errors were returned when passing through the official [W3C validator](https://validator.w3.org)

| .html PAGE | RESULT |
|:-----:|:-----:|
| base | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_base.jpg) |
| index | [VIEW](static/readme/code_validation/html/pp05_val-html_index.jpg) |
| signup | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_signup.jpg) |
| login | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_login.jpg) |
| logout | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_logout.jpg) |
| 404 | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_404.jpg) |
| main-nav | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_main-nav.jpg) |
| products | [VIEW](static/readme/code_validation/html/pp05_val-html_products_products.jpg) |
| product_detail | [VIEW](static/readme/code_validation/html/pp05_val-html_products_product_detail.jpg) |
| bag | [VIEW](static/readme/code_validation/html/pp05_val-html_bag_bag.jpg) |
| bag-total | [VIEW](static/readme/code_validation/html/pp05_val-html_bag_bag-total.jpg) |
| checkout-buttons | [VIEW](static/readme/code_validation/html/pp05_val-html_bag_checkout-buttons.jpg) |
| product-image | [VIEW](static/readme/code_validation/html/pp05_val-html_bag_product-image.jpg) |
| product-info | [VIEW](static/readme/code_validation/html/pp05_val-html_bag_product-info.jpg) |
| quantity-form | [VIEW](static/readme/code_validation/html/pp05_val-html_bag_quantity-form.jpg) |
| add_product | [VIEW](static/readme/code_validation/html/pp05_val-html_products_add_product.jpg) |
| edit_product | [VIEW](static/readme/code_validation/html/pp05_val-html_products_edit_product.jpg) |
| checkout | [VIEW](static/readme/code_validation/html/pp05_val-html_checkout.jpg) |
| checkout_success | [VIEW](static/readme/code_validation/html/pp05_val-html_checkout_success.jpg) |
| contact | [VIEW](static/readme/code_validation/html/pp05_val-html_contact.jpg) |
| contact_success | [VIEW](static/readme/code_validation/html/pp05_val-html_contact_success.jpg) |
| view_feedback | [VIEW](static/readme/code_validation/html/pp05_val-html_feedback_view_feedback.jpg) |
| add_feedback | [VIEW](static/readme/code_validation/html/pp05_val-html_feedback_add_feedback.jpg) |
| edit_feedback | [VIEW](static/readme/code_validation/html/pp05_val-html_feedback_edit_feedback.jpg) |
| profile | [VIEW](static/readme/code_validation/html/pp05_val-html_profile.jpg) |
| mobile-top-header | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_mob-top-head.jpg) |
| toast_error | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_toast_error.jpg) |
| toast_info | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_toast_info.jpg) |
| toast_success | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_toast_success.jpg) |
| toast_warning | [VIEW](static/readme/code_validation/html/pp05_val-html_templates_toast_warning.jpg) |
| other | [VIEW](static/readme/code_validation/html/) |
| other | [VIEW](static/readme/code_validation/html/) |
| other | [VIEW](static/readme/code_validation/html/) |
| other | [VIEW](static/readme/code_validation/html/) |
| other | [VIEW](static/readme/code_validation/html/) |
| other | [VIEW](static/readme/code_validation/html/) |

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org)

| .css PAGE | RESULT |
|:-----:|:-----:|
| base | [VIEW](static/readme/code_validation/css/pp05_val-css_base.jpg) |
| checkout | [VIEW](static/readme/code_validation/css/pp05_val-css_checkout.jpg) |
| contact | [VIEW](static/readme/code_validation/css/pp05_val-css_contact.jpg) |
| feedback | [VIEW](static/readme/code_validation/css/pp05_val-css_feedback.jpg) |
| profiles | [VIEW](static/readme/code_validation/css/pp05_val-css_profiles.jpg) |

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

## jshint Validator Testing 

- JavaScript
  - No errors were returned when passing through the [JSHint validator](https://jshint.com/)

| .js PAGE | RESULT |
|:-----:|:-----:|
| countryfield | [VIEW](static/readme/code_validation/js/pp05_val-js_countryfield.jpg) |
| stripe_elements | [VIEW](static/readme/code_validation/js/pp05_val-js_stripe_elements.jpg) |

## PEP8 Validator Testing

- PEP8
  - All Project .py files passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) without issue

| APP | .py FILE | RESULT |
|:-----:|:-----:|:-----:|
| artstuff | urls | [VIEW](static/readme/code_validation/python/) |
| bag | context | [VIEW](static/readme/code_validation/python/pp05_val-py_bag_contexts.jpg) |
| bag | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_bag_urls.jpg) |
| bag | views | [VIEW](static/readme/code_validation/python/pp05_val-py_bag_views.jpg) |
| checkout | admin | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_admin.jpg) |
| checkout | forms | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_forms.jpg) |
| checkout | models | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_models.jpg) |
| checkout | signals | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_signals.jpg) |
| checkout | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_urls.jpg) |
| checkout | views | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_views.jpg) |
| checkout | wh_handler | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_wh_handler.jpg) |
| checkout | webhooks | [VIEW](static/readme/code_validation/python/pp05_val-py_checkout_wh.jpg) |
| contact | admin | [VIEW](static/readme/code_validation/python/pp05_val-py_contact_admin.jpg) |
| contact | forms | [VIEW](static/readme/code_validation/python/pp05_val-py_contact_forms.jpg) |
| contact | models | [VIEW](static/readme/code_validation/python/pp05_val-py_contact_models.jpg) |
| contact | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_contact_urls.jpg) |
| contact | views | [VIEW](static/readme/code_validation/python/pp05_val-py_contact_views.jpg) |
| feedback | admin | [VIEW](static/readme/code_validation/python/pp05_val-py_feedback_admin.jpg) |
| feedback | forms | [VIEW](static/readme/code_validation/python/pp05_val-py_feedback_forms.jpg) |
| feedback | models | [VIEW](static/readme/code_validation/python/pp05_val-py_feedback_models.jpg) |
| feedback | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_feedback_urls.jpg) |
| feedback | views | [VIEW](static/readme/code_validation/python/pp05_val-py_feedback_views.jpg) |
| home | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_home_urls.jpg) |
| home | views | [VIEW](static/readme/code_validation/python/pp05_val-py_home_views.jpg) |
| products | admin | [VIEW](static/readme/code_validation/python/pp05_val-py_products_admin.jpg) |
| products | forms | [VIEW](static/readme/code_validation/python/pp05_val-py_products_forms.jpg) |
| products | models | [VIEW](static/readme/code_validation/python/pp05_val-py_products_models.jpg) |
| products | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_products_urls.jpg) |
| products | views | [VIEW](static/readme/code_validation/python/pp05_val-py_products_views.jpg) |
| products | widgets | [VIEW](static/readme/code_validation/python/pp05_val-py_products_widgets.jpg) |
| profiles | forms | [VIEW](static/readme/code_validation/python/pp05_val-py_profiles_forms.jpg) |
| profiles | models | [VIEW](static/readme/code_validation/python/pp05_val-py_profiles_models.jpg) |
| profiles | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_profiles_urls.jpg) |
| profiles | views | [VIEW](static/readme/code_validation/python/pp05_val-py_profiles_views.jpg) |
| rjw_artstuff | settings | [VIEW](static/readme/code_validation/python/pp05_val-py_rjw_settings.jpg) |
| rjw_artstuff | urls | [VIEW](static/readme/code_validation/python/pp05_val-py_rjw_urls.jpg) |
| rjw_artstuff | views | [VIEW](static/readme/code_validation/python/pp05_val-py_rjw_views.jpg) |
| root | custom_storages | [VIEW](static/readme/code_validation/python/pp05_val-py_root_custom_sorages.jpg) |
| root | manage | [VIEW](static/readme/code_validation/python/pp05_val-py_root_manage.jpg) |

**Google Developer Tools**

- I made use of the built-in **Chrome Dev Tools** to experiment and debug while coding, in addition to testing simulated responsive behaviour across a range of mobile and desktop devices, and finally checking all pages Performance using **Lighthouse**. 

Performance scores were persistently sub-90%, predominantly due to issues relating to waits for external resources (Stripe, Bootstrap, etc.) and 'enormous network payloads' created by the higher resolution (2048px * 2048px) product images used on-site, something the site owner is not overly keen on changing given the nature of the business.

![example lighthouse](static/readme/lighthouse/pp05_lighthouse_desk_product_all.jpg)

More **Lighthouse** test results in this folder [**here**](static/readme/lighthouse/).

**Response Testing**

In order to make sure that **RJW ARTSTUFF** was responsive to all device sizes, I used [amiresponsive](http://ami.responsivedesign.is/)

![amiresponsive](static/readme/am_i_responsive/pp05_am_i_responsive.jpg)

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
| All users can view, search and sort all products | products.html | PASS |
| All users can view product details | product_detail.html | PASS |
| All users can easily register or login to access user features | signup.html/login.html | PASS |
| All users can access the contact form and newsletter subscriptions | contact.html/contact_success.html | PASS |
| *Unregistered* users can't leave product feedback | signup.html/login.html | PASS |
| *Unregistered* users can't leave/adjust product ratings | signup.html/login.html | PASS |
| Registered users can log out easily | logout.html | PASS |
| Staff/admin users can easily create new data | add_product.html | PASS |
| Staff/admin users can easily update existing data | edit_product.html | PASS |
| Staff/admin users can easily delete existing data | edit_product.html | PASS |
| Registered users can view/add/edit/remove feedbacks | view_feedback.html/add_feedback.html/edit_feedback.html | PASS |
| Registered users can easily view and updated saved profile data | profile.html | PASS |
| Registered users can easily view their previous order history | profile.html | PASS |
| Users can easily select, add, edit & purchase products  | bag.html/checkout.html/checkout_success.html | PASS |
| Registered users can log out easily | logout.html | PASS |
| Registered users can log out easily | logout.html | PASS |

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

- Setup project **Heroku** to use **Amazon S3** and **ElephantSQL** when deployed.
 
  - Create new **Heroku app**
    - Sign into **Heroku**
    - Select *New*
    - Select *Create new app*
    - Enter a relevant app name: `pp05-rjw-artstuff`
    - Select appropriate region
    - Select the *Create app* button

  - Create & attach **ElephantSQL database**

    - Log in to **ElephantSQL** to dashboard
    - Create `New Instance` and name: `pp05_rjw_artstuff`
    - Select free plan: `Tiny Turtle`
    - Select region and data centre `EU-West-1 (Ireland) | Amazon Web Services`
    - Click `review`, check and click `Create Instance`
    - Return to dashboard, select newly-created instance; in the `URL` section click to copy `URL` to clipboard

    - Goto Heroku dashboard and open `settings` tab of **Heroku** app `pp05-rjw-artstuff`
    - Add `DATABASE_URL` Config Var and paste in **ElephantSQL** value  

  - Connect **ElephantSQL** database to **Heroku** via **GitPod**

    - In GitPod terminal type: `pip3 install dj_database_url==0.5.0 pscopg2`
    - Update `requirements.txt` with newly installed packages using terminal command `pip3 freeze > requirements.txt`
    - Import **dj_database_url** beneath `import os` at the top of `settings.py`
    - Edit `settings.py` `DATABASES` section to connect to ElephantSQL instead of local `sqlite3`:

        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.sqlite3',
        #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #     }
        # }
            
        DATABASES = {
            'default': dj_database_url.parse('your-database-url-here')
        }
    
      **WARNING:** Don't committhis file! It will be removed shortly...

    - Run migrations in the terminal using `python3 manage.py showmigrations`
    - If a list of un-checked migrations appear, run migrations using `python3 manage.py migrate`
    - Load fixtures in order, *categories* first followed by *products*
      - `python3 manage.py loaddata categories`
      - `python3 manage.py loaddata products`
    - Create a new superuser using terminal command `python3 manage.py createsuperuser`
    - To prevent exposing the database when pushing to GitHub, ammend `settings.py` and reconnect to local **sqlite** database. `DATABASE` setting in `settings.py` file should look like:

          DATABASES = {
              'default': {
                  'ENGINE': 'django.db.backends.sqlite3',
                  'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
              }
          }
    - Check **ElephantSQL** has received migrations by selecting `BROWSER` from left of the ElephantSQL database page
    - Click `Table queries`, select `auth_user` and click `EXECUTE`
    - The newly-created superuser data confirms a successful migration

    - Ammend `settings.py` to reflect the following changes:
          if 'DATABASE_URL' in os.environ:
              DATABASES = {
                  'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
              }
          else:
              DATABASES = {
                  'default': {
                      'ENGINE': 'django.db.backends.sqlite3',
                      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                  }
              }
    
    - Install gunicorn using terminal command `pip3 install gunicorn`
    - Freeze gunicorn into `requirements.txt`: `pip3 freeze > requirements.txt`
    - Create a root-level `Procfile` and create **Heroku** *web dyno* by typing:
      - `web: gunicorn pp05_rjw_artstuff.wsgi:application` on the first line of the `Procfile` 
    - Log in to **Heroku** via **GitPod terminal**: `heroku login -i` and using email and **Heroku** api key
    - Temporarily disable collect static: `heroku config:set DISABLE_COLLECTSTATIC=1 --app pp05_rjw_artstuff` in the **GitPod** terminal
    - Add **Heroku** `deployed_app_address` and `localhost` to `settings.py` / `ALLOWED HOSTS`
    - Add, commit and push all changes 
    - Push committed changes to Heroku using `git push heroku main`
    - Test!

    - Search and connect **GitHub** project repository in **Heroku/Deploy**
    - Enable `Automatic deploys` in **Heroku**/Deploy, all local **GitHub** pushes now deploy to **Heroku**
    - Goto **Amazon S3 Bucket**, create `Media` folder and import files using `upload`

    - Go back to settings.py and replace the secret key setting with the call to get it from the environment, and use empty string as a default. 
          ```
          SECRET_KEY = os.environ.get('SECRET_KEY', '')
          ```
          Set debug to be true only if there's a variable called development in the environment.
          ```
          DEBUG = 'DEVELOPMENT' in os.environ
          ```
          

## **AWS Bucket Creation**   

All static and media files in this project are stored in [Amazon Web Services S3 bucket](https://aws.amazon.com/) which is a cloud based storage service. You can create your own bucket by following these steps:   
- Go to [Amazon Web Service website](https://aws.amazon.com/) and click on Create An AWS Account, or login if you already have an account.  
- Login to your new account, go to AWS Management Console and find service S3. Click on Create Bucket.   
   - Give it a name (recommended naming your bucket to match the Heroku app name), choose region closest to you.  
   - In Object Ownership section, choose ACLS enabled. and Bucket Owner Preffered.   
   - Uncheck box 'Block All Public Access'. 
   - Check box 'I acknowledge that the current settings might result in this bucket and the objects within becoming public.'  
   - Click on Create Bucket, and your bucket is created.  
- Click on your newly created bucket, and navigate to the Properties tab. Scroll down to the bottom until you find Static Website Hosting. Click on Edit, then enable. 
   - Hosting type: choose Host a Static Website   
   - Index document: index.html  
   - Error document: error.html
   - Click on Save Changes.  
- Navigate to the Permissions tab. Scroll down to the bottom until you find Cross-origin resource sharing (CORS). Click on Edit, and paste in this Cors Configuration below, which is going to set up the required access between the Heroku app and this S3 bucket. Click on Save Changes. 
 
          ```
          [
              {
                "AllowedHeaders": [
                    "Authorization"
                ],
                "AllowedMethods": [
                    "GET"
                ],
                "AllowedOrigins": [
                    "*"
                ],
                "ExposeHeaders": []
              }
          ]
          ```   
-Still on the Permissions tab, find Bucket policy, click on Edit, and then go to Policy Generator. 
  - Select Type of Policy: choose S3 Bucket Policy   
  - Effect: choose Allow   
  - Principal: *   
  - Actions: select GetObject   
  - Fill in the Amazon Resource Name (ARN), from the Bucket ARN back in the Bucket Policy   
  - Click on the Add Statement and then Generate Policy. Copy the policy and paste in the bucket policy editor.  
  - Add a slash star on to the end of the resource key (because we want to allow access to all resources in this bucket). Click Save.

      The resource key should look like this
      ```  
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*",  
      ```  
   
- Still on Permissions tab, go to Access Control List (ACL) section, click Edit and enable List for Everyone (public access), and accept the warning box.  

- With the bucket ready, now we need to create a user to access it through another service called IAM which stands for Identity and Access Management. Go back to the service menu and open IAM.   
   a. Create a group for our user to live in.  
      Click User Groups, and then create a new group with a name you want. I gave the group the name: manage-shoes-and-more. Scroll down to the bottom and click on Create Group.     
   b. Create an access policy giving the group access to the S3 bucket that has been created.  
      - Click on Policy, and then Create Policy. Go to the JSON tab, and then select import managed policy, which will let us import one that AWS has pre-built for full access to S3. Search for S3, then import the AmazonS3FullAccess policy.   
      - Because we only want to allow full access to our new bucket and everything within it, paste the bucket ARN (from the bucket policy page in s3) in the JSON editor.

          ```
          "Resource": [
            "arn:aws:s3:::YOUR_BUCKET_NAME",
            "arn:aws:s3:::YOUR_BUCKET_NAME/*"
          ]
          ```  

      Now click on Next:Tags, then click Next:Review. 
      - Give the review policy a name and a description, then click Create Policy. The policy has now been created. 
      
   c. Finally, assign the user to the group so it can use the policy to access all our files.  
      - Go to User Groups, and select the group. Go to the Permissions tab, open the Add Permissions dropdown, and click Attach Policies.  
      - Select the policy and click Add permissions at the bottom.  
      - Create a user to put in the group, by going to the Users page, and clicking Add Users.  
      - Set a user name, give them access type: Programmatic access, and then click Next: Permissions.   
      - Check on the group that has the policy attached. Click Next: Tags, then click Next: Review, and lastly Create User.     
      - Download the csv file and save it.  


## **Connect Django to AWS Bucket**

Note: If you've forked the repository, all of these steps are already done/ written on the files. Make sure you've installed all dependencies in the requirements.txt file, add all the AWS-related Config Vars to Heroku, and remove the DISABLE_COLLECTSTATIC variable from Heroku.   

Here are the steps to connect Django to AWS:  
- Install two new packages: boto3 and django-storages. Freeze them into requirements.txt.   

   ```
   pip3 install boto3
   pip3 install django-storages 
   pip3 freeze > requirements.txt  
   ```  

- Add storages to the Installed Apps in settings.py.
- In settings.py, we need to set cache control, set bucket configurations, set static and media files location, and override static and media URLs in production. We'll only want to do this on Heroku, so add an if statement as well.

      ```
      if 'USE_AWS' in os.environ:
          # Cache control
          AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
          }

          # Bucket Config
          AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
          AWS_S3_REGION_NAME = 'YOUR_REGION'
          AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
          AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
          AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

          # Static and media files
          STATICFILES_STORAGE = 'custom_storages.StaticStorage'
          STATICFILES_LOCATION = 'static'
          DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
          MEDIAFILES_LOCATION = 'media' 

          # Override static and media URLs in production
          STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
          MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
      ```

   Set the Config Vars on Heroku. On your app's dashboard on Heroku, go to Settings and click Reveal Convig Vars. Set this variables:
   Variables | Value
   --- | ---
   AWS_ACCESS_KEY_ID | your access key id from the csv file that you've downloaded before
   AWS_SECRET_ACCESS_KEY | your secret access key from the csv file that you've downloaded before
   USE_AWS | True    

   Also remove the COLLECTSTATIC variable from the Config Vars.   

- We then want to tell Django that in production we want to use S3 to store our static files whenever someone runs collectstatic, and that we sent any uploaded images to go there as well.  
Create a custom_storages.py file in your project's root directory, and inside it, include the Static and Media Storage locations: 

      ```
      from django.conf import settings
      from storages.backends.s3boto3 import S3Boto3Storage
    

      class StaticStorage(S3Boto3Storage):
          location = settings.STATICFILES_LOCATION


      class MediaStorage(S3Boto3Storage):
          location = settings.MEDIAFILES_LOCATION
      ```  

- Finally, push these changes on Github.

      ```
      git add .
      git commit -m "Your commit message"
      git push
      ```

- Deploy *rjw_artstuff* to **Heroku**!

----

## **CHALLENGES, BUGS and FIXES**

**SOLVED BUGS**

### **Bug: %00 Errors on my deployed project
  
  • *Issue:* After local development pushes, my deployed **Heroku** started throwing 500 errors
  
  • *Fix:* I had created several new apps in my local environment and these changes were not reflected in the **ElephantSQL** databases. A chat with **Code Institute** *Tutor Support* and a migration using Heroku in the terminal thankfully solved the issue. *Phew, thank you, Ed!*

  ![DB bug](static/readme/bug/pp05_bug_1-1.jpg)
  [Further bug files for this issue](static/readme/bug/)

----
### **CONTRIBUTERS**

Other coders code that I've referenced, learnt from, been inspired by or just plain borrowed:

----

## **CREDITS**

Firstly, I'd like to thank my family and folks for putting up with me during my studies! Thanks must also go to my Mentor, Marcel, for his ongoinging support and advice. 

----

![banner](static/readme/site/pp05_readme_banner.jpg)