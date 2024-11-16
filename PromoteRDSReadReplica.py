import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize RDS client
rds_client = boto3.client('rds')

def lambda_handler(event, context):
    # Replace this with your RDS read replica identifier
    read_replica_identifier = "<your-read-replica-identifier>"

    try:
        logger.info(f"Promoting read replica: {read_replica_identifier}")

        # Promote the read replica to a standalone DB instance
        response = rds_client.promote_read_replica(
            DBInstanceIdentifier=read_replica_identifier
        )
        
        logger.info("Promotion initiated successfully!")
        logger.info(f"Response: {response}")
        
        return {
            "statusCode": 200,
            "body": f"Read replica {read_replica_identifier} promotion initiated successfully."
        }
    except Exception as e:
        logger.error(f"Failed to promote read replica: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error promoting read replica: {str(e)}"
        }
