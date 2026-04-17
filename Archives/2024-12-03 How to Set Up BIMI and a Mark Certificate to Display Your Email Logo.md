---
type: Web
authors: '[[Casey Crane]]'
url: >-
  https://www.thesslstore.com/blog/how-to-set-up-bimi-and-a-mark-certificate-to-display-your-email-logo/?utm_source=www.civicshoutnewsletter.com&utm_medium=newsletter&utm_campaign=bimi-why-your-logo-belongs-in-the-inbox&_bhlid=3991d48410c7083733a40d3ff78630d6033f1ada
published: 2024-12-03T00:00:00.000Z
created: 2026-03-23T00:00:00.000Z
tags:
  - digital-campaigning
  - content-marketing
---


## This step-by-step guide walks you through the process that will display your brand avatar in email recipients’ inboxes using a BIMI certificate

Having up-front brand recognition is everything when you consider that [email recipients spend an average of 11 seconds](https://dma.org.uk/research/consumer-email-tracker-2023) on an email.

This research, from the Data & Marketing Association’s (DMA) 2023 Email Consumer Tracking report, also indicates that three in five email recipients view brand recognition as the top factor when making a decision about whether to open an email. The third most important factor for opening emails? Seeing the brand’s recognizable logo.

This comprehensive how-to article will walk you through everything you need to know — configuring your BIMI and DNS records, handling the specifics of your logo, selecting the right type of [Mark Certificate](https://www.thesslstore.com/products/mark-certificates.aspx) (i.e., a BIMI certificate), and all that’s needed to start sending emails with your brand’s logo in the sender field.

Let’s hash it out.

Looking for the Latest Mark Certificates and BIMI Updates?

Learn how organizations and email service providers (ESPs) are adopting the Brand Indicators for Message Identification (BIMI) standard on a global scale in the article [6 Updates to Know About Mark Certificates and BIMI](https://www.thesslstore.com/blog/mark-certificates-and-bimi-updates/).

## BIMI Certificate TL;DR — Everything to Know in 60 Seconds or Less

![An example of how brand logos display in recipients' inboxes when using a BIMI Certificate. Image courtesy of DigiCert.](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/mark-certificate-inbox-examples.png)

An example of how companies’ brand logos display when using BIMI and a Mark Certificate.

- **BIMI displays your logo in the email sender field.** Recipients will see your logo in their inbox (before they even open the email), which improves email open and engagement rates. Like this (see image).
- **Set up DMARC on your domain**. This includes setting up SPF, DKIM and DMARC DNS records. You can set the DMARC policy to either *p=quarantine* or *p=reject*.
- **Ensure your logo is saved using a supported format**. A BIMI-compliant image is a square image that’s saved as an [SVG Tiny PS](https://bimigroup.org/creating-bimi-svg-logo-files/) file.
- **Validate your brand logo by getting a Mark Certificate**. This requires validation checks and approval by a trusted Mark Verifying Authority (MVA) such as DigiCert. You can get a Common Mark Certificate (CMC) for a non-trademarked logo or a Verified Mark Certificate (VMC) for one that has a trademark.
- **Configure the BIMI record on your domain**. The [BIMI Group’s inspector and generator](https://bimigroup.org/bimi-generator/) tool simplifies the process of generating a new BIMI record, a DNS record that includes links to your SVG logo file and BIMI Mark Certificate.

Here’s a quick comparison that shows the difference of what it looks like when you do (or don’t) use BIMI and a Mark Certificate:

![A side-by-side peek at how it looks when you don't use a BIMI certificate (left) versus when you use a Common Mark Certificate (center) or a Verified Mark Certificate (right). ](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/mark-certificate-mini-comparison-shadow-2048x275.jpg)

Image caption: This side-by-side comparison showcases the difference between using no Mark Certificate (left), a Common Mark Certificate (middle), and a Verified Mark Certificate (right) in the Gmail app on an iOS device.

Now that you know why businesses should use BIMI and have a basic idea of the implementation process, let’s go through everything step by step!

## Step 1: Ensure Your Domain Is DMARC Compliant

Before you can start setting up your logo to display, there’s one prerequisite you’ll need to have in place: the BIMI standard requires that your domain have a DMARC record (a type of DNS record) set to *p=reject* or *p=quarantine*.

[DMARC](https://www.thesslstore.com/blog/dmarc-reporting-and-email/) works hand-in-hand with Sender Policy Framework ([SPF](https://www.thesslstore.com/blog/email-security-spf/)) and Domainkeys Identified Mail ([DKIM](https://www.thesslstore.com/blog/dkim-domainkeys-identified-mail/)), two other types of DNS records, to block unauthorized senders from sending emails using your domain. DMARC tells email servers what to do with emails from your domain that fail SPF and/or DKIM authentication.

### Before Setting Up Your DMARC Record…

First, you’ll need to ensure that you have SPF and/or DKIM records on your domain that cover every place you send emails from (when the from address is @yourdomain.com). For example: MailChimp, AWS SES, your own email server, Microsoft 365, etc. Each email service provider should give you instructions for setting up an SPF and/or DKIM record (you don’t need both, just one for each email service is fine).

**NOTE:** If you don’t create an SPF or DKIM record for an email service, emails sent from that email service will be blocked after you implement DMARC. There are a few tricks you can use to be sure you’ve covered everything — more on that in a moment.

### Set Up DMARC Monitoring

After you’ve got your SPF and SKIM records set up, you’ll want to set up DMARC in reporting-only mode. This way, you can check that you’ve covered all of the email services/senders you need to before you turn on enforcement.

To set up DMARC for monitoring, use the following example but replace the email info with your domain:

```
v=DMARC1; p=none; rua=mailto:account@itsatest.site
```

This will give you a chance to identify any messages falsely flagged by SPF and DKIM. Give it a bit of time, as you’ll want to ensure you have a chance to identify all the legitimate senders you might have missed in your SPF/DKIM records.

To make this process easier, we recommend using a DMARC reporting service (for example, Valimail) that collects and displays the reports in a more readable format.

### Set Up DMARC Enforcement

Once you’ve figured out whether there are senders not accounted for in your SPF record, it’s time to set DMARC enforcement.

You can set DMARC to enforcement by setting it to one of the following options:

- *p=reject*
- *p=quarantine*

## Step 2: Format Your Logo File

Your logo’s image file must be an SVG file and meet certain formatting criteria to be BIMI compliant. Adhere to the following guidelines for the best results:

- Use a 1:1 (square) aspect ratio
- Center your graphic, as it’ll display either in a circle or a round-edged square
- Use a solid, non-transparent background such as white
- Ungroup any layers so all paths display in a single column
- Don’t include any linked files within the graphic
- Keep it small: your image should be no larger than 32 kilobytes (KB)

Don’t Want to Manually Convert Your Logo?

Normally, since there is no preconfigured template for this in Adobe Illustrator, you’d have to handle the conversion manually. However, you’re in luck: The BIMI Group published several [SVG conversion tools](https://bimigroup.org/svg-conversion-tools-released/), including an [Adobe Illustrator Export Script](https://github.com/authindicators/svg-ps-converters/tree/master/illustrator-script/) that automates the conversion of your SVG file into the required format for BIMI (SVG P/S).

### Start by Converting Your File to SVG Format in Illustrator

For starters, you must format your logo as a Scalable Vector Graphic (SVG) file that meets the [SVP Portable/Secure (SVG-P/S)](https://datatracker.ietf.org/doc/html/draft-svg-tiny-ps-abrotman) profile. For this example, I’m using Adobe Creative Cloud’s Illustrator program version 29.0.1.

### Save the File in Illustrator Using the SVG Tiny 1.2 Profile

This part of the process involves exporting your vector graphic as an SVG Tiny 1.2 format SVG image file. To do this, go to **File** > **Save as**. Here, you’ll select the *.svg* file option in the menu.

This will bring up a new window (SVG Options) where you can select the SVG Profile “SVG Tiny 1.2”, as shown below:

![A screenshot from Adobe Illustrator's SVG Options screen that shows where you can select the SVG Tiny 1.2 profile.](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/convert-to-svg-tiny-v2-shadow.png)

Image caption: A screenshot showing where to select the SVG Tiny 1.2 profile for your logo.

This is as close as you’ll get in Illustrator’s native settings because Illustrator doesn’t have a conversion tool for the *tiny-ps* profile specifically. (Maybe this will change in the future — who knows?)

Next, under Options, click **Image Location** and select **Preserve** from the drop-down menu. Click **OK** to save your selection. The next steps will require manual intervention in the file’s code.

### Review the SVG Image Code

Knowing this, open your SVG file in a TXT editor such as Notepad++. (**NOTE:** Be sure to check that you can open, edit, and re-save the file to a “txt” format while retaining the file extension.*svg*.)

Using a TXT editor allows you to display the image’s TXT file to see whether the file’s code is displaying the Tiny-PS 1.2 profile info in the *baseProfile=* and *version=* elements. This information should be displayed near the top of the file, as shown in the screenshot below.

![An example of the code that auto populates when you've selected the SVG Tiny 1.2 profile in Adobe Illustrator. ](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/svg-code-before-shadow.jpg)

Image caption: A screenshot that illustrates what the SVG image code may look like after you’ve selected Adobe Illustrator’s tiny 1.2 profile.

Here’s a closer look at that part of the code:

![A close up look at the code that displays when you've selected the SVG Tiny 1.2 profile in Adobe Illustrator. ](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/svg-code-before-crop-shadow.jpg)

A “zoomed in” look at that part of the code that gives you a closer look.

Does yours just say “tiny” like our illustration above shows? This means you’re not done yet. There are a [few more things you’ll need to do to the code](https://bimigroup.org/creating-bimi-svg-logo-files/) to get it into the appropriate format.

### Manually Make the Following Changes to the SVG Image Code

- **Change the profile info to reflect *tiny-ps*.** You can do this by typing *\-ps* in the existing *baseProfile=“tiny”* field so it becomes *baseProfile=“tiny **–** ps”.*
- **Add the required *<title>* element to your script.** Simply hit the return key after the *xml:space=* “ *preserve”>* text at the end of one of the upper lines of code and insert *<title>Tile Goes Here</title>*. A good rule of thumb is to put your company’s name in the title area (although that’s not a hard-and-fast rule).
- **Remove any *x=* and *y=* attributes from the code (if displayed).** They’re not allowed in BIMI. So, if you’re using an earlier version of Adobe Illustrator that inserts these attributes, then go ahead and nix ’em.
- **Delete any external links or unnecessary elements.** Have unnecessary scripts or interactive elements in your code? Delete ’em. Just be sure to not eliminate any specified XML namespaces.

Alright, your code should look something akin to the following example now:

![An example of the code modifications you'll want to make your logo BIMI compliant.](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/svg-code-after-shadow.jpg)

Image caption: A screenshot showing how the logo SVG code may look after making the necessary manual amendments.

Let’s again take a little closer look:

![A close-up look at the code modifications you'll want to make your logo BIMI compliant.](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/svg-code-after-crop-shadow.jpg)

A “zoomed in” look at the updated section of the SVG code example that provides a closer look.

Does your file code look different from the example shown in the last example above, or are you having other issues with this process? Reach out to our [Support Team](https://www.thesslstore.com/support/), who can help walk you through the process.

## Step 3: Buy a Mark Certificate (BIMI Certificate)

Now that you’ve got a logo that’s properly configured (and trademarked, in the case of organizations that want Google’s verified blue checkmark), it’s time to move on to the digital certificate part of the process.

Gmail and other major email providers require you to have a Mark Certificate, a digital certificate that verifies your logo (otherwise, anyone could upload and display the logo of any brand!)

### Common Mark Certificate vs Verified Mark Certificates

There are two different types of [BIMI Mark Certificates](https://www.thesslstore.com/resources/category/mark-certificates/) you can choose from:

- **Common Mark Certificate:** Choose this certificate if your logo is not a registered trademark or you want to modify a logo that is a registered trademark.
- **Verified Mark Certificate:** Choose this certificate if your logo is either a registered trademark or a government mark. It’s supported by most major email clients and adds a blue verified checkmark in Gmail.

### What to Know When Shopping for a Mark Certificate

When deciding between getting a Common Mark Certificate and a Verified Mark Certificate, there are two important questions you must ask yourself:

1. **Is your logo a registered trademark or a government mark?** (A government mark is a logo that’s established for a government agency by law.) If your business has a trademark registered with one of the 17 authorities mentioned below, you can get a VMC. Otherwise, you’ll be limited to a CMC.
2. **Do you want your logo to display a blue “verified” checkmark in Gmail?** It’s similar to the blue checkmarks you see on social media platforms. You’ll need a VMC to get this.
3. **Will you display the logo for one email domain or multiple?** For example, do you want to use it to display a sender logo in emails from @yourmaincompany.com only, or from @yourmaincompany.com *and* @oneofyourproductbrands.com? Then you’ll need a separate certificate for each logo.
4. **Do you have variations of your logo?** Some [brands like to get festive with their logos](https://brandsymbol.com/best-holiday-brand-logo-redesigns/) during the holidays or use different logos for different geographic regions. If this is the case for your company, then you’ll need to have a separate certificate for each logo variation.
![A basic flowchart that helps determine which BIMI certificate is most suitable based on your organization's specific needs and use case(s).](https://www.thesslstore.com/blog/wp-content/uploads/2024/12/mark-certificate-decision-flowchart-final-1380x2048.png)

Image caption: A basic flow diagram showing an overview of the decision-making process when choosing a BIMI certificate.

### Trademark Requirements for VMCs

If you’ve chosen to get a CMC, you can skip this section. This step is only required for businesses that want to display the VMC’s verified blue checkmark next to the sender name field and accompanying logo in emails to recipients in Gmail and other major email clients.

To get a VMC, your logo must be registered with one of the following 17 trademark offices. (If your logo isn’t registered, we recommend getting a CMC.)

### Americas

- [United States Patent and Trademark Office](https://www.uspto.gov/) (USPTO)
- [Canadian Intellectual Property Office](https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en) (CIPO)
- Brazil’s [Instituto Nacional da Propriedade Industrial](https://www.gov.br/inpi/en) (INPI)

### Europe

- [Denmark Ministry of Culture](https://kum.dk/english/)
- [European Union Intellectual Property Office](https://european-union.europa.eu/institutions-law-budget/institutions-and-bodies/search-all-eu-institutions-and-bodies/european-union-intellectual-property-office-euipo_en) (EUIPO)
- France’s [Bureau de la propriété littéraire et artistique](http://www.inpi.fr/) (INPI)
- Germany’s [Deutsches Patent- und Markenamt](https://www.dpma.de/) (DPMA)
- [Benelux Office for Intellectual Property](https://www.boip.int/en) (BOIP), which covers the Netherlands, Belgium, and Luxembourg
- [Spanish Patent and Trademark Office](https://www.oepm.es/en/) (SPTO)
- [Swedish Intellectual Property Office](https://www.prv.se/en/) (PRV)
- [Swiss Federal Institute of Intellectual Property](https://www.ige.ch/en/) (IPI)
- [UK Intellectual Property Office](https://www.gov.uk/government/organisations/intellectual-property-office) (IPO)

### Asia-Pacific

- India’s [Rajiv Gandhi National Institute of Intellectual Property Management](https://ipindia.gov.in/) (RGNIIPM)
- [IP Australia](https://www.ipaustralia.gov.au/)
- [Japan Patent Office](https://www.jpo.go.jp/e/) (JPO)
- [Korean Intellectual Property Office](https://www.kipo.go.kr/en/) (KIPO)
- [Intellectual Property Office of New Zealand](https://www.iponz.govt.nz/) (IPONZ)

Publishing Your BIMI Mark Certificate

Your Mark Certificate will need to be saved as a PEM file (i.e., in the *.pem* format) and hosted on a publicly accessible server using a secure (HTTPS) URL.  
  
To simplify this process when purchasing your Common or Verified Mark Certificate from DigiCert, you can choose to allow the CA to host the BIMI certificate file for you.

## Step 4: Await the Issuing CA’s Validation Process

Before the Mark Verifying Authority (i.e. DigiCert) can issue a BIMI certificate, it first must vet your organization, logo, and domain. The [Mark Certificate issuing authority is going to check](https://www.thesslstore.com/resources/can-i-get-a-bimi-certificate-for-free-vmc-cmc/) the official records and documentation you provide to ensure

- your organization is legitimate,
- you control the sender email domain(s) in question, and
- you can prove ownership of the logo with either 1) a registered trademark or government mark (for VMCs) or 2) a modified trademark or can prove at least 12 months of prior logo usage (for CMCs).

## Step 5: Set Up Your BIMI Record

Brand Indicators for Message Identification (BIMI) is the standard that allows you to display your logo(s) in participating email clients. In the practical sense, it’s just a simple TXT record that you must add to your DNS records.

You can easily generate your BIMI record using the free tool provided by the [BIMI Group](https://bimigroup.org/bimi-generator/).

The good news is that you’ve already completed most of the preparations needed to set up your BIMI record. But there are still some things to know…

### Core Elements of a BIMI Record

A standard BIMI record typically consists of a few components called tags:

1. **Version tag (v=).** This element specifies the version of the BIMI version you’re using.
2. **Logo URL tag (l=).** This tag specifies the secure (HTTPS) URL where your logo’s *.svg* file is stored.
3. **Assertion record tag (a=).** This tag is used to specify the secure URL where your Mark Certificate’s *.pem* file is securely stored.

This means that a traditional BIMI record would look like this for either a CMC or VMC:

```
v=BIMI1; l=https://full/path/to/your/file/logo.svg; a=https://full/path/to/your/certfile/logo_vmc.pem
```

## FAQs Regarding BIMI and Mark Certificates

Did you run into some issues when trying to complete one of these steps? No worries — it happens to the best of us!

### Q: Can I Set DMARC Enforcement Incrementally?

A: If you’ve had your DMARC in monitoring mode for a while and are sure you’ve identified all legitimate sources, this step shouldn’t be necessary. But if you’re setting things up for the first time, jumping straight to using the quarantine or reject parameter may not be a good idea. In this case, you may want to do so incrementally until you reach the specified parameter (*pct=100*).

For example, set DMARC at 50% filter enforcement (*pct=50*) and then increase the percentage until you make your way up to full 100%:

```
v=DMARC1; p=quarantine; pct=50; rua=mailto:account@itsatest.site
```

Once you’ve reached that target percentage, we’ll want to switch to *p=quarantine* or *p=reject*. Once you add the DMARC version tag and the policy that specifies how to respond to non-compliant emails, your DMARC record should look something like this:

```
v=DMARC1; p=quarantine; pct=100; rua=mailto:account@itsatest.site
```
```
v=DMARC1; p=reject; rua=mailto:account@itsatest.site
```

### Q: Which Certificate Authorities Are Approved as Mark Verifying Authorities (MVAs)?

**A:** DigiCert and Entrust are the only two certification authorities (CAs) that are approved to issue Mark Certificates.

### Q: Can You Get a VMC in a Country That Isn’t on DigiCert’s Approved List?

**A:** No. A VMC is only available to businesses and government entities in specific countries (i.e., one of DigiCert’s 17 approved countries). However, CMCs are available to almost all other countries (minus those with U.S. sanctions or other restrictions in place).

### Q: Does My Organization Have to Undergo Business Validation to Get a BIMI Certificate?

**A:** Yes, business validation is part of the process for both VMC and CMC. For example,

- **Common Mark Certificate:** If you just want to display your logo but don’t care about the blue verified checkmark, then you can get a CMC. Although this doesn’t require having a trademarked logo (although you can use a registered mark), it does require you to undergo organization and domain validation. You’ll also have to prove either 12+ months of logo use or that your logo is a modified trademark.
- **Verified Mark Certificate:** You must undergo a [more extensive validation process](https://knowledge.digicert.com/solution/vmc-new-validation-steps) to use a VMC and have a government or registered business logo. This means validating your business is a legitimate entity, that you control your domain, and that you have a registered trademark or government mark in order to display your verified logo in most major email clients and the blue verified checkmark in Gmail.

### Can I Use One Mark Certificate to Display a Logo Across Multiple Domains?

**A:** Yes! Let’s say you have multiple sending domains for which you wish to display your logo in emails to customers. You can easily do this using a single CMC or VMC.

### Can I Use One BIMI Certificate for Multiple Logos?

**A:** No, you’ll need a separate Mark Certificate for each individual logo. This is because each BIMI certificate can be associated with a distinct logo and accompanying trademark.

Here’s a quick overview table that will help you determine which type(s) of VMCs or CMCs you need and how many:

| **Domain Structure** | **Number of Logos** | **Common Mark Certificate** | **Verified Mark Certificate** |
| --- | --- | --- | --- |
| One Domain | One | One |  |
| One Domain | Two or more | One CMC per logo | One VMC per logo |
| Multiple Domains | One | One CMC will cover all of them | One VMC will cover all of them |
| Multiple Domains | Two or more | Multiple: One CMC per logo | Multiple: One VMC per logo |
| Multiple Subdomains | One | One CMC will cover all of them | One VMC will cover all of them |
| Multiple Subdomains | Two or more | Multiple: One CMC per logo | Multiple: One VMC per logo |
