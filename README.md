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
1. 


## Code structure


## Current issue



## Related Links

