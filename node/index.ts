import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';

export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {
    // Event will contain things passed via request as --data
    console.log("Example of Environment variable access:", process.env.TEST_VAR)
    const txHash = event.body? JSON.parse(event.body).txHash : event.txHash;

    return {
        statusCode: 200,
        body: JSON.stringify({
            message: `Processed TxHash ${txHash}`,
        }),
    };
};
