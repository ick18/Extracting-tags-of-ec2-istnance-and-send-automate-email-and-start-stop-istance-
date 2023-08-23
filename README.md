# Extracting-tags-of-ec2-istnance-and-send-automate-email-and-start-stop-istance-
# EC2 Management Lambda Script

This project showcases the development of an AWS Lambda script designed to manage Amazon Elastic Compute Cloud (EC2) instances based on specified tags. The script is implemented using Python and the Boto3 library, enabling seamless interaction with various AWS services. The core functionalities of the script include sending email notifications about EC2 instances, starting instances, and stopping instances as needed.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Lambda Script](#lambda-script)
- [Configuration](#configuration)
- [Usage](#usage)
- [Email Notifications](#email-notifications)
- [Scheduled Execution](#scheduled-execution)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- AWS Account: You must have an active AWS account to utilize AWS services.
- IAM User: Create an IAM user with the necessary permissions for EC2 and Simple Email Service (SES).
- Python Environment: Ensure Python 3.x is installed on your local machine.

## Getting Started

1. Clone this repository to your local machine.
2. Configure your AWS credentials either through the AWS CLI or environment variables.
3. Install required Python packages using `pip install -r requirements.txt`.

## Lambda Script

The heart of the project is the `lambda_function.py` script. The script's key tasks include:

- Fetching EC2 instances based on specific tags (e.g., "Environment: Production").
- Generating an email report with instance details (AMI ID, instance type, region, etc.).
- Starting instances based on specified tags (e.g., "Status: Start").
- Stopping instances based on specified tags (e.g., "Status: Stop").

## Configuration

- Customize the `lambda_handler` function to modify email content and EC2 tag filters.
- Update the SES email source and destination addresses in the `send_email` function.

## Usage

1. Deploy the Lambda script using the AWS Lambda service.
2. Upon execution, the script sends an email report with EC2 instance details.
3. Instances tagged with specific criteria are automatically started or stopped based on script logic.

## Email Notifications

- The script employs Amazon SES to send email notifications.
- Configure your SES settings and sender email address to ensure proper email delivery.

## Scheduled Execution

- The CloudFormation template includes a scheduled rule for the Lambda function's execution.
- Customize the `ScheduleExpression` to define the desired execution frequency.

## Contributing

- Contributions are welcome! If you identify issues or have ideas for improvements, submit a pull request to collaborate on enhancing the script.

## License

- This project is licensed under the MIT License, granting you the freedom to use and modify the code.

Feel free to reach out if you have any questions or need assistance with the project!
