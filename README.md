# internship-application-tracker

A Python command-line project I'm building to organize internship application records and follow-ups.

## Status: Work in progress

## Why I'm building this

I'm currently tracking internship applications in a spreadsheet. I want to build a small tool that reads those records, summarizes application statuses, and helps me see which applications need my attention.

The spreadsheet will remain the place where I enter and update records. This tool will focus on reading and analyzing the data.

## Planned first version

Read application records from a CSV file. Summarize the number of applications in each status. List active applications whose follow-up dates have arrived.

Follow-up dates will be entered by the user. The tool will not send messages or submit applications.

My first implementation milestone is CSV loading and basic record display. Summaries and follow-up filtering will come afterward.

## Planned data format

Each record will contain:
company role applied_date status follow_up_date

Dates will use YYYY-MM-DD. The initial statuses will be applied, interview, offer, rejected, and withdrawn.

Public examples will use fictional data. Personal application records will stay outside the public repository.

## Learning goals:
Through this project, I want to practice file handling, data validation, date comparisons, testing, and writing clear documentation.

The first version will use Python's standard library. A web interface, database, email integration, and automated applications are outside the initial scope.
