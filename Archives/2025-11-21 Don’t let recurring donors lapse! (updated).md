---
type: Web
authors: '[[Mark Ristaino]]'
url: >-
  https://blog.actionkit.com/dont-let-recurring-donors-lapse-updated/?utm_source=www.civicshoutnewsletter.com&utm_medium=newsletter&utm_campaign=what-happens-when-a-recurring-charge-fails&_bhlid=f7fdb2e7d6a6b921c214d184574cb76b04f71e78
published: 2025-11-21T00:00:00.000Z
created: 2026-06-30T00:00:00.000Z
tags:
  - fundraising
  - narzędzia-AI
---


*In 2021 Shannon posted the super useful [“Don’t let recurring donors lapse”](https://blog.actionkit.com/dont-let-recurring-donors-lapse/) blog post on how to recapture donors with expiring credit cards. This year, we’ve updated the walk-through to account for the numerous new features added to ActionKit since then. Enjoy!*

---

Recurring donors are often your most committed supporters — so it’s especially important not to let them lapse.

[ActionKit comes standard with about 300 built-in reports](https://docs.actionkit.com/docs/manual/developer/report_reference.html), including a few that can help you identify donors whose cards are about to expire and whose cards recently failed.

These reports are meant to be used for targeting recurring mailings, allowing you to automate the process of checking up on donors.

You can also create pages where your users can [manage](https://docs.actionkit.com/docs/manual/guide/pages.html#update-recurring-donation-pages) their existing recurring commitments (including changing their credit card number, billing address, or amount) or [cancel](https://docs.actionkit.com/docs/manual/guide/pages.html#cancel-recurring-donation-pages) them. These are called “Update” and “Cancel” page types, and you have to create one of each. In order to see their donation, a donor will have to set a password and login, but we have some tricks to make this easier as well. Read on to learn more.

Generally the workflow is eight step.

1. **Create the ActionKit page.**

Go to “pages > Add page > Update Recurring Donation” or “pages > Add page > Cancel Recurring Donation” and fill out the form.

![](https://s3.us-east-1.amazonaws.com/clientcon/images/Screenshot_2025-10-25_at_12.27.43PM.png)

**2**. **Get your donor login string**

Donors who wish to update recurring donations will be prompted to create a login in order to see their recurring donation. These account login pages are public-facing, and you can change their look and feel (You can assign a template to them on the “Account Tools” page)

![](https://blog.actionkit.com/wp-content/uploads/2025/11/image.png)

**You can make this flow easier if you pass a login string via the mailer.** The login string can link your donor directly to their donation profile without having to set a password. A login string looks like this:

```js
https://docs.actionkit.com/login/?next=/pledge/update/{{page_name}}/&i={{ user|login_string }}&l=1
```

It bypasses the account creation screen, making it much easier for a user to access their profile page. [You can read more about login strings here.](https://docs.actionkit.com/docs/manual/guide/customtags.html?highlight=%20login_string) If a user clicks into a login string url from an email sent from ActionKit, they will become logged in automatically.

Since these URLs let anyone log in as the user, you could include a warning, like “Please **don’t forward this email**: the link above is personalized, and can be used to manage your credit card info.”

**After logging in, the donor will be able to update or cancel their recurring donation.**

![](https://blog.actionkit.com/wp-content/uploads/2025/11/image-1.png)

The default recurring donation update page

**3\. Create your mailing**

Compose a mailing that briefly tells donors their cards are about to expire, how much you appreciate them, and how they can update their credit card so their donations can continue to be processed.

**4\. Link to the page you created using the login string.**

How can donors update their credit card? This is where the [Update Recurring Donation](https://docs.actionkit.com/docs/manual/guide/pages.html#recurring-donations-desc) page type comes in. Link to the “Update Recurring Donation” page you created in step 1 using the login string from step 2, similar to the screenshot below.

![](https://s3.amazonaws.com/clientcon/images/update-recurring-donation-mailing.png)

This mailing links to the Update your Monthly Donation page

**5\. Test it out!**

Set up a recurring donation of your own, then send yourself a proof of this mailing using your user ID that has this recurring donation, so you can see exactly what the process will look like to your users.

![](https://s3.amazonaws.com/clientcon/images/send-myself-proof-for-me.png)

Sending myself a proof, showing what my mailing will look like, to an email with a recurring donation

**6\. Target your mailing using the built-in targeting**

ActionKit’s built-in query “Donors Whose Cards Expire Next Month” is exactly what we need to include on the Target screen. This report finds all subscribers with an active recurring donation whose credit cards are about to expire:

![](https://s3.amazonaws.com/clientcon/images/cards-about-expire.png)

Include the “Donors Whose Cards Expire Next Month” query in your mailing

7\. **Make it recurring**

Next, on the Proof and Send screen, we’ll need to tell ActionKit we want to make this mailing recurring, which will allow us to set it and forget it.

At the bottom of the proof and send screen is an option to make this mailing recurring:

![](https://s3.amazonaws.com/clientcon/images/cards-about-expire-2.png)

When we make this mailing recurring, we can set it and forget it

8\. **Create a new recurring mailing series**

Next, we’ll either choose an existing recurring mailing series or create a new one. For this example, I’ll create a new one:

![](https://s3.amazonaws.com/clientcon/images/cards-about-expire-3.png)

In this example, the recurring mailing series only emails once per month. But other recurring mailing series can email much more frequently. Some are even configured to send every hour. If you’re using a recurring mailing series that can potentially send frequently, be sure to configure its targeting to exclude those who already received the mailing recently.

To do so, select “Recurring Mailing Series” from the *Excludes* section of the mailing and find the recurring series you want to exclude in the pulldown. Most of the time, you’ll want to exclude anyone who has ever received the series, but you can also exclude people who have received it within a designated number of days using the “Time Limited” pulldown.

![](https://blog.actionkit.com/wp-content/uploads/2025/11/image-2.png)

**Try it out!**

The example above shows how to set this up for cards that are about to expire. ActionKit also includes a built-in report for cards that have recently failed. Using this blog post, try to set up a recurring mailing for recently failed cards, too!

---

Interested in scheduling a demo with ActionKit? [Let us know!](mailto:demos@wawd.com)
