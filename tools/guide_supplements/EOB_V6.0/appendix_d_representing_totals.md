When representing totals in a [https://hl7.org/fhir/us/carin-bb/STU1.1/](https://hl7.org/fhir/us/carin-bb/STU1.1/) v.1.0.0 `ExplanationOfBenefit` (EOB) the total amounts must be provided within the EOB.

<img src="assets/appendix_d_1.png" alt="Totals element within an EOB" class="overall-implementation-diagram" />

Within the `totals` element, each total expresses a category and an amount.

The list of allowable values for category may be found under the definition for the `adjudication_category` type:

<img src="assets/appendix_d_2.png" alt="adjudication_category allowable values" class="overall-implementation-diagram" />

To clarify the meaning of these codes, here are the definitions* (also see Notes on Fields in the C4BB IG):

(*Definitions not pertinent to this context have been intentionally omitted)

| Code | C4BB Definition (verbatim) | Additional Clarification |
|------|----------------------------|--------------------------|
| submitted | The total submitted amount for the claim or group or line item. | The total charge submitted by the provider before any contractual discounts are applied. |
| copay | Patient Co-Payment | A co-payment amount. That is, under the rules of their plan, an amount the member must always pay for a particular type of service. |
| eligible | Amount of the change which is considered for adjudication. | The submitted amount minus contractual discounts (and any ineligible amount). Eligible amount = submitted amount - the noncovered amount - discount |
| deductible | Amount deducted from the eligible amount prior to adjudication. | Under the rules of the plan, an amount the member must pay because their deductible has not yet been met. |
| benefit | Amount payable under the coverage | Once all discounts, ineligible amounts, and patient responsibilities have been considered, the total amount insurance is finally going to pay, usually to the provider. It is possible, but rare, for the benefit to be paid to the member (patient). |
| coinsurance | The amount the insured individual pays, as a set percentage of the cost of covered medical services, as an out-of-pocket payment to the provider. Example: Insured pays 20% and the insurer pays 80%. | Usually after a deductible is met, the member will typically be responsible for a percentage of the eligible amount. This is a coinsurance amount. |
| noncovered | The portion of the cost of this service that was deemed not eligible by the insurer because the service or member was not covered by the subscriber contract. | An amount considered to be outside the benefits, limits, or rules of plan. That is, amounts that are simply not considered for payment. |
| paidbypatient | The amount paid by the patient at the point of service. | An amount paid by the patient at the time of service, to offset an anticipated outstanding balance due. |
| paidtopatient | Paid to patient | A benefit amount paid to the patient (not typical). The eligible amount - the member liability is the payment amount to the provider (`paidtoprovider`) or the subscriber (`paidtopatient`). |
| paidtoprovider | The amount paid to the provider. | A benefit amount paid to the provider (typical). The eligible amount - the member liability is the payment amount to the provider (`paidtoprovider`) or the subscriber (`paidtopatient`). |
| memberliability | The amount of the member's liability. | Member liability = deductible + coinsurance + copay + noncovered. Part of the member liability may have already been paid to the provider as `paidbypatient` |
| discount | The amount of the discount | Discount is the amount used to reduce the submitted amount to the amount allowed by contractual agreement. |
{: .heatMap}

<h3 id="total-mathematical-illustration-medical-eob" style="color:#E60073">Total Mathematical Illustration: Medical EOB</h3>

These categories relate to each other according to the following mathematical illustration:

<img src="assets/appendix_d_3.png" alt="Medical EOB total mathematical illustration" class="overall-implementation-diagram" />

Conceptually, the XML would be as shown on the following diagram.

<img src="assets/appendix_d_4.png" alt="Medical EOB totals XML example" class="overall-implementation-diagram" />

<h3 id="total-mathematical-illustration-pharmacy-eob" style="color:#E60073">Total Mathematical Illustration: Pharmacy EOB</h3>

<img src="assets/appendix_d_5.png" alt="Pharmacy EOB total mathematical illustration" class="overall-implementation-diagram" />
