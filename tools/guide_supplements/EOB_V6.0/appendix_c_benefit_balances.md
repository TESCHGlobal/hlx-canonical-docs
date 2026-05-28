Version 1.0.0 STU of the CARIN BB provides for the optional expression of benefit_balance within an EOB, such as deductible met to date or number of used/remaining for a particular type of benefit. While optional, such information may be useful to members.

<h3 style="color:#E60073">Principal Concepts for Expressing benefit_balance Information</h3>

For a given benefit_balance, these are the key fields:

- `benefit.balance.category` is required. This details the general category of benefit being described (such as medical, dental, or vision).
- Assuming one or more financials are provided, then `financial_type` is also required. This describes concepts such as deductible, visit, etc.
- This element is allowed and used to convey concepts regarding the full extent of benefit as well as how much benefit has been consumed. These concepts may be expressed as money (e.g., a deductible), or allowable number of visits (integer).
- This element allows for the expression of concepts such as "For this Health Benefit Plan Coverage (a benefit_balance.category), $2500 (financial type of used_money) of a $4000 deductible (a financial.type used_money) has been met as of the date of the EOB," or, similarly, "For this vision coverage (a benefit_balance category), the one exam (financial type of vision-exam, allowed_unsigned_int of 1) is all that is allowed for the year (used_unsigned_int of 1)."

<h3 style="color:#E60073">Example Use of Benefit Balance</h3>

**Scenario:**

Subscriber has a family vision plan. Assuming in-network providers are used, the plan allows one exam per year per individual member on the plan (no co-pay, no deductible), and a $500 yearly benefit for frames after a $100 yearly deductible. One member of the family visits an optometrist for their annual exam and purchases glasses costing $400 dollars. The member pays the deductible at the time of the appointment. Insurance pays for the exam in full plus $300 as a glasses benefit ($400 cost of glasses minus $100 deductible). In the EOB to the member, we wish to convey that the one exam allowed per member per year has been used, that the deductible has been met, and that $300 of the $500 glasses benefit for the plan year has been used.

Conceptually, the XML would be as on the following page:

<img src="assets/appendix_c.png" alt="Appendix C benefit balance XML example" class="overall-implementation-diagram" />
