# Geoscape API proxying with Zappa

A sample to show how to deploy a proxy for the Geoscape APIs into AWS lambda, using [Zappa](https://github.com/Miserlou/Zappa); a simple and scaleable way to use the APIs in front-end JS applicaiotns without exposing your API key.

This example proxys the follow services, with some limited properties:
- Address Prediction, under the `/suggest` url
  - It defaults to the GNAF dataset and a maxiumum of 10 results
- Single Building from GNAF id, under the `/getBuilding` url
  - It returns the `footprint2d` and `maximumRoofHeight` for the buildings

## Requirements

- An API Key ([get it here](https://developer.psma.com.au/))
- Python >= 3.6
- An [AWS CLI](https://aws.amazon.com/cli/) setup with your information

## Usage

### Setup and Deploy

1. Clone the repo (or download and unzip)
2. Paste your API key into the `api_key` variable in `flaskApp.py`
3. Open a terminal/console/command prompt in the repository directory
4. Create virtual environment (`python -m venv env`)
5. Activate virtual envorinemnt (`.\env\scripts\activate`)
6. Install requirements (`pip install -r requirements.txt`)
7. Run `zappa init`
   1. Define your environement name, the default is `dev`; I'll use that for the rest of the readme
   2. Specify the AWS CLI profile that will be used to create and manage the AWS services
   3. Set the name for the S3 bucket that Zappa uploads to
   4. Zappa will auto discover `flaskApp.py` and identify it as the source to use for the lambdas, so just press enter
   5. This one lets you deploy the lambdas to all AWS regions, unless you *really* want to do this, just press enter.
   6. Review the results and press enter if good.
8. Run `zappa deploy dev`
9. Your proxy will now be available on the supplied URL
