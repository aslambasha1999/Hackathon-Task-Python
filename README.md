# Automated Step Definition Generator for Gherkin Feature Files

## Table of Contents
- [Overview]
- [Key Features]
- [Requirements]
- [Installation]
- [Usage]
  - [Individual Step Definition Generation]
  - [Batch Execution]
- [Logs]
- [Reports]
- [Utilities]
  - [Imported Modules from Utilities]


## Overview
This project automates the creation of step definition files for Gherkin feature files and implements Selenium methods based on keywords present in Gherkin steps. It supports both individual and batch execution of the step definition generation process and provides comprehensive logging and reporting functionalities.

## Key Features
- **Automatic Step Definition Generation:** Generates step definition files corresponding to feature files written in Gherkin syntax.
- **Selenium Method Implementation:** Implements Selenium methods based on keywords present in Gherkin steps, facilitating automation testing.
- **Individual and Batch Execution:** Supports both individual and batch execution of the step definition generation process for flexibility and scalability.
- **Logging:** Logs detailed information about the execution process, including timestamps, log levels, and error messages, for debugging and monitoring.
- **Reporting:** Generates HTML reports summarizing the execution results, including feature file names, execution status (Pass/Fail), execution time, and color-coded status indicators, for easy interpretation.

## Requirements
- Python 3.x
- Selenium (if using Selenium methods in feature files)
- Other dependencies as specified in 'requirements.txt'

   git clone <repository-url>

2. Navigate to the project directory:  

   cd project-directory

3. Install dependencies:

   pip install -r requirements.txt
   
# Configuration
This project requires minimal configuration. Ensure that your Gherkin feature files follow the standard syntax and structure. 
You can customize the output file format and adjust the selenium keyword mappings in the respective files if needed.
Configure logging in project.log file.
Customize import statements and method implementations as needed in Utilities directory

## Usage
### Individual Step Definition Generation
1. Place feature files in the `Features` directory.
2. Run the `StepDefinitionGenerator.py` script to generate step definitions:

    python StepDefinitionGenerator.py

### Batch Execution
1. Place feature files in the `Features` directory.
2. Run the `StepDefinitionRunner.py` script to execute the step definition generation process for multiple feature files:

    python StepDefinitionRunner.py

## Logs
- Individual logs for the step definition generation process are saved in the `Logs/Individual Logs` directory.
- Batch logs for the execution process are saved in the `Logs/Batch Logs` directory.

## Reports
- HTML reports summarizing the execution results are generated in the `Reports` directory.

## Utilities
- Custom utility functions/modules provided in the `Utilities` directory enhance the functionality and usability of the project.

### Imported Modules from Utilities
- `generate_report`: Contains functions for generating HTML reports.
- `generate_Imports`: Contains functions for generating import statements.
- `format_Step_Annotations`: Contains functions for formatting step annotations.
- `format_Step_Funtion_name`: Contains functions for formatting step function names.
- `implement_Selenium_Methods`: Contains functions for implementing Selenium methods.
- `java_stepdefinitions_implementations`: Contains functions for writing step definitions in Java.

### Advantages of Using this Project

* Time Savings: Automated generation of step definitions can save a significant amount of time, especially for large test suites with numerous scenarios. Developers can quickly create step definitions without manually writing each one.

* Consistency: Automated generation ensures consistency in step definition format and structure across different scenarios and feature files. This reduces the risk of errors and inconsistencies that may arise from manual writing.

* Standardization: Your automated project enforces standardization in step definition naming conventions and code structure, leading to uniformity and readability of test scripts.

* Reduced Repetition: By automating the generation of step definitions, developers can avoid repetitive tasks and focus on higher-level testing activities such as scenario design and test case validation.

* Ease of Maintenance: Automated generation simplifies the maintenance of step definitions, as updates or modifications can be applied uniformly across multiple scenarios using the same template.

# Custom Reporting: 

*Granular Test Reports: Your project generates detailed test reports that provide insights into the execution status of individual features, scenarios, and steps, aiding in pinpointing failures and analyzing test results.
* Failure Analysis: Detailed reports facilitate quick identification and analysis of failing scenarios, helping developers and testers understand the root cause of issues and expedite bug resolution.

# Flexible Argument Handling:

* Parameterization: Your project allows for parameterization of Cucumber scenarios, enabling dynamic test data generation and reusability of step definitions with different input values.
* Contextual Information: In addition to test data, your project supports passing contextual information to Selenium methods, enhancing test flexibility and versatility.





