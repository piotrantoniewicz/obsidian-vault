---
type: Web
authors: '[[Austin Park]]'
url: 'https://votehub.com/2025/07/16/does-posting-win-elections/'
published: 2025-07-16T00:00:00.000Z
created: 2026-03-25T00:00:00.000Z
tags:
  - digital-campaigning
  - content-marketing
---


VoteHub is proud to have launched [CivicTracker](https://civictracker.us/) earlier this week, an all-in-one platform to track the actions of all three branches of the federal government. CivicTracker provides live updates on executive orders, Supreme Court decisions, presidential schedules and actions, and social media updates from the legislative and executive branches.

CivicTracker’s API enables VoteHub to aggregate statistics on the social media activity of members of Congress, and—by comparing these to [Split Ticket’s WAR database](https://split-ticket.org/full-wins-above-replacement-war-database/) —determine if, and how, social media activity is correlated with electoral performance. It has been long-held that politicians that are successful at practicing retail politics perform better electorally, especially in smaller constituencies, and much punditry has been had of candidates who stay “offline” performing better in races.

We collect social media posts from the official Twitter accounts of members of Congress in a two week span from June 29 to July 13, tracking the number of posts, total character count, and characters per post from each member of Congress currently serving who ran in a contested election and has an active Twitter account, and take WAR figures from their last contested election in the previous six years: for House members and Class I senators (and Pete Ricketts, who ran in a special election in 2024), these are from the 2024 cycle; for Class III senators, these are from the 2022 cycle; and for Class II senators, these are from the 2020 cycle.

We find a slight negative correlation between both the number of posts and the total number of characters in social media posts and Split Ticket WAR, though most members are clustered around roughly 50 to 100 posts in the timeframe and 10,000 to 30,000 characters. Of the five most frequent posters—all of whom are Republicans—four of them post negative WAR from their most recent elections, most notably Mariannette Miller-Meeks, who tweeted 225 times in the last two weeks and underperformed fundamentals by 11.3 points in her razor-thin reelection in Iowa’s first congressional district. Notably, despite having a governing trifecta, Republican members of congress tweet more frequently than their Democratic counterparts, and are some of the most virulent social media users in Congress: of the twelve members who tweeted more than 150 times in the last two weeks, just one—Pramila Jayapal—is a Democrat.

<iframe title="Does Posting Win Elections?" aria-label="Scatter Plot" src="https://datawrapper.dwcdn.net/uM7E0/1/" frameborder="0" height="466"></iframe>

The same trends persist when looking at the most verbose members—still, the five most verbose members remain Republicans, with all but Don Bacon (1.6 WAR) posting negative WAR figures. Here too, of eighteen members who tweeted over 40,000 characters, just five were Democrats while thirteen came from the Republican Party.

<iframe title="Does Posting Win Elections?" aria-label="Scatter Plot" src="https://datawrapper.dwcdn.net/xFBAO/2/" frameborder="0" height="466"></iframe>

As it happens, however, Americans may have a preference for members of Congress with lengthier posts as we find a slight positive correlation between post length and WAR. While most legislators are clustered around a few hundred characters, mirroring Twitter’s old 280 character limit, the three members with the lengthiest tweets—Brian Fitzpatrick (R-PA-01), Doug LaMalfa (R-CA-01), and Henry Cuellar (D-TX-28)—all have fairly significantly positive WAR figures. Notably, the distribution of post length, especially on the upper end, is more evenly divided with respect to partisanship.

<iframe title="Does Posting Win Elections?" aria-label="Scatter Plot" src="https://datawrapper.dwcdn.net/6yvaw/2/" frameborder="0" height="466"></iframe>

Ultimately, none of the correlations in this piece are statistically significant—in fact, the coefficients of determination are all around 0.01. This is, perhaps, largely is due to the clustering of the datapoints. Nevertheless, the data here fit the eye test, with the greatest outliers at least somewhat adhering to the overall trends.

CivicTracker is free for general use, and is offering a free seven day trial for full access. You can also find live updates to federal government activity on Twitter [@CivicTracker](https://twitter.com/CIvicTracker).
