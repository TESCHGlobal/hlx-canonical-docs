XML is a markup language similar to HTML, allowing users to describe data with tags. Utilizing an XML file enables richer data provisioning for multiple elements of the same type. This feature is called **Cardinality** and is defined as the lower and upper bounds of instances an element may be allowed to appear in a resource. If the cardinality begins with a `"0"`, then that element is not required.

Each schema contains sections with tables noting all parent and child elements within that element. If a parent exists, the hierarchy is noted in the **Parent Elements** column.

**Examples:**

- The `address.geolocations.geolocation` parent elements are noted as `address>geolocations`.
- Longitude for the geolocation (`address.geolocations.geolocation.longitude`) has the parent elements of `address>geolocations>geolocation`.

Elements and values required for compliance with [HL7 FHIR](https://www.hl7.org/fhir/R4/) standards are noted. All other elements and values listed within the tables are also supported. For maximum value and functionality, all elements in all tables are recommended. For details about data types and their requirements, please refer to Appendix B.

**NOTE:** In addition to the patient profile, at least one secondary profile must be present within the clinical document when provided by payers.
