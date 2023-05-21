# Stock Transaction Analysis

## About

An app which perform basic analysis on user uploaded excel file and produce output which is downloadable as excel file.

### Steps:
1. Upload excel file and click `Run`. Expected columns in input file:
    1. `Date, Name Of Client, Code, Counter, Quantity, NetAmount, Price`
2. To filter the inputs, fill in filter parameters and click `Run`. Possible columns that can be filtered are:
    1. `Date (From)`
    2. `Date (To)`
    3. `Code (Client Codes)`
    4. `Counter (Counters)`
3. The processed outputs will be displayed on the app and consist of following columns.
    1. `Code, Name of Client, Counter, Quantity, Loss/Profit,Average Cost`
    2. The output is computed by first grouping inputs by `Code`, `Name of Client` and `Counter`. Then compute the `Quantity`as sum of quantity, `Loss/Profit` as sum of `Net Amount`, `Average Cost` as `Net Amount / Quantity`
4. To download the processed results, enable the `Download` checkbox and click `Run`. The output files will be displayed in the `Output Files` tab. Output file consists of the following sheets
    1. `Result` - processed output as viewed on the app
    2. `Filtered` - Input data filtered as per the filter parameters set.

## Setup

1. Install python and git
2. Clone git repo
3. Install requirements
    ```
    pip install -r requirements.txt
    ```
4. Start app
    ```
    mercury run
    ```

## Troubleshoot

1. `ImportError: DLL load failed while importing _greenlet: The specified module could not be found.`
    Fix by install `msvc-runtime`
    ```
    pip install msvc-runtime
    ```