import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';
import { Buffer } from "buffer";

const decode = (str: string):string => Buffer.from(str, 'base64').toString('binary');

export const handler = async (event: APIGatewayEvent, _context: Context): Promise<APIGatewayProxyResult> => {
    // Event will contain things passed via request as --data
    console.log("Example of Environment variable access:", process.env.TEST_VAR)
    let txHash: string;
    if (event.body !== null) {
        txHash = JSON.parse(decode(event.body)).txHash;
    } else {
        txHash = (event as any).txHash;
    }
    // const txHash = event.body? JSON.parse(event.body).txHash : (event as any).txHash;

    return {
        statusCode: 200,
        body: JSON.stringify({
            message: `Processed TxHash ${txHash}`,
        }),
    };
};
