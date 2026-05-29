<img src="assets/General_Structure.png" alt="General Structure for Clinical XSD" class="clinical-option-diagram" />

We can accept one XSD schema file as the vehicle for submission of all clinical data types. The XSD begins with information required to describe a **US Core Patient**, which will always be required. Information for a given patient is then followed by definitions for all supported types of Clinical data, at least one of which must be provided.

**NOTE:** It is permissible to submit more than one type of clinical data for a given Patient within the same file, if desired.
