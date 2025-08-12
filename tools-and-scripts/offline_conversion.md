# ⚙️ Automated Offline Conversion Tracking for Google Ads using Zapier

Automates sending **qualified lead / sale events** from your CRM to **Google Ads Offline Conversions**.  
No more weekly CSV uploads. Near real-time uploads → faster optimisation, better CPA.

---

## 🚀 Why this matters
- **Speed:** Conversions land in Google Ads within minutes, not days.
- **Accuracy:** Reduces manual errors from spreadsheets.
- **Smarter bidding:** Feeds real outcomes back to Google’s bidding models (Max Conv./tCPA/tROAS).

---

## 🧭 Flow (at a glance)
Form/Call → CRM status changes (e.g., Closed Won)
↘ Zapier Trigger
↘ Find gclid / gbraid / wbraid + conversion data
↘ Zapier "Upload Offline Conversion" (Google Ads)
↘ Success logged back to CRM (optional)

markdown
Copy
Edit

---

## ✅ Requirements
- Google Ads account with **Auto-tagging ON** (captures `gclid`)
- A **Conversion Action** set to **Import from clicks** in Google Ads
- CRM or DB that stores **gclid/gbraid/wbraid** with each lead (or use **Enhanced Conversions for Leads** as fallback)
- Zapier account (Google Ads + your CRM apps connected)

---

## 🛠 Setup (Zapier)
1. **Trigger** – choose your CRM event (e.g., *Deal Stage = Won*, *Lead Status = Qualified*, or *New Row in Google Sheets*).
2. **Find the Click ID** – map the field where you stored `gclid` (or `gbraid`/`wbraid` for iOS).
3. **Action** – *Google Ads → Upload Offline Conversion*  
   Map:
   - **Conversion action**: the exact name you created in Google Ads
   - **Google click ID**: `gclid` (or `gbraid`/`wbraid`)
   - **Conversion time**: ISO 8601 timestamp (e.g., `2025-08-12T14:30:00Z`)
   - **Conversion value**: e.g., `250.00`
   - **Currency**: `GBP`
   - (Optional) **Order ID** to dedupe
4. **(Optional) Action** – Update the CRM record with the upload status / Google Ads response.

---

## 🧪 Testing
- Create a test lead via your form (confirm a `gclid` is captured).
- Move the lead to your “conversion” stage to fire the Zap.
- In Google Ads, go to **Tools & Settings → Conversions → Uploads** to confirm.
- Allow up to **3–6 hours** for the conversion to appear in standard reports.

---

## 🩹 Troubleshooting
- **No `gclid`?** Ensure Auto-tagging is ON and landing pages don’t strip query params.  
- **iOS traffic:** Use `gbraid`/`wbraid` fields (Zapier supports them).  
- **Leads without click IDs:** Use **Enhanced Conversions for Leads (ECL)** with **hashed** PII (email/phone) instead.  
- **Time zone mismatches:** Use account time zone or UTC; pass ISO timestamps.  
- **Duplicates:** Set and reuse **Order ID** to dedupe.

---

## 🔐 Privacy
Hash any personal data before sending (SHA-256 for ECL). Share only the minimum fields req
