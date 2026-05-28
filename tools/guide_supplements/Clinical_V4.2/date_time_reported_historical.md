The Interoperability and Patient Access Rule requires all HealthLX customers to submit EOB data for all historical members who had active coverage at any time from January 01, 2016 to the present.

In addition, HealthLX customers who maintain clinical data are required to submit all clinical records from January 01, 2016 forward for any/all members with active coverage at any time from January 01, 2017 to the present.

Any active XSD version of the appropriate file type may be used to submit this information. If the same record (as identified by `eob_identifier` for EOB, or `unique_identifier` for Clinical records) is submitted more than once, HealthLX will return the most recent version of that document when a user makes a request via the API. HealthLX uses the `date_time_reported` field that appears near the beginning of an XSD to make the determination of what is most recent.

When submitting a historical Clinical or EOB file, submission processes must be followed with regard to the `date_time_reported` value, or an older version will be treated as the most recent, overwriting the more current data.

To ensure historical data does not overwrite current data, the recommended approach requires a payer to send chronologically defined batches with the appropriate `date_time_reported` value corresponding to the batch endpoint (time).

All historical Roster, EOB and Clinical files must contain "Historical" in the file name.

**Example:**

If sending a historical Clinical file for the week of January 01, 2017 through January 07, 2017, the `date_time_reported` value for that file would be `2017-01-07T23:59:59+XX:00` (XX:00 represents user time zone value).

When sending the next historical Clinical file for the week of January 08, 2017 through January 14, 2017, the `date_time_reported` value for that file would be `2017-01-14T23:59:59+XX:00` (XX:00 represents user time zone value).

Batch groupings may be for an arbitrary time period, as long as each file submitted complies with the maximum allowable size.
