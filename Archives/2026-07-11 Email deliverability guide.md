---
type: "Web"
authors: "[[ECDA]]"
url: "https://www.centerfordigitalaction.eu/resources/technology/email-deliverability-guide?source=newsletter&email_referrer=email_3305908&email_subject=hows-your-content-looking&can_id=32cae499f95a9349c734a72403321b9c&link_id=12"
published:
created: 2026-07-11
tags:
  - "digital-campaigning"
  - "fundraising"
---


Written by the European Center for Digital Action

## Introduction

**Email deliverability is the ability to successfully land an email in the recipient's primary inbox, rather than having it blocked by an ISP (Internet Service Provider) or routed to the spam, junk, or promotions folder.**

**This guide covers how to ensure your emails are delivered to your supporters inboxes including an overview to deliverability, steps to take when setting up a new mailing software, indicators to assess your list health and tips to maintain a healthy list.**

![](https://static.wixstatic.com/media/af4285_5a273bac0a1a4fcd8d014ed8ed61a066~mv2.jpg/v1/fill/w_950,h_584,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/af4285_5a273bac0a1a4fcd8d014ed8ed61a066~mv2.jpg)

## Why is email deliverability important?

**Emails are the most effective way to directly communicate with a large number of supporters; everyone has an email address, messages can be highly personalized, and with mass mailers we can see a lot of information about how our supporters engage with those emails.**

**But sending your email to a supporter is not the whole story, you must also consider email deliverability which includes landing in the primary inbox, avoiding ending up in spam, the promotions folder or even being blocked.**

## Vocabulary

- ##### Email deliverability:
	**is the ability to successfully land an email in the recipient's primary inbox, rather than having it blocked by an ISP (Internet Service Provider) or routed to the spam, junk, or promotions folder.**
- ##### Domain:
	**A domain name is your website’s name. It’s the address where people can access your website. Ours is** [**centerfordigitalaction.eu**](http://centerfordigitalaction.eu/)
- ##### DNS:
	**Domain Name System. It’s like a phonebook for the internet. It contains all the domains across the internet.**
- ##### SPF:
	**Sender Policy Framework. SPF defines which IP addresses can send emails from your domain. It lets the owner of the domain specify which servers can send mail from their domain.**
- ##### DKIM:
	**DomainKeys Identified Mail. It links your domain to the emails you send, which allows your organization to take responsibility for a message that can be verified by mailbox providers. It’s pretty complicated, but it basically prevents the “bad guys” from impersonating you as an email sender by letting the recipient’s server check if the sender was really you or not. This means your emails are more likely to get delivered (and not go to spam).**
- ##### DMARC:
	**Domain-based Message Authentication, Reporting, and Conformance. This tells email providers what to do if an email fails DKIM or SPF authentication. It's only required for organizations sending with lists larger than 5,000.**

## Email deliverability and setting up/migrating to a new mailing software

**We recommend using ActionNetwork, a tool developed by organizers for organizers and available only to progressive organizations. If you are using other tools, however, the basic rules are more or less the same.**

1. ### Buy a domain
	**Getting a** [**domain**](https://www.godaddy.com/) **is essential for managing an email list, in addition to having a more professional look, allows you to set all the parameters necessary to ensure maximum deliverability.**
2. ### Set up
	**Now that you own your domain and have connected it to ActionNetwork or another tool, you need to install DKIM and SPF. If you have a list of 5,000 or more contacts, you will need to install DMARC as well.**
	**Setting up is dependent on what mailer you use and you’ll need to use their dedicated helpdesk or contact them directly for support:**
	- **If you are using ActionNetwork in partnership with ECDA, our IT team will help you set everything up during the onboarding process.**
		- **If you aren’t working with ECDA,** [**you can find a detailed guide here**](https://help.actionnetwork.org/hc/en-us/articles/360014433271-Installing-DKIM-SPF-and-DMARC-records) **on how to install and set up DKIM, SPF & MARC on ActionNetwork.**
		- **If you are using other tools, you will find detailed guides on how to set everything up on their help pages.**
	**Want to check if your DKIM, SPF and DMARC is set up correctly? Check using a deliverability checker** [**like this one.**](https://www.inboxally.com/email-spam-checker)
3. ### Warm up your contact list
	**If you have existing contacts, whether you are migrating to a new mailing software or setting up your first mailing system it is important to test and warm up the list, especially if some time has passed since the last time you sent an email to them. To do this, divide the list into small random groups and send an email to the first group, check the data (as per our table below), and slowly increase the number of mailings over a few weeks.**
	**For example, if you have 20,000 contacts, you can start by sending a first email to 500 contacts; if the data is good, the next day you can go up to 1,000, and so on until the entire list is completed. At the end of this process, you must eliminate all bouncing addresses. You will also have created two main targets: a “warm” list of people who opened at least one email you sent, and a “cold” list of people who have a valid email address but have not opened the** **email.**

How to remove email addresses that bounce

- **Create a Report or Query in Action Network:**
	- **Create the report by filtering by Subscription Status.**
		- **To see the exact reason for the bounce, include the Subscription Detail field in your report.**
		- **This will display the actual bounce message error code returned by the recipient's mail server.**
		- **Remove the bounced emails from your subscriber list**

## How do you know if your emails are being delivered to the primary inbox?

**Having a healthy email list is one of the most important factors for email deliverability. We have made a handy table to help you know if your list is healthy or not. You need to monitor your list health and make sure each parameter is at least "okay."**

![](https://static.wixstatic.com/media/af4285_0f226dc020854fdf9632c975e48dbd10~mv2.png/v1/fill/w_898,h_336,al_c,lg_1,q_85,enc_auto/af4285_0f226dc020854fdf9632c975e48dbd10~mv2.png)

**If the numbers aren’t good, it’s not a big problem, but there are some things you’ll need to do to improve those numbers and make sure your messages end up in your activists’ inboxes.**

## Best practices for deliverability

### 1\. Good opt-in policies

**This is a legal requirement under GDPR, but it is also important for having a healthy list. You want to be sure that people really want to receive communications from you and that they can unsubscribe at any time. It is always better to have one fewer person than someone who reports you for spam.**

### 2\. Have a good welcome sequence

**When people join your list, it is good to have a series of automatic emails that introduce them to your organization, what your goals are, etc. People feel more involved and are more likely to open your emails.**

### 3\. Remove or reactivate inactive users

**You can create automations to remove from the list all people who have never opened an email in the last 6 months/1 year, or you can set up a reactivation automation to send an email to those who haven't opened emails for a long time before removing them.**

### 4\. Create content that engages people

**Emails are a great way to build a relationship with people, not just for sending vertical top-down communications. Include clear calls to action in your emails to activate the people who receive them.**

### 5\. Create the right target

**ActionNetwork (and other tools) allow you to divide your list into smaller segments using many different parameters (interactions, people who open emails more or less, but also based on specific interests, such as who signed a petition, or geographic, like who lives in a certain area). Send the communication to the right person, and you will get great results!**

### 6\. Let the numbers guide you!

**Always check the statistics of the emails you send. If the data is good, according to the parameters we indicated at the beginning, everything is fine. Otherwise, start over: warm up your list, create more precise targets, etc.**

## Related resources

- [**Everything about writing emails**](https://www.centerfordigitalaction.eu/toolbox/email/everything-email)
- [**Action Network tutorials**](https://www.centerfordigitalaction.eu/toolbox/technology/an-email-tutorial)
- [**AN Help Center**](https://help.actionnetwork.org/hc)
- [**A/B Testing**](https://www.centerfordigitalaction.eu/resources/technology/ab-testing)

**If you need more support and guidance for your organization, party or union, check out our upcoming trainings or reach out directly to us at** [info@centerfordigitalaction.eu](mailto:info@centerfordigitalaction.eu)