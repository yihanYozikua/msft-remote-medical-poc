# MSFT Remote Medical POC
#### Author: Yvonne Hsiao, Vivian Chan

The POC for remote medical clinic.
This code demonstrates a system where once the email, start date and end date is entered, the system sents an email with a teams link to the entered email address.
Currently, there are issues in generating links.
We will adress this issue in details in the following document.

## How to run the code

First, run
```
git clone ....
cd msft-remote-medical-poc
```
Then, you will need to add a file named `oauth_settings.yml`, and add the following file into it.
```
app_id: "[app_id]"
app_secret: "[app_secret]"
redirect: "http://localhost:8000/callback"
scopes:
  - user.read
  - mailboxsettings.read
  - calendars.readwrite
  - onlinemeetings.readwrite
authority: "https://login.microsoftonline.com/common"
```
Note that the `app_id` and `app_secret` needs to be filled out.
To get the two ids, you will first need a [Azure Portal](https://portal.azure.com/).

In the Azure portal, please follow these steps:
1. Select `Azure Active Directory` in the side bar.

![](https://i.imgur.com/W9SXCXl.png)

2. Select `App registration` in the side bar.

![](https://i.imgur.com/yMW7WdE.png)

3. Click `New registration`

![](https://i.imgur.com/tJmP8tJ.png)

4. Fill out the form as shown in image and press `Register`

![](https://i.imgur.com/XRsyRzj.png)

5. It will return to the newly created registration. The `[app_id]` is the value in the red box.
> NOTE that the square bracket is NOT needed in the file.

![](https://i.imgur.com/O3KZ8D4.png)

6. Select `Certificate & secrets` from the side bar and add a `New Client Secret`.

![](https://i.imgur.com/ZnnClmj.png)

7. After filling out the description and clicking `Add`, 
The `[app_secret]` will be in the red box as shown.

![](https://i.imgur.com/hQcbvu3.png)

After completing the `oauth_settings.yml` file, open the terminal and run this script under the `msft-remote-medical-poc` file.
```
python3 main/manage.py runserver
```


## Code structure

Aside from the [tutorial](https://docs.microsoft.com/en-us/graphtutorials/python), we modified `main/tutorial/graph_helper` and `main/tutorial/views.py` to create our own function `create_meeting`.

The resulted link in `create_meeting` gets send back to line 129 in `views.py`.
The link is later on passed to `create_event` to become the content of the email.


## Current issue

The API that is supposed to return the meeting link currently returns a 400 error.
The error message is as below.
```
{"error":{"code":"General","message":"Request payload cannot be null.","innerError":{"request-id":"034a7e3d-5b9d-4555-927d-3a44b7d5052c","date":"2021-06-29T17:10:43","client-request-id":"034a7e3d-5b9d-4555-927d-3a44d7d3052c"}}}
```

> NOTE: After solving this error, please modify line 262 in `graph_helper.py` into the responsed link. It is set to no link recieved now because the API isn't working.g


## Related Links

[Build Python Django apps with Microsoft Graph](https://docs.microsoft.com/en-us/graphtutorials/python)

[Create onlineMeeting](https://docs.microsoft.com/en-us/graph/api/application-post-onlinemeetings?view=graph-rest-beta&tabs=javascript)

