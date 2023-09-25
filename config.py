snowflake_user = "SNOWGPT"
snowflake_password = "SnowGPT@202308"
snowflake_account = "anblicksorg_aws.us-east-1"
snowflake_warehouse = "SNOWGPT_WH"
snowflake_database = "SNOWGPT_DB"
snowflake_schema = "STG"
stage_name = "snowgpt_s3_stage"

conn = {
    "user"  : snowflake_user,
    "password": snowflake_password,
    "account": snowflake_account,
    "warehouse": snowflake_warehouse,
    "database": snowflake_database,
    "schema": snowflake_schema
}

query = "SELECT DISTINCT GET_PRESIGNED_URL(@snowgpt_s3_stage, METADATA$FILENAME) FROM @snowgpt_s3_stage"

api_key="741d647c-da49-4048-9d88-3b56e9e8e7f3"     
environment="gcp-starter"  

index_name="snowpineidx"

# openai_api_key = "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"

# os.environ["OPENAI_API_KEY"] = "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"
# cursor.execute(f"LIST {stage_file_path}")
# cursor.execute("SELECT $1 FROM @snowgpt_db.snowgpt_schema.snowgpt_stage/sampleTextFile.txt")