These value sets were updated July 23, 2020. For updated value sets, visit [https://hl7.org/fhir/R4/index.html](https://hl7.org/fhir/R4/index.html).

<h3 style="color:#E60073">DrugTierID Codes</h3>

The following DrugTierID Codes can be found here: [http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-DrugTierVS.html](http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-DrugTierVS.html)

| Code | Display | Definition |
| --- | --- | --- |
| generic | Generic | Commonly prescribed generic drugs that cost more than drugs in the 'preferred-generic' tier. |
| preferred-generic | Preferred Generic | Commonly prescribed generic drugs. |
| non-preferred-generic | Non-preferred Generic | Generic drugs that cost more than drugs in the 'generic' tier. |
| specialty | Specialty | Drugs used to treat complex conditions like cancer and multiple sclerosis. They can be generic or brand-name and are typically the most expensive drugs on the formulary. |
| brand | Brand | Brand-name drugs that cost more than 'preferred-brand' drugs. |
| preferred-brand | Preferred Brand | Brand-name drugs |
| non-preferred-brand | Non-preferred Brand | Brand-name drugs that cost more than 'brand' drugs. |
| zero-cost-share-preventive | Zero-cost-share preventive | Preventive medications and products available at no cost. |
| medical-service | Medical Service | Drugs that must be administered by a clinician or in a facility and may be covered under a medical benefit. |
{: .heatMap}

<h3 style="color:#E60073">PharmacyType Codes</h3>

The following PharmacyType Codes can be found here: [http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-PharmacyTypeVS.html](http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-PharmacyTypeVS.html)

| Code | Display | Definition |
| --- | --- | --- |
| 1-month-in-retail | 1 month in network retail | 1-month supply via in-network retail pharmacy. |
| 1-month-out-retail | 1 month out of network retail | 1-month supply via out-of-network retail pharmacy. |
| 1-month-in-mail | 1 month in network mail order | 1-month supply via in-network mail order pharmacy. |
| 1-month-out-mail | 1 month out of network mail order | 1-month supply via out-of-network mail order pharmacy. |
| 3-month-in-retail | 3 month in network retail | 3-month supply via in-network retail pharmacy. |
| 3-month-out-retail | 3 month out of network retail | 3-month supply via out-of-network retail pharmacy. |
| 3-month-in-mail | 3 month in network mail order | 3-month supply via in-network mail order pharmacy. |
| 3-month-out-mail | 3 month out of network mail order | 3-month supply via out-of-network mail order pharmacy. |
{: .heatMap}

<h3 style="color:#E60073">Currency Codes</h3>

The currency codes list is too large to be included in this guide. An up-to-date version can be found here: [http://hl7.org/fhir/R4/valueset-currencies.html](http://hl7.org/fhir/R4/valueset-currencies.html)

<h3 style="color:#E60073">Copay Options Codes</h3>

The following copay options codes can be found here: [http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-CopayOptionVS.html](http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-CopayOptionVS.html)

| Code | Display | Definition |
| --- | --- | --- |
| after-deductible | After Deductible | The consumer first pays the deductible, and after the deductible is met, the consumer is responsible only for the copay (it indicates that this benefit is subject to the deductible). |
| before-deductible | Before Deductible | The consumer first pays the copay, and any net remaining allowed charges accrue to the deductible (it indicates that this benefit is subject to the deductible). |
| no-charge | No Charge | No cost sharing is charged (this indicates that this benefit is not subject to the deductible). |
| no-charge-after-deductible | No Charge After Deductible | The consumer first pays the deductible, and after the deductible is met, no copayment is charged (it indicates that this benefit is subject to the deductible). |
{: .heatMap}

<h3 style="color:#E60073">Coinsurance Options</h3>

The following Coinsurance options codes can be found here: [http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-CoinsuranceOptionVS.html](http://hl7.org/fhir/us/Davinci-drug-formulary/ValueSet-usdf-CoinsuranceOptionVS.html)

| Code | Display | Definition |
| --- | --- | --- |
| after-deductible | After Deductible | The consumer first pays the deductible, and after the deductible is met, the consumer pays the coinsurance portion of allowed charges (it indicates that this benefit is subject to the deductible). |
| no-charge | No Charge | No cost sharing is charged (it indicates that this benefit is not subject to the deductible). |
| no-charge-after-deductible | No Charge After Deductible | The consumer first pays the deductible, and after the deductible is met, no coinsurance is charged (it indicates that this benefit is subject to the deductible). |
{: .heatMap}

<h3 style="color:#E60073">RxNorm Codes</h3>

The RxNorm codes list is too large to be included in this guide. An up-to-date version can be found here: [http://hl7.org/fhir/us/core/STU3/ValueSet-us-core-medication-codes.html](http://hl7.org/fhir/us/core/STU3/ValueSet-us-core-medication-codes.html)

<h3 style="color:#E60073">Medication Knowledge Status Codes</h3>

The following medication knowledge status codes can be found here: [http://hl7.org/fhir/R4/valueset-medicationknowledge-status.html](http://hl7.org/fhir/R4/valueset-medicationknowledge-status.html)

| Code | Display | Definition |
| --- | --- | --- |
| active | Active | The medication is available for use. |
| inactive | Inactive | The medication is not available for use. |
| entered-in-error | Entered in Error | The medication was entered in error. |
{: .heatMap}

<h3 style="color:#E60073">Organization Type Codes</h3>

The following organization type codes can be found here: [http://hl7.org/fhir/R4/valueset-organization-type.html](http://hl7.org/fhir/R4/valueset-organization-type.html)

| Code | Display | Definition |
| --- | --- | --- |
| prov | Healthcare Provider | An organization that provides healthcare services. |
| dept | Hospital Department | A department or ward within a hospital (generally is not applicable to top-level organizations). |
| team | Organizational team | An organizational team is usually a grouping of practitioners that perform a specific function within an organization (which could be a top-level organization or a department). |
| govt | Government | A political body, often used when including organization records for government bodies such as a federal government, state or local government. |
| ins | Insurance Company | A company that provides insurance to its subscribers and may include healthcare related policies. |
| pay | Payer | A company, charity or governmental organization, which processes claims and/or issues payments to providers on behalf of patients or groups of patients. |
| edu | Educational Institute | An educational institution that provides education or research facilities. |
| reli | Religious Institution | An organization that is identified as a part of a religious institution. |
| crs | Clinical Research Sponsor | An organization that is identified as a pharmaceutical/clinical research sponsor. |
| cg | Community Group | An unincorporated community group. |
| bus | Non-Healthcare Business or Corporation | An organization that is a registered business or corporation but not identified by other types. |
| other | Other | Other types of organization not already specified. |
{: .heatMap}

<h3 style="color:#E60073">DoseForm Codes</h3>

The DoseForm codes list is too large to be included in this guide. An up-to-date version can be found here: [http://hl7.org/fhir/R4/valueset-medication-form-codes.html](http://hl7.org/fhir/R4/valueset-medication-form-codes.html)

<h3 style="color:#E60073">Substance Category Codes</h3>

The following substance category codes can be found here: [http://hl7.org/fhir/R4/valueset-substance-category.html](http://hl7.org/fhir/R4/valueset-substance-category.html)

| Code | Display | Definition |
| --- | --- | --- |
| allergen | Allergen | A substance that causes an allergic reaction. |
| biological | Biological Substance | A substance that is produced by or extracted from a biological source. |
| body | Body Substance | A substance that comes directly from a human or an animal (e.g. blood, urine, feces, tears, etc.). |
| chemical | Chemical | Any organic or inorganic substance of a particular molecular identity, including (i) any combination of such substances occurring in whole or in part as a result of a chemical reaction or occurring in nature and (ii) any element or uncombined radical (http://www.epa.gov/opptintr/import-export/pubs/importguide.pdf). |
| food | Dietary Substance | A food, dietary ingredient, or dietary supplement for human or animal. |
| drug | Drug or Medicament | A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in man or other animals (Federal Food Drug and Cosmetic Act). |
| material | Material | A finished product which is not normally ingested, absorbed or injected (e.g. steel, iron, wood, plastic and paper). |
{: .heatMap}

<h3 style="color:#E60073">Substance Codes</h3>

The substance codes list is too large to be included in this guide. An up-to-date version can be found here: [http://hl7.org/fhir/R4/valueset-substance-code.html](http://hl7.org/fhir/R4/valueset-substance-code.html)
