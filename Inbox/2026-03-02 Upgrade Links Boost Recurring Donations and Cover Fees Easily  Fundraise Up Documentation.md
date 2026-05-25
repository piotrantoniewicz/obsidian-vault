---
type: Web
authors: "[[Fundraise Up]]"
url: https://fundraiseup.com/docs/upgrade-links/
published:
created: 2026-03-02T00:00:00.000Z
tags:
  - fundraising
  - automatyzacja
  - narzędzia-AI
---


[Overview](https://fundraiseup.com/docs/engage/)

Donor Portal

[Overview](https://fundraiseup.com/docs/donor-portal/)

[Configure your Donor Portal](https://fundraiseup.com/docs/donor-portal-configuration/)

[Supporter experience in Donor Portal](https://fundraiseup.com/docs/donor-portal-experience/)

[Integrate Fundraise Up Donor Portal with your platform](https://fundraiseup.com/docs/seamless-donor-portal/)

[External donations](https://fundraiseup.com/docs/offline-donations/)

Upgrade Links

[Overview](https://fundraiseup.com/docs/upgrade-links/)

[How to create Upgrade Links](https://fundraiseup.com/docs/creating-upgrade-links/)

[Configure supporter emails](https://fundraiseup.com/docs/emails-settings/)

[Receipts](https://fundraiseup.com/docs/receipt-settings/)

[Home](https://fundraiseup.com/docs/) [Engage supporters](https://fundraiseup.com/docs/engage/)

## Upgrade Links

Learn how to use Upgrade Links to help recurring supporters increase their donations or start covering transaction costs.

Upgrade Links let supporters increase their recurring donation amount or start covering transaction costs without re-entering payment details. Each link is personalized for a specific supporter and recurring plan.

Your organization creates and distributes these links through your own communication channels like email campaigns, SMS, or newsletters. Fundraise Up provides the tools to generate the links, but you control when and how to send them to supporters.

Upgrade Links only allow supporters to increase donations or add cost coverage. Supporters can't decrease or cancel their recurring donations through these links. They need to use the Donor Portal for those actions.

This link lets supporters increase their monthly donation amount. When a supporter opens the link, they'll see 3 suggested amounts and an option to enter a custom amount.

![Donation increase options for Helping Hand Foundation, showing choices to add $10, $20, or $45 to monthly donations, with a checkbox for covering transaction costs and buttons to confirm or decline the increase.](https://ucarecdn.com/bba1ef12-433e-45ee-9744-947df818fada/-/format/auto/-/quality/normal/-/resize/1392x/)

Fundraise Up’s AI calculates the suggested amounts based on the supporter's location and donation history. For example, if a supporter currently donates $50 per month, they might see options for $60, $70, and $95.

Supporters can also choose to cover transaction costs if they don't already. If they already cover costs and increase their donation amount, their cost coverage updates automatically to match the new donation.

#### How cost coverage updates work

When a supporter who covers transaction costs increases their donation, the cost coverage amount adjusts to reflect the new donation total.

Example:

- Current donation: $50
- Transaction costs: $1.75
- Total amount: $51.75

If the supporter increases their donation to $95:

- New donation amount: $95
- New transaction costs: $3.33
- New total: $98.33

The increase goes from $51.75 to $98.33 (not $96.75). Supporters see this breakdown before confirming.

![Donation increase options for Helping Hand Foundation, showing current donation of $51.75/month and suggested increases of $10, $20, and $45 with corresponding future totals. Buttons for confirming or declining the increase are present.](https://ucarecdn.com/2e73548b-89b1-4e19-aa14-07c0d1ebb472/-/format/auto/-/quality/normal/-/resize/1392x/)

This link prompts supporters who don't cover transaction costs to start doing so. For example, if a supporter donates $50 per month without covering fees, the link shows them the option to increase their total to $51.75 to include the $1.75 in processing fees.

![Donation form prompting users to cover transaction costs, showing $1.75 for transaction fees and a total donation of $51.75. Options to confirm or decline are provided.](https://ucarecdn.com/8b92b00b-0d35-4e8c-bc40-f9d78fc2bfcf/-/format/auto/-/quality/normal/-/resize/1392x/)

After a supporter confirms cost coverage, they'll see options to increase their main donation amount. If a supporter who already covers costs receives this type of link, they'll only see options to increase their donation amount.

![Your transaction costs are already covered. Options to increase your donation amount by $5, $10, or $20, with updated future donation amounts displayed. Buttons to confirm or decline the increase.](https://ucarecdn.com/26c87ddb-f26f-42ee-b968-f2721b912c55/-/format/auto/-/quality/normal/-/resize/1392x/)

Understanding the hash function is important before you begin creating Upgrade Links.

When you create Upgrade Links, you can include a secure hash function. This affects how supporters confirm their donation changes:

- **With hash function**: Supporters confirm their increase directly on the Upgrade screen. No email confirmation needed.
- **Without hash function**: Supporters must confirm through a follow-up email.

All Upgrade Links created through Fundraise Up include a hash by default. You can create links without a hash manually if needed.

A hash function combines your organization's Secret key, the Supporter ID, and the Recurring ID into a secure code. This code verifies that the link came from your organization. The hash can't be reversed to reveal the original data.

Fundraise Up uses SHA256 for Upgrade Link hashes.

Here's what an Upgrade Link with a hash looks like:

https://ropsi.org/upgrade?recurring=RWLFHRKE&supporter=SWLFHRKJ&signature=RCFHHQFGRCFHHQFGXn56QgSe1C3Tf64cwd7E8nq1EeJycwHE

The `signature` parameter contains the hash. Because this signature validates the link's authenticity, supporters don't need email confirmation.

Links with hash functions skip the email confirmation step, which typically results in more supporters completing the upgrade. However, these links must go to the correct supporter. If you send a hashed link to the wrong person, they can modify someone else's recurring donation.

If you accidentally send a hashed link to the wrong supporter, reset your Secret key immediately using the instructions below.

Reset your Secret key only when necessary. Resetting affects all previously created Upgrade Links — they'll still work, but supporters will need to confirm upgrades through email.

Only users with the Organization Administrator role can reset the Secret key.

To reset your Secret key:

1. Go to [**Settings** > **Recurring plans**](https://dashboard.fundraiseup.com/settings/recurring-plans).
2. In the **Upgrade links** section, Click **Roll key** and follow the instructions.

After you reset the key, existing Upgrade Links continue to function but require email confirmation, just like links without hash functions.

One-time receipt emails include an option for supporters to set up a recurring donation. The email shows two preset amounts and an **Other amount** option. When supporters click an amount, they go to a confirmation page where they can set up monthly giving and choose an installment date without re-entering payment details.

![Thank you email from Relief Operations International, expressing appreciation for a donation. It includes options for monthly contributions of $9 or $30, or an alternative amount, and a button to access the donor portal.](https://ucarecdn.com/89f632f1-a584-45d1-bbee-2f14d7e6ecd0/-/format/auto/-/quality/normal/-/resize/1392x/)

This works when:

- One-time receipt emails are [enabled](https://dashboard.fundraiseup.com/settings/emails-settings/templates/customerChargeSuccess).
- Your campaign accept both one-time and monthly donations.
- The payment method supports recurring donations (excludes crypto, Venmo, and PayPal without reference transactions).

This doesn't work for:

- Donations with tributes.
- Donations made in Test mode.

Supporters choose which date their recurring installments process. The recurring plan uses the same campaign as the original one-time donation. Each one-time donation can create only one recurring plan. The confirmation links don't expire.

Starting with the second installment, supporters see an option to increase their donation amount directly from the email. The suggested amounts are calculated by Fundraise Up’s AI based on supporter data.

Supporters with plan limits (maximum installments, maximum donation amount, or cut-off date) don't see the increase option in their final installment email.

After a supporter increases their donation, they won't see the increase option in the next two installment emails.

[Why disabling Upgrade Links in installment receipts is not possible →](https://fundraiseup.com/support/upgrade-links-emails/)

The annual summary email includes preset amounts that supporters can click to increase their recurring donation. Clicking an amount takes them to an Upgrade page where they can confirm the increase without re-entering payment details.

Only supporters with active monthly recurring plans see this option.

When someone receives a tribute notification by email (because a supporter honored them with a donation), the email includes a **Make a difference now** button. This button opens either the Checkout Modal or a  Campaign Page (depending on your setup) with the same campaign as the original tribute. The tribute recipient can then make their own donation.

Active recurring plans in the Donor Portal show a  **Give more** button. Supporters can click this to increase their donation amount or start covering transaction costs.

The page that opens depends on whether the supporter already covers costs:

- If they cover costs, they see options to increase their donation amount.
- If they don't cover costs, they see options to cover processing fees and increase their donation amount.

Next, learn [how to create Upgrade Links →](https://fundraiseup.com/docs/creating-upgrade-links/)

In this article

[Types of Upgrade Links](https://fundraiseup.com/docs/upgrade-links/#types-of-upgrade-links)

[Recurring amount upgrade](https://fundraiseup.com/docs/upgrade-links/#recurring-amount-upgrade)

[Cost coverage upgrade](https://fundraiseup.com/docs/upgrade-links/#cost-coverage-upgrade)

[Hash function](https://fundraiseup.com/docs/upgrade-links/#hash-function)

[What a hash function does](https://fundraiseup.com/docs/upgrade-links/#what-a-hash-function-does)

[When to use links with hash functions](https://fundraiseup.com/docs/upgrade-links/#when-to-use-links-with-hash-functions)

[How to reset the Secret key](https://fundraiseup.com/docs/upgrade-links/#how-to-reset-the-secret-key)

[Upgrade Links in emails](https://fundraiseup.com/docs/upgrade-links/#upgrade-links-in-emails)

[One-time receipt email](https://fundraiseup.com/docs/upgrade-links/#one-time-receipt-email)

[Installment emails](https://fundraiseup.com/docs/upgrade-links/#installment-emails)

[Annual summary receipt email](https://fundraiseup.com/docs/upgrade-links/#annual-summary-receipt-email)

[Tribute email](https://fundraiseup.com/docs/upgrade-links/#tribute-email)

[Fundraiser donation notification](https://fundraiseup.com/docs/upgrade-links/#fundraiser-donation-notification)

[Upgrade Links in the Donor Portal](https://fundraiseup.com/docs/upgrade-links/#upgrade-links-in-the-donor-portal)
