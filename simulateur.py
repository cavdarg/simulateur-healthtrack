# simulateur.py
import boto3, json, random, time
from datetime import datetime

region = "eu-west-3"
stream_name = "healthtrack-data-stream"
patients = [
    "c5d5de7c-5cb3-4741-8ac7-7bf81eaeec50",
    "6951fc9b-715e-4e3d-8fb7-ebd561b8d97c",
    "86f061d7-6560-4916-84bb-4f8c8749f1ef"
]

kinesis = boto3.client("kinesis", region_name=region)

def generate():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "patient_id": random.choice(patients),
        "heart_rate": random.randint(60, 130),
        "blood_pressure": random.randint(90, 160),
        "glucose_level": random.randint(70, 200)
    }

if __name__ == "__main__":
    while True:
        data = generate()
        print("Sending:", data)
        kinesis.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=data["patient_id"]
        )
        time.sleep(60)

