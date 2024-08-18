# Sample online inference
http://localhost:6789/api/pipeline_schedules/1/pipeline_runs/ef46ef6d89f44853b3d31ef771991bc5

Use the following CURL command to get real-time predictions:

```curl
curl --location 'http://localhost:6789/api/runs' \
--header 'Authorization: Bearer ef46ef6d89f44853b3d31ef771991bc5' \
--header 'Content-Type: application/json' \
--header 'Cookie: lng=en' \
--data '{
    "run": {
        "pipeline_uuid": "predict",
        "block_uuid": "inference",
        "variables": {
            "inputs": [
                {
                    "Date/Time": "01 01 2018 00:30",
                    "Wind Speed (m/s)": 5.659674,
                    "Theoretical_Power_Curve (KWh)": 516.127569
                    "Wind Direction (°)": 271.258087 
                },
                {
                    "Date/Time": "01 01 2018 00:40",
                    "Wind Speed (m/s)": 5.577941,
                    "Theoretical_Power_Curve (KWh)": 491.702972
                    "Wind Direction (°)": 265.674286
                }
            ]
        }
    }
}'
```

## Note

The `Authorization` header is using this pipeline’s API trigger’s token value.
The token value is set to `fire` for this project.
If you create a new trigger, that token will change.
Only use a fixed token for testing or demonstration purposes.