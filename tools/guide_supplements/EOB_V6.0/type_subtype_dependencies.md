The following table provides a summary of second level type/sub_type element dependencies and requirements for an EOB file.

- "X" required field / "o" field must NOT be present

**NOTE:** In the United States, vision claims bill using the "professional" type so the "vision" eob/type code should not be used. Additionally, the CARIN Blue Button IG does not currently provide a profile for "oral" (dental) claims, so that eob/type is not currently supported.

| Element | Parent | institutional / inpatient | institutional / outpatient | pharmacy | professional |
| --- | --- | --- | --- | --- | --- |
| sub_type | eob | X | X | – | – |
| billable_period | eob | X | X | – | – |
| diagnoses | eob | X (1..1) | X (1..1) | – | X (1..1) |
| diagnosis | diagnoses | X (1..*) | X (1..*) | – | X (1..*) |
| type | diagnosis | X | X | – | X |
| on_admission | diagnosis | X | – | – | – |
| revenue | item | X | X | – | – |
| serviced_period | serviced | – | o | o | – |
| adjudication_amount_type | adjudication | – | – | X (1..*) | X (1..*) |
| in_out_network | adjudication | – | – | – | X |
| product_or_service | item | X (See Note_1) | X | X | X |
| admission_period | supporting_info | X | – | – | – |
| days_supply | supporting_info | – | – | X | – |
| dawcode | supporting_info | – | – | X | – |
| refill_num | supporting_info | – | – | X | – |
{: .heatMap}

**Note_1:** A CPT / HCPCS code may not be available for some (inpatient) institutional claims. For this subset of claims, It is recommended payers provide a data absent reason when a CPT / HCPCS code is not available.
