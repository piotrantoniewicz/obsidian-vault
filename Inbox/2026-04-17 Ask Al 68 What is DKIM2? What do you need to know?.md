---
type: "Web"
authors: "[[Valimail]]"
url: "https://www.youtube.com/watch?v=K7z_62tUXkQ"
published: 2026-04-17
created: 2026-05-07
tags:
---


![](https://www.youtube.com/watch?v=K7z_62tUXkQ)

This week Al Iverson explains what's going on with the new version of the DomainKeys Identified Mail (DKIM) email authentication protocol. What is DKIM2, and what do you need to know about it? And if you'd like to watch DKIM2 evolve more closely and/or participate in the process, be sure to join the IETF DKIM working group: https://xnnd.com/ietf  
  
Episode 68 of Your Email Authentication and Deliverability Questions Answered.

## Transcript

**0:00** · Hey friends, Al Iverson here. It's time for another of your email authentication and deliverability questions answered.

**0:07** · Today's question, what is DKIM 2 and what do you need to know? DKIM 2 is a proposed update to domain keys identified mail DKIM the email authentication method that uses a cryptographic signature to show which domain is responsible for a given email message. Born out of Yahoo's original domain keys, email authentication protocol, the DKIM that we know and love today has been around for a bit over 20 years and is very widely used.

**0:41** · So, a group of email experts, mailbox providers, email service providers, and email security/domain protection vendors is working on DKIM 2 to improve email authentication to address three specific issues. DKIM replay, back scatter, and message changes that break email authentication. Let me walk through these quickly.

**1:04** · First, DKIM replay. Now, this is where a bad actor takes a legitimate DKIM signed message and resends it to lots of new recipients. Because the signature is still valid, it can pass authentication and inherit the original domain's reputation. Bad guys can maybe sneak their way into the inbox based on a stolen domain having a good reputation and then can damage that domain's reputation thanks to that negative fallout and spam complaints that would result from that unwanted mail.

**1:38** · DIM 2 aims to fix this by tying a message more closely to its intended recipient. If a message shows up somewhere it wasn't meant to go, a mailbox provider can detect and reject it. Next, back scatter. Back scatter is when you get a bounce back for a message that you never sent. This problem is as old as time itself. Back in my anti-PAM days, we would call a bucket full of unwanted back scatter bounces a Joe job, named after a famous spam incident from way back in 1997.

**2:09** · DKIM2 proposes signing and aligning the bounce address with the messages domain that helps ensure that bounces go to the right place and reduces false non-dely notifications. It also opens the door for more delayed bounces, giving mailbox providers more time to analyze messages before deciding to accept or reject them. message changes.

**2:36** · Things like forwarding, mailing lists, and link rewriting often break DKIM today. DKIM 2 aims to allow controlled message changes with each step adding its own signature and documenting what changed. That way, the final receiver can trace the chain and still validate the original sender. There's an older spec called authenticated receive chain or ARC that tried to solve this.

**3:00** · Uh the jury's out on that, but a lot of folks involved in DKIM 2 think that DKIM 2 offers a better path to address this.

**3:12** · So what does this mean for email senders? Honestly, probably not much day-to-day. If you run your own mail servers, you'll eventually need to upgrade software. If you use a platform like Amazon SCES or Sen Grid, they'll handle most of those upgrades for you.

**3:30** · It's nothing you'll need to touch. You might have some DNS updates, but hopefully nothing too disruptive. And I think the hope is even that existing DKIM keys in DNS would work for DKIM 2.

**3:44** · Mailbox providers, on the other hand, will have more work to do.

**3:50** · This is all still in development through the Internet Engineering Task Force or IATF. Details may change.

**3:59** · If you're in the email space, it's worth paying attention to this. The group is open, free to join, and could always benefit from more participation. So, I participate in the IATF DKIM working group, and maybe I'll see you there.

**4:13** · I'll drop a link to that DKIM working group in the video description. And one last thing, a quick note on Demar. While it's a bit early to say exactly how DKIM2 might have an impact on Demar, I don't think Demar's going anywhere. Its reporting is just too useful, too valuable, and a lot of us are invested in keeping Demar alive and useful and valuable like it is today.

**4:41** · And that's it for today. Thanks so much for watching. Send me your thoughts, feedback, questions at al.versonval.com.

**4:50** · And be sure to visit our website at valamale.com when you're ready to embark upon your Demar journey.