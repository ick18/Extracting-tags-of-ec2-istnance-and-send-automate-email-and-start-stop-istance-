# Automated EC2 Management and Reporting using AWS Services

This project focuses on automating the management of Amazon EC2 instances, extracting resource tags, generating summarized data, and sending automated emails using various AWS services. The project is divided into several phases, including manual setup, automation script development, AWS CloudFormation template creation, and deployment.

## Project Overview

1. **Manual EC2 Instance Setup:**
   - Manually create Amazon EC2 instances.
   - Add necessary tags to EC2 instances, such as `Name`, `Environment`, etc.

2. **Automation Script (Boto3) - Extracting and Summarizing Resource Tags:**
   - Develop a Boto3 Python script to extract tags from EC2 instances.
   - Summarize the extracted tags and generate meaningful data.
   - Store the summarized data for further use.

3. **AWS CloudFormation Template 1 - Scheduled Email Generation:**
   - Create an AWS CloudFormation template in YAML format.
   - Define IAM roles, policies, Lambda function, CloudWatch Events rule.
   - Schedule the Lambda function to trigger at specific intervals.
   - Configure the Lambda function to send automated emails using Amazon SES.
   - Include permissions for necessary AWS services.

4. **AWS CloudFormation Template 2 - Automated EC2 Start and Stop:**
   - Create another CloudFormation template in YAML.
   - Define IAM roles, policies, Lambda functions, CloudWatch Events rules.
   - Develop Boto3 scripts to start and stop EC2 instances.
   - Schedule the Lambda functions to trigger at specific times.
   - Configure permissions for EC2, Lambda, CloudWatch Events, and CloudWatch Logs.

5. **S3 Bucket Setup:**
   - Create an Amazon S3 bucket to store Boto3 script files.
   - Organize the bucket with folders for each script.

## Project Execution

1. **Automation Script Execution:**
   - Run the Boto3 script to extract and summarize resource tags.
   - Store the summarized data in a structured format.

2. **AWS CloudFormation Template 1 Deployment:**
   - Create an S3 bucket to host the Boto3 script.
   - Upload the zipped script file to the S3 bucket.
   - Deploy the CloudFormation template.
   - Verify the automated email generation and delivery.
   - Monitor CloudWatch Logs for Lambda function activities.

3. **AWS CloudFormation Template 2 Deployment:**
   - Create another S3 bucket for the new Boto3 scripts.
   - Upload the zipped files for start and stop scripts.
   - Deploy the second CloudFormation template.
   - Observe scheduled start and stop actions.
   - Check CloudWatch Logs for Lambda function executions.

## Getting Started

To set up and deploy this project, follow the steps outlined in the [Project Setup Guide](https://github.com/ick18/Extracting-tags-of-ec2-istnance-and-send-automate-email-and-start-stop-istance).

## Conclusion

By completing this project, you have successfully demonstrated the automation of EC2 management, data extraction, email notifications, and scheduled actions using AWS services. This project provides an efficient and cost-effective solution for managing and monitoring EC2 instances.

For a detailed walkthrough, refer to the [complete project documentation](https://github.com/ick18/Extracting-tags-of-ec2-istnance-and-send-automate-email-and-start-stop-istance/wiki).

For any inquiries, contact [Your Contact Email](mailto:akshaykhanna7798@gmail.com).

