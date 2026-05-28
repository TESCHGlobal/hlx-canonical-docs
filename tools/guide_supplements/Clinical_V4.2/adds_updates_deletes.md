The `clinicals/clinical/patient/.../record_type` elements indicating that a submission is an "Add" or an "Update" are "required" according to the Schema version 4.0, but HealthLX does not use this information to distinguish "Adds" and "Updates".

**Adds**

New submissions are added to the repository. Each clinical record (lab_observation, allergy_intolerance, etc) has a `unique_identifier` that must be unique to the given record. It must be present within the document when it is initially submitted.

**Updates**

If an existing record must be updated, submit it in the usual fashion (in its entirety, but with the updated information present instead). Use the same clinical record `unique_identifier` that was used upon initial submission. HealthLX will then update the record, ie, replace the previous version of the clinical record with the new one being submitted.

**Deletes**

If a record must be deleted at a later time, please contact HealthLX for support.
