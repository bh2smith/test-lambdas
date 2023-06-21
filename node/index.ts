import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';

export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {
    // Event will contain things passed via request as --data
    return {
        statusCode: 200,
        body: JSON.stringify({
            message: 'hello world',
            ctx: context,
            evt: event
        }),
    };
};
