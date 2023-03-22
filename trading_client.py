import os
import grpc
import logging
from dotenv import load_dotenv

from generated.TradingAPI_pb2_grpc import AccessServiceStub
from generated.AccessService_pb2 import LoginRequest

logger = logging.getLogger()


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    
    hostname = os.getenv("TRADING_API_HOSTNAME")
    secret = os.getenv("LOGIN_SECRET")

    logger.info(f"Trying to connect to hostname: {hostname}")    
  
    with open(os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"], 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
        logger.info(f"Using credentials: {creds}")
    
    with grpc.secure_channel(hostname, creds) as channel:
        stub = AccessServiceStub(channel)
        request = LoginRequest(secret=secret)
        access_token = stub.Login(request)
        logger.info(f'Access token received: {access_token}')
        
        

if __name__ == "__main__":
    main()