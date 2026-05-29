When HealthLX receives an EOB, it is associated with the most current Roster file. The sole field utilized to match an EOB record to the Roster is the `eob/patient/person/unique_person_id` value. If the `unique_person_id` value is not included, the EOB record will not be processed.

Unique Identifiers are **case sensitive** and **MUST** match across file types.

For example: If the `unique_person_id` = `t9808041455` on the Roster file, using a lower-case `"t"`, but `T9808041455` on the EOB file with an upper-case `"T"`, the EOB will not be tied to the correct `Patient` resource/member.
