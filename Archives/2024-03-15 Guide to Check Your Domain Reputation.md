---
type: Web
authors: '[[Brian Godiksen]]'
url: >-
  https://www.socketlabs.com/blog/google-postmaster-tools/?utm_campaign=deliverability_rate&utm_medium=blog&utm_source=senditright
published: 2024-03-15T00:00:00.000Z
created: 2026-04-27T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
---


<iframe frameborder="0" title="Submit HubSpot product feedback" src="https://app.hubspot.com/feedback-web-fetcher"></iframe>

[![SocketLabs Logo](https://www.socketlabs.com/wp-content/uploads/2024/04/logo-dark.svg)](https://www.socketlabs.com/)

## How to Check Your Domain Reputation with Google Postmaster Tools

Google released a new version of Google Postmaster Tools this week, ostensibly to better support bulk senders in the wake of their [new bulk sender requirements](https://www.socketlabs.com/blog/first-2024-priority-meeting-google-and-yahoo-email-standards/) they began enforcing in February 2024. Now senders will have an easier time understanding whether or not they’re compliant with the rules. Thanks, Google! It’s a little hard to find the new dashboard, so **[click here to go directly there](https://postmaster.google.com/v2/sender_compliance)**.

![](https://www.socketlabs.com/wp-content/uploads/2021/08/image-3.png)

There are a few important things to note.

- Only domains that sent more than 5,000 messages to Gmail in a single day since January 1, 2024, will have data on their compliance page.
- There is no such thing as sub-domain level compliance with Google. So, if you pick a subdomain (marketing.example.com), you are still viewing the compliance status of the parent domain (example.com).
- In the same way that legality doesn’t necessarily equal inbox placement, compliance with Google’s new policies does not mean your messages are guaranteed to reach the inbox. There are hundreds of factors that go into how they view you as a sender; they’re only reporting on a few.

Stay tuned, as you can see they’re planning to add more data visibility in the future!

***Original content below:***

The mindboggling complexities of delivering email are what make our tagline “The Science of Hitting the Inbox” so appropriate. Maintaining a great sending reputation for our shared IPs is one key aspect of this science. But even more critical is a sender’s own reputation. As this article explains, your reputation at Google is a performance driver you can see and manage…and this week’s [Google Workspace service outages](https://www.zdnet.com/article/google-heres-what-caused-our-big-global-outage/) offer us a reminder of why.

Google plays a pervasive role in global business communications – and the [Google Workspace service outages](https://www.zdnet.com/article/google-heres-what-caused-our-big-global-outage/) illustrate the degree of disruption caused when email can’t be delivered to Gmail accounts. Thankfully, Socketlabs was able to make rapid adjustments to minimize the impact on our customers. However, as the incidents remind us, Google inboxes are used by hundreds of millions of businesses and consumers. That’s why you need to manage your email delivery reputation at Google to ensure your email is viewed positively by Gmail inboxes. The good news? As the industry leader, Google’s filters and standards set a high bar. If you can build a strong sender reputation with Google, your reputation and ability to inbox with other ISPs is also greatly enhanced.

### How to Check Your Domain Reputation with Google Postmaster Tools

Google Postmaster Tools (GPT) is a free service from Google that provides email senders with insights and analytics about their email processing and deliverability. Utilizing Google Postmaster Tools, domain owners can retrieve data in aggregate regarding spam complaint rates, IP reputation, domain reputation, feedback loops, delivery errors, authentication, and transit encryption.

Google Postmaster Tools helps answer the questions like “What is my IP reputation at Google?” While Google provides helpful documentation, they leave some ambiguity that we can help clear up. In this blog we are going to cover what the Google Postmasters Tools are, how you get access, how you can use them, and other questions that don’t specifically get answered elsewhere.

### What Are Google Postmaster Tools?

Google Postmaster Tools is a completely free set of email analytics tools that allow domain owners to monitor important factors associated with their email performance through Gmail. The tools give senders insight into important metrics that can help identify problem areas in their email sending practices and fix these areas to improve overall success rate and deliverability. Once the sender sets up their account and verifies their domain, they have free access to the following information:

- Domain Reputation
- IP Reputation
- Spam Rate
- Feedback Loop
- Authentication
- Encryption
- Delivery Errors

There are a few caveats to understand regarding all these data points and metrics. First is that Google Postmaster Tools only reports on messages that they successfully associate to a domain via either SPF or DKIM authentication. Organizations that do not properly authenticate their mail with their own domain are not able to access this data.

Next, is there a certain minimum daily email volume threshold for data to populate in the Google Postmaster Tools. This means very small senders may not have data appear in their reporting dashboard. Google doesn’t publish the specific threshold, but we’ve found our customers sending more than 100 messages per day to unique Gmail users will reliably have reputation data generate for the day. Mail sent to Google Workspace (formerly G Suite) does not accrue in the Google Postmaster Tools platform, as only messages to @gmail.com users will be used in the calculation of most metrics provided by Google Postmaster Tools.

Reports generated by Google update once per day providing insights into the prior day’s performance. We’ve found data is usually populated by around 12:00PM Pacific or 7:00PM UTC. So there is a lag in the availability of data. This delay of insights into performance means that Google Postmaster Tools can not instantaneously be used to gauge performance of a specific campaign per-se. Realistically, the tool is much better suited for tracking high-level performance over time.

This brings us to our final caveat, which is data is only provided in aggregate. This leaves lots of ambiguity to the data that they provide, for example – rather than give you a score of 0-100, Google will bucket IPs and Domains into groups such as “High” or “Medium” performance tiers. Let’s first learn how to get access to your data and then break down the tiers you may encounter!

### Getting Access to Google Postmaster Tools

The process of using Google Postmaster Tools all starts with having a Google account and validating your ownership of sending domain(s). The first step is to visit the website for Google Postmaster Tools and sign-in to your Google Account.

**[Click right here to get started.](https://postmaster.google.com/)**

Once signed-in, if you haven’t verified ownership of any domains previously, you’ll be asked to add your first domain.

![set up google postmaster tools](https://www.socketlabs.com/wp-content/uploads/2020/08/setup1.png)

If you already have a domain verified, you can add additional domains using the red plus icon in the lower right-hand corner of the page.

![setup google postmaster tools](https://www.socketlabs.com/wp-content/uploads/2020/08/setup2.png)

Once you’ve entered your first domain, Google will provide you with the unique DNS record that you will need to create to verify ownership. The primary verification method that Google presents is a DNS TXT record. They also indicate a secondary verification method of CNAME record. Due to the general bloat of DNS TXT records, SocketLabs recommends that everyone uses the DNS CNAME verification method.

It may take some time before Google can verify the DNS record. You’ll see the domain in your management list, but access to the data is not provided until the DNS records are verified.

![postmaster tools setup](https://www.socketlabs.com/wp-content/uploads/2020/08/setup4.png)

You see the domain status flip to “Verified” once the DNS records have been properly published.

![google postmaster tools setup guide](https://www.socketlabs.com/wp-content/uploads/2020/08/setup5.png)

**It is critical that you DO NOT delete the DNS record once it is verified**. Google will re-verify the DNS record exists every month. If verification fails, access to the data for the domain is removed from the Google account.

This is a great moment to point out that while we always encourage you to actively review your raw GPT data, our [StreamScore uses their information to help us calculate your score](https://www.socketlabs.com/hub/streamscore/). So, even if you’re not checking this daily, the evolving data in there is impacting your StreamScore and as such, it will reflect if something is going awry.

### Sharing Access Within your Organization and with SocketLabs

Once you’ve verified ownership of your domain, you can manage and delegate access to Google Postmaster Tools to others. Providing access to all necessary stakeholders is essential to ensure the data is properly being monitored. To start sharing access with others you can follow these steps:

- Sign-in to Gmail Postmaster Tools – https://postmaster.google.com
- Hover your cursor over the domain for which you want to share access
- On the right side of the list item, click the “⋮” options menu and click “Manage Users” ![google postmaster tools access](https://www.socketlabs.com/wp-content/uploads/2020/08/setup6.png)
- Additional users can be added by clicking the red “+” button in the lower right-hand corner of the screen.
- In the pop-up wizard, add the email address of the user you’d like to have access. For SocketLabs customers sharing access with SocketLabs the following address should be added \[ GPT@socketlabs.com \]

SocketLabs is excited to be building an integration directly with Google Postmaster Tools that will require you to share access for the functionality to work. Sharing access with SocketLabs also helps our team of email experts provide help if you encounter delivery issues to Gmail, and help monitor your service performance. Once you share access with SocketLabs please send an email to support@socketlabs.com so we can start monitoring this data for your account.

### The Reputation Tiers

Now that you have access to Postmaster Tools, the first thing that we recommend you dive into is the IP and Domain reputation insights. When providing reputation data, Google Postmaster Tools categorizes domains and IPs into one of four buckets – High, Medium, Low, and Bad. Google defines each in their documentation as:

***High****: Has a good track record of a very low spam rate, and complies with Gmail’s sender guidelines. Mail will rarely be marked by the spam filter.*

***Medium****: Known to send good mail, but has occasionally sent a low volume of spam. Most of the email from this entity will have a fair deliverability rate, except when there’s a notable increase in spam levels.*

***Low****: Known to send a considerable volume of spam regularly, and mail from this sender will likely be marked as spam.*

***Bad****: A history of sending an enormously high volume of spam. Mail coming from this entity will almost always be rejected at SMTP or marked as spam.*

One little known secret about these buckets that we can share from our experience with these tools is that the buckets once had different names. During its beta testing phase, Google Postmaster Tools used the following bucket names:

**Beautiful** (now High)

**Good** (now Medium)

**Bad** (now Low)

**Ugly** (now Bad)

You can actually still see a trace of this in the URL query string parameters within GPT.

![](https://www.socketlabs.com/wp-content/uploads/2020/08/setup7.png)

We’ve found that knowing the original bucket names helps senders be more accepting of their “Medium” categorization, as this is a bucket many marketers find themselves in. This also helps us here at SocketLabs in forming our recommendations to our customers. We suggest that they maintain High or Medium reputations for their domains and dedicated IPs to ensure reliable inbox placement rates.

How does reputation correlate into actual performance? For research we conducted and presented during our Summer of 2020 deliverability webinar series, we found drastic performance differences in the reputation buckets, especially at the top and bottom buckets. The following slide excerpt shows the average unique Gmail open rate for customers sending on a dedicated IP address in the corresponding reputation bucket.

![](https://www.socketlabs.com/wp-content/uploads/2020/08/setup8.png)

I think the biggest take-away here is that Bad reputation IP addresses don’t reach the inbox at all, and that the Low and Medium reputation buckets can still reach the inbox, but with obviously decreasing rates of success. Since our analysis only looked at IP reputation, it is very likely the other factors like Domain reputation influenced the success for messages sent by the IPs in these buckets. This is why low IP reputation senders are able to still achieve unique open rates at ~17%.

Now that we have a full understanding of these reputation buckets, let’s take a look at how the tool presents this data and what other things you need to know about each data point.

### Domain Reputation

![postmaster domain reputation](https://www.socketlabs.com/wp-content/uploads/2020/08/domain-rep.png) The most heavily weighted metric by the Gmail spam filters when determining inbox vs. junk folder message placement is domain reputation. So, it is no surprise that this metric is the most frequently asked about of all the data points provided by Google. For many senders, especially those using shared IPs for the delivery of their messages, there is a reliance on their domain reputation to ensure successful delivery of messages. This makes it one of the most important metrics to monitor.

We find that performance begins to significantly tail off at the Low or Bad reputation tiers. Senders with domains in these tiers will want to look at their email practices and adjust accordingly. It is important to note that the domain reputation in Google Postmaster is only for the domain that was configured in the set-up process, and it is derived from an analysis of all authenticated messages sent to Gmail. If a single given domain sends multiple streams of authenticated messages – transactional, marketing, and personal then this domain reputation will be an aggregate of performance across all of these streams. This includes mail sent across different vendors or platforms, assuming messages are using SPF or DKIM authentication.

While Google presents this data on a day-to-day basis, we find that the actual calculation is based on a trailing period of time. Messages sent weeks or months ago may still be impacting the reputation Google calculates for you today. We believe the reputation of prior days slowly trails off in terms of its weight, with most recent messages bearing the most weight. Ultimately this stabilizes the data and prevents drastic increases or decreases. This also means that changes to sending practices may take significant time to be realized in the data displayed in Google Postmaster Tools.

![](https://www.socketlabs.com/wp-content/uploads/2020/08/setup9.png)

For a more finite analysis, you can also add sub-domains to Google Postmaster Tools. Once you’ve verified ownership of an organizational domain, all sub-domains can be added and are instantly verified without any additional DNS records being created. The reputation of all sub-domains will always automatically bleed/aggregate up to the organizational domain, but you can monitor performance on individual sub-domains as well. Keep in mind, the sub-domain must be used in the authentication of messages in order for a reputation to be calculated. For example, SocketLabs customers can add their Custom Bounce Domain to GPT to calculate SocketLabs specific domain reputation performance.

### IP Reputation

IP reputation, like domain reputation will help provide insights regarding the success of your messages. The higher your reputation, the more mail is landing in Gmail inboxes. It is important for senders that are monitoring this metric to understand if the IP addresses listed in GPT are dedicated or shared IP addresses. Dedicated IP addresses obviously more accurately and directly reflect performance. The reputation of Shared IP addresses may not be a direct reflection of the performance of a sender. It is still important to monitor though as it may indicate potential performance issues caused by those the IP address is shared with on the given service. Over 97% of shared IP addresses operated by SocketLabs maintain a “High” postmaster reputation at Google, the rest in the “Medium” tier. We closely monitor and manage the performance of our shared IP addresses to ensure excellent performance for all customers.

![postmaster ip reputation](https://www.socketlabs.com/wp-content/uploads/2020/08/ip-rep.png)

One of the drawbacks to the IP reputation insights offered by Google are the means in which they visualize the data for users. For each day, Google presents a bar that represents the count of how many IP addresses fall into each category. This can be extremely misleading as an organization that sends mail across 2 IP addresses where one that sends 10 million messages per day with a bad reputation and one that sends 5 thousand messages per day with a good reputation, each will be weighted equally with 50% of the graph. Beyond the lack of volume being incorporated to the visual representation, it is nearly impossible to track a single IP address over time in the visualization presented by Google.

### User Reported Spam Rate

The User Reported Spam Rate page in Google Postmaster Tools helps senders identify the rate at which their messages are being marked as spam by recipients. Unlike most other large mailbox providers, Google does not offer a recipient specific feedback loop service. This means that data about individual users that click spam is not available. They only provide this data as an aggregate rate. This metric is essentially equivalent to the compliant rate generated by SocketLabs in your Control Panel. We recommend senders keep their User Reported Spam Rates at 0.0% or 0.1%.

![](https://www.socketlabs.com/wp-content/uploads/2024/03/image-27.png)

Because the reporting is so high level, you will not get too much additional information on your email other than X% of your total messages are being moved from inbox to the spam folder by recipients. Most SocketLabs customers achieve a 0.03% compliant rate or below, and that’s what Google has specified as their ideal threshold as well.

Some good senders may see spikes in this data, but we’ve often found they’ve correlated to send volume decreases. Since complaints are asynchronous events, if you send a large campaign (100k+) on a Tuesday, but only send a hundred messages on Wednesday, a handful of complaints from Tuesday’s campaign that are initiated by users on Wednesday could drive your User Report Spam Rate on to be confusingly high on Wednesday. For consistent large volume senders this metric should remain fairly consistent.

### Feedback Loop

The Google Postmaster Tools Feedback Loop (FBL) is the only feature offered by Google that pre-dates the launch of the postmaster tools. It was originally launched in 2014 as a mechanism for high volume senders like SocketLabs and other ESPs to identify abusive accounts. The feedback loop is not like the traditional FBLs offered by other mailbox providers like Microsoft’s Hotmail/Outlook or Verizon Media. The Google Feedback Loop does not provide details about specific individuals that mark messages as spam. ![postmaster feedback loop](https://www.socketlabs.com/wp-content/uploads/2020/08/feedback-loop.png)

The Google FBL relies on the process of tagging messages with group identifiers. Identifiers are added to a special message header before being sent. If any group identifier is present in an excessive ratio of complaints, then Google will list the identifier along with the rate at messages tagged with that identifier were marked as spam. All data is presented in the Google Postmaster Tools web interface, and no actual email Abuse Reporting Format (ARF) messages are sent. SocketLabs automatically adds identifiers to every message for customers sending through its cloud services. The identifiers that we automatically add are the ServerID and MailingID.

When Google tags an identifier this implies that you need to take some sort of action to prevent the same type of mail from generating the same reaction. Ignoring feedback loops alerts will lead to that group or stream of email messages consistently being placed in the spam folder. You can however avoid this outcome if you are continuously monitoring and resolving issues that are identified by these feedback loops.

It is also important to note that messages Google is already placing in the junk folder is unlikely to generate a feedback loop. Mail that is already in spam cannot be marked as spam (again) by recipients to create a feedback loop. Senders with a Bad or Low reputation are therefore much less likely to generate a feedback loop.

### Delivery Errors

When Google rejects a given message, whether temporarily or permanently, these events are logged and the ratio for which they occur is displayed in the Delivery Errors postmaster tools page. Much of this data may already be available to senders in reports like the failures report offered by SocketLabs.

![](https://www.socketlabs.com/wp-content/uploads/2020/09/Google-Postmaster-Tools-Delivery-Errors-blog-2048x1509.jpg)

The most common types of delivery errors typically noted in the dashboard and can include malicious attachments, DMARC policy issues, suspected spammy content, and receiving/sending rate limits being exceeded. The delivery errors section will not tell you if you are outright blocked due to an extremely reputation because Google will reject messages from blocked IPs before any authentication occurs, and as previously stated, Google Postmaster Tools only reports on mail which can be authenticated back to the configured domain(s).

**Encryption**

In the encryption dashboard you can see the rate of success your domain has communicating with Google TLS encryption. Google provides this data for both messages sent to your domain and received by your domain. This dashboard will always show a 100% inbound TLS success rate for all mail sent by SocketLabs, as we honor the MTA-STS policy published by gmail.com.

### Authentication

The authentication dashboard shows you the success rate of SPF, DKIM and DMARC for your messages. This dashboard can be a bit confusing or misleading, as in order for data to populate in Google Postmaster Tools proper authentication must have been applied to a message. This dashboard is to best identify spikes in the failure rate of a given authentication mechanism. For example, if SPF authentication passes on a given message, but DKIM fails, then this insight will appear in the Google Postmaster dashboard. If both SPF and DKIM fail, then the data for this message will not appear in this report.

![](https://www.socketlabs.com/wp-content/uploads/2020/09/Google-Postmaster-Tools-Authentication-blog-2048x797.jpg)

### Does Google Postmaster have an API?

Yes, Google recently announced that there is a Postmaster API that allows users programmatic access to all of the areas mentioned above: IP reputation, domain reputation, spam, errors, feedback loop, authentication, and encryption. Here at SocketLabs we have implemented some basic tools around this API for robust internal monitoring and reporting tools and we look forward to bring the data and insights to customers directly in the SocketLabs Control Panel and as part of the SocketLabs StreamScore.

### Using Google Postmaster Tools to Improve Your Email Deliverability

Using Google Postmaster tools helps senders better understand their email efforts with high-level reporting on important metrics. Whether you’re looking for how to check your domain reputation or trying keep an eye on your encryption and authentication, Google Postmaster Tools help all high-volume senders get more insight into their email. It’s even free.

Remember, we track this information for you directly within your SocketLabs dashboard, as part of our proprietary StreamScore. [Learn more about how StreamScore can improve your email performance](https://www.socketlabs.com/blog/streamscore-email-deliverability-solution/) or reach out to us directly so we can show you the best ways to utilize your score. [Let’s Talk Email.](https://www.socketlabs.com/contact/)

#### Categories

- [Transactional Email](https://www.socketlabs.com/blog/category/transactional-email/)
- [Tools](https://www.socketlabs.com/blog/category/tools/)
- [SMTP](https://www.socketlabs.com/blog/category/smtp/)
- [Service Provider](https://www.socketlabs.com/blog/category/service-provider/)
- [Product Updates](https://www.socketlabs.com/blog/category/product-updates/)
- [On-Demand](https://www.socketlabs.com/blog/category/on-demand/)
- [News](https://www.socketlabs.com/blog/category/news/)
- [Migrations](https://www.socketlabs.com/blog/category/migrations/)
- [Integrations](https://www.socketlabs.com/blog/category/integrations/)
- [Hurricane MTA Server](https://www.socketlabs.com/blog/category/hurricane-mta-server/)
- [Events](https://www.socketlabs.com/blog/category/events/)
- [Email Marketing](https://www.socketlabs.com/blog/category/email-marketing-2/)
- [Email Analytics](https://www.socketlabs.com/blog/category/email-analytics/)
- [Developers & APIs](https://www.socketlabs.com/blog/category/development/)
- [Deliverability](https://www.socketlabs.com/blog/category/deliverability/)
- [Customer Experience](https://www.socketlabs.com/blog/category/customer-experience/)
- [Community](https://www.socketlabs.com/blog/category/community/)
- [Best Practices](https://www.socketlabs.com/blog/category/best-practices/)
- [Authentication & Security](https://www.socketlabs.com/blog/category/authentication-security/)

<iframe src="https://app.hubspot.com/conversations-visitor/5046138/threads/utk/ae47fc7f06614f2584398f96cf620e93?uuid=3a54980ffac44d588eeb0a6fffdb52cf&amp;mobile=false&amp;mobileSafari=false&amp;hideWelcomeMessage=false&amp;hstc=257878996.5f7a8dac7988abbddb7c85a8820f7202.1777314367729.1777314367729.1777314367729.1&amp;domain=socketlabs.com&amp;inApp53=false&amp;messagesUtk=ae47fc7f06614f2584398f96cf620e93&amp;url=https%3A%2F%2Fwww.socketlabs.com%2Fblog%2Fgoogle-postmaster-tools%2F%3Futm_campaign%3Ddeliverability_rate%26utm_medium%3Dblog%26utm_source%3Dsenditright&amp;inline=false&amp;isFullscreen=false&amp;globalCookieOptOut=&amp;isFirstVisitorSession=true&amp;isAttachmentDisabled=false&amp;isInitialInputFocusDisabled=false&amp;enableWidgetCookieBanner=false&amp;isInCMS=false&amp;hideScrollToButton=true&amp;isIOSMobile=false&amp;hubspotUtk=5f7a8dac7988abbddb7c85a8820f7202" title="Widżet czatu" allowfullscreen=""></iframe>
