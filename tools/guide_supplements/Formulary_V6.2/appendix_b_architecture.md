The overall architecture for implementation of the schema is based on the following two references:

- https://davinci-pdex-formulary-client.logicahealth.org/
- http://hl7.org/fhir/us/Davinci-drug-formulary/

The CoveragePlan profile of the FHIR R4 List resource provides links to information about the plan and formulary, contact information, a description of the drugTiers and associated cost sharing models of the plan, and a list of FormularyDrugs.

The FormularyDrug profile of the FHIR R4 MedicationKnowledge resource provides plan-specific information about a prescribable drug identified by an RxNORM identifier. Cost sharing for the drug is described by reference to a drug tier defined as part of the coverage plan. Extensions to the MedicationKnowledge resource support important search use cases. Due to the immaturity of the MedicationKnowledge resource, it is expected that it will undergo changes, and those changes may require evolution of the FormularyDrug profile.

<img src="assets/formulary_diagram.png" alt="Formulary architecture overview" class="overall-implementation-diagram" />

The following diagram shows a logical model of the implementation. There are two defined coverage plans, and within those coverage plans are drug tiers that can be defined arbitrarily from one plan to the next, including number, names, and cost-sharing details. It is important to note that even though multiple plans contain the same drug, that drug can be classified differently in terms of tier, prior auth, step therapy, and quantity limit.

<img src="assets/formulary_diagram_2.png" alt="Formulary logical model diagram" class="overall-implementation-diagram" />

<img src="assets/formulary_diagram_3.png" alt="Formulary implementation diagram" class="overall-implementation-diagram" />
