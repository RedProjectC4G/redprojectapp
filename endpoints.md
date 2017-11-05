# Endpoints
## Login
**POST**

*Parameters*
  * UserId

*Returns*
  * Session info for user

---
## CreateUser
**POST**

*Parameters*
  * First Name
  * Last Name
  * User Type????

*Returns*
  * Generated Id

---
## DisableUser
**Post**

*Parameters*
  * UserId

*Returns*
  * N/A

---
## SearchForParticipantById
**GET**

*Parameters*
  * ParticipantId

*Returns*
  * Matching Participant(s)

---
## SearchForParticipantByForm
**GET**

*Parameters*
  * Gender
  * First Initial
  * Birth Day
  * Birth Month
  * Birth Year
  * Mother's First Initial
  
*Returns*
  * Matching Participant(s)

---
## GetPatientInfo
**GET**

*Parameters*
  * ParticipantId

*Returns*
  * Participant Info
  * Visit History
  * Risk Assessments
  * Dispense Reports
  * Reversal Reports

---
## CreateNewParticipant
**POST**

*Parameters*
  * Participant Info(saved as JSON blob)

*Returns*
  * N/A

---
## UpdateParticipant
**PUT**

*Parameters*
  * Participant Info

*Returns*
  * N/A

---
## AddNewVisit
**POST**

*Parameters*
  * Date
  * Safe Crack
  * Overdose Kits
  * Do you want an HIV test?
  * Do you want a Hep C test?
  * ET 28g 1/2" 1cc
  * ET 30g 5/16" 1cc
  * BD/ET 27g 1/2" 1cc
  * BD 1/2cc
  * 3cc
  * Other Syringes
  * Secondary Syringe Exchange
  * Referral Notes
  * General Notes
  * Location

*Returns*
  * N/A

---
## UpdateVisit
**PUT**

*Parameters*
  * Same as AddNewVisit

*Returns*
  * N/A

---
## RiskAssessment
##POST##

*Parameters*
  * See Q & A file for list

*Returns*
  * N/A

---
## ReversalReport
**POST**

*Parameters*
  * See Q & A file for list

*Returns*
  * N/A

---
## DispenseReport
**POST**

*Parameters*
  * See Q & A file for list

*Returns*
  * N/A