# web-scrape

**Author**: Amber Falbo
**Version**: 1.0.0 
<!-- (increment the patch/fix version number up if you make more commits past your first submission) -->

## Overview
Creating a web scraper that can automate the process of manually using the site.

## Getting Started
- $ poetry new web-scraper
- Use the folder created by Poetry as the root of your project’s git repository.
- poetry add requests
- poetry add beautifulsoup4


## Example
<!-- Show them what looks like and how how to use the application.  -->

## Architecture
- Scrape a Wikipedia page and record which passages need citations.
    - E.g. History of Mexico has 7 “citation needed” cases, as of this writing.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
    - E.g. Citation needed for “lorem spam and impsum eggs”
    - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Added functionality to add and delete some things. -->