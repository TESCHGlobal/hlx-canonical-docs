<h3 style="color:#E60073">Overall Architecture</h3>

The overall architecture used to define the data schema is based on the following reference:

[https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/](https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/)

<img src="assets/provider_diagram_1.png" alt="Plan-Net overall architecture diagram" class="overall-implementation-diagram" />

Diagrams presented in the next section provide a visual representation of the data model above.

<h3 style="color:#E60073">Data Model Visualization</h3>

A practitioner or participating organization who provides services is associated with a `PractitionerRole` or `OrganizationAffiliation` (respectively).

A `PractitionerRole` is associated with one employer for which the practitioner works (or another organization with which the participating organization is affiliated).

The `PractitionerRole` or `OrganizationAffiliation` can specify multiple `networks` within which the practitioner (or participating organization) operates, even if from different insurers. It may also specify `healthcare_services` offered and all locations where the practitioner works (or, in the case of a `ParticipatingOrganization`, a single location).

While not illustrated, it is conceivable a practitioner could work for multiple employers and thus could have multiple `PractitionerRole` resources. Or, in the case of a participating organization, the practitioner could be associated with multiple `OrganizationAffiliation` resources.

<img src="assets/provider_diagram_2.png" alt="Plan-Net practitioner and organization data model" class="overall-implementation-diagram" />

Payers establish their own networks and insurance plans, with each insurance plan specifying through which network(s) a plan may be offered. Each plan may also specify one or more coverage areas.

<img src="assets/provider_diagram_3.png" alt="Plan-Net payer networks and insurance plans data model" class="overall-implementation-diagram" />
